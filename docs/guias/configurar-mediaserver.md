# Configurar Mediaserver

:::info Objetivo
Configurar um Servidor de Mídia no Windows, usando software popular e confiável
para automatizar o processo.
:::

## Software

- Instale [Prowlarr](https://prowlarr.com/)
- Baixe [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) em `C:\Tools`
- Instale [Radarr](https://radarr.video/)
- Instale [Sonarr](https://sonarr.tv/)
- Instale [Jellyfin](https://jellyfin.org/)
- Instale [qBittorrent](https://www.qbittorrent.org/)
- Instale [Python](https://www.python.org/)
- Baixe [MKVToolNix](https://mkvtoolnix.download/) em `C:\Tools` e insira no PATH
- Baixe [flaresolverr.ps1](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/flaresolverr.ps1) em `C:\Scripts`
- Baixe [remux.py](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/remux.py) e [run-remux.bat](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/run-remux.bat) em `C:\Scripts`

## Prowlarr

- Conexões: Radarr/Sonarr
- Indexadores: [Catálogo BeTor](https://catalogo.betor.top/guia/prowlarr/)
- Etiquetas: Adicione `flaresolverr`

## FlareSolverr

- Inicialização automática: Execute e instale `C:\Scripts\flaresolverr.ps1`

## qBittorrent

- Interface Web: Ativado
- Limite de semeadura: Parar ao alcançar 0,0
- Modo de gerenciamento de torrents: Automático
- Máximo de conexões por torrent: 250
- Inibir sono do sistema enquanto faz download: Ativado

## Radarr/Sonnar

- Conexões: qBittorrent
- Renomear automaticamente: Ativado
- Conexões: Adicione o script `C:\Scripts\run-remux.bat`

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
