# ex01 — testShell00

**Lista:** [Shell 00](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `testShell00.tar`

**Funções permitidas:** nenhuma

---

## Objetivo

Reproduzir permissões e tamanho de um arquivo dentro de um tar.

## Tarefa

Crie um arquivo `testShell00` com **40 bytes** e permissão `-r--r-xr-x` (modo 0545). Depois gere `testShell00.tar` com `tar -cf testShell00.tar testShell00 .`. O conteúdo do arquivo não é avaliado, apenas nome, tamanho e modo.

## Protótipo

```text
testShell00.tar
```

## Exemplo

```text
ls -l
-r--r-xr-x 1 hilde hilde 40 ... testShell00
```

## Dica

`yes A | head -c 40 > testShell00` cria os 40 bytes. `chmod 545 testShell00` ajusta o modo. Se o Windows ignorar o chmod, use `tar --mode=545 -cf testShell00.tar testShell00 .`. O validador local também aceita 0444 como fallback do NTFS.

## Erros comuns

- Criar o tar antes de ajustar o modo.
- Usar 0444 em vez de 0545.
- Esquecer o ponto final do comando tar (ele inclui o diretório atual).

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O script roda com `bash arquivo.sh` (ou `/bin/sh`).
- [ ] Permissões, conteúdo e saída seguem o enunciado.
- [ ] Testei com `moulinette Shell00/ex01`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
