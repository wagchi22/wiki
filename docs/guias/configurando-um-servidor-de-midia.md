<!-- markdownlint-disable MD040 MD031-->

# 🎬 Configurando um servidor de mídia

## ⬇️ Instalar software

:::tip 💡 Arr
Marque a opção __Install shortcuts in Startup folder__ durante a instalação.

Desative a opção __Start browser on startup__ nas configurações.
:::

- [Prowlarr](https://prowlarr.com/)
- [Radarr](https://radarr.video/)
- [Sonarr](https://sonarr.tv/)
- [Jellyfin](https://jellyfin.org/) + Webhook
- [qBittorrent](https://www.qbittorrent.org/)
- [Node.js](https://nodejs.org/pt-br) + [whatsapp-web.js](https://github.com/wwebjs/whatsapp-web.js) + [qrcode-terminal](https://github.com/gtanner/qrcode-terminal)

Opcional:

- [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) + [flaresolverr-autorun.ps1](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/flaresolverr.ps1)
- [MKVToolNix](https://mkvtoolnix.download/) (coloque no PATH) + [Python](https://www.python.org/) + [remux-media.py](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/scripts/remux.py)

## 🔎 Prowlarr

- Conexões: Radarr/Sonarr
- Indexadores: [Catálogo BeTor](https://catalogo.betor.top/guia/prowlarr/)
- Etiquetas: flaresolverr

## 🔓 FlareSolverr

- Inicio automático: Execute `flaresolverr-autorun.ps1` e instale a tarefa agendada

## 🧲 qBittorrent

- Interface Web: Ativado
- Modo de gerenciamento de torrents: Automático

## 🎞️ Radarr/Sonnar

:::tip 💡 Categorias
Altere o nome das categorias padrão do Radarr e Sonarr ao configurar o cliente de download, garantindo que os arquivos sejam baixados diretamente para o local de sua escolha.
:::

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

    - Pastas:
      ```
      {Series TitleYear}
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

## 🍿 Jellyfin

- Agrupar filmes em coleções: Ativado
- App (TV):
  - Taxa de atualização: Escala no dispositivo
  - Cor da legenda: Amarelo
  - Tamanho da legenda: 125%
  - Modo noturno para áudio: Ativado

## 🔔 Webhook WhatsApp

:::info ℹ️ Módulo qrcode-terminal
Esse módulo deve ser instalado dentro da pasta `whatsapp-web.js` sem a opção `-g`.
:::

Crie o arquivo `whatsapp-web.js\server.js` e coloque isso:

```js
console.log('Creating QR Code, please wait...');

const { Client } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

const client = new Client();

client.on('qr', (qr) => {
    console.log('QR Code created, scan with your phone:');
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.initialize();
```

Inicie o servidor:

```
node .\server.js
```
