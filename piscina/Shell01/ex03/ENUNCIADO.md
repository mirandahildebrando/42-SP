# ex03 — count_files

**Lista:** [Shell 01](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `count_files.sh`

**Funções permitidas:** nenhuma

---

## Objetivo

Contar arquivos e diretórios recursivamente, incluindo o ponto.

## Tarefa

Crie `count_files.sh`, um script que conte e mostre o número de arquivos regulares e diretórios no diretório atual e em todos os subdiretórios, incluindo o diretório inicial `.`.

## Protótipo

```c
count_files.sh
```

## Exemplo

```text
./count_files.sh | cat -e
42$
```

## Dica

`find . | wc -l` conta todas as entradas, inclusive `.`. A saída deve ser só o número.

## Erros comuns

- Contar apenas arquivos regulares.
- Não incluir o diretório inicial.
- Deixar espaços antes do número.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette Shell01/ex03`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
