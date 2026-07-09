# Configurar Servidor de Mídia

:::info Objetivo
Configurar um Servidor de Mídia no Windows, usando software popular e confiável para automatizar o processo.
:::

## Locais

- Servarr: C:\ProgramData
- Torrents: E:\torrents
- Mídia: E:\media

## Software

- Recomendado:
	- [Prowlarr](https://prowlarr.com/)
	- [Radarr](https://radarr.video/)
	- [Sonarr](https://sonarr.tv/)
	- [Bazarr](https://www.bazarr.media/)
	- [Jellyfin](https://jellyfin.org/)
	- [qBittorrent](https://www.qbittorrent.org/)
- Opcional:
	- [Byparr](https://github.com/ThePhaseless/Byparr)
	- [MediaInfo](https://mediaarea.net/pt/MediaInfo)
	- [Script](https://github.com/wagchi22/meus-arquivos/blob/main/scripts/remux.py) (_Requer [python](https://www.python.org/) e [mkvmerge](https://mkvtoolnix.download/)_)

## Prowlarr

- Usuário: Coloque um nome qualquer
- Senha: Insira uma senha qualquer
- Conexões (requer Chave API): Adicione o Radarr e Sonarr
- Indexadores: [Catálogo BeTor](https://github.com/wagchi22/wiki/blob/main/scripts/catalogo-betor.yml)
- Mínimo de semeadores: 0
- Proxy: Byparr

## Byparr

- Execute: [byparr.bat](https://github.com/wagchi22/meus-arquivos/blob/main/scripts/byparr.bat)

## qBittorrent

- Interface Web: Ativado
- Usuário: Coloque um nome qualquer
- Senha: Insira uma senha qualquer
- Limite de semeadura: Parar ao alcançar 0,0
- Modo de gerenciamento de torrents: Automático

## Radarr

- Usuário: Coloque um nome qualquer
- Senha: Insira uma senha qualquer
- Conexões: Adicione o qBittorrent (_Requer Chave API_)
- Propers e repacks: Desativado
- Monitorar: Somente filme
- Perfis de qualidade: 
	- 1080p
   		- Atualizações Permitidas: Ativado
     	- Atualizar até a qualidade: Bluray-1080p
      	- Atualizar até pontuação de formato personalizado: 10000
		- Ordem e definições de qualidades: (_Retire dos grupos e os mova para o topo da lista_)
			- Bluray-1080p: 50,8/1999/2000
			- WEBDL-1080p: 12,5/1999/2000
		- Pontuações:
			- Bluray: 4000
			- WEBDL: 3000
   			- DUAL: 1500
   			- Português: 1000
			- Inglês: 500
	- 2160p
   		- Atualizações Permitidas: Ativado
     	- Atualizar até a qualidade: Bluray-1080p
      	- Atualizar até pontuação de formato personalizado: 10000
		- Ordem e definições de qualidades: (_Retire dos grupos e os mova para o topo da lista_)
			- Bluray-2160p: 102/1999/2000
			- WEBDL-2160p: 34,5/1999/2000
		- Pontuações:
			- Bluray: 4000
			- WEBDL: 3000
   			- DUAL: 1500
   			- Português: 1000
			- Inglês: 500
- Renomear automaticamente: Ativado
	- Pastas: `{Movie CleanTitle} ({Release Year})`
	- Arquivos: `{Movie.CleanTitle}.{Release.Year}.{Quality Title}.{MediaInfo VideoCodec}.{Custom.Formats}.{Mediainfo AudioChannels}`
- Formatos personalizados: Acesse [aqui](https://github.com/wagchi22/wiki/blob/main/scripts/custom-formats.json)
- Script Personalizado: `C:\ProgramData\Remux.py` e marque _ao obter; importar; atualizar; adicionar; interação manual_
- País da certificação: Brazil

## Sonarr

- Usuário: Coloque um nome qualquer
- Senha: Insira uma senha qualquer
- Conexões: Adicione o qBittorrent (_Requer Chave API_)
- Propers e repacks: Desativado
- Monitorar: Episódios ausentes
- Perfis de qualidade padrão: HD-1080p
	- Idioma: Any
	- Ordem e definições de qualidades:
		- WEBDL-1080p: 10 100 200 (_Retire todos do grupo_)
		- Bluray-1080p: 8 80 180
		- HDTV-1080p: 4 40 140
	- Pontuações:
		- Portuguese: 30
		- English: 20
		- WEBDL-1080p: 15
		- Bluray-1080p: 10
		- HDTV-1080p: 5
- Perfis de lançamentos:
	- Não deve conter: multi fullhd hdr10+ imax
- Renomear automaticamente: Ativado
	- Pastas: `{Series CleanTitle} ({Series Year})`
	- Arquivos: `{Series.CleanTitle}.S{season:00}E{episode:00}.{Episode.CleanTitle}.{Quality Title}.{MediaInfo VideoCodec}.{MediaInfo.AudioCodec}.{MediaInfo AudioChannels}`
- Formatos personalizados: Acesse [aqui](https://github.com/wagchi22/wiki/blob/main/scripts/custom-formats.json)
- Script Personalizado: `C:\ProgramData\Remux.py` e marque _ao obter; importar; atualizar; adicionar; interação manual_

## Bazarr

- Usuário: Coloque um nome qualquer
- Senha: Insira uma senha qualquer
- Conexões: Adicione o Radarr e Sonarr (_Requer Chave API_)
- Legenda padrão para nova mídia: Ativado
- Sincronização automática de legenda: Ativado
- Modificações Sub-Zero: Ative as opções principais
- Provedor de legendas: [OpenSubtitles.com](https://www.opensubtitles.com/)

## Jellyfin

- Usuário: Coloque um nome qualquer
- Senha: Insira uma senha qualquer
- Agrupar filmes em coleções: Ativado
- Cliente:
	- Taxa de atualização: No dispositivo
	- Cor de legenda: Amarelo
	- Tamanho de legenda: 125%
