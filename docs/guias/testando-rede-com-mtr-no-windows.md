# Testando rede com MTR no Windows

## Visão geral

Compile o MTR no Cygwin para analisar latência e perda de pacotes em rotas de rede.

:::tip Confiabilidade
Use cabo Ethernet em vez de Wi-Fi para reduzir interferências durante o teste.
:::

## Instalação

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

## Executar testes

No terminal do Cygwin, execute os testes IPv4 e IPv6:

```bash
mtr -4 -c 1000 -i 0.5 -n -r 8.8.8.8
mtr -6 -c 1000 -i 0.5 -n -r 2001:4860:4860::8888
```
