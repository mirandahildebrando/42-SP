# ex00 — ft_putchar

**Lista:** [C 00](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_putchar.c`

**Funções permitidas:** `write`

---

## Objetivo

Escrever um único caractere na saída padrão.

## Tarefa

Escreva uma função que receba um caractere e o envie para a saída padrão usando `write(1, &c, 1)`.

## Protótipo

```c
void ft_putchar(char c);
```

## Exemplo

```text
ft_putchar('A');  ->  A
```

## Dica

`write` recebe o endereço do byte: `write(1, &c, 1)`. Confira o retorno de `write`? Na piscina, o retorno é ignorado sem problema.

## Erros comuns

- Usar `printf` ou `putchar` (proibido).
- Esquecer o `#include <unistd.h>`.
- Passar `c` em vez de `&c` para `write`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C00/ex00`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
