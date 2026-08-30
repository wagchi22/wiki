import json,os,subprocess,sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

VIDEO_EXTENSIONS={".mkv",".mp4"}
PT_LANGS={"por","pt","pt-br","pb","por-br","português","portugues"}
VERIFY_WORKERS=4

if hasattr(sys.stdout,"reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

if hasattr(sys.stderr,"reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def get_info(path):
    try:
        result=subprocess.run(
            ["mkvmerge","-J",str(path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=True
        )

        return json.loads(result.stdout)

    except (subprocess.SubprocessError,json.JSONDecodeError):
        return None


def get_language(track):
    properties=track.get("properties",{})

    return (
        properties.get("language_ietf")
        or properties.get("language")
        or "und"
    ).lower()


def normalize_language(track):
    language=get_language(track)

    if language in PT_LANGS:
        return "por"

    if language in {"eng","en"}:
        return "eng"

    if language.startswith("en-"):
        return "eng"

    return "und"


def should_skip_subtitle(track):
    properties=track.get("properties",{})

    if properties.get("hearing_impaired"):
        return True

    if properties.get("forced_track"):
        return True

    title=properties.get("track_name","").lower()

    return any(
        value in title
        for value in ("sdh","forced","stripped")
    )


def get_ptbr_subtitles(info):
    return [
        track
        for track in info.get("tracks",[])
        if (
            track["type"]=="subtitles"
            and normalize_language(track)=="por"
            and not should_skip_subtitle(track)
        )
    ]


def is_dirty(info):
    tracks=info.get("tracks",[])

    audio=[
        track
        for track in tracks
        if track["type"]=="audio"
    ]

    subtitles=get_ptbr_subtitles(info)

    # Se já existe exatamente uma legenda PT-BR válida,
    # ela será mantida dentro do MKV.
    #
    # Porém, qualquer existência de legendas ainda torna o arquivo
    # candidato a remux para remover as legendas indesejadas.
    has_subtitles=any(
        track["type"]=="subtitles"
        for track in tracks
    )

    if has_subtitles:
        return True

    if len(audio)==2:
        if normalize_language(audio[0])!="por":
            return True

        if normalize_language(audio[1])!="eng":
            return True

    elif any(
        normalize_language(track) not in {"por","eng"}
        for track in audio
    ):
        return True

    videos=[
        track
        for track in tracks
        if track["type"]=="video"
    ]

    if len(videos)!=1:
        return True

    if any(
        info.get(value)
        for value in (
            "attachments",
            "global_tags",
            "chapters"
        )
    ):
        return True

    return any(
        track.get("properties",{}).get("track_name")
        for track in tracks
    )


def set_audio_languages(path):
    info=get_info(path)

    if not info:
        return False

    audio=[
        track
        for track in info.get("tracks",[])
        if track["type"]=="audio"
    ]

    if len(audio)!=2:
        return True

    first_id=audio[0]["id"]
    second_id=audio[1]["id"]

    command=[
        "mkvpropedit",
        str(path),
        "--edit",
        f"track:{first_id+1}",
        "--set",
        "language=por",
        "--set",
        "language-ietf=pt",
        "--edit",
        f"track:{second_id+1}",
        "--set",
        "language=eng",
        "--set",
        "language-ietf=en"
    ]

    result=subprocess.run(
        command,
        capture_output=True
    )

    if result.returncode!=0:
        return False

    info=get_info(path)

    if not info:
        return False

    audio=[
        track
        for track in info.get("tracks",[])
        if track["type"]=="audio"
    ]

    if len(audio)!=2:
        return False

    first=audio[0].get("properties",{})
    second=audio[1].get("properties",{})

    return (
        first.get("language")=="por"
        and first.get("language_ietf")=="pt"
        and second.get("language")=="eng"
        and second.get("language_ietf")=="en"
    )


def remux_file(path,info):
    tracks=info.get("tracks",[])

    video=[
        track
        for track in tracks
        if track["type"]=="video"
    ]

    audio=[
        track
        for track in tracks
        if track["type"]=="audio"
    ]

    subtitles=get_ptbr_subtitles(info)

    temp=path.with_name(
        f"{path.stem}_temp.mkv"
    )

    command=[
        "mkvmerge",
        "-o",
        str(temp),

        "--no-attachments",
        "--no-global-tags",
        "--no-chapters",

        "--title",
        ""
    ]

    # VIDEO
    if video:
        video_id=video[0]["id"]

        command.extend([
            "--video-tracks",
            str(video_id),
            "--language",
            f"{video_id}:und",
            "--track-name",
            f"{video_id}:"
        ])

    # AUDIO
    if audio:
        command.extend([
            "--audio-tracks",
            ",".join(
                str(track["id"])
                for track in audio
            )
        ])

        for track in audio:
            track_id=track["id"]

            command.extend([
                "--track-name",
                f"{track_id}:",
                "--default-track",
                f"{track_id}:no"
            ])

    else:
        command.append("--no-audio")

    # SUBTITLES
    #
    # Mantém somente as legendas PT-BR válidas
    # diretamente dentro do MKV.
    if subtitles:
        subtitle_ids=",".join(
            str(track["id"])
            for track in subtitles
        )

        command.extend([
            "--subtitle-tracks",
            subtitle_ids
        ])

        for index,track in enumerate(subtitles):
            track_id=track["id"]

            # A primeira legenda PT-BR fica como padrão.
            default="yes" if index==0 else "no"

            command.extend([
                "--language",
                f"{track_id}:pt",
                "--track-name",
                f"{track_id}:",
                "--default-track",
                f"{track_id}:{default}",
                "--forced-track",
                f"{track_id}:no"
            ])

    else:
        command.append("--no-subtitles")

    command.append(str(path))

    try:
        result=subprocess.run(
            command,
            capture_output=True
        )

        if result.returncode not in (0,1):
            print(f"Falha: {path.name}")
            return

        if not temp.exists():
            print(f"Falha: {path.name}")
            return

        if not set_audio_languages(temp):
            print(f"Falha: {path.name}")
            temp.unlink(missing_ok=True)
            return

        new_info=get_info(temp)

        if not new_info:
            print(f"Falha: {path.name}")
            temp.unlink(missing_ok=True)
            return

        new_audio=[
            track
            for track in new_info.get("tracks",[])
            if track["type"]=="audio"
        ]

        new_subtitles=[
            track
            for track in new_info.get("tracks",[])
            if track["type"]=="subtitles"
        ]

        # VERIFICA ÁUDIO
        if len(audio)==2:
            if len(new_audio)!=2:
                print(f"Falha: {path.name}")
                temp.unlink(missing_ok=True)
                return

            first=new_audio[0].get("properties",{})
            second=new_audio[1].get("properties",{})

            if (
                first.get("language")!="por"
                or first.get("language_ietf")!="pt"
            ):
                print(f"Falha: {path.name}")
                temp.unlink(missing_ok=True)
                return

            if (
                second.get("language")!="eng"
                or second.get("language_ietf")!="en"
            ):
                print(f"Falha: {path.name}")
                temp.unlink(missing_ok=True)
                return

        # VERIFICA LEGENDAS
        if len(new_subtitles)!=len(subtitles):
            print(f"Falha: {path.name}")
            temp.unlink(missing_ok=True)
            return

        # Substitui o MKV original
        path.unlink()
        temp.rename(path)

    except Exception:
        print(f"Falha: {path.name}")

    finally:
        if temp.exists():
            temp.unlink(missing_ok=True)


def collect_files(targets):
    files=[]

    for target in targets:
        path=Path(target)

        if not path.exists():
            continue

        if path.is_file():
            if (
                path.suffix.lower() in VIDEO_EXTENSIONS
                and "_temp" not in path.name
            ):
                files.append(path)

            continue

        if path.is_dir():
            for root,dirs,names in os.walk(path):
                for filename in names:
                    file=Path(root)/filename

                    if file.suffix.lower() not in VIDEO_EXTENSIONS:
                        continue

                    if "_temp" in file.name:
                        continue

                    files.append(file)

    return files


def verify_file(path):
    info=get_info(path)

    if not info:
        return path,None

    if not is_dirty(info):
        return path,False

    return path,info


def process_target(target):
    path=Path(target)

    if not path.exists():
        print(f"Não encontrado: {path}")


def main():
    event=(
        os.environ.get("radarr_eventtype")
        or os.environ.get("sonarr_eventtype")
    )

    if event=="Test":
        sys.exit(0)

    radarr_target=os.environ.get("radarr_moviefile_path")
    sonarr_target=os.environ.get("sonarr_episodefile_path")

    if radarr_target:
        targets=[radarr_target]

    elif sonarr_target:
        targets=[sonarr_target]

    else:
        targets=sys.argv[1:]

    if not targets:
        print("Nenhum caminho informado")
        sys.exit(1)

    files=collect_files(targets)

    print("Verificando...")

    dirty_files=[]

    with ThreadPoolExecutor(
        max_workers=VERIFY_WORKERS
    ) as executor:
        results=executor.map(
            verify_file,
            files
        )

        for path,info in results:
            if info:
                dirty_files.append(
                    (path,info)
                )

    for path,info in dirty_files:
        print(f"Processando: {path.name}")
        remux_file(path,info)

    if not dirty_files:
        print("Não precisa ser remuxado.")

    print("Operação concluída.")


if __name__=="__main__":
    main()
