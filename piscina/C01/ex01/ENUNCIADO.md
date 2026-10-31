# ex01 — ft_ultimate_ft

**Lista:** [C 01](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_ultimate_ft.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Seguir nove níveis de indireção sem se perder.

## Tarefa

Escreva uma função que receba um ponteiro de ponteiro (nove vezes) e coloque 42 no inteiro final.

## Protótipo

```c
void ft_ultimate_ft(int *********nbr);
```

## Exemplo

```text
int n; ... int *********p9 = &p8; ft_ultimate_ft(p9); // n == 42
```

## Dica

São nove `*` antes de `nbr = 42`. Conte no papel, não no olho.

## Erros comuns

- Errar a quantidade de asteriscos.
- Declarar os ponteiros na ordem errada.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C01/ex01`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
