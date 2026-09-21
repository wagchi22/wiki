# Meus ajustes gerais

## TV LG

:::warning TVs de entrada e HDR
Se a TV tiver menos de 600 nits, recomenda-se desativar o HDR (pesquise `modelo-da-tv nits` no Google para descobrir).

Portanto, as opções de HDR mencionadas abaixo são recomendadas apenas para TVs que possuem HDR acima de 600 nits.
:::

:::info Backlight e Constraste em HDR
Geralmente essas duas opções devem ficar no máximo.
:::

- Local: Parede
- Propagandas na tela inicial: Desativado
- Modo de imagem: Padrão ou Jogos
  - Just Scan: Ativado
  - Backlight: 70
  - Contraste: 80
  - Brilho: 50
  - Nitidez: 10
  - Cor: 50
  - Gama: 2.2
  - Gama de cores: Automático
  - Nível de preto: Automático
  - Temperatura de cor: W2
  - Cinema Real: Ativado
  - Full LED: Baixo
  - Demais opções: Desativado
- Modo de áudio: Padrão

## Fire TV

- Igualar taxa de quadros: Ativado
- HDR: Conforme a TV
- Intensidade de cores (bits): Conforme a TV

## PlayStation 5

:::tip No jogo
Para HDR é necessário ajustar o __branco papel__ ([referência](https://nikitamgrimm.github.io/hlg-reference-white-calc/)) e __brilho máximo__ (valor máximo em nits da sua TV).

O brilho geralmente não precisa ajustar mas a regra é seguir o que é descrito sem deixar a imagem nem muito escura nem muito clara.
:::

:::warning Antes de calibrar o HDR
Defina o mapeamento de tom dinâmico na TV para HGiG.
:::

- HDR: Conforme a TV
- Calibragem HDR:
  - Etapa 1/2: [Referência](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/images/hdtvtest.jpg)
  - Etapa 3: 0

## PC Dell

- Recomendações: Desativado
- Destaques da pesquisa: Desativado
- Status da tela de bloqueio: Nenhum
- Melhorias do Waves MaxxAudioPro: Desativado
- Volume do microfone: 100
- Aprimorar precisão do mouse: Desativado
- Dados brutos do mouse (jogos): Ativado
- Desligar vídeo: 5 minutos
- Suspender: 5 horas
- IP: Estático
- DNS: [Cloudflare](https://one.one.one.one/dns/)
- Softwares:
  - [Office](https://files.rg-adguard.net/files/031460f7-375b-1168-38bd-9c6a581d8920) + [ativador](https://github.com/massgravel/Microsoft-Activation-Scripts)
  - [iCloud](https://support.apple.com/pt-br/103232)
  - [iTunes](https://www.apple.com/br/itunes/)
  - [Firefox](https://www.firefox.com/pt-BR/) + uBlock Origin e esses [filtros](https://raw.githubusercontent.com/wagchi22/wiki/refs/heads/main/images/ubo.png)
  - [VS Code](https://code.visualstudio.com/)
  - [Git](https://git-scm.com/)
  - [Node.js](https://nodejs.org/pt-br)

## iPhone

- Apps:
  - [Firefox](https://apps.apple.com/br/app/firefox-browser-privado/id989804926) e ative o adblocker
- Anti-spam:
  - [Não Me Perturbe](https://www.naomeperturbe.com.br/)
  - Filtar números desconhecidos: Perguntar motivo da ligação

## Roteador

:::tip Otimização de Sinal
Use esse [software](https://matthafner.com/wifi-analyzer)
para encontrar o melhor canal.
:::

- Local: Parede
- Band Steering: Desativado
- Rede 2.4 GHz:
  - Largura de banda: 40 MHz
  - Melhores canais: 1, 6, 11
- Rede 5 GHz:
  - Largura de banda: 80 MHz
  - Melhores canais: 36-48, 149-161

## HD Toshiba

- Tipo de partição: exFAT
