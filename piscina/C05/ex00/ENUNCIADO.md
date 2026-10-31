# ex00 — ft_iterative_factorial

**Lista:** [C 05](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `ft_iterative_factorial.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Fatorial com loop.

## Tarefa

Retorne o fatorial de `nb`. Se `nb` for negativo, retorne 0. Lembre: 0! = 1.

## Protótipo

```c
int ft_iterative_factorial(int nb);
```

## Exemplo

```text
5! = 120
```

## Dica

Comece o resultado em 1 e multiplique de 2 até nb. Nunca multiplique por 0 sem tratar o caso base.

## Erros comuns

- Retornar 0 para 0!.
- Loop que inclui o 0 e zera tudo.
- Overflow acima de 12!.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C05/ex00`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
