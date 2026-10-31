# ex02 — ft_swap

**Lista:** [C 01](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_swap.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Trocar dois valores usando uma variável temporária.

## Tarefa

Escreva uma função que troque os valores apontados por `a` e `b`.

## Protótipo

```c
void ft_swap(int *a, int *b);
```

## Exemplo

```text
int a = 1, b = 2; ft_swap(&a, &b); // a == 2, b == 1
```

## Dica

Salve `*a` em um `int tmp` antes de sobrescrever.

## Erros comuns

- Trocar os ponteiros em vez dos valores.
- Esquecer a variável temporária e perder um dos valores.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C01/ex02`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
