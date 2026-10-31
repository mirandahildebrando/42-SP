# ex02 — ft_putnbr

**Lista:** [C 04](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_putnbr.c`

**Funções permitidas:** `write`

---

## Objetivo

Imprimir um inteiro completo, sem printf.

## Tarefa

Mostre o inteiro `nb`, incluindo sinal e `INT_MIN`.

## Protótipo

```c
void ft_putnbr(int nb);
```

## Exemplo

```text
ft_putnbr(-42) -> -42
```

## Dica

Recursão: divida por 10, imprima o resto depois, e trate o negativo antes.

## Erros comuns

- Overflow em `-nb` com INT_MIN.
- Ordem dos dígitos invertida.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C04/ex02`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
