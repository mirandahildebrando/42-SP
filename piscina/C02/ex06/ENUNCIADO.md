# ex06 — ft_str_is_printable

**Lista:** [C 02](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_str_is_printable.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Reconhecer caracteres imprimíveis da tabela ASCII.

## Tarefa

Retorne 1 se a string contiver apenas caracteres imprimíveis (32 a 126), e 0 caso contrário. String vazia retorna 1.

## Protótipo

```c
int ft_str_is_printable(char *str);
```

## Exemplo

```text
ft_str_is_printable("Hello 42!") -> 1; ("a\tb") -> 0
```

## Dica

`c >= 32 && c <= 126`. Não use `isprint`.

## Erros comuns

- Aceitar `\n` ou `\t`.
- Confundir 127 (DEL) com imprimível.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C02/ex06`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
