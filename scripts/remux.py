import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

VIDEO_EXTENSIONS = {".mkv", ".mp4"}
PT_LANGS = {"pt", "pt-br"}
EN_LANGS = {"en"}
VERIFY_WORKERS = 4

for s in (sys.stdout, sys.stderr):
    if hasattr(s, "reconfigure"):
        s.reconfigure(encoding="utf-8")


def get_info(path):
    try:
        r = subprocess.run(
            ["mkvmerge", "-J", str(path)],
            capture_output=True, text=True,
            encoding="utf-8", errors="replace", check=True
        )
        return json.loads(r.stdout)
    except (subprocess.SubprocessError, json.JSONDecodeError, OSError):
        return None


def tracks(info, kind):
    return [t for t in info.get("tracks", []) if t.get("type") == kind]


def props(track):
    return track.get("properties", {})


def track_language(track):
    p = props(track)
    return str(p.get("language_ietf") or p.get("language") or "und").lower()


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
                "sdh", "forced", "hearing impaired",
                "hearing-impaired", "stripped"
            )
        )
    )


def find_best_subtitle(info):
    subs = [
        t for t in tracks(info, "subtitles")
        if normalize_language(t) == "pt" and not bad_subtitle(t)
    ]
    return min(
        subs,
        key=lambda t: (
            not props(t).get("default_track", False),
            t["id"]
        ),
        default=None
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

    single_pt_audio_with_single_pt_subtitle = (
        single_pt_audio
        and len(subtitles) == 1
        and normalize_language(subtitles[0]) == "pt"
    )

    # Áudios
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

    # Legendas
    if not single_pt_audio_with_single_pt_subtitle:
        if len(subtitles) > 1:
            errors.append(f"legendas={len(subtitles)}")

        elif len(subtitles) == 1:
            sub = subtitles[0]
            p = props(sub)

            if normalize_language(sub) != "pt":
                errors.append(f"legenda={track_language(sub)}")
            if bad_subtitle(sub):
                errors.append("legenda=inválida")
            if not p.get("default_track", False):
                errors.append("legenda=não-padrão")

    # Container
    for key in ("attachments", "global_tags", "chapters"):
        if info.get(key):
            errors.append(key)

    if info.get("container", {}).get("properties", {}).get("title"):
        errors.append("título")

    for t in info.get("tracks", []):
        if props(t).get("track_name"):
            errors.append(f"track {t['id']} tem nome")

    return errors


def show_tracks(info):
    for t in info.get("tracks", []):
        p = props(t)
        print(
            f"  ID {t['id']} | {t['type']} | "
            f"language={p.get('language', 'und')} | "
            f"ietf={p.get('language_ietf', 'und')} | "
            f"default={p.get('default_track', False)}"
        )


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

    if output.exists():
        try:
            output.unlink()
        except OSError:
            print(f"Falha: {path.name} — não foi possível remover arquivo temporário")
            return

    command = [
        "mkvmerge", "-o", str(output),
        "--no-attachments", "--no-global-tags", "--no-chapters",
        "--title", "",
        "--video-tracks", str(videos[0]["id"]),
        "--language", f"{videos[0]['id']}:und",
        "--track-name", f"{videos[0]['id']}:",
    ]

    # Áudios
    if audios:
        command += [
            "--audio-tracks",
            ",".join(str(a["id"]) for a in audios)
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
                command += [
                    "--default-track",
                    f"{aid}:{default}"
                ]
    else:
        command.append("--no-audio")

    # Legenda
    if subtitle:
        sid = subtitle["id"]
        slang = "pt-BR" if special_pt else "pt"

        command += [
            "--subtitle-tracks", str(sid),
            "--language", f"{sid}:{slang}",
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
            if output.exists():
                try:
                    output.unlink()
                except OSError:
                    pass
            return

        if not output.exists():
            print(f"Falha: {path.name} — arquivo MKV não criado")
            return

        new_info = get_info(output)

        if not new_info:
            print(
                f"Falha: {path.name} — "
                f"não foi possível validar o novo MKV"
            )
            try:
                output.unlink()
            except OSError:
                pass
            return

        errors = validation_errors(new_info)

        if errors:
            print(
                f"Falha: {path.name} — "
                f"{', '.join(errors)}"
            )
            try:
                output.unlink()
            except OSError:
                pass
            return

        # MKV -> substitui original
        if path.suffix.lower() == ".mkv":
            try:
                os.replace(output, path)
                print(f"OK: {path.name}")
            except OSError as e:
                print(
                    f"Falha: {path.name} — "
                    f"não foi possível substituir o original: {e}"
                )
                if output.exists():
                    try:
                        output.unlink()
                    except OSError:
                        pass

        # MP4 -> remove original após MKV validado
        else:
            try:
                path.unlink()
                print(f"OK: {path.name} -> {output.name}")
            except OSError as e:
                print(
                    f"Falha: {path.name} — "
                    f"MKV criado, mas não foi possível remover "
                    f"o MP4 original: {e}"
                )

    except Exception as e:
        print(f"Falha: {path.name} — {e}")
        if output.exists():
            try:
                output.unlink()
            except OSError:
                pass


def collect_files(targets):
    files = []

    for target in targets:
        path = Path(target)

        if not path.exists():
            continue

        if path.is_file():
            candidates = [path]
        else:
            candidates = path.rglob("*")

        files.extend(
            f for f in candidates
            if (
                f.is_file()
                and f.suffix.lower() in VIDEO_EXTENSIONS
                and "_remux" not in f.stem.lower()
                and "__remux_temp__" not in f.stem.lower()
            )
        )

    return files


def verify_file(path):
    info = get_info(path)

    if not info:
        print(f"Falha ao ler: {path.name}")
        return path, None

    return path, info if validation_errors(info) else False


def main():
    event = (
        os.environ.get("radarr_eventtype")
        or os.environ.get("sonarr_eventtype")
    )

    if event == "Test":
        return

    target = (
        os.environ.get("radarr_moviefile_path")
        or os.environ.get("sonarr_episodefile_path")
    )

    targets = [target] if target else sys.argv[1:]

    if not targets:
        print("Nenhum caminho informado")
        return

    files = collect_files(targets)

    if not files:
        print("Nenhum arquivo encontrado.")
        return

    print(f"Verificando {len(files)} arquivo(s)...")

    with ThreadPoolExecutor(max_workers=VERIFY_WORKERS) as executor:
        results = list(executor.map(verify_file, files))

    dirty = []

    for path, info in results:
        if info is False:
            print(f"Ignorado: {path.name}")
        elif info is not None:
            dirty.append((path, info))

    for path, info in dirty:
        print(f"Processando: {path.name}")
        remux_file(path, info)

    if not dirty:
        print("Nenhum arquivo precisa ser remuxado.")

    print("Operação concluída.")


if __name__ == "__main__":
    main()