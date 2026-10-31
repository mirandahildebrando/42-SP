# ex01 — ft_range

**Lista:** [C 07](../README.md)  •  **Nível:** 3/3  •  **Arquivos:** `ft_range.c`

**Funções permitidas:** `malloc`

---

## Objetivo

Criar um array com todos os inteiros de min até max-1.

## Tarefa

Retorne um array alocado contendo `min, min+1, ..., max-1`. Se `min >= max`, retorne NULL.

## Protótipo

```c
int *ft_range(int min, int max);
```

## Exemplo

```text
ft_range(1, 5) -> [1, 2, 3, 4]
```

## Dica

O tamanho é `max - min`. Aloque `sizeof(int) * tamanho` e preencha.

## Erros comuns

- Alocar um a menos.
- Não tratar min >= max.
- Retornar array não alocado.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C07/ex01`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
