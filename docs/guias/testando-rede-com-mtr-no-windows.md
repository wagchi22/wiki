# Testando rede com MTR no Windows

:::tip Confiabilidade
Use cabo Ethernet ao invés do Wi-Fi.
:::

## MTR

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

Reinicie o terminal do Cygwin e execute:

```
mtr -4 -c 1000 -i 0.5 -n -r 8.8.8.8
mtr -6 -c 1000 -i 0.5 -n -r 2001:4860:4860::8888
```
