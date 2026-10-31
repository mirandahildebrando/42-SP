# C 01 — ponteiros e arrays

A lista que separa quem entendeu ponteiros de quem só decorou. Aqui você passa endereços, modifica valores na função chamadora e percorre arrays com aritmética de ponteiros. Desenhe a memória no papel antes de codar: vale mais que qualquer vídeo.

## Regras da lista

- Cabeçalho 42 em todos os arquivos.
- Nada de `main` nos exercícios de função.
- Use apenas `write` quando o exercício pedir saída (ft_putstr).
- Nunca acesse fora dos limites do array.
- Norminette: no máximo 25 linhas por função e 4 parâmetros.

## Exercícios

| # | Exercício | Arquivo(s) | Permitidas |
|---|---|---|---|
| ex00 | [ft_ft](ex00/ENUNCIADO.md) | `ft_ft.c` | — |
| ex01 | [ft_ultimate_ft](ex01/ENUNCIADO.md) | `ft_ultimate_ft.c` | — |
| ex02 | [ft_swap](ex02/ENUNCIADO.md) | `ft_swap.c` | — |
| ex03 | [ft_div_mod](ex03/ENUNCIADO.md) | `ft_div_mod.c` | — |
| ex04 | [ft_ultimate_div_mod](ex04/ENUNCIADO.md) | `ft_ultimate_div_mod.c` | — |
| ex05 | [ft_putstr](ex05/ENUNCIADO.md) | `ft_putstr.c` | `write` |
| ex06 | [ft_strlen](ex06/ENUNCIADO.md) | `ft_strlen.c` | — |
| ex07 | [ft_rev_int_tab](ex07/ENUNCIADO.md) | `ft_rev_int_tab.c` | — |
| ex08 | [ft_sort_int_tab](ex08/ENUNCIADO.md) | `ft_sort_int_tab.c` | — |

## Como treinar esta lista

```sh
cd piscina/C01
moulinette .             # corrige a lista inteira
moulinette C01/ex00   # corrige um exercício
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
