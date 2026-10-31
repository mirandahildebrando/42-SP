# ex01 — ft_strncmp

**Lista:** [C 03](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_strncmp.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Comparar no máximo n bytes.

## Tarefa

Compare no máximo `n` caracteres de `s1` e `s2`, retornando o sinal da diferença.

## Protótipo

```c
int ft_strncmp(char *s1, char *s2, unsigned int n);
```

## Exemplo

```text
ft_strncmp("abc", "abd", 2) == 0
```

## Dica

Pare quando `i == n` ou quando um dos caracteres for `\0`.

## Erros comuns

- Ignorar o limite n.
- Comparar n+1 bytes.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C03/ex01`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
