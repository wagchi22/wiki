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
   	- (Opcional) Script: [remux.py](https://github.com/wagchi22/meus-arquivos/blob/main/scripts/remux.py).

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
:::
