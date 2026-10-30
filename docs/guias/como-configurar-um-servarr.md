# Como configurar um Servarr

:::info Visão geral
Guia rápido de instalação do Servarr.
:::

## Estrutura

:::info Armazenamento
Eu estarei usando um HD externo na unidade E:\ com bind mounts.
:::

```text
media/
├── docker-compose.yml
└── data/
    ├── torrents/
        ├── movies/
        ├── porn/
        └── tv/
    ├── movies/
    ├── porn/
    └── tv/
```

## Docker

Veja [como instalar o Docker](como-instalar-o-docker.md).<br>

Salve o arquivo [docker-compose.yml](scripts/docker-compose.yml).

Para crie o container, execute no terminal do Docker:

```powershell
"[wsl2]`nprocessors=2`nmemory=2GB`nswap=0" | Set-Content -Path "$env:USERPROFILE\.wslconfig" -Encoding ASCII
cd <local-do-docker-compose.yml>
docker compose up -d
```

## qBittorrent

Para criar os diretórios, execute no terminal do WSL:

```bash
mkdir -p /mnt/e/media/data/{movies,porn,tv} /mnt/e/media/data/torrents/{movies,porn,tv}
```

- Login/senha: procure nos logs (altere depois de fazer login)
- Modo de gerenciamento de torrents: Automático
- Locais de salvamento: 
  - Padrão: /data/torrents
  - Categoria movies: /data/torrents/movies
  - Categoria porn: /data/torrents/porn
  - Categoria tv: /data/torrents/tv

Reinicie o container para aplicar as mudanças.

## Prowlarr

Adicione o indexador [Catálogo BeTor](https://catalogo.betor.top/guia/prowlarr/).

## Radarr

- Renomear automaticamente: Ativado
- Categoria usada no qBittorrent: movies

## Sonarr

- Renomear automaticamente: Ativado
- Categoria usada no qBittorrent: tv

## Jellyfin

- Agrupar filmes em coleções: Ativado
- Usuários:
  - Reproduzir áudio padrão independente do idioma: Desativado
  - Idioma do áudio: Português (Brasil)
  - Idioma da legenda: Português (Brasil)
  - Tipo de legenda: Apenas legendas forçadas
- App (TV):
  - Taxa de atualização: Escala no dispositivo
  - Cor da legenda: Amarelo
  - Tamanho da legenda: 125%
  - Áudio: Downmix para estéreo
  - Modo noturno para áudio: Ativado

## Notificações

Veja em [jwbot](https://github.com/wagchi22/jwbot).
