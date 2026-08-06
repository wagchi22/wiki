# Remove legendas antigas de filmes do Radarr
# Equivalente ao script Python original

$VIDEO_EXTENSIONS = @(
    ".mkv",
    ".mp4",
    ".avi",
    ".m4v"
)

$SUBTITLE_EXTENSIONS = @(
    ".srt",
    ".ass",
    ".ssa",
    ".sub"
)


function Convert-Name($name) {

    # Converte para minúsculo
    $name = $name.ToLower()

    # Remove extensão
    $name = [System.IO.Path]::GetFileNameWithoutExtension($name)

    # Remove idiomas comuns no final do nome
    $name = $name -replace "\.(pt[-_.]?br|por|pt|eng|en|spa|es)$", ""

    return $name
}


function Clean($moviePath) {

    if ([string]::IsNullOrEmpty($moviePath)) {
        Write-Host "RADARR_MOVIE_PATH não informado"
        return
    }


    $folder = $moviePath

    if (-not (Test-Path $folder -PathType Container)) {
        $folder = Split-Path $folder -Parent
    }


    if (-not (Test-Path $folder)) {
        Write-Host "Pasta não encontrada: $folder"
        return
    }


    $files = Get-ChildItem -Path $folder -File


    $videoNames = @()


    foreach ($file in $files) {

        $ext = $file.Extension.ToLower()

        if ($VIDEO_EXTENSIONS -contains $ext) {

            $videoNames += Normalize-Name $file.Name
        }
    }


    foreach ($file in $files) {

        $ext = $file.Extension.ToLower()

        if ($SUBTITLE_EXTENSIONS -notcontains $ext) {
            continue
        }


        $subtitleName = Normalize-Name $file.Name


        # Se nenhuma mídia possui o mesmo nome base,
        # considera legenda antiga

        if ($videoNames -notcontains $subtitleName) {

            $subtitlePath = $file.FullName

            Write-Host "Removendo legenda antiga: $subtitlePath"

            Remove-Item -Path $subtitlePath -Force
        }
    }
}


$moviePath = $env:RADARR_MOVIE_PATH

Clean $moviePath