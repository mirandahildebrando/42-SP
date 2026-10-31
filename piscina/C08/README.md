# C 08 — headers, macros e structs

A última lista de C da piscina junta tudo: arquivos de cabeçalho, include guards, macros, typedefs, structs e arrays de structs com alocação. É a ponte para o projeto libft. Aqui o `#include "..."` e os protótipos precisam estar perfeitos.

## Regras da lista

- Cabeçalho 42 em todos os arquivos (norminette com -R CheckForbiddenSourceHeader).
- Include guards em todos os headers: `#ifndef`, `#define`, `#endif`.
- Header não compila sozinho: apenas declara tipos e protótipos.
- Structs e typedefs exatamente como o subject pede.
- Nos exercícios 04 e 05, o header ft_stock_str.h é fornecido.

## Exercícios

| # | Exercício | Arquivo(s) | Permitidas |
|---|---|---|---|
| ex00 | [ft.h](ex00/ENUNCIADO.md) | `ft.h` | — |
| ex01 | [ft_boolean.h](ex01/ENUNCIADO.md) | `ft_boolean.h` | — |
| ex02 | [ft_abs.h](ex02/ENUNCIADO.md) | `ft_abs.h` | — |
| ex03 | [ft_point.h](ex03/ENUNCIADO.md) | `ft_point.h` | — |
| ex04 | [ft_strs_to_tab](ex04/ENUNCIADO.md) | `ft_strs_to_tab.c` | `malloc`, `free` |
| ex05 | [ft_show_tab](ex05/ENUNCIADO.md) | `ft_show_tab.c` | `write` |

## Como treinar esta lista

```sh
cd piscina/C08
moulinette .             # corrige a lista inteira
moulinette C08/ex00   # corrige um exercício
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
