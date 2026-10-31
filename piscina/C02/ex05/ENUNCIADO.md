# ex05 — ft_str_is_uppercase

**Lista:** [C 02](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_str_is_uppercase.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Reconhecer somente maiúsculas.

## Tarefa

Retorne 1 se a string contiver apenas letras maiúsculas, e 0 caso contrário. String vazia retorna 1.

## Protótipo

```c
int ft_str_is_uppercase(char *str);
```

## Exemplo

```text
ft_str_is_uppercase("ABC") -> 1; ("AbC") -> 0
```

## Dica

`c >= 'A' && c <= 'Z'`.

## Erros comuns

- Aceitar minúsculas.
- Aceitar números.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C02/ex05`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
