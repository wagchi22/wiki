#!/usr/bin/env python3

import os,sys,shutil,logging,subprocess

from pathlib import Path

from fractions import Fraction

logging.basicConfig(
    filename="hdr10_converter.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def log(msg):
    print(msg)
    logging.info(msg)

def run(cmd):
    log("> "+" ".join(map(str,cmd)))
    subprocess.run(cmd,check=True)

def probe(args):
    return subprocess.run(
        ["ffprobe","-v","error",*args],
        capture_output=True,
        text=True,
        check=True
    ).stdout.strip()

def stream(file,key):
    return probe([
        "-select_streams","v:0",
        "-show_entries",f"stream={key}",
        "-of","default=noprint_wrappers=1:nokey=1",
        str(file)
    ])

def get_input():
    if len(sys.argv)>1:
        return Path(sys.argv[1]).resolve()

    for env in (
        "radarr_moviefile_path",
        "sonarr_episodefile_path"
    ):
        value=os.getenv(env)
        if value:
            return Path(value).resolve()

    log("Nenhum arquivo recebido pela stack *arr.")
    return None

def has_dv(file):
    data=probe([
        "-select_streams","v:0",
        "-show_entries","stream=side_data_list",
        "-of","json",
        str(file)
    ]).lower()

    return any(x in data for x in (
        "dolby vision",
        "dovi",
        "dvhe",
        "dvh1"
    ))

def get_fps(file):
    value=stream(file,"avg_frame_rate")

    if value=="0/0":
        raise RuntimeError("FPS inválido.")

    return f"{float(Fraction(value)):.6f}"

def main():
    src=get_input()

    if not src:
        log("Teste *arr concluído.")
        return 0

    if not src.exists():
        log(f"Arquivo inexistente: {src}")
        return 0

    temp=src.with_suffix(".hevc")
    bl=src.with_name(f"{src.stem}.BL.hevc")
    output=src.with_name(f"{src.stem}_HDR10.mkv")
    backup=src.with_suffix(".backup.mkv")

    try:
        log(f"Processando: {src}")

        if stream(src,"codec_name").lower()!="hevc":
            log("Não é HEVC.")
            return 0

        if not has_dv(src):
            log("Dolby Vision não encontrado.")
            return 0

        fps=get_fps(src)

        run([
            "ffmpeg",
            "-hide_banner",
            "-loglevel","error",
            "-y",
            "-i",str(src),
            "-map","0:v:0",
            "-c:v","copy",
            "-bsf:v",
            "hevc_mp4toannexb",
            str(temp)
        ])

        run([
            "dovi_tool",
            "remove",
            "-i",str(temp),
            "-o",str(bl)
        ])

        run([
            "mkvmerge",
            "-o",str(output),
            "--default-duration",
            f"0:{fps}fps",
            str(bl),
            "--no-video",
            str(src)
        ])

        if not output.exists():
            raise RuntimeError("MKV final não criado.")

        shutil.move(src,backup)

        try:
            shutil.move(output,src)
            backup.unlink(missing_ok=True)
        except:
            if backup.exists():
                shutil.move(backup,src)
            raise

        log("Conversão concluída.")
        return 0

    except Exception as e:
        log(f"ERRO: {e}")
        return 1

    finally:
        for file in (temp,bl,output):
            try:
                file.unlink(missing_ok=True)
            except:
                pass

if __name__=="__main__":
    sys.exit(main())