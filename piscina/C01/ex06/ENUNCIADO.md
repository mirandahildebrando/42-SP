# ex06 — ft_strlen

**Lista:** [C 01](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_strlen.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Contar bytes de uma string sem usar strlen.

## Tarefa

Escreva uma função que retorne o tamanho de uma string (sem contar o `\0`).

## Protótipo

```c
int ft_strlen(char *str);
```

## Exemplo

```text
ft_strlen("42SP") -> 4
```

## Dica

Um contador e um `while (str[i]) i++;`.

## Erros comuns

- Contar o terminador nulo.
- Usar `strlen` (proibido).

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C01/ex06`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
