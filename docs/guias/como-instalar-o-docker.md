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
Leia o guia do [itexto](https://insights.itexto.com.br/o-guia-do-wsl/).
:::

Ative a opção para **Iniciar com o Windows** nas configurações do aplicativo.

Rode no terminal como administrador:

```powershell
# Exclui a pasta do disco virtual do Docker no Windows Defender
Add-MpPreference -ExclusionPath "$env:LOCALAPPDATA\Docker\wsl\disk"

# Exclui os processos do WSL no Windows Defender
Add-MpPreference -ExclusionProcess "vmmemWSL"
Add-MpPreference -ExclusionProcess "wsl"
Add-MpPreference -ExclusionProcess "wslhost"
Add-MpPreference -ExclusionProcess "wslrelay"
Add-MpPreference -ExclusionProcess "wslservice"

# Limita recursos do WSL2 (2 CPUs, 2 GB de RAM, sem swap)
"[wsl2]`nprocessors=2`nmemory=2GB`nswap=0" | Set-Content -Path "$env:USERPROFILE\.wslconfig" -Encoding ASCII
```

## Manutenção

Rode no terminal como administrador:

```powershell
# Fazer limpeza
docker system prune -a
docker builder prune -a

# Compactar disco
wsl --shutdown
diskpart
select vdisk file="$env:LOCALAPPDATA\Docker\wsl\disk\docker_data.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
```
