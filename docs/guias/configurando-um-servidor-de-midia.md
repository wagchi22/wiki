# Configurando um servidor de mídia

## Visão geral

Este guia descreve uma configuração doméstica para automatizar downloads, organizar bibliotecas e reproduzir mídia no Jellyfin.

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

## Prowlarr

- Conexões: Radarr/Sonarr
- Indexadores: [Catálogo BeTor](https://catalogo.betor.top/guia/prowlarr/)

## qBittorrent

- Interface Web: Ativado
- Modo de gerenciamento de torrents: Automático

## Radarr/Sonarr

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
  - Modo noturno para áudio: Ativado

## Notificações

Siga o passo a passo [aqui](https://github.com/wagchi22/jeliwhats-bot).
