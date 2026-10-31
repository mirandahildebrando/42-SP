# ex03 — ft_div_mod

**Lista:** [C 01](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_div_mod.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Devolver dois resultados por parâmetros de saída.

## Tarefa

Divida `a` por `b`, guarde o quociente em `*div` e o resto em `*mod`. Considere `b` diferente de zero.

## Protótipo

```c
void ft_div_mod(int a, int b, int *div, int *mod);
```

## Exemplo

```text
42 / 5 -> div = 8, mod = 2
```

## Dica

Use `/` e `%` uma única vez cada; cuidado com números negativos (truncamento de C).

## Erros comuns

- Inverter quociente e resto.
- Não escrever nos dois ponteiros.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C01/ex03`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
