# Configurando um servidor de mídia

## Visão geral

Este guia descreve uma configuração doméstica para automatizar downloads, organizar bibliotecas e reproduzir mídia no Jellyfin. Os componentes são:

- `Prowlarr` para pesquisa de indexadores
- `qBittorrent` para downloads
- `Radarr` e `Sonarr` para organização de filmes e séries
- `Jellyfin` para reprodução e biblioteca
- `FlareSolverr` para facilitar acesso a indexadores
- `jeliwhats-bot` para notificações via WhatsApp para acompanhar eventos

## Checklist rápido

Antes de começar, confirme:

- acesso administrativo no Windows
- espaço suficiente em disco para downloads e biblioteca final
- um cliente de torrent funcional
- um processo para monitorar downloads e renomeações

## Instalação

:::tip Arr
Instale os atalhos na pasta de inicialização e desative o início automático nas configurações.
:::

- [Prowlarr](https://prowlarr.com/)
- [Radarr](https://radarr.video/)
- [Sonarr](https://sonarr.tv/)
- [Jellyfin](https://jellyfin.org/)
- [qBittorrent](https://www.qbittorrent.org/)
- [jeliwhats-bot](https://github.com/wagchi22/jeliwhats-bot)

Opcional:

- [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) + [flaresolverr-autorun.ps1](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/flaresolverr.ps1)
- [MKVToolNix](https://mkvtoolnix.download/) colocando no PATH + [Python](https://www.python.org/) + [remux-media.py](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/remux.py)

## Prowlarr

- Conexões: Radarr/Sonarr
- Indexadores: [Catálogo BeTor](https://catalogo.betor.top/guia/prowlarr/)
- Etiquetas: flaresolverr

## FlareSolverr

- Inicio automático: Execute `flaresolverr-autorun.ps1` e instale a tarefa agendada

## qBittorrent

- Interface Web: Ativado
- Modo de gerenciamento de torrents: Automático

## Radarr/Sonnar

- Cliente de download: qBittorrent
- Renomear automaticamente: Ativado
  - Filmes:
    - Arquivos:

      ```
      {Movie Title} ({Release Year}) {Custom Formats} {MediaInfo VideoCodec} {MediaInfo AudioCodec} {MediaInfo AudioChannels}
      ```

  - Séries:
    - Arquivos:

      ```
      {Series Title} S{season:00}E{episode:00} {Episode Title} {Custom Formats} {MediaInfo VideoCodec} {MediaInfo AudioCodec} {MediaInfo AudioChannels}
      ```

- Formatos personalizados:
  - Filmes:

    :::details Exibir
    ```json
    {
      "name": "Bluray 1080p",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "Fonte",
          "implementation": "SourceSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": 9
          }
        },
        {
          "name": "Resolução",
          "implementation": "ResolutionSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": 1080
          }
        }
      ]
    }
    ```

    ```json
    {
      "name": "WEB-Rip 1080p",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "Fonte",
          "implementation": "SourceSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": 8
          }
        },
        {
          "name": "Resolução",
          "implementation": "ResolutionSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": 1080
          }
        }
      ]
    }
    ```

    ```json
    {
      "name": "Dual Áudio",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "Idioma",
          "implementation": "LanguageSpecification",
          "negate": false,
          "required": true,
          "fields": {
            "value": 1,
            "exceptLanguage": false
          }
        },
        {
          "name": "Idioma",
          "implementation": "LanguageSpecification",
          "negate": false,
          "required": true,
          "fields": {
            "value": 18,
            "exceptLanguage": false
          }
        }
      ]
    }
    ```

    ```json
    {
      "name": "Dublado",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "Idioma",
          "implementation": "LanguageSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": 30,
            "exceptLanguage": false
          }
        }
      ]
    }
    ```

    ```json
    {
      "name": "Legendado",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "Idioma",
          "implementation": "LanguageSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": -2,
            "exceptLanguage": false
          }
        }
      ]
    }
    ```

    ```json
    {
      "name": "WEB-DL 1080p",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "Fonte",
          "implementation": "SourceSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": 7
          }
        },
        {
          "name": "Resolução",
          "implementation": "ResolutionSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": 1080
          }
        }
      ]
    }
    ```
    :::

  - Séries:

    :::details Exibir
    ```json
    {
      "name": "Bluray 1080p",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "Fonte",
          "implementation": "SourceSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": 6
          }
        },
        {
          "name": "Resolução",
          "implementation": "ResolutionSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": 1080
          }
        }
      ]
    }
    ```

    ```json
    {
      "name": "WEB-Rip 1080p",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "Fonte",
          "implementation": "SourceSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": 4
          }
        },
        {
          "name": "Resolução",
          "implementation": "ResolutionSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": 1080
          }
        }
      ]
    }
    ```

    ```json
    {
      "name": "Dual Áudio",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "Idioma",
          "implementation": "LanguageSpecification",
          "negate": false,
          "required": true,
          "fields": {
            "value": 1,
            "exceptLanguage": false
          }
        },
        {
          "name": "Idioma",
          "implementation": "LanguageSpecification",
          "negate": false,
          "required": true,
          "fields": {
            "value": 18,
            "exceptLanguage": false
          }
        }
      ]
    }
    ```

    ```json
    {
      "name": "Dublado",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "Idioma",
          "implementation": "LanguageSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": 33,
            "exceptLanguage": false
          }
        }
      ]
    }
    ```

    ```json
    {
      "name": "Legendado",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "Idioma",
          "implementation": "LanguageSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": -2,
            "exceptLanguage": false
          }
        }
      ]
    }
    ```

    ```json
    {
      "name": "WEB-DL 1080p",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "Fonte",
          "implementation": "SourceSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": 3
          }
        },
        {
          "name": "Resolução",
          "implementation": "ResolutionSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": 1080
          }
        }
      ]
    }
    ```
    :::

- Perfil HD-1080p:
  - Ordem de qualidades:
    - Bluray 1080p
    - WEB-DL 1080p
    - WEB-Rip 1080p
  - Atualizações Permitidas: Ativado
  - Atualizar até: Bluray-1080p
  - Atualizar até pontuação de formato personalizado: 10000
  - Pontuação:
    - Bluray 1080p: 5000
    - Dual Áudio: 5000
    - WEB-DL 1080p: 4000
    - WEB-Rip 1080p: 4000
    - Dublado: 0
    - Legendado: 0
- Conexões: Adicione o script `remux-media.py` e marque obter, importar e atualizar

## Jellyfin

- Agrupar filmes em coleções: Ativado
- Usuários:
  - Reproduzir a faixa de áudio padrão, independente do idioma: Desativado
  - Idioma do áudio: Português (Brasil)
  - Idioma da legenda: Português (Brasil)
  - Tipo de legenda: Inteligente
- App (TV):
  - Taxa de atualização: Escala no dispositivo
  - Cor da legenda: Amarelo
  - Tamanho da legenda: 125%
  - Modo noturno para áudio: Ativado

## Notificações

Siga o passo a passo [aqui](https://github.com/wagchi22/jeliwhats-bot).
