# C 02 — strings e caracteres

Strings em C são arrays de `char` terminados por `\0`. Nesta lista você copia, classifica e transforma strings sem usar a libc. A regra de ouro: sempre pare no terminador nulo e nunca escreva fora do buffer.

## Regras da lista

- Cabeçalho 42 e Norminette.
- Nenhuma função da libc (nem `strlen`, nem `strcpy`).
- Só `write` quando o exercício for de saída; aqui quase tudo retorna valor.
- Trate string vazia como caso válido.
- Não altere strings literais: o comportamento é indefinido.

## Exercícios

| # | Exercício | Arquivo(s) | Permitidas |
|---|---|---|---|
| ex00 | [ft_strcpy](ex00/ENUNCIADO.md) | `ft_strcpy.c` | — |
| ex01 | [ft_strncpy](ex01/ENUNCIADO.md) | `ft_strncpy.c` | — |
| ex02 | [ft_str_is_alpha](ex02/ENUNCIADO.md) | `ft_str_is_alpha.c` | — |
| ex03 | [ft_str_is_numeric](ex03/ENUNCIADO.md) | `ft_str_is_numeric.c` | — |
| ex04 | [ft_str_is_lowercase](ex04/ENUNCIADO.md) | `ft_str_is_lowercase.c` | — |
| ex05 | [ft_str_is_uppercase](ex05/ENUNCIADO.md) | `ft_str_is_uppercase.c` | — |
| ex06 | [ft_str_is_printable](ex06/ENUNCIADO.md) | `ft_str_is_printable.c` | — |
| ex07 | [ft_strupcase](ex07/ENUNCIADO.md) | `ft_strupcase.c` | — |
| ex08 | [ft_strlowcase](ex08/ENUNCIADO.md) | `ft_strlowcase.c` | — |
| ex09 | [ft_strcapitalize](ex09/ENUNCIADO.md) | `ft_strcapitalize.c` | — |
| ex10 | [ft_strlcpy](ex10/ENUNCIADO.md) | `ft_strlcpy.c` | — |

## Como treinar esta lista

```sh
cd piscina/C02
moulinette .             # corrige a lista inteira
moulinette C02/ex00   # corrige um exercício
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
