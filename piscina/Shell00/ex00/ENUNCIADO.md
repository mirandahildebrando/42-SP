# ex00 — Z

**Lista:** [Shell 00](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `z`

**Funções permitidas:** nenhuma

---

## Objetivo

Criar um arquivo cujo conteúdo é exatamente Z e uma quebra de linha.

## Tarefa

Crie o arquivo `z` com o caractere `Z` seguido de `\n`. O comando `cat z` deve imprimir `Z` e nada mais.

## Protótipo

```text
z
```

## Exemplo

```text
cat z
Z
```

## Dica

`printf 'Z\n' > z` é o caminho mais curto. Evite `echo` se não souber como ele trata `\n`.

## Erros comuns

- Deixar um espaço depois do Z.
- Criar `Z` com maiúscula no nome do arquivo.
- Esquecer a quebra de linha final.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O script roda com `bash arquivo.sh` (ou `/bin/sh`).
- [ ] Permissões, conteúdo e saída seguem o enunciado.
- [ ] Testei com `moulinette Shell00/ex00`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
