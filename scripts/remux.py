import json
import os
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


VIDEO_EXTENSIONS = {".mkv", ".mp4"}
PT_LANGS = {"pt", "por", "pt-br"}
EN_LANGS = {"en", "eng"}
VERIFY_WORKERS = 4

MKVMERGE = shutil.which("mkvmerge")

for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8")


def get_info(path):
    if not MKVMERGE:
        print("ERRO: mkvmerge não encontrado no PATH.")
        return None

    try:
        result = subprocess.run(
            [MKVMERGE, "-J", str(path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=True,
        )
        return json.loads(result.stdout)

    except (subprocess.SubprocessError, json.JSONDecodeError, OSError) as e:
        print(f"ERRO ao analisar {path.name}: {e}")
        return None


def tracks(info, kind):
    return [t for t in info.get("tracks", []) if t.get("type") == kind]


def props(track):
    return track.get("properties", {})


def normalize_language(track):
    values = {
        str(props(track).get(k, "")).lower()
        for k in ("language", "language_ietf")
    }

    if any(v in PT_LANGS or v.startswith("pt-") for v in values):
        return "pt"

    if any(v in EN_LANGS or v.startswith("en-") for v in values):
        return "en"

    return "und"


def audio_language(audio, total):
    lang = normalize_language(audio)
    return "en" if total == 1 and lang == "und" else lang


def bad_subtitle(track):
    p = props(track)
    name = str(p.get("track_name") or "").lower()

    return (
        p.get("forced_track", False)
        or p.get("hearing_impaired", False)
        or any(
            x in name
            for x in (
                "sdh",
                "forced",
                "hearing impaired",
                "hearing-impaired",
                "stripped",
            )
        )
    )


def find_best_subtitle(info):
    subtitles = [
        t for t in tracks(info, "subtitles")
        if normalize_language(t) == "pt" and not bad_subtitle(t)
    ]

    return min(
        subtitles,
        key=lambda t: (
            not props(t).get("default_track", False),
            t["id"],
        ),
        default=None,
    )


def validation_errors(info):
    errors = []
    videos = tracks(info, "video")
    audios = tracks(info, "audio")
    subtitles = tracks(info, "subtitles")

    if len(videos) != 1:
        errors.append(f"vídeo={len(videos)}")

    single_pt_audio = (
        len(audios) == 1 and normalize_language(audios[0]) == "pt"
    )

    special_pt = (
        single_pt_audio
        and len(subtitles) == 1
        and normalize_language(subtitles[0]) == "pt"
    )

    if len(audios) > 2:
        errors.append(f"áudios={len(audios)}")

    elif len(audios) == 2:
        if {normalize_language(a) for a in audios} != {"pt", "en"}:
            errors.append("áudios=esperado pt+en")

        if not props(audios[0]).get("default_track", False):
            errors.append("áudio 1=não-padrão")

        if props(audios[1]).get("default_track", False):
            errors.append("áudio 2=padrão")

    elif len(audios) == 1:
        if not props(audios[0]).get("default_track", False):
            errors.append("áudio 1=não-padrão")

    if not special_pt:
        if len(subtitles) > 1:
            errors.append(f"legendas={len(subtitles)}")

        elif len(subtitles) == 1:
            sub = subtitles[0]
            p = props(sub)

            if normalize_language(sub) != "pt":
                errors.append(
                    f"legenda={p.get('language_ietf') or p.get('language') or 'und'}"
                )

            if bad_subtitle(sub):
                errors.append("legenda=inválida")

            if not p.get("default_track", False):
                errors.append("legenda=não-padrão")

    for key in ("attachments", "global_tags", "chapters"):
        if info.get(key):
            errors.append(key)

    if info.get("container", {}).get("properties", {}).get("title"):
        errors.append("título")

    if any(props(t).get("track_name") for t in info.get("tracks", [])):
        errors.append("track com nome")

    return errors


def remux_file(path, info):
    videos = tracks(info, "video")
    audios = tracks(info, "audio")
    subtitles = tracks(info, "subtitles")
    subtitle = find_best_subtitle(info)

    if len(videos) != 1:
        print(f"Falha: {path.name} — vídeos={len(videos)}")
        return

    single_pt_audio = (
        len(audios) == 1 and normalize_language(audios[0]) == "pt"
    )

    special_pt = (
        single_pt_audio
        and len(subtitles) == 1
        and normalize_language(subtitles[0]) == "pt"
    )

    output = (
        path.with_suffix(".mkv")
        if path.suffix.lower() == ".mp4"
        else path.with_name(f"{path.stem}.__remux_temp__.mkv")
    )

    try:
        if output.exists():
            output.unlink()
    except OSError as e:
        print(f"Falha: {path.name} — não foi possível remover temporário: {e}")
        return

    command = [
        MKVMERGE,
        "-o", str(output),
        "--no-attachments",
        "--no-global-tags",
        "--no-chapters",
        "--title", "",
        "--video-tracks", str(videos[0]["id"]),
        "--language", f"{videos[0]['id']}:und",
        "--track-name", f"{videos[0]['id']}:",
    ]

    if audios:
        command += [
            "--audio-tracks",
            ",".join(str(a["id"]) for a in audios),
        ]

        for i, audio in enumerate(audios):
            aid = audio["id"]
            lang = audio_language(audio, len(audios))

            if special_pt and lang == "pt":
                lang = "pt-BR"

            command += [
                "--language", f"{aid}:{lang}",
                "--track-name", f"{aid}:",
            ]

            if len(audios) == 1:
                default = "yes"
            elif len(audios) == 2:
                default = "yes" if i == 0 else "no"
            else:
                default = None

            if default:
                command += ["--default-track", f"{aid}:{default}"]
    else:
        command.append("--no-audio")

    if subtitle:
        sid = subtitle["id"]
        lang = "pt-BR" if special_pt else "pt"

        command += [
            "--subtitle-tracks", str(sid),
            "--language", f"{sid}:{lang}",
            "--track-name", f"{sid}:",
            "--default-track", f"{sid}:yes",
            "--forced-track", f"{sid}:no",
        ]
    else:
        command.append("--no-subtitles")

    command.append(str(path))

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

        if result.returncode not in (0, 1):
            print(
                f"Falha: {path.name} — "
                f"mkvmerge retornou {result.returncode}"
            )
            if result.stderr:
                print(result.stderr.strip())
            return

        if not output.exists():
            print(f"Falha: {path.name} — MKV não criado")
            return

        new_info = get_info(output)

        if not new_info:
            output.unlink(missing_ok=True)
            print(f"Falha: {path.name} — MKV não pôde ser validado")
            return

        errors = validation_errors(new_info)

        if errors:
            output.unlink(missing_ok=True)
            print(f"Falha: {path.name} — {', '.join(errors)}")
            return

        if path.suffix.lower() == ".mkv":
            os.replace(output, path)
            print(f"OK: {path.name}")
        else:
            path.unlink()
            print(f"OK: {path.name} -> {output.name}")

    except Exception as e:
        print(f"Falha: {path.name} — {type(e).__name__}: {e}")
        try:
            output.unlink(missing_ok=True)
        except OSError:
            pass


def collect_files(targets):
    files = []

    for target in targets:
        path = Path(target)

        if not path.exists():
            print(f"Caminho não encontrado: {path}")
            continue

        candidates = [path] if path.is_file() else path.rglob("*")

        files.extend(
            f for f in candidates
            if (
                f.is_file()
                and f.suffix.lower() in VIDEO_EXTENSIONS
                and "_remux" not in f.stem.lower()
                and "__remux_temp__" not in f.stem.lower()
            )
        )

    return list(dict.fromkeys(files))


def verify_file(path):
    info = get_info(path)

    if not info:
        return path, None

    return path, info if validation_errors(info) else False


def main():
    if not MKVMERGE:
        print("ERRO: mkvmerge não foi encontrado no PATH.")
        return 1

    event = (
        os.environ.get("radarr_eventtype")
        or os.environ.get("sonarr_eventtype")
    )

    if event == "Test":
        print("Teste do Radarr/Sonarr OK.")
        print(f"Python: {sys.executable}")
        print(f"mkvmerge: {MKVMERGE}")
        return 0

    targets = []

    target = (
        os.environ.get("radarr_moviefile_path")
        or os.environ.get("sonarr_episodefile_path")
    )

    if target:
        targets.append(target)
    else:
        targets.extend(sys.argv[1:])

    if not targets:
        print("Nenhum caminho informado.")
        return 1

    files = collect_files(targets)

    if not files:
        print("Nenhum arquivo encontrado.")
        return 0

    print(f"Verificando {len(files)} arquivo(s)...")

    with ThreadPoolExecutor(max_workers=VERIFY_WORKERS) as executor:
        results = list(executor.map(verify_file, files))

    dirty = [
        (path, info)
        for path, info in results
        if info is not False and info is not None
    ]

    for path, info in dirty:
        print(f"Processando: {path.name}")
        remux_file(path, info)

    print(
        "Nenhum arquivo precisa ser remuxado."
        if not dirty
        else "Operação concluída."
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())