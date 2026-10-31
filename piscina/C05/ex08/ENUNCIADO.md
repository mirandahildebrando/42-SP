# ex08 — ft_ten_queens_puzzle

**Lista:** [C 05](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `ft_ten_queens_puzzle.c`

**Funções permitidas:** `write`

---

## Objetivo

Backtracking clássico: 10 rainhas sem se atacarem.

## Tarefa

Coloque 10 rainhas em um tabuleiro 10x10, uma por coluna, sem que duas se ataquem. Imprima todas as 724 soluções, cada uma como uma sequência de 10 dígitos (a coluna da rainha em cada linha), seguidas de `\n`. Retorne o número de soluções.

## Protótipo

```c
int ft_ten_queens_puzzle(void);
```

## Exemplo

```text
Uma solução começa com 0257948136 (primeira linha na coluna 0, etc.)
```

## Dica

Recursão por coluna: teste linhas de 0 a 9, verificando coluna e diagonais (`abs(linha - linha_anterior) != abs(coluna - coluna_anterior)`). Guarde o tabuleiro em um array de 10.

## Erros comuns

- Esquecer de verificar as diagonais.
- Não imprimir o `\n` depois de cada solução.
- Retornar o número errado (são 724).
- Usar `printf` em vez de `write`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C05/ex08`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
