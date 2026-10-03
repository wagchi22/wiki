# Soluções comuns

Diagnósticos objetivos para problemas comuns. Para comandos e ajustes de referência, consulte [Referências rápidas](./referencias-rapidas).

## Rede lenta ou instável

### Sintoma

- pings altos
- perda de pacotes
- buffering em vídeo ou instabilidade em downloads

### Diagnóstico

- compare o resultado por Wi-Fi e por cabo Ethernet
- execute os testes descritos no [guia de MTR](./guias/testando-rede-com-mtr-no-windows)
- verifique se a falha ocorre em mais de um dispositivo

### Próximo passo

Consulte as recomendações de canais em [Referências rápidas](./referencias-rapidas#configuracao-de-rede) antes de alterar a configuração do roteador.

## TV com imagem muito clara ou muito escura

### Sintoma

- imagem apagada no HDR
- brilho excessivo ou pouco contraste
- sensação de "lavada" ou muito escura

### Diagnóstico

- confirme se o modo HDR está ativo na TV e na fonte de vídeo
- confira o modo de imagem e o nível de preto
- compare o resultado com o conteúdo exibido em SDR

### Próximo passo

Consulte as configurações recomendadas em [Ajustes de dispositivos](./guias/ajustes-de-dispositivos#tv) e calibre gradualmente.

## Instalação de software no Windows

### Sintoma

- pacote não instala
- atualização falha ou ambiente fica inconsistente

### Diagnóstico

- Winget está instalado e atualizado
- permissões de administrador estão presentes
- a fonte de pacote não foi bloqueada por política de segurança

### Próximo passo

Confira a lista e o processo de atualização no guia de [Winget](./guias/gerenciando-atualizacoes-com-winget).

## Servidor de mídia sem organização correta

### Sintoma

- filmes ou séries com nomes incorretos
- arquivos duplicados ou não renomeados
- biblioteca confusa

### Diagnóstico

- cliente de download e renomeação ativos
- regras de qualidade e formato personalizadas
- leitura de media info e tags
- script de remux funcionando quando necessário

### Próximo passo

Use o [guia de configuração do servidor de mídia](./guias/configurando-um-servidor-de-midia) para conferir as conexões, regras de renomeação e organização da biblioteca.
