# Configurar Mediaserver

:::info Objetivo
Configurar um Servidor de Mídia no Windows, usando software popular e confiável
para automatizar o processo.
:::

## Software

- [Prowlarr](https://prowlarr.com/)
- [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr)
- [Radarr](https://radarr.video/)
- [Sonarr](https://sonarr.tv/)
- [Jellyfin](https://jellyfin.org/)
- [qBittorrent](https://www.qbittorrent.org/)
- [Python](https://www.python.org/)
- [MKVToolNix](https://mkvtoolnix.download/)

## Scripts

- [flaresolver.ps1](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/flaresolverr.ps1)
- [remux.py](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/remux.py)
- [run-remux.bat](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/run-remux.bat)

## Prowlarr

- Conexões: Radarr/Sonarr
- Indexadores:
  - [Catálogo BeTor](https://catalogo.betor.top/guia/prowlarr/)

## FlareSolverr

- Conexões: Radarr/Sonarr

## qBittorrent

- Interface Web: Ativado
- Limite de semeadura: Parar ao alcançar 0,0
- Modo de gerenciamento de torrents: Automático
- Máximo de conexões por torrent: 250
- Inibir sono do sistema enquanto faz download: Ativado

## Radarr/Sonnar

- Conexões: qBittorrent
- Renomear automaticamente: Ativado
- Conexões: `C:\GitHub\wiki\scripts\run.bat`

## Jellyfin

- Agrupar filmes em coleções: Ativado
- Transcodificação por hardware: Intel QSV
- Codificador de hardware Intel H.264 de baixo processamento: Ativado
- Mapeamento de tons: Ativado
- Limitar transcodificação: Ativado
- Remover segmentos: Ativado
- Wholphin (TV):
  - Taxa de atualização: Automático
  - Tamanho da legenda: 26
  - Cor da legenda: Amarelo
