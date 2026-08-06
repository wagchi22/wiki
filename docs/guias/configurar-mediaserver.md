<!-- markdownlint-disable MD013 -->

# Configurar Mediaserver

:::info Objetivo
Configurar um Servidor de Mídia no Windows, usando software popular e confiável
para automatizar o processo.
:::

## Fontes

- [Gemini](https://gemini.google.com/)
- [TRaSH Guides](https://trash-guides.info)
- [Reddit](https://reddit.com/)

## Locais

- Indexadores: `C:\ProgramData\Prowlarr\Definitions\Custom`
- Ferramentas: `C:\Tools`
- Scripts: `C:\Scripts`
- Torrents: `E:\Torrents`
- Mídia: `E:\Media`

## Software

- Necessário:
  - [Prowlarr](https://prowlarr.com/)
  - [FlareSolverr](https://github.com/Flaresolverr/Flaresolverr)
  - [Radarr](https://radarr.video/)
  - [Sonarr](https://sonarr.tv/)
  - [Bazarr](https://www.bazarr.media/)
  - [Jellyfin](https://jellyfin.org/)
    - Plugins:  
      - [Prevent Sleep](https://github.com/jonschz/jellyfin-plugin-preventsleep)
  - [qBittorrent](https://www.qbittorrent.org/)
  - [MediaInfo](https://mediaarea.net/MediaInfo)
- Opcional:
  - Ferramentas: (_Insira no PATH do sistema_)
    - [Python](https://www.python.org/)
    - [MKVToolNix](https://mkvtoolnix.download/)
    - [dovi_tool](https://github.com/quietvoid/dovi_tool)
  - Scripts:
    - [remux-mkv.py](../../scripts/remux-mkv.py)
    - [remove-dolby-vision.py](/wiki/scripts/remove-dolby-vision.py)
    - [clean-orphan-subs.ps1](/wiki/scripts/clean-orphan-subs.ps1)
    - [flaresolverr-manager.ps1](/wiki/scripts/flaresolverr-manager.ps1)

## Prowlarr

- Usuário: Coloque um nome qualquer
- Senha: Insira uma senha qualquer
- Conexões (requer Chave API): Adicione o Radarr e Sonarr
- Indexadores:
  - [Catálogo BeTor](/scripts/catalogo-betor.yml)
  - Knaben
- Mínimo de semeadores: 0
- Etiquetas: `flaresolverr`

## FlareSolverr

- Execute o script `C:\Scripts\flaresolverr-manager.ps1` para iniciar automaticamente

## qBittorrent

- Interface Web: Ativado
- Usuário: Coloque um nome qualquer
- Senha: Insira uma senha qualquer
- Limite de semeadura: Parar ao alcançar 0,0
- Modo de gerenciamento de torrents: Automático
- Protocolo: TCP
- Máximo de conexões por torrent: 250
- Encriptação: Requerido

## Radarr

- Usuário: Coloque um nome qualquer
- Senha: Insira uma senha qualquer
- Conexões: Adicione o qBittorrent (_Requer Chave API_)
- Propers e repacks: Desativado
- Monitorar: Somente filme
- Perfis, formatos e nomeclatura: Obtenha [aqui](https://trash-guides.info/)
- Renomear automaticamente: Ativado
- Conexões:
  - Scripts Personalizados:
    - Remux MKV:
      - Caminho: `C:\Scripts\remux-mkv.py`
      - Opções: Obter, importar e atualizar
    - Clean orphan subs:
      - Caminho: `C:\Scripts\clean-orphan-subs.ps1`
      - Opções: Importar, atualizar e renomear

## Sonarr

- Usuário: Coloque um nome qualquer
- Senha: Insira uma senha qualquer
- Conexões: Adicione o qBittorrent (_Requer Chave API_)
- Propers e repacks: Desativado
- Monitorar: Todos os episódios
- Perfis, formatos e nomeclatura: Obtenha [aqui](https://trash-guides.info/)
- Renomear automaticamente: Ativado
- Conexões:
  - Scripts Personalizados:
    - Remux MKV:
      - Caminho: `C:\Scripts\remux-mkv.py`
      - Opções: Obter, importar e atualizar
    - Clean orphan subs:
      - Caminho: `C:\Scripts\clean-orphan-subs.ps1`
      - Opções: Importar, atualizar e renomear

## Bazarr

- Usuário: Coloque um nome qualquer
- Senha: Insira uma senha qualquer
- Conexões: Adicione o Radarr e Sonarr (_Requer Chave API_)
- Filtro de idioma:
  - Português
  - Português (Brasil)
  - Inglês
- Perfil de idioma:
  - Português:
    - Idioma: Português (Brasil)
  - Inglês:
    - Idioma: Inglês
- Legenda padrão para nova mídia: Português
- Sincronização automática de legenda: Ativado
- Modificações Sub-Zero: Hearing Impaired
- Provedor de legendas:
  - [OpenSubtitles.com](https://www.opensubtitles.com/)
  - Gestdown
  - SubDL

## Jellyfin

- Usuário: Coloque um nome qualquer
- Senha: Insira uma senha qualquer
- Agrupar filmes em coleções: Ativado
- Cliente:
  - Taxa de atualização: No dispositivo
  - Cor de legenda: Amarelo
  - Tamanho de legenda: 125%
- Transcodificação por hardware: Intel QSV
- Codificador de hardware Intel H.264 de baixo processamento: Ativado
- Mapeamento de tons: Ativado
- Limitar transcodificação: Ativado
- Remover segmentos: Ativado
