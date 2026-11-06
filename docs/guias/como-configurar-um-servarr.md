# Como configurar um Servarr

:::info Visão geral
Guia rápido de instalação do Servarr.
:::

## Estrutura

:::info Armazenamento
Mídias em `\media\data` e configurações em `\mnt\docker-desktop-disk\data\docker\volumes`.
:::

```text
media/
├── docker-compose.yml (pode ser apagado após deploy)
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

Salve o arquivo [docker-compose.yml](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/docs/guias/scripts/docker-compose.yml).

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
- Algoritmo downmix estéreo: NightmodeDialogue
- Aumento do áudio ao executar downmix: 3
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

Para conectar o WhatsApp, abra o Windows Terminal, maximize a janela e execute:

```powershell
docker restart jwbot
docker logs -f jwbot
```

Escaneie o QR code exibido nos logs usando o app WhatsApp do celular. Se o código expirar, aguarde o próximo ou reinicie o container para gerar outro.
