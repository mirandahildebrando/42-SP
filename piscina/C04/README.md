# C 04 — números e bases

A lista da aritmética de caracteres. Você vai converter texto em inteiro, inteiro em texto e transitar entre bases numéricas. É também onde `INT_MIN` aparece para lembrar que `-2147483648` não cabe positivo em um `int`.

## Regras da lista

- Cabeçalho 42 e Norminette.
- Só `write` nos exercícios de saída; nada de `printf`.
- Bases válidas têm pelo menos 2 caracteres, sem repetição, sem `+`, `-` ou espaços.
- Cuidado com overflow: negue depois de converter para `long` ou trate `INT_MIN`.

## Exercícios

| # | Exercício | Arquivo(s) | Permitidas |
|---|---|---|---|
| ex00 | [ft_strlen](ex00/ENUNCIADO.md) | `ft_strlen.c` | — |
| ex01 | [ft_putstr](ex01/ENUNCIADO.md) | `ft_putstr.c` | `write` |
| ex02 | [ft_putnbr](ex02/ENUNCIADO.md) | `ft_putnbr.c` | `write` |
| ex03 | [ft_atoi](ex03/ENUNCIADO.md) | `ft_atoi.c` | — |
| ex04 | [ft_putnbr_base](ex04/ENUNCIADO.md) | `ft_putnbr_base.c` | `write` |
| ex05 | [ft_atoi_base](ex05/ENUNCIADO.md) | `ft_atoi_base.c` | — |

## Como treinar esta lista

```sh
cd piscina/C04
moulinette .             # corrige a lista inteira
moulinette C04/ex00   # corrige um exercício
```

O progresso detalhado fica em [PROGRESSO.md](../PROGRESSO.md).

### Ordem recomendada

1. Leia o enunciado inteiro e escreva o protótipo no papel.
2. Implemente sem pressa; compile cedo para pegar erros de sintaxe.
3. Rode `norminette` e corrija a forma **antes** de depurar a lógica.
4. Rode `moulinette` e leia a primeira falha, não todas de uma vez.
5. Quando passar, refaça o exercício de memória no dia seguinte.

---

[Voltar para a piscina](../README.md) • [Progresso](../PROGRESSO.md)
