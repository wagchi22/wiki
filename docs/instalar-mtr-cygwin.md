<!-- markdownlint-disable MD040 -->

# Instalar MTR Cygwin

:::info Objetivo
Este guia descreve como instalar e compilar o MTR no Windows utilizando o ambiente Cygwin com suporte a:

- IPv4
- IPv6
- ASN (Sistema Autônomo)
- Relatórios estatísticos
- Medição de perda, latência e jitter
:::

## Fontes

- [Gemini](https://gemini.google.com/)

## Instalar o Cygwin

Baixe o instalador oficial do Cygwin [aqui](https://www.cygwin.com/):

Utilize:

```
setup-x86_64.exe
```

Execute o instalador.

Selecione:

```
Install from Internet
```

Defina o diretório raiz:

```
C:\cygwin64
```

Escolha um mirror próximo da sua localização.

Exemplo:

```
https://linorg.usp.br/cygwin/
```

---

## Instalar pacotes necessários

Na tela de seleção de pacotes, instale:

### Ferramentas de compilação

```
gcc-core
gcc-g++
make
automake
autoconf
libtool
pkg-config
```

### Dependências do MTR

```
libncurses-devel
libjansson-devel
```

### Ferramentas auxiliares

```
git
dos2unix
```

---

## Validar instalação do Cygwin

Abra o:

```
Cygwin64 Terminal
```

Teste:

```bash
gcc --version
```

```bash
make --version
```

```bash
git --version
```

```bash
pkg-config --version
```

Os comandos devem retornar as versões instaladas.

---

## Configurar o Git

O Cygwin utiliza arquivos no padrão Unix (LF).
Configure o Git para não converter finais de linha:

```bash
git config --global core.autocrlf false
```

---

## Baixar o código-fonte do MTR

No terminal Cygwin:

```bash
cd ~
```

Clone o repositório oficial:

```bash
git clone https://github.com/traviscross/mtr.git
```

Entre no diretório:

```bash
cd mtr
```

---

## Corrigir arquivos CRLF (se necessário)

Caso apareçam erros como:

```
$'\r': command not found
```

converta os arquivos:

```bash
find . -type f -exec dos2unix {} \;
```

Verifique um script:

```bash
file build-aux/git-version-gen
```

Resultado esperado:

```
POSIX shell script, ASCII text executable
```

---

## Gerar arquivos de compilação

Execute:

```bash
./bootstrap.sh
```

Uma execução correta apresenta mensagens semelhantes:

```
configure.ac: installing ...
Makefile.am: installing ...
```

---

## Configurar a compilação

Execute:

```bash
./configure
```

Verifique se o suporte necessário está habilitado:

```
ipv6     :yes
ipinfo   :yes
ncursesw :yes
jansson  :yes
```

Exemplo:

```
build options:
--------------
ipv6     :yes
braille  :yes
ipinfo   :yes
ncursesw :yes
jansson  :yes
--------------
```

---

## Compilar o MTR

Compile utilizando todos os núcleos disponíveis:

```bash
make -j$(nproc)
```

Ao final devem existir:

```
mtr.exe
mtr-packet.exe
```

---

## Testar o binário

Verifique a versão:

```bash
./mtr --version
```

Exemplo:

```
mtr 0.96
```

---

## Testes IPv4 e IPv6

### IPv4

Modo interativo:

```bash
./mtr -4 google.com
```

Relatório:

```bash
./mtr -4 -r -c 100 google.com
```

---

### IPv6

Modo interativo:

```bash
./mtr -6 google.com
```

Relatório:

```bash
./mtr -6 -r -c 100 google.com
```

---

## Exibir ASN dos saltos

O parâmetro:

```
-z
```

habilita a identificação de Sistema Autônomo.

IPv4:

```bash
./mtr -4 -z -r -c 100 google.com
```

IPv6:

```bash
./mtr -6 -z -r -c 100 google.com
```

Exemplo de saída:

```
2.|-- operadora.example   ASXXXXX
3.|-- backbone.example    ASYYYYY
4.|-- google.example      AS15169
```

---

## Gerar relatórios comparativos

### Relatórios IPv4

```bash
./mtr -4 -z -r -c 200 -w google.com > mtr_ipv4_google.txt
```

### Relatórios IPv6

```bash
./mtr -6 -z -r -c 200 -w google.com > mtr_ipv6_google.txt
```

---

## Parâmetros principais do MTR

| Parâmetro | Função |
| --- | --- |
| `-4` | Força IPv4 |
| `-6` | Força IPv6 |
| `-z` | Exibe ASN |
| `-r` | Modo relatório |
| `-c` | Quantidade de ciclos |
| `-w` | Saída em formato largo |

---

## Comparação IPv4 x IPv6

Ao analisar os relatórios compare:

| Campo | Significado |
| --- | --- |
| Loss% | Perda de pacotes |
| Avg | Latência média |
| Best | Menor latência |
| Wrst | Maior latência |
| StDev | Variação/jitter |

Também avalie:

- Quantidade de saltos
- ASNs percorridos
- Diferenças de caminho entre IPv4 e IPv6
- Diferenças de latência

---

## Atualizar o MTR

Para atualizar o código:

```bash
cd ~/mtr
git pull
```

Depois recompilar:

```bash
./bootstrap.sh
./configure
make -j$(nproc)
```

---

## Conclusão

Após este procedimento, o Windows terá uma versão oficial do MTR
compilada via Cygwin, permitindo:

- diagnóstico avançado de rotas;
- comparação IPv4 versus IPv6;
- identificação de Sistemas Autônomos;
- análise de perda, latência e jitter.
