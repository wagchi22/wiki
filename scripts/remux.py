import os, sys, subprocess, json, ctypes

def get_info(path):
    try:
        return json.loads(subprocess.run(["mkvmerge", "-J", path], capture_output=True, text=True, encoding='utf-8').stdout)
    except: return None

def process_file(path):
    if not path.lower().endswith(('.mkv', '.mp4')) or "_temp" in path: return
    
    info = get_info(path)
    if not info: return

    tracks = info.get("tracks", [])
    v_track = next((t for t in tracks if t['type'] == 'video'), None)
    a_tracks = [t for t in tracks if t['type'] == 'audio']
    
    # Verifica necessidade de processar
    is_dirty = (
        len([t for t in tracks if t['type'] == 'video']) > 1 or
        any(t['type'] == 'subtitles' for t in tracks) or
        info.get("attachments") or info.get("global_tags") or info.get("chapters") or
        any(t['properties'].get('track_name') for t in tracks) or
        any(t['properties'].get('language_ietf', t['properties'].get('language', 'und')).lower() not in ['por', 'pt', 'pt-br', 'pb', 'português', 'portugues', 'eng', 'en'] for t in a_tracks)
    )

    if not is_dirty:
        print(f"Pulado: {os.path.basename(path)}")
        return

    print(f"Processando: {os.path.basename(path)}")
    tmp = os.path.splitext(path)[0] + "_temp.mkv"
    mux = ctypes.windll.kernel32.CreateMutexW(None, False, "Local\\RemuxMutex")
    ctypes.windll.kernel32.WaitForSingleObject(mux, -1)

    try:
        cmd = ["mkvmerge", "-o", tmp, "--no-subtitles", "--no-attachments", "--no-global-tags", "--no-chapters", "--title", ""]
        if v_track: cmd.extend(["--video-tracks", str(v_track['id']), "--language", f"{v_track['id']}:und", "--track-name", f"{v_track['id']}:"])
        
        if a_tracks:
            a_ids = [str(t['id']) for t in a_tracks]
            cmd.extend(["--audio-tracks", ",".join(a_ids)])
            for t in a_tracks:
                lang = t['properties'].get('language_ietf', t['properties'].get('language', 'und')).lower()
                l = 'por' if lang in ['por', 'pt', 'pt-br', 'pb', 'português', 'portugues'] else 'eng'
                cmd.extend(["--language", f"{t['id']}:{l}", "--default-track", f"{t['id']}:no", "--track-name", f"{t['id']}:"])
        else: cmd.append("--no-audio")
            
        cmd.append(path)
        if subprocess.run(cmd, capture_output=True).returncode in [0, 1]:
            os.remove(path)
            os.rename(tmp, os.path.splitext(path)[0] + ".mkv")
    finally:
        if os.path.exists(tmp):
            try: os.remove(tmp)
            except: pass
        ctypes.windll.kernel32.ReleaseMutex(mux)
        ctypes.windll.kernel32.CloseHandle(mux)

target = os.environ.get('radarr_moviefile_path') or os.environ.get('sonarr_episodefile_path') or (sys.argv[1] if len(sys.argv) > 1 else None)

if target:
    print("")
    if os.path.isdir(target):
        for r, _, files in os.walk(target):
            for f in files: process_file(os.path.join(r, f))
    elif os.path.isfile(target):
        process_file(target)
