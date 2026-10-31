# ex04 — ft_putnbr_base

**Lista:** [C 04](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_putnbr_base.c`

**Funções permitidas:** `write`

---

## Objetivo

Imprimir um número em qualquer base.

## Tarefa

Mostre `nbr` na base representada por `base`. A base define os símbolos e o tamanho. Números negativos começam com `-`. Considere a base sempre válida.

## Protótipo

```c
void ft_putnbr_base(int nbr, char *base);
```

## Exemplo

```text
42 na base "01" -> 101010; -42 na base decimal -> -42
```

## Dica

Descubra o tamanho da base, trate o sinal e use recursão com `% base_len` e `/ base_len`.

## Erros comuns

- Assumir base 10.
- Não tratar negativo.
- Overflow com INT_MIN.
- Imprimir o dígito antes da recursão (ordem invertida).

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C04/ex04`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
