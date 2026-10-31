# ex02 — ft_iterative_power

**Lista:** [C 05](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `ft_iterative_power.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Potência com loop.

## Tarefa

Retorne `nb` elevado a `power`. Se `power` for negativo, retorne 0. `0^0` vale 1.

## Protótipo

```c
int ft_iterative_power(int nb, int power);
```

## Exemplo

```text
2^10 = 1024
```

## Dica

Resultado começa em 1; multiplique `power` vezes. O caso 0^0 cai naturalmente em 1.

## Erros comuns

- Retornar 0 para potência 0.
- Tratar expoente negativo como positivo.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C05/ex02`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
