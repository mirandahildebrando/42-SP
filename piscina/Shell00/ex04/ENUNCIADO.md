# ex04 — midLS

**Lista:** [Shell 00](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `midLS`

**Funções permitidas:** nenhuma

---

## Objetivo

Listar arquivos por data, com vírgulas e barras nos diretórios.

## Tarefa

Coloque no arquivo `midLS` **uma única linha de comando** que liste os arquivos e diretórios do diretório atual (sem ocultos e sem `.`/`..`), separados por vírgula, em ordem de data de modificação, com `/` no final dos diretórios. Não adicione cabeçalho, comentários ou um `main`.

## Protótipo

```text
midLS (uma linha de comando)
```

## Exemplo

```text
arquivo_novo, pasta_nova/, arquivo_antigo
```

## Dica

`ls -1tp` já coloca `/` nos diretórios e ordena por data; depois use `sed`/`tr` para as vírgulas.

## Erros comuns

- Usar `ls -l` e deixar o cabeçalho/total na saída.
- Esquecer a barra nos diretórios.
- Deixar uma vírgula sobrando no final (o validador tolera, mas o ideal é não deixar).

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O script roda com `bash arquivo.sh` (ou `/bin/sh`).
- [ ] Permissões, conteúdo e saída seguem o enunciado.
- [ ] Testei com `moulinette Shell00/ex04`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
