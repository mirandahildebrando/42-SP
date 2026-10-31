# ex01 — ft_recursive_factorial

**Lista:** [C 05](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `ft_recursive_factorial.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Fatorial recursivo e caso base.

## Tarefa

Retorne o fatorial de `nb` usando recursão. Negativo retorna 0.

## Protótipo

```c
int ft_recursive_factorial(int nb);
```

## Exemplo

```text
5! = 5 * 4!
```

## Dica

`if (nb < 0) return 0; if (nb <= 1) return 1; return nb * ft_recursive_factorial(nb - 1);`

## Erros comuns

- Esquecer o caso base (stack overflow).
- Chamar com nb - 1 sem limite.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C05/ex01`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
