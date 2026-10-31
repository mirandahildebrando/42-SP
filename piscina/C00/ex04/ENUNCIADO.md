# ex04 — ft_is_negative

**Lista:** [C 00](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_is_negative.c`

**Funções permitidas:** `write`

---

## Objetivo

Classificar um inteiro como negativo ou não.

## Tarefa

Escreva uma função que mostre `N` se o inteiro recebido for negativo e `P` caso contrário. Zero é não-negativo.

## Protótipo

```c
void ft_is_negative(int n);
```

## Exemplo

```text
ft_is_negative(-42); -> N
ft_is_negative(0); -> P
```

## Dica

Use um `if (n < 0)` e dois `write`, um em cada caminho.

## Erros comuns

- Tratar zero como negativo.
- Usar `printf`.
- Escrever os dois caracteres sempre.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C00/ex04`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
