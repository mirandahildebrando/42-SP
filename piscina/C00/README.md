# C 00 — write, loops e ASCII

A primeira lista da piscina. Aqui você aprende a usar apenas `write` para falar com o terminal, a construir loops simples e a pensar em cada caractere como um byte. Não use `printf`, `puts` ou funções da libc: a graça é fazer tudo na mão.

## Regras da lista

- Todos os arquivos precisam do cabeçalho 42 (rode `42header arquivo.c`).
- Norminette deve passar: tabs, 25 linhas por função, 80 colunas, etc.
- Compile com `gcc -Wall -Wextra -Werror`.
- Nenhum `main` nos exercícios de função.
- Só é permitido usar `write` (e mais nada da libc).

## Exercícios

| # | Exercício | Arquivo(s) | Permitidas |
|---|---|---|---|
| ex00 | [ft_putchar](ex00/ENUNCIADO.md) | `ft_putchar.c` | `write` |
| ex01 | [ft_print_alphabet](ex01/ENUNCIADO.md) | `ft_print_alphabet.c` | `write` |
| ex02 | [ft_print_reverse_alphabet](ex02/ENUNCIADO.md) | `ft_print_reverse_alphabet.c` | `write` |
| ex03 | [ft_print_numbers](ex03/ENUNCIADO.md) | `ft_print_numbers.c` | `write` |
| ex04 | [ft_is_negative](ex04/ENUNCIADO.md) | `ft_is_negative.c` | `write` |
| ex05 | [ft_print_comb](ex05/ENUNCIADO.md) | `ft_print_comb.c` | `write` |
| ex06 | [ft_print_comb2](ex06/ENUNCIADO.md) | `ft_print_comb2.c` | `write` |
| ex07 | [ft_putnbr](ex07/ENUNCIADO.md) | `ft_putnbr.c` | `write` |
| ex08 | [ft_print_combn](ex08/ENUNCIADO.md) | `ft_print_combn.c` | `write` |

## Como treinar esta lista

```sh
cd piscina/C00
moulinette .             # corrige a lista inteira
moulinette C00/ex00   # corrige um exercício
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
