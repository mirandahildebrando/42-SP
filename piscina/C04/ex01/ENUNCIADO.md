# ex01 — ft_putstr

**Lista:** [C 04](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_putstr.c`

**Funções permitidas:** `write`

---

## Objetivo

Imprimir uma string com write.

## Tarefa

Mostre a string recebida, caractere por caractere.

## Protótipo

```c
void ft_putstr(char *str);
```

## Exemplo

```text
ft_putstr("42SP") -> 42SP
```

## Dica

Pare no `\0`; não tente imprimi-lo.

## Erros comuns

- Usar printf.
- Loop infinito por não avançar o ponteiro.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C04/ex01`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
