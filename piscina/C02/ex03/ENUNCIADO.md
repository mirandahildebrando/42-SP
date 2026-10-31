# ex03 — ft_str_is_numeric

**Lista:** [C 02](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_str_is_numeric.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Reconhecer apenas dígitos.

## Tarefa

Retorne 1 se a string contiver apenas dígitos (0-9), e 0 caso contrário. String vazia retorna 1.

## Protótipo

```c
int ft_str_is_numeric(char *str);
```

## Exemplo

```text
ft_str_is_numeric("0123") -> 1; ("12a") -> 0
```

## Dica

`c >= '0' && c <= '9'`.

## Erros comuns

- Aceitar sinal ou espaço.
- Retornar 0 para vazia.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C02/ex03`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
