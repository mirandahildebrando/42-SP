# ex07 — ft_rev_int_tab

**Lista:** [C 01](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_rev_int_tab.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Manipular um array in-place com dois índices.

## Tarefa

Escreva uma função que inverta a ordem dos elementos de um array de inteiros.

## Protótipo

```c
void ft_rev_int_tab(int *tab, int size);
```

## Exemplo

```text
[1, 2, 3, 4] -> [4, 3, 2, 1]
```

## Dica

Use dois índices (`i = 0`, `j = size - 1`) e troque até se cruzarem.

## Erros comuns

- Trocar apenas metade dos elementos.
- Estourar o array com size 0.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C01/ex07`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
