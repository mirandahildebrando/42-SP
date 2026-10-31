# ex04 — ft_convert_base

**Lista:** [C 07](../README.md)  •  **Nível:** 3/3  •  **Arquivos:** `ft_convert_base.c`, `ft_convert_base2.c`

**Funções permitidas:** `malloc`, `free`

---

## Objetivo

Converter um número entre duas bases.

## Tarefa

Leia `nbr` na base `base_from` (com espaços e sinal, como no ft_atoi_base), converta para `int` e devolva uma string alocada na base `base_to`, com `-` se negativo. Considere as bases válidas.

## Protótipo

```c
char *ft_convert_base(char *nbr, char *base_from, char *base_to);
```

## Exemplo

```text
("42", decimal, hex) -> "2A"
```

## Dica

Separe em duas funções: atoi_base e putnbr_base em string. Calcule quantos dígitos o número precisa antes de alocar.

## Erros comuns

- Não alocar espaço para o sinal e o `\0`.
- Perder o sinal.
- Overflow com INT_MIN.
- Imprimir em vez de retornar.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C07/ex04`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
