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

- Baixe [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) em __C:\Tools__
- Instale [Python](https://www.python.org/)
- Baixe [MKVToolNix](https://mkvtoolnix.download/) em __C:\Tools__ e insira no PATH
- Baixe [flaresolverr.ps1](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/flaresolverr.ps1) em __C:\Scripts__
- Baixe [remux.py](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/remux.py) em __C:\Scripts__

## Prowlarr

- Conexões: Radarr/Sonarr
- Indexadores: [Catálogo BeTor](https://catalogo.betor.top/guia/prowlarr/)
- Etiquetas: __flaresolverr__

## FlareSolverr

- Inicio automático: Execute e instale __C:\Scripts\flaresolverr.ps1__

## qBittorrent

- Interface Web: Ativado
- Modo de gerenciamento de torrents: Automático
- Limites de velocidade:
  - Download: 15 MB/s
  - Upload: 5 MB/s

## Radarr/Sonnar

:::tip Categorias
Altere o nome das categorias padrão utilizadas pelo Radarr e Sonarr ao configurar o cliente de download neles. Isso garante que os arquivos sejam baixados diretamente para o local de sua escolha ao invés de uma pasta separada.
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
- Conexões: Marque __Ao obter__, __Ao importar__, __Ao atualizar__ e o caminho __C:\Scripts\remux.py__

## Jellyfin

- Agrupar filmes em coleções: Ativado
- Transcodificação por hardware: Intel QSV
- Codificador de hardware Intel H.264 de baixo processamento: Ativado
- Limitar transcodificação: Ativado
- App (TV):
  - Taxa de atualização: Escala no dispositivo
  - Saída de áudio: Downmix para estéreo
  - Cor da legenda: Amarelo
  - Tamanho da legenda: 125%
