# C 05 — recursão e algoritmos

A lista mais temida por quem trava em recursão. Fatorial, potência, Fibonacci, primalidade e, no final, o problema das 10 rainhas com backtracking. Faça os seis primeiros até ficarem automáticos: eles aparecem em exames e rushes.

## Regras da lista

- Cabeçalho 42 e Norminette.
- Nenhuma função da libc (exceto `write` no ten_queens).
- Trate os casos inválidos exatamente como o subject pede (0, -1, etc.).
- Cuidado com overflow: teste os limites antes de multiplicar.

## Exercícios

| # | Exercício | Arquivo(s) | Permitidas |
|---|---|---|---|
| ex00 | [ft_iterative_factorial](ex00/ENUNCIADO.md) | `ft_iterative_factorial.c` | — |
| ex01 | [ft_recursive_factorial](ex01/ENUNCIADO.md) | `ft_recursive_factorial.c` | — |
| ex02 | [ft_iterative_power](ex02/ENUNCIADO.md) | `ft_iterative_power.c` | — |
| ex03 | [ft_recursive_power](ex03/ENUNCIADO.md) | `ft_recursive_power.c` | — |
| ex04 | [ft_fibonacci](ex04/ENUNCIADO.md) | `ft_fibonacci.c` | — |
| ex05 | [ft_sqrt](ex05/ENUNCIADO.md) | `ft_sqrt.c` | — |
| ex06 | [ft_is_prime](ex06/ENUNCIADO.md) | `ft_is_prime.c` | — |
| ex07 | [ft_find_next_prime](ex07/ENUNCIADO.md) | `ft_find_next_prime.c` | — |
| ex08 | [ft_ten_queens_puzzle](ex08/ENUNCIADO.md) | `ft_ten_queens_puzzle.c` | `write` |

## Como treinar esta lista

```sh
cd piscina/C05
moulinette .             # corrige a lista inteira
moulinette C05/ex00   # corrige um exercício
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
