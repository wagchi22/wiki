<!-- markdownlint-disable MD040 -->

# Diagnosticando rede usando MTR no Windows 11

:::tip Confiabilidade dos testes
Prefira cabo Ethernet ao invés do Wi-Fi.
:::

## Instalar software

Baixe o [Cygwin](https://www.cygwin.com/) e execute no terminal:

```
setup-x86_64.exe -q -R C:\cygwin64 -s https://linorg.usp.br/cygwin/ -W -P automake,pkg-config,make,gcc-core,libncurses-devel,libjansson-devel
```

Execute no terminal do Cygwin:

```
git clone https://github.com/traviscross/mtr
cd mtr
find . -type f -not -path './.git/*' -exec sed -i 's/\r$//' {} \;
bootstrap.sh && ./configure && make
make install
echo 'export PATH="/usr/local/sbin:$PATH"' >> ~/.bashrc
```

Reinicie o terminal do Cygwin.

## Diagnósticos

Execute no terminal do Cygwin:

```
mtr -4 -r -c 100 8.8.8.8
mtr -6 -r -c 100 2001:4860:4860::8888
```
