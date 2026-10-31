# ex03 — ft_recursive_power

**Lista:** [C 05](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `ft_recursive_power.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Potência com recursão.

## Tarefa

Retorne `nb` elevado a `power` usando recursão. Expoente negativo retorna 0.

## Protótipo

```c
int ft_recursive_power(int nb, int power);
```

## Exemplo

```text
2^10 = 2 * 2^9
```

## Dica

Caso base `power == 0` retorna 1; `nb * ft_recursive_power(nb, power - 1)`.

## Erros comuns

- Não tratar power negativo antes de recursar.
- Stack overflow com expoente enorme.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C05/ex03`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
