# ex05 — ft_print_comb

**Lista:** [C 00](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_print_comb.c`

**Funções permitidas:** `write`

---

## Objetivo

Gerar todas as combinações crescentes de 3 dígitos.

## Tarefa

Escreva uma função que mostre todas as combinações diferentes de três dígitos em ordem crescente, separadas por `, `, sem repetir a mesma combinação em ordem diferente. A menor é `012` e a maior é `789`.

## Protótipo

```c
void ft_print_comb(void);
```

## Exemplo

```text
012, 013, 014, ..., 789
```

## Dica

Três loops aninhados (a < b < c). Para imprimir os três dígitos sem repetir código, crie uma função auxiliar `ft_putchar` no mesmo arquivo (permitido).

## Erros comuns

- Imprimir vírgula depois da última combinação.
- Gerar combinações repetidas (ex.: 012 e 021).
- Usar `printf`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C00/ex05`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
