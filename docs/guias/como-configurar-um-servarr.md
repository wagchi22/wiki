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
- Algoritmo downmix estéreo: NightmodeDialogue
- Aumento do áudio ao executar downmix: 3
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

Pré-instalado no container, aprenda a configurar em [jwbot](https://github.com/wagchi22/jwbot).

Para conectar o WhatsApp, abra o Windows Terminal, maximize a janela e execute:

```powershell
docker restart jwbot
docker logs -f jwbot
```

Escaneie o QR code exibido nos logs em **WhatsApp → Aparelhos conectados → Conectar aparelho**. Se o código expirar, aguarde o próximo ou reinicie o container para gerar outro. Não compartilhe capturas dos logs enquanto um QR code estiver visível: ele pode ser usado para conectar à sessão do WhatsApp.
