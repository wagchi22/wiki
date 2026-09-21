<!-- markdownlint-disable MD040 -->

# Corrigindo miniaturas MP4 no Windows 11

## Guia

Copie e cole o código abaixo em um arquivo de texto e salve como __fix-mp4-thumbs.reg__:

```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\.mp4\ShellEx\{BB2E617C-0920-11D1-9A0B-00C04FC2D6C1}]
@="{9DBD2C50-62AD-11D0-B806-00C04FD706EC}"

[HKEY_CLASSES_ROOT\.mp4\ShellEx\{e357fccd-a995-4576-b01f-234630154e96}]
@="{9DBD2C50-62AD-11D0-B806-00C04FD706EC}"
```

Execute o arquivo recém criado.

Reinicie o processo __Windows Explorer__.

Pode apagar o arquivo após o uso.
