<!-- markdownlint-disable MD040 -->

# Instalar MTR Cygwin

:::info Objetivo
Como instalar e compilar o MTR no Windows utilizando o ambiente Cygwin com suporte a análises e diagnóstico avançado de rede.
:::

## Instalar o Cygwin

Baixe o Cygwin [aqui](https://www.cygwin.com/) e depois instale.

## Instalar pacotes necessários

Execute no terminal:

```
setup-x86_64.exe -q -P gcc-core,gcc-g++,make,automake,autoconf,libtool,pkg-config,libncurses-devel,libjansson-devel,git,dos2unix
```

## Instalar o MTR

Execute no terminal do Cygwin:

```
cd ~
git config --global core.autocrlf false
git clone https://github.com/traviscross/mtr.git
cd ~/mtr
find . -type f -exec dos2unix {} \;
./bootstrap.sh
./configure
make -j"$(nproc)"
```

## Atualizar o MTR

Execute no terminal do Cygwin:

```
cd ~/mtr
git pull
find . -type f -exec dos2unix {} \;
./bootstrap.sh
./configure
make -j"$(nproc)"
```
