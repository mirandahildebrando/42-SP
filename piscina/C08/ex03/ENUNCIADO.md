# ex03 — ft_point.h

**Lista:** [C 08](../README.md)  •  **Nível:** 3/3  •  **Arquivos:** `ft_point.h`

**Funções permitidas:** nenhuma

---

## Objetivo

Definir uma struct e um typedef em um header.

## Tarefa

Crie `ft_point.h` de forma que o main do subject compile e use `t_point` com os campos `x` e `y`.

## Protótipo

```c
typedef struct s_point { int x; int y; } t_point;
```

## Exemplo

```text
t_point p; set_point(&p); // p.x == 42, p.y == 21
```

## Dica

A struct precisa se chamar `s_point`? O subject usa apenas `t_point`; o typedef é o que importa. Use include guard.

## Erros comuns

- Esquecer o typedef.
- Errar o nome dos campos.
- Declarar a struct dentro de uma função.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C08/ex03`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
