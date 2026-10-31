# ex08 — ft_sort_int_tab

**Lista:** [C 01](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_sort_int_tab.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Ordenar um array in-place (bubble/selection/insertion).

## Tarefa

Escreva uma função que ordene um array de inteiros em ordem crescente.

## Protótipo

```c
void ft_sort_int_tab(int *tab, int size);
```

## Exemplo

```text
[3, 1, 4, 1, 5] -> [1, 1, 3, 4, 5]
```

## Dica

Bubble sort é suficiente: dois loops e uma troca. Cuide do size 0.

## Erros comuns

- Esquecer de repetir as passagens.
- Acessar `tab[j + 1]` quando j chega ao fim.
- Não tratar arrays já ordenados (não é erro, mas faça o loop terminar).

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C01/ex08`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
