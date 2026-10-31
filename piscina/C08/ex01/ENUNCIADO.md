# ex01 — ft_boolean.h

**Lista:** [C 08](../README.md)  •  **Nível:** 3/3  •  **Arquivos:** `ft_boolean.h`

**Funções permitidas:** nenhuma

---

## Objetivo

Definir tipos, macros e mensagens em um header.

## Tarefa

Crie `ft_boolean.h` para compilar o main do subject. Ele precisa definir `t_bool` (int), `TRUE` (1), `FALSE` (0), `SUCCESS` (0), a macro `EVEN(nbr)` e as strings `EVEN_MSG` e `ODD_MSG` com as mensagens do enunciado, incluindo o `\n`.

## Protótipo

```c
ft_boolean.h com t_bool, TRUE, FALSE, SUCCESS, EVEN, EVEN_MSG, ODD_MSG
```

## Exemplo

```text
EVEN(42) -> verdadeiro; EVEN(41) -> falso
```

## Dica

EVEN pode ser `((nbr) % 2 == 0)`. Coloque parênteses em volta do argumento da macro.

## Erros comuns

- Não incluir `<unistd.h>` se o main usar write (o main de teste inclui).
- Esquecer o `\n` nas mensagens.
- Definir EVEN sem parênteses e quebrar com expressões.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C08/ex01`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
