# ex04 — ft_ultimate_div_mod

**Lista:** [C 01](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_ultimate_div_mod.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Escrever o resultado da divisão de volta nos próprios argumentos.

## Tarefa

Divida o valor apontado por `a` pelo valor apontado por `b`. Coloque o quociente em `*a` e o resto em `*b`.

## Protótipo

```c
void ft_ultimate_div_mod(int *a, int *b);
```

## Exemplo

```text
a = 42, b = 5  ->  a = 8, b = 2
```

## Dica

Guarde o divisor antes de alterar `*b`, ou use variáveis locais.

## Erros comuns

- Sobrescrever `*b` antes de calcular o resto.
- Assumir que `b` continua com o valor original.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C01/ex04`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
