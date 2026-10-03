# Referências rápidas

Comandos e ajustes recorrentes. Para instruções completas, consulte os [guias](./inicio).

## Winget

Verificar atualizações:

```powershell
winget upgrade
```

Instalar tudo disponível:

```powershell
winget upgrade -r
```

## Diagnóstico de rede com MTR

Comandos de teste IPv4 e IPv6. Veja a [instalação e uso no Windows](./guias/testando-rede-com-mtr-no-windows):

```bash
mtr -4 -c 1000 -i 0.5 -n -r 8.8.8.8
mtr -6 -c 1000 -i 0.5 -n -r 2001:4860:4860::8888
```

## Configuração de rede

- use Wi-Fi Analyzer para escolher canais menos congestionados
- em redes 2.4 GHz, canais 1, 6 e 11 costumam ser os mais estáveis
- em redes 5 GHz, faixas 36-48 e 149-161 normalmente funcionam bem

## Ajustes de imagem

- modo imagem: padrão ou jogos
- consulte [Ajustes de dispositivos](./guias/ajustes-de-dispositivos) para as demais configurações
