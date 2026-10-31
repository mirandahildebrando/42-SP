# C 07 — malloc, arrays e split

A lista de `malloc`. A partir daqui você cria dados que sobrevivem ao retorno da função. Regra número um: cada alocação precisa de espaço para o terminador quando for string, e o resultado precisa ser testável. `ft_convert_base` e `ft_split` são clássicos de exame.

## Regras da lista

- Cabeçalho 42 e Norminette.
- Permitido: `malloc` e `free` (e `write` em convert_base, se necessário).
- Sempre pense no `\0` extra ao alocar strings.
- Não vaze memória nos seus testes; use free quando terminar.
- Retorne NULL em erro de alocação quando o subject pedir.

## Exercícios

| # | Exercício | Arquivo(s) | Permitidas |
|---|---|---|---|
| ex00 | [ft_strdup](ex00/ENUNCIADO.md) | `ft_strdup.c` | `malloc` |
| ex01 | [ft_range](ex01/ENUNCIADO.md) | `ft_range.c` | `malloc` |
| ex02 | [ft_ultimate_range](ex02/ENUNCIADO.md) | `ft_ultimate_range.c` | `malloc` |
| ex03 | [ft_strjoin](ex03/ENUNCIADO.md) | `ft_strjoin.c` | `malloc` |
| ex04 | [ft_convert_base](ex04/ENUNCIADO.md) | `ft_convert_base.c`, `ft_convert_base2.c` | `malloc`, `free` |
| ex05 | [ft_split](ex05/ENUNCIADO.md) | `ft_split.c` | `malloc`, `free` |

## Como treinar esta lista

```sh
cd piscina/C07
moulinette .             # corrige a lista inteira
moulinette C07/ex00   # corrige um exercício
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
