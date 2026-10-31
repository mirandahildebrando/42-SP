# ex04 — ft_fibonacci

**Lista:** [C 05](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `ft_fibonacci.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Sequência de Fibonacci recursiva.

## Tarefa

Retorne o `index`-ésimo número de Fibonacci (F0=0, F1=1). Se `index` for negativo, retorne -1.

## Protótipo

```c
int ft_fibonacci(int index);
```

## Exemplo

```text
F10 = 55
```

## Dica

Dois casos base e a soma das duas chamadas anteriores. A versão recursiva é exponencial; aceite isso.

## Erros comuns

- Começar em 1 e 1 em vez de 0 e 1.
- Não tratar índice negativo.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C05/ex04`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
