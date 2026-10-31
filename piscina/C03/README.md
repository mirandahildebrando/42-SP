# C 03 — comparar, juntar, procurar

Agora as strings começam a interagir. Você vai comparar byte a byte, concatenar respeitando o terminador e procurar uma substring. Cuidado com `unsigned char` nas comparações e com o espaço disponível no destino.

## Regras da lista

- Cabeçalho 42 e Norminette.
- Nenhuma função da libc.
- O destino de concatenação precisa ter espaço suficiente.
- Retorne o ponteiro pedido pelo protótipo (quase sempre `dest` ou `str`).

## Exercícios

| # | Exercício | Arquivo(s) | Permitidas |
|---|---|---|---|
| ex00 | [ft_strcmp](ex00/ENUNCIADO.md) | `ft_strcmp.c` | — |
| ex01 | [ft_strncmp](ex01/ENUNCIADO.md) | `ft_strncmp.c` | — |
| ex02 | [ft_strcat](ex02/ENUNCIADO.md) | `ft_strcat.c` | — |
| ex03 | [ft_strncat](ex03/ENUNCIADO.md) | `ft_strncat.c` | — |
| ex04 | [ft_strstr](ex04/ENUNCIADO.md) | `ft_strstr.c` | — |

## Como treinar esta lista

```sh
cd piscina/C03
moulinette .             # corrige a lista inteira
moulinette C03/ex00   # corrige um exercício
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
