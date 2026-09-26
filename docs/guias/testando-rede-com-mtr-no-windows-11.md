<!-- markdownlint-disable MD040 -->

# 🛜 Testando rede com MTR no Windows 11

:::tip 💡 O que é e como usar o MTR
[Blog ServerSP](https://serversp.com.br/blog/informacoes/mtr-teste-rede-windows-linux/)
:::

## ⬇️ Instalar software

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

## ✅ Testes

Execute no terminal do Cygwin:

```
mtr -4 -r -c 500 8.8.8.8
mtr -6 -r -c 500 2001:4860:4860::8888
```

## Comparativo e outras ferramentas

| Ferramenta | O que faz | Quando usar |
| --- | --- | --- |
| __iPerf3__ | Testa velocidade e desempenho da rede. | Quando quiser medir __throughput/banda__ entre dois pontos. |
| __SmokePing__ | Monitora latência e perda de pacotes ao longo do tempo. | Quando quiser __acompanhar a estabilidade__ da rede por horas ou dias. |
| __PingPlotter__ | Mostra graficamente latência e perda em cada salto. | Quando quiser __investigar problemas de conexão__ de forma visual. |
| __MTR__ | Combina ping e traceroute continuamente. | Quando quiser __identificar em qual salto__ pode estar ocorrendo latência ou perda. |
| __WinMTR__ | Versão para Windows do conceito do MTR. | Quando estiver no __Windows__ e precisar diagnosticar problemas por salto. |
