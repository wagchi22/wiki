# Como configurar um Servarr

:::info Visão geral
Guia rápido de instalação do Servarr.
:::

## Diretórios

Crie a árvore de diretórios (no caso estarei usando em `E:\`):

```text
data/
└── media/
    ├── downloads/
        ├── movies/
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

## Imagens

:::warning Autenticação
A maioria das imagens ao ser iniciada geram credências temporárias localizado nos logs do Docker, sendo recomendado alterar isso após o login.
:::

### qBittorrent

- Modo de gerenciamento de torrents: Automático
- Locais de salvamento: 
  - Padrão: /data/downloads
  - Categoria movies: /data/downloads/movies
  - Categoria porn: /data/media/porn
  - Categoria tv: /data/downloads/tv

Reinicie o container para aplicar as mudanças.

### Prowlarr

Adicione o indexador [Catálogo BeTor](https://catalogo.betor.top/guia/prowlarr/).

### Radarr

- Renomear automaticamente: Ativado
- Categoria usada no qBittorrent: movies
- Perfil de qualidade padrão: HD-1080p

### Sonarr

- Renomear automaticamente: Ativado
- Categoria usada no qBittorrent: tv
- Perfil de qualidade padrão: HD-1080p

### Jellyfin

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

### Jwbot

:::warning QR code
Não compartilhe capturas contendo o QR code.
:::

Aprenda a configurar em [jwbot](https://github.com/wagchi22/jwbot).
