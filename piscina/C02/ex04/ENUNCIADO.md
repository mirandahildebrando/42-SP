# ex04 — ft_str_is_lowercase

**Lista:** [C 02](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_str_is_lowercase.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Reconhecer somente minúsculas.

## Tarefa

Retorne 1 se a string contiver apenas letras minúsculas, e 0 caso contrário. String vazia retorna 1.

## Protótipo

```c
int ft_str_is_lowercase(char *str);
```

## Exemplo

```text
ft_str_is_lowercase("abc") -> 1; ("aBc") -> 0
```

## Dica

`c >= 'a' && c <= 'z'`.

## Erros comuns

- Aceitar maiúsculas.
- Aceitar números.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C02/ex04`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
