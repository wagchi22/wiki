# Como instalar o Docker

:::info Visão geral
Guia rápido de instalação do Docker.
:::

## Ativar o WSL

Execute no terminal como administrador:

```powershell
wsl --install
```

## Instalar o Docker

Baixe o [Docker](https://www.docker.com/products/docker-desktop/?at_exp=DO112.B0) e execute.

## Configurar o Docker

:::tip Dicas
Mais informações leia o guia do [itexto](https://insights.itexto.com.br/o-guia-do-wsl/).
:::

## Desempenho

:::warning Aviso
Desativar o Windows Defender é arriscado e pode afetar a segurança.<br>
Prossiga por sua conta e risco.
:::

Para um melhor desempenho, rode no terminal como administrador:

```powershell
# Adiciona os itens abaixo na lista de exclusões do Windows Defender
Add-MpPreference -ExclusionPath "%LOCALAPPDATA%\Docker\wsl\disk"
Add-MpPreference -ExclusionProcess "vmmemWSL"
Add-MpPreference -ExclusionProcess "wsl"
Add-MpPreference -ExclusionProcess "wslhost"
Add-MpPreference -ExclusionProcess "wslrelay"
Add-MpPreference -ExclusionProcess "wslservice"
```

## Manutenção

Rode no terminal como administrador:

```powershell
# Fazer limpeza
docker system prune -a
docker builder prune -a

# Compactar disco virtual
docker desktop stop
wsl --shutdown
diskpart
select vdisk file="%LOCALAPPDATA%\Docker\wsl\disk\docker_data.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
```
