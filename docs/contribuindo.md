# Contribuindo

Esta wiki cresce melhor quando cada artigo mantém um padrão simples, útil e fácil de consultar.

## Padrão recomendado

Todo guia novo deve seguir esta estrutura:

1. Visão geral
2. Pré-requisitos
3. Passo a passo
4. Configurações relevantes
5. Troubleshooting

## Template base

Use o [Template de guia](./templates/guia-template) como referência para novos documentos.

## Boas práticas

- escreva em português claro
- mantenha instruções objetivas
- prefira exemplos reais e verificáveis
- se houver passos sensíveis, destaque riscos e validações
- atualize a documentação quando houver mudança de ferramenta ou ambiente

## Validação local

Antes de finalizar, rode:

```bash
npm run docs:build
```

Isso confirma que a wiki continua renderizando corretamente sem publicar em nuvem.
