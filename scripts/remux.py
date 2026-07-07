import os, sys, subprocess, json, ctypes

def is_dirty(file_path):
    try:
        info = json.loads(subprocess.run(["mkvmerge", "-J", file_path], capture_output=True, text=True).stdout)
        tracks = info.get("tracks", [])
        if len([t for t in tracks if t['type'] == 'video']) > 1: return True
        if any(t['type'] == 'subtitles' for t in tracks): return True
        if info.get("attachments"): return True
        if info.get("global_tags"): return True
        
        allowed_langs = {'por', 'pt', 'pt-br', 'pb', 'eng', 'en'}
        for t in tracks:
            if t['type'] == 'audio' and t['properties'].get('language', 'und') not in allowed_langs:
                return True
        return False
    except:
        return True

def process_file(file_path):
    if not file_path.lower().endswith(('.mkv', '.mp4')) or "_temp" in file_path:
        return
        
    fn = os.path.basename(file_path)
    if not is_dirty(file_path):
        print(f"\nJá processado: {fn}")
        return

    print(f"\nProcessando: {fn}")
    info = json.loads(subprocess.run(["mkvmerge", "-J", file_path], capture_output=True, text=True, encoding='utf-8').stdout)
    
    tracks = {t['type']: [] for t in info.get("tracks", [])}
    for t in info.get("tracks", []): tracks[t['type']].append(t)

    v = next((str(t['id']) for t in tracks.get('video', [])), None)
    audio = {t['properties'].get('language', 'und'): str(t['id']) for t in tracks.get('audio', [])}
    
    pt = audio.get('por') or audio.get('pt') or audio.get('pt-br') or audio.get('pb')
    en = audio.get('eng') or audio.get('en')
    
    base_path = os.path.splitext(file_path)[0]
    tmp = base_path + "_temp.mkv"
    
    mux = ctypes.windll.kernel32.CreateMutexW(None, False, "Local\\RemuxMutex")
    ctypes.windll.kernel32.WaitForSingleObject(mux, -1)

    try:
        cmd = ["mkvmerge", "-o", tmp, "--no-subtitles", "--no-attachments", "--no-global-tags", "--title", ""]
        if v: cmd.extend(["--video-tracks", v, "--language", f"{v}:und", "--track-name", f"{v}:"])
        
        a_ids = [i for i in [pt, en] if i]
        if a_ids:
            cmd.extend(["--audio-tracks", ",".join(a_ids)])
            for i, lang in [(pt, "pt-BR"), (en, "eng")]:
                if i: cmd.extend(["--language", f"{i}:{lang}", "--default-track", f"{i}:{'yes' if lang=='pt-BR' else 'no'}", "--track-name", f"{i}:"])
            cmd.extend(["--track-order", f"0:{v}," + ",".join(f"0:{i}" for i in a_ids)])
        else: cmd.append("--no-audio")
            
        cmd.append(file_path)
        if subprocess.run(cmd, capture_output=True, text=True).returncode in [0, 1]:
            os.remove(file_path)
            os.rename(tmp, base_path + ".mkv")
            print(f"Concluído: {fn}")
    finally:
        if os.path.exists(tmp):
            try: os.remove(tmp)
            except: pass
        ctypes.windll.kernel32.ReleaseMutex(mux)
        ctypes.windll.kernel32.CloseHandle(mux)

target = os.environ.get('radarr_moviefile_path') or os.environ.get('sonarr_episodefile_path') or (sys.argv[1] if len(sys.argv) > 1 else None)

if target:
    if os.path.isdir(target):
        print(f"\nIniciando varredura recursiva na pasta: {target}")
        for r, _, files in os.walk(target):
            for f in files: process_file(os.path.join(r, f))
        print("Varredura e processamento concluídos!")
    elif os.path.isfile(target):
        process_file(target)
