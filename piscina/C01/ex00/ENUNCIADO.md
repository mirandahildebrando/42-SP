# ex00 — ft_ft

**Lista:** [C 01](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_ft.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Entender que uma função pode alterar a variável do chamador.

## Tarefa

Escreva uma função que coloque o valor 42 no inteiro apontado por `nbr`.

## Protótipo

```c
void ft_ft(int *nbr);
```

## Exemplo

```text
int n = 0; ft_ft(&n);  // n agora vale 42
```

## Dica

`*nbr = 42;` — o `*` acessa o valor apontado, não o endereço.

## Erros comuns

- Fazer `nbr = 42` (muda o ponteiro local).
- Esquecer o `*`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C01/ex00`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
