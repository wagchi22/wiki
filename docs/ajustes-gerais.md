# Criando Servidor de Mídia

---

:::info Objetivo
Criar um Servidor de Mídia no Windows, usando software popular e confiável para automatizar o processo.
:::

---

## Locais

- Servarr: C:\ProgramData.
- Torrents: E:\torrents.
- Mídia: E:\media.

## Software

- Instale:
  - Indexador: [Prowlarr](https://prowlarr.com/) + [Byparr](https://github.com/ThePhaseless/Byparr).
  - Automação: [Radarr](https://radarr.video/) + [Sonarr](https://sonarr.tv/) + [Bazarr](https://www.bazarr.media/). 
  - Streaming: [Jellyfin](https://jellyfin.org/).
  - Cliente de Torrent: [qBittorrent](https://www.qbittorrent.org/).
  - (Opcional) Script: [remux.py](https://github.com/wagchi22/meus-arquivos/blob/main/scripts/remux.py). (_Requer [ffmpeg](https://ffmpeg.org/) e [python](https://www.python.org/)_).

---

## Prowlarr

- Usuário: Coloque um nome qualquer.
- Senha: Insira uma senha qualquer.
- Conexões (requer Chave API): Adicione o Radarr e Sonarr.
- Indexadores: 1337x, [Catálogo BeTor](https://catalogo.betor.top/static/catalogo-betor.yml).
- Mínimo de semeadores: 0.
- Proxy: Byparr.

## Byparr

- Execute: [byparr.bat](https://github.com/wagchi22/meus-arquivos/blob/main/scripts/byparr.bat)

## qBittorrent

- Interface Web: Ativado.
- Usuário: Coloque um nome qualquer.
- Senha: Insira uma senha qualquer.
- Limite de semeadura: Parar ao alcançar 0,0.
- Modo de gerenciamento de torrents: Automático.

## Radarr

- Usuário: Coloque um nome qualquer.
- Senha: Insira uma senha qualquer.
- Conexões: Adicione o qBittorrent. (*Requer Chave API*).
- Renomear automaticamente: Ativado.
- Propers e repacks: Desativado.
- Monitorar: Somente filme.
- Perfis de qualidade padrão: HD-1080p.
  - Idioma: Any.
  - Ordem e definições de qualidades:
    - WEBDL-1080p: 10 100 200. (_Retire todos do grupo_).
    - Bluray-1080p: 8 80 180.
    - HDTV-1080p: 4 40 140.
  - Pontuações:
    - Portuguese: 30.
    - English: 20.
    - WEBDL-1080p: 15.
    - Bluray-1080p: 10.
    - HDTV-1080p: 5.
- Perfis de lançamentos:
  - Não deve conter: multi fullhd hdr10+ imax.
- Formatos personalizados:

<details>
  <summary><b>Exibir código</b></summary>

```json
[
  { "name": "WEBDL-1080p", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Fonte", "implementation": "SourceSpecification", "negate": false, "required": false, "fields": { "value": 7 } } ] },
  { "name": "Portuguese", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Idioma", "implementation": "LanguageSpecification", "negate": false, "required": false, "fields": { "value": 18, "exceptLanguage": false } } ] },
  { "name": "HDTV-1080p", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Fonte", "implementation": "SourceSpecification", "negate": false, "required": false, "fields": { "value": 6 } } ] },
  { "name": "English", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Idioma", "implementation": "LanguageSpecification", "negate": false, "required": false, "fields": { "value": 1, "exceptLanguage": false } } ] },
  { "name": "Bluray-1080p", "includeCustomFormatWhenRenaming": false, "specifications": [ { "name": "Fonte", "implementation": "SourceSpecification", "negate": false, "required": false, "fields": { "value": 9 } } ] }
]
