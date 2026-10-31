# ex00 — ft_strcmp

**Lista:** [C 03](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_strcmp.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Comparar duas strings lexicograficamente.

## Tarefa

Compare `s1` e `s2` byte a byte (como `unsigned char`) e retorne um valor negativo, zero ou positivo se `s1` for menor, igual ou maior que `s2`.

## Protótipo

```c
int ft_strcmp(char *s1, char *s2);
```

## Exemplo

```text
ft_strcmp("abc", "abd") < 0; ("abc", "abc") == 0
```

## Dica

Percorra enquanto os caracteres forem iguais e não chegar ao fim; retorne a diferença dos bytes.

## Erros comuns

- Comparar assinado e tratar acentos como negativos.
- Retornar apenas -1/0/1 (o subject aceita sinal, mas a diferença é mais fiel).
- Acessar depois do `\0`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C03/ex00`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
