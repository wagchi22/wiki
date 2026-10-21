# Testando rede com MTR no Windows

## Visão geral

Analisa rotas de rede ao combinar teste de latência e perda de pacotes.

:::tip Confiabilidade do teste
Use cabo Ethernet em vez de Wi-Fi para reduzir interferências durante o teste.
:::

## Opção 1 - WinMTR

Apenas baixe e execute __(recomendado)__.

:::details Exibir
Baixe o [WinMTR-](https://github.com/leeter/WinMTR-refresh) e execute.

Antes de testar, vá em em opções e desative __Resolve names__.

Em __Hosts__, insira um IP para teste e clique em __Start__.

Para um teste preciso, aguarde o envio de pelo menos 500 pacotes.
:::

## Opção 2 - MTR

Requer Cygwin e compilar o binário.

:::details Exibir
Instale o [Cygwin](https://www.cygwin.com/) com os pacotes necessários:

```bash
setup-x86_64.exe -q -R C:\cygwin64 -s https://linorg.usp.br/cygwin/ -W -P automake,pkg-config,make,gcc-core,libncurses-devel,libjansson-devel
```

No terminal do Cygwin, compile e instale o MTR:

```bash
git clone https://github.com/traviscross/mtr
cd mtr
find . -type f -not -path './.git/*' -exec sed -i 's/\r$//' {} \;
bootstrap.sh && ./configure && make
make install
echo 'export PATH="/usr/local/sbin:$PATH"' >> ~/.bashrc
```

Reinicie o terminal do Cygwin.

No terminal do Cygwin, execute os testes IPv4 e IPv6:

```bash
mtr -4 -c 1000 -i 0.5 -n -r 8.8.8.8
mtr -6 -c 1000 -i 0.5 -n -r 2001:4860:4860::8888
```
:::
