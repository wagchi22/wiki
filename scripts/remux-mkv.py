import json,os,subprocess,sys
from pathlib import Path

VIDEO_EXTENSIONS={".mkv",".mp4"}
PT_LANGS={"por","pt","pt-br","pb","por-br","português","portugues"}

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

def is_dirty(info):
    tracks=info.get("tracks",[])

    if any(
        track["type"]=="subtitles"
        for track in tracks
    ):
        return True

    audio=[
        track
        for track in tracks
        if track["type"]=="audio"
    ]

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

def extract_ptbr(path,info):
    subtitles=[
        track
        for track in info.get("tracks",[])
        if (
            track["type"]=="subtitles"
            and normalize_language(track)=="por"
            and not should_skip_subtitle(track)
        )
    ]

    for index,track in enumerate(subtitles,1):
        suffix=f".{index}" if index>1 else ""

        output=(
            path.parent
            /f"{path.stem}.pt-BR{suffix}.srt"
        )

        result=subprocess.run(
            [
                "mkvextract",
                "tracks",
                str(path),
                f"{track['id']}:{output}"
            ],
            capture_output=True
        )

        if result.returncode!=0:
            return False

    return True

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
    if not extract_ptbr(path,info):
        print("Falha ao processar")
        return

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

    temp=path.with_name(
        f"{path.stem}_temp.mkv"
    )

    command=[
        "mkvmerge",
        "-o",
        str(temp),
        "--no-subtitles",
        "--no-attachments",
        "--no-global-tags",
        "--no-chapters",
        "--title",
        ""
    ]

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

    command.append(str(path))

    try:
        result=subprocess.run(
            command,
            capture_output=True
        )

        if result.returncode not in (0,1):
            print("Falha ao processar")
            return

        if not temp.exists():
            print("Falha ao processar")
            return

        if not set_audio_languages(temp):
            print("Falha ao processar")
            temp.unlink(missing_ok=True)
            return

        new_info=get_info(temp)

        if not new_info:
            print("Falha ao processar")
            temp.unlink(missing_ok=True)
            return

        new_audio=[
            track
            for track in new_info.get("tracks",[])
            if track["type"]=="audio"
        ]

        if len(audio)==2:
            if len(new_audio)!=2:
                print("Falha ao processar")
                temp.unlink(missing_ok=True)
                return

            first=new_audio[0].get("properties",{})
            second=new_audio[1].get("properties",{})

            if (
                first.get("language")!="por"
                or first.get("language_ietf")!="pt"
            ):
                print("Falha ao processar")
                temp.unlink(missing_ok=True)
                return

            if (
                second.get("language")!="eng"
                or second.get("language_ietf")!="en"
            ):
                print("Falha ao processar")
                temp.unlink(missing_ok=True)
                return

        path.unlink()
        temp.rename(path)

        print("Concluído com sucesso")

    except Exception:
        print("Falha ao processar")

    finally:
        if temp.exists():
            temp.unlink(missing_ok=True)

def process_file(path):
    path=Path(path)

    if (
        path.suffix.lower() not in VIDEO_EXTENSIONS
        or "_temp" in path.name
    ):
        return

    info=get_info(path)

    if not info:
        print("Falha ao processar")
        return

    if not is_dirty(info):
        print(f"Já processado: {path.name}")
        return

    print(f"Processando: {path.name}")
    remux_file(path,info)

def process_target(target):
    path=Path(target)

    if path.is_dir():
        for file in path.rglob("*"):
            if file.is_file():
                process_file(file)

    elif path.is_file():
        process_file(path)

event=(
    os.environ.get("radarr_eventtype")
    or os.environ.get("sonarr_eventtype")
)

if event=="Test":
    sys.exit(0)

target=(
    os.environ.get("radarr_moviefile_path")
    or os.environ.get("sonarr_episodefile_path")
    or (
        sys.argv[1]
        if len(sys.argv)>1
        else None
    )
)

if target:
    process_target(target)