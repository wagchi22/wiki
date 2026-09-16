<!-- markdownlint-disable MD040 MD031-->

# Configurar Mediaserver

:::info Objetivo
Configurar um Servidor de Mídia no Windows, usando software popular e confiável
para automatizar o processo.
:::

## Software

:::tip Servarr
Ao instalar, marque a opção __Install shortcuts in Startup folder__.

Depois desative __Start browser on startup__ nas configurações.
:::

Necessário:

- Instale [Prowlarr](https://prowlarr.com/)
- Instale [Radarr](https://radarr.video/)
- Instale [Sonarr](https://sonarr.tv/)
- Instale [Jellyfin](https://jellyfin.org/)
- Instale [qBittorrent](https://www.qbittorrent.org/)

Opcional:

- Baixe [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) em C:\Tools
- Instale [Python](https://www.python.org/)
- Baixe [MKVToolNix](https://mkvtoolnix.download/) em C:\Tools e insira no PATH
- Baixe [flaresolverr.ps1](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/flaresolverr.ps1) em C:\Scripts
- Baixe [remux.py](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/remux.py) em C:\Scripts

## Prowlarr

- Conexões: Radarr/Sonarr
- Indexadores: [Catálogo BeTor](https://catalogo.betor.top/guia/prowlarr/)
- Etiquetas: flaresolverr

## FlareSolverr

- Inicio automático: Execute e instale C:\Scripts\flaresolverr.ps1

## qBittorrent

- Interface Web: Ativado
- Modo de gerenciamento de torrents: Automático
- Layout do conteúdo do torrent: Não criar sub-pasta

## Radarr/Sonnar

:::tip Categorias
Altere o nome das categorias padrão do Radarr e Sonarr ao configurar o cliente de download, garantindo que os arquivos sejam baixados diretamente para o local de sua escolha.
:::

- Cliente de download: qBittorrent
- Renomear automaticamente: Ativado
  - Filmes:

    ```
    {Movie Title} ({Release Year}) {Custom Formats} {MediaInfo VideoCodec} {MediaInfo AudioCodec} {MediaInfo AudioChannels}
    ```

  - Séries:

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
- Conexões: Script C:\Scripts\remux.py e marque obter, importar e atualizar

## Jellyfin

- Agrupar filmes em coleções: Ativado
- Algoritmo de downmix estéreo: NightmodeDialogue
- App (TV):
  - Taxa de atualização: Escala no dispositivo
  - Saída de áudio: Downmix para estéreo
  - Cor da legenda: Amarelo
  - Tamanho da legenda: 125%
