<!-- markdownlint-disable MD040 -->

# Configurar Mediaserver

:::info Objetivo
Configurar um Servidor de Mídia no Windows, usando software popular e confiável
para automatizar o processo.
:::

## Software

:::tip Servarr
Ao instalar, marque a opção `Install shortcuts in Startup folder`.

Depois desative `Start browser on startup` nas configurações.
:::

- Instale [Prowlarr](https://prowlarr.com/)
- (Opcional) Baixe [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) em `C:\Tools`
- Instale [Radarr](https://radarr.video/)
- Instale [Sonarr](https://sonarr.tv/)
- Instale [Jellyfin](https://jellyfin.org/)
- Instale [qBittorrent](https://www.qbittorrent.org/)
- Instale [Python](https://www.python.org/)
- Baixe [MKVToolNix](https://mkvtoolnix.download/) em `C:\Tools` e insira no PATH
- Baixe [flaresolverr.ps1](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/flaresolverr.ps1) em `C:\Scripts`
- Baixe [remux.py](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/remux.py) em `C:\Scripts`

## Prowlarr

- Conexões: Radarr/Sonarr
- Indexadores: [Catálogo BeTor](https://catalogo.betor.top/guia/prowlarr/)
- Etiquetas: `flaresolverr`

## FlareSolverr

- Inicialização automática: Execute e instale `C:\Scripts\flaresolverr.ps1`

## qBittorrent

- Interface Web: Ativado
- Limite de semeadura: Parar ao alcançar 0,0
- Modo de gerenciamento de torrents: Automático
- Inibir sono do sistema enquanto faz download: Ativado

## Radarr/Sonnar

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

  - Séries:

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

- Perfil HD-1080p:
  - Ordem de qualides: Bluray-1080p/WEBDL-1080p
  - Atualizações Permitidas: Ativado
  - Atualizar até: Bluray-1080p
  - Atualizar até pontuação de formato personalizado: 10000
  - Pontuação:
    - Bluray 1080p: 5000
    - Dual Áudio: 5000
    - WEB-DL 10180p: 4000
    - Dublado: 0
    - Legendado: 0
- Conexões: Marque `Ao obter`, `Ao importar`, `Ao atualizar` e coloque o caminho `C:\Scripts\remux.py`

## Jellyfin

- Agrupar filmes em coleções: Ativado
- Transcodificação por hardware: Intel QSV
- Codificador de hardware Intel H.264 de baixo processamento: Ativado
- Mapeamento de tons: Ativado
- Limitar transcodificação: Ativado
- Remover segmentos: Ativado
- Wholphin (TV):
  - Taxa de atualização: Automático
  - Sempre mixar para estéreo: Ativado
  - Tamanho da legenda: 26
  - Cor da legenda: Amarelo
