# C 06 — argc e argv

Pela primeira vez você entrega programas completos, com `main`. `argc` é a quantidade de argumentos (incluindo o nome do programa) e `argv` é o array de strings. Todo programa aqui usa `write`; nada de `printf`.

## Regras da lista

- Cabeçalho 42 e Norminette.
- Agora sim: `int main(int argc, char **argv)` é obrigatório.
- Use apenas `write`.
- Não acesse `argv` fora de `0 .. argc - 1`.

## Exercícios

| # | Exercício | Arquivo(s) | Permitidas |
|---|---|---|---|
| ex00 | [ft_print_program_name](ex00/ENUNCIADO.md) | `ft_print_program_name.c` | `write` |
| ex01 | [ft_print_params](ex01/ENUNCIADO.md) | `ft_print_params.c` | `write` |
| ex02 | [ft_rev_params](ex02/ENUNCIADO.md) | `ft_rev_params.c` | `write` |
| ex03 | [ft_sort_params](ex03/ENUNCIADO.md) | `ft_sort_params.c` | `write` |

## Como treinar esta lista

```sh
cd piscina/C06
moulinette .             # corrige a lista inteira
moulinette C06/ex00   # corrige um exercício
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
