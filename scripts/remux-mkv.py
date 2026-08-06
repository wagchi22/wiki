import json, os, subprocess, sys
from pathlib import Path

VIDEO_EXTENSIONS={".mkv",".mp4"}
PT_LANGS={"por","pt","pt-br","pb","por-br","português","portugues"}


def get_info(path):
    try:
        r=subprocess.run(["mkvmerge","-J",str(path)],capture_output=True,text=True,encoding="utf-8",errors="replace",check=True)
        return json.loads(r.stdout)
    except (subprocess.SubprocessError,json.JSONDecodeError):
        return None


def get_language(track):
    p=track.get("properties",{})
    return (p.get("language_ietf") or p.get("language") or "und").lower()


def normalize_language(track):
    lang=get_language(track)
    if lang in PT_LANGS:return "por"
    if lang in {"eng","en"} or lang.startswith("en-"):return "eng"
    return "und"


def should_skip_subtitle(track):
    p=track.get("properties",{})

    if p.get("hearing_impaired"):
        return True

    if p.get("forced_track"):
        return True

    title=p.get("track_name","").lower()

    return any(x in title for x in (
        "sdh",
        "forced",
    ))


def is_dirty(info):
    tracks=info.get("tracks",[])

    if any(t["type"]=="subtitles" for t in tracks):
        return True

    audio=[t for t in tracks if t["type"]=="audio"]

    if any(normalize_language(t) not in {"por","eng"} for t in audio):
        return True

    if len([t for t in tracks if t["type"]=="video"])!=1:
        return True

    if any(info.get(x) for x in ("attachments","global_tags","chapters")):
        return True

    return any(t.get("properties",{}).get("track_name") for t in tracks)


def extract_ptbr(path,info):
    subs=[
        t for t in info.get("tracks",[])
        if (
            t["type"]=="subtitles"
            and normalize_language(t)=="por"
            and not should_skip_subtitle(t)
        )
    ]

    for i,t in enumerate(subs,1):
        suffix=f".{i}" if i>1 else ""

        out=path.parent/f"{path.stem}.pt-BR{suffix}.srt"

        r=subprocess.run(
            [
                "mkvextract",
                "tracks",
                str(path),
                f"{t['id']}:{out}"
            ],
            capture_output=True
        )

        if r.returncode!=0:
            return False

    return True


def remux_file(path,info):
    if not extract_ptbr(path,info):
        print("Falha ao processar")
        return

    tracks=info.get("tracks",[])

    video=next(
        (t for t in tracks if t["type"]=="video"),
        None
    )

    audio=[
        t for t in tracks
        if t["type"]=="audio"
    ]

    temp=path.with_name(
        path.stem+"_temp.mkv"
    )

    cmd=[
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
        vid=str(video["id"])

        cmd += [
            "--video-tracks",
            vid,
            "--language",
            f"{vid}:und",
            "--track-name",
            f"{vid}:"
        ]

    if audio:
        cmd += [
            "--audio-tracks",
            ",".join(str(t["id"]) for t in audio)
        ]

        for t in audio:
            tid=t["id"]

            cmd += [
                "--language",
                f"{tid}:{normalize_language(t)}",
                "--default-track",
                f"{tid}:no",
                "--track-name",
                f"{tid}:"
            ]

    else:
        cmd.append("--no-audio")

    cmd.append(str(path))

    try:
        r=subprocess.run(cmd,capture_output=True)

        if r.returncode not in (0,1):
            print("Falha ao processar")
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

    if path.suffix.lower() not in VIDEO_EXTENSIONS or "_temp" in path.name:
        return

    info=get_info(path)

    if not info:
        print(f"Falha ao processar")
        return

    if not is_dirty(info):
        print(f"Já processado: {path.name}")
        return

    print(f"Processando: {path.name}")
    remux_file(path,info)


def process_target(target):
    path=Path(target)

    if path.is_dir():
        for f in path.rglob("*"):
            if f.is_file():
                process_file(f)

    elif path.is_file():
        process_file(path)


event=os.environ.get("radarr_eventtype") or os.environ.get("sonarr_eventtype")

if event=="Test":
    sys.exit(0)

target=(
    os.environ.get("radarr_moviefile_path")
    or os.environ.get("sonarr_episodefile_path")
    or (sys.argv[1] if len(sys.argv)>1 else None)
)

if target:
    process_target(target)