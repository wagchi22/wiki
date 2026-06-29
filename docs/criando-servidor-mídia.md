# 📜 Criando Servidor de Mídia

---

:::info 🤔 Objetivo deste guia?
Criar um Servidor de Mídia no Windows.
Usa software popular e confiável para automatizar o processo.
:::

---

:::tip ⌛ Siga estas etapas:
	
1. 🧰 **Definir os locais padrão:**

	- Servarr: `C:\ProgramData`.
   	- Torrents: `E:\torrents`.
   	- Mídia: `E:\media`.

2. ⚙️ **Software necessário:** (_Baixe e instale cada um deles_).

   	- Indexador: [Prowlarr](https://prowlarr.com/) + [Byparr](https://github.com/ThePhaseless/Byparr).
   	- Automação: [Radarr](https://radarr.video/) + [Sonarr](https://sonarr.tv/) + [Bazarr](https://www.bazarr.media/). 
   	- Streaming: [Jellyfin](https://jellyfin.org/).
   	- Cliente de Torrent: [qBittorrent](https://www.qbittorrent.org/).

3. 🔵 **Configurar Prowlarr:**

   	- Usuário: Coloque um nome qualquer.
   	- Senha: Insira uma senha qualquer.
   	- Conexões (requer Chave API): Adicione o Radarr e Sonarr.
   	- Indexadores: 1337x, [Catálogo BeTor](https://catalogo.betor.top/static/catalogo-betor.yml).
   	- Mínimo de semeadores: `0`.
   	- Proxy: Byparr.

4. 🟡 **Configurar Radarr:**

   	- Usuário: Coloque um nome qualquer.
   	- Senha: Insira uma senha qualquer.
   	- Conexões: Adicione o qBittorrent. (*Requer Chave API*).
   	- Renomear automaticamente: Ativado.
   	- Propers e repacks: Desativado.
   	- Monitorar: Somente filme.
   	- Perfis de qualidade padrão: HD-1080p.
		- Idioma: Any.
   		- Ordem e definições de qualidades:
   			- WEBDL-1080p: `10` `100` `200`. (_Retire todos do grupo_).
   			- Bluray-1080p: `8` `80` `180`.
   			- HDTV-1080p: `4` `40` `140`.
   		- Pontuações:
   			- Portuguese: `30`.
   			- English: `20`.
   			- WEBDL-1080p: `15`.
   			- Bluray-1080p: `10`.
   			- HDTV-1080p: `5`.
	- Perfis de lançamentos:
		- Não deve conter: `multi` `fullhd` `hdr10+` `imax`.
   	- Formatos personalizados: (_Insira no painel cada código abaixo_).

 	<details>
      <summary><b>👉 Ver o código</b></summary>
 
    ```json
    { "name": "WEBDL-1080p", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Fonte", "implementation": "SourceSpecification", "negate": false, "required": false, "fields": { "value": 7 } } ] }
    { "name": "Portuguese", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Idioma", "implementation": "LanguageSpecification", "negate": false, "required": false, "fields": { "value": 18, "exceptLanguage": false } } ] }
    { "name": "HDTV-1080p", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Fonte", "implementation": "SourceSpecification", "negate": false, "required": false, "fields": { "value": 6 } } ] }
    { "name": "English", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Idioma", "implementation": "LanguageSpecification", "negate": false, "required": false, "fields": { "value": 1, "exceptLanguage": false } } ] }
    { "name": "Bluray-1080p", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Fonte", "implementation": "SourceSpecification", "negate": false, "required": false, "fields": { "value": 9 } } ] }
    ```

 </details>

5. 🟢 **Configurar Sonarr:**

   	- Usuário: Coloque um nome qualquer.
   	- Senha: Insira uma senha qualquer.
   	- Conexões: Adicione o qBittorrent. (_Requer Chave API_).
   	- Renomear automaticamente: Ativado.
   	- Propers e repacks: Desativado.
   	- Sonarr: Episódios ausentes.
   	- Perfis de qualidade padrão: HD-1080p.
		- Idioma: Any.
   		- Ordem e definições de qualidades:
   			- WEBDL-1080p: `10` `100` `200`. (_Retire todos do grupo_).
   			- Bluray-1080p: `8` `80` `180`.
   			- HDTV-1080p: `4` `40` `140`.
   		- Pontuações:
   			- Portuguese: `30`.
   			- English: `20`.
   			- WEBDL-1080p: `15`.
   			- Bluray-1080p: `10`.
   			- HDTV-1080p: `5`.
	- Perfis de lançamentos:
		- Não deve conter: `multi` `fullhd` `hdr10+` `imax`.
   	- Formato de pasta das séries: `{Series TitleYear}`.
   	- Formatos personalizados: (_Insira no painel cada código abaixo_).

<details>
  <summary><b>👉 Ver o código</b></summary>
  
  ```json
  { "name": "WEBDL-1080p", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Fonte", "implementation": "SourceSpecification", "negate": false, "required": false, "fields": { "value": 3 } } ] }
  { "name": "Portuguese", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Idioma", "implementation": "LanguageSpecification", "negate": false, "required": false, "fields": { "value": 18, "exceptLanguage": false } } ] }
  { "name": "HDTV-1080p", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Fonte", "implementation": "SourceSpecification", "negate": false, "required": false, "fields": { "value": 1 } } ] }
  { "name": "English", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Idioma", "implementation": "LanguageSpecification", "negate": false, "required": false, "fields": { "value": 1, "exceptLanguage": false } } ] }
  { "name": "Bluray-1080p", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Fonte", "implementation": "SourceSpecification", "negate": false, "required": false, "fields": { "value": 6 } } ] }
  ```

</details>

6. 🔴 **Configurar Bazarr:**

	- Usuário:Coloque um nome qualquer.
	- Senha: Insira uma senha qualquer.
	- Conexões: Adicione o Radarr e Sonarr. (_Requer Chave API_).
	- Legenda padrão para nova mídia: Ativado.
	- Sincronização automática de legenda: Ativado.
	- Modificações Sub-Zero: Ative as opções principais.
	- Provedor de legendas: [Open Subtitles](https://www.opensubtitles.com/).

7. 🟣 **Configurar Jellyfin:**

	- Usuário: Coloque um nome qualquer.
	- Senha: Insira uma senha qualquer.
	- Agrupar filmes em coleções: Ativado.
	- Cliente:
		- Taxa de atualização: No dispositivo.
		- Cor de legenda: Amarelo.
		- Tamanho de legenda: 125%.

8. ⬇️ **Configurar qBittorrent:**

	- Interface Web: Ativado.
	- Usuário: Coloque um nome qualquer.
	- Senha: Insira uma senha qualquer.
	- Limite de semeadura: Parar ao alcançar 0,0.
	- Modo de gerenciamento de torrents: Automático.

9. 🔓 **Configurar Byparr:**

	No **Agendador de Tarefas** (`taskschd.msc`), crie a tarefa `"Byparr"` configurada para rodar `"Ao inicializar"` (mesmo deslogado e sem limite de tempo), definindo a ação para iniciar o executável `...\uv.exe` com os argumentos `run "main.py"` a partir de `C:\ProgramData\Byparr`.

10. 📄 **(Opcional) Script Remux:** (_Requer [python](https://www.python.org/) e [ffmpeg](https://ffmpeg.org/)_).

	Adicione o código abaixo no **Bloco de Notas** e salve como `Remux.py` na pasta do **Servarr**. No **Agendador de Tarefas** (`taskschd.msc`), crie uma nova tarefa chamada `"Remux"` configurada para rodar `"Ao inicializar"` (mesmo deslogado e sem limite de tempo), definindo a ação de *Iniciar um programa* para executar o script Python via comando `C:\Program Files\Python314\python.exe Remux.py "E:\media"` a partir do diretório `C:\ProgramData`.

<details>
  <summary><b>👉 Ver o código</b></summary>

  ```python
  import os, sys, subprocess, ctypes, json

  def get_file_info(file_path):
      try:
          r = subprocess.run(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", file_path], capture_output=True, text=True, encoding='utf-8', errors='ignore', timeout=5)
          data = json.loads(r.stdout)
          
          ft = data.get("format", {}).get("tags", {})
          dirty_tags = {"title", "description", "synopsis", "comment", "show", "season_number", "episode_id", "date", "year", "creation_time", "network", "genre"}
          has_dirty = any(k.lower() in dirty_tags for k in ft)
          
          st = data.get("streams", [])
          v_st = [s for s in st if s.get("codec_type") == "video"]
          a_st = [s for s in st if s.get("codec_type") == "audio"]
          
          v_lang = any("language" in s.get("tags", {}) for s in v_st)
          
          def p(s):
              l = (s.get("tags", {}).get("language") or "").lower()
              return 0 if l in ["por", "pt", "ptb"] else 1 if l in ["eng", "en"] else 2

          sorted_audios = sorted(range(len(a_st)), key=lambda i: p(a_st[i]))
          a_wrong = list(range(len(a_st))) != sorted_audios
          
          has_sub = any(s.get("codec_type") == "subtitle" for s in st)
          has_img = any((s.get("codec_name") or "").lower() in ["mjpeg", "png", "bmp"] or s.get("disposition", {}).get("attached_pic") == 1 for s in st)
          
          is_dirty = has_dirty or has_sub or any("title" in "".join(s.get("tags", {}).keys()).lower() for s in st) or has_img or len(v_st) > 1 or v_lang or a_wrong
          return is_dirty, sorted_audios
      except Exception:
          return True, []

  def process_file(file_path):
      if not file_path.lower().endswith(('.mkv', '.mp4')) or "_temp" in file_path: return

      is_dirty, sorted_audios = get_file_info(file_path)
      fn = os.path.basename(file_path)
      if not is_dirty: return print(f"Já processado: {fn}")

      dir_n, ext = os.path.dirname(file_path), os.path.splitext(fn)[1]
      tmp = os.path.join(dir_n, f"{os.path.splitext(fn)[0]}_temp{ext}")

      mux = ctypes.windll.kernel32.CreateMutexW(None, False, "Local\\RadarrSonarrRemuxQueueMutex")
      ctypes.windll.kernel32.WaitForSingleObject(mux, -1)

      cmd = ["ffmpeg", "-y", "-i", file_path, "-map", "0:v:0?"]
      for i in sorted_audios: cmd.extend(["-map", f"0:a:{i}"])
      if not sorted_audios: cmd.extend(["-map", "0:a?"])
      
      meta = ["title", "description", "synopsis", "comment", "show", "season_number", "episode_id", "date", "year", "creation_time", "imdb", "tmdb", "network", "genre"]
      for m in meta: cmd.extend(["-metadata", f"{m}="])
      cmd.extend(["-sn", "-c", "copy", "-metadata:s:v", "title=", "-metadata:s:v", "language=", "-metadata:s:a", "title=", "-flush_packets", "0", tmp])

      print(f"\nProcessando: {fn}")
      try:
          subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='ignore')
          os.remove(file_path)
          os.rename(tmp, file_path)
          print(f"Concluído com sucesso: {fn}")
      except subprocess.CalledProcessError as e:
          print(f"Erro crítico no FFmpeg para {fn}. Código: {e.returncode}")
          if os.path.exists(tmp): os.remove(tmp)
      finally:
          ctypes.windll.kernel32.ReleaseMutex(mux)
          ctypes.windll.kernel32.CloseHandle(mux)

  env = os.environ.get
  if env('radarr_eventtype') == 'Test' or env('sonarr_eventtype') == 'Test':
      print("Teste de conexão recebido e validado com sucesso!"); sys.exit(0)

  target = env('radarr_moviefile_path') or env('sonarr_episodefile_path') or (sys.argv[1] if len(sys.argv) > 1 else None)
  if not target: print("Erro: Nenhum arquivo ou pasta detectado."); sys.exit(1)

  if os.path.isdir(target):
      print(f"Iniciando varredura recursiva na pasta: {target}\n")
      for r, _, files in os.walk(target):
          for f in files: process_file(os.path.join(r, f))
      print("\nVarredura e processamento concluídos!")
  elif os.path.isfile(target):
      process_file(target)
  ```

</details>

:::
