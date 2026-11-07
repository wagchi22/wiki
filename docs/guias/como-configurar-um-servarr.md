# Como configurar um Servarr

:::info Visão geral
Guia rápido de instalação do Servarr.
:::

## Estrutura

:::tip Acessibilidade
Mapear as unidades de rede facilitará o acesso ao sistema de arquivos da distribuição Linux do WSL.
:::

:::info Armazenamento
Biblioteca de mídia em `\media\data`.<br>
Configurações em `\mnt\docker-desktop-disk\data\docker\volumes`.
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

Veja [como instalar o Docker](como-instalar-o-docker.md).

Baixe o arquivo [docker-compose.yml](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/docs/guias/scripts/docker-compose.yml).

Execute no terminal do Docker:

```powershell
# Indica o local onde está o docker-compose.yml
cd <local-do-docker-compose.yml>

# Inicia o container no Docker
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
- Aumento do áudio ao executar downmix: 3
- Algoritmo downmix estéreo: NightmodeDialogue
- Usuários:
  - Reproduzir áudio padrão independente do idioma: Desativado
  - Idioma do áudio e legenda: Português (Brasil)
  - Tipo de legenda: Apenas legendas forçadas
- App da TV:
  - Tamanho do pôster: Grande
  - Taxa de atualização: Escala no dispositivo
  - Cor da legenda: Amarelo
  - Tamanho da legenda: 125%
  - Áudio: Downmix para estéreo

## Notificações

:::warning QR code
Não compartilhe capturas contendo o QR code.
:::

Pré-instalado no container, aprenda a configurar em [jwbot](https://github.com/wagchi22/jwbot).
