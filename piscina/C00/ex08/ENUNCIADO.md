# ex08 — ft_print_combn

**Lista:** [C 00](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_print_combn.c`

**Funções permitidas:** `write`

---

## Objetivo

Generalizar ft_print_comb para qualquer n de 1 a 9.

## Tarefa

Escreva uma função que mostre todas as combinações de `n` dígitos em ordem crescente, separadas por `, `, sem repetição. `n` estará entre 1 e 9.

## Protótipo

```c
void ft_print_combn(int n);
```

## Exemplo

```text
n=2 -> 01, 02, ..., 89
n=3 -> 012, 013, ..., 789
```

## Dica

Recursão é o caminho natural: escolha o próximo dígito sempre maior que o anterior. Guarde os dígitos em um array de 10 e imprima quando o array estiver cheio. Para o separador, imprima antes de cada combinação, exceto na primeira.

## Erros comuns

- Não tratar n=1.
- Estourar o buffer de dígitos.
- Separador errado ou combinações fora de ordem.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C00/ex08`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
