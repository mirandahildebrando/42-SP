# ex05 — ft_putstr

**Lista:** [C 01](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_putstr.c`

**Funções permitidas:** `write`

---

## Objetivo

Percorrer uma string até o terminador nulo.

## Tarefa

Escreva uma função que mostre, um a um, os caracteres de uma string.

## Protótipo

```c
void ft_putstr(char *str);
```

## Exemplo

```text
ft_putstr("42SP");  ->  42SP
```

## Dica

`while (*str) write(1, str++, 1);`

## Erros comuns

- Usar `printf` ou `puts`.
- Esquecer de avançar o ponteiro.
- Tentar imprimir o `\0`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C01/ex05`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
