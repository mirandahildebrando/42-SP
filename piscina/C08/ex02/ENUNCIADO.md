# ex02 — ft_abs.h

**Lista:** [C 08](../README.md)  •  **Nível:** 3/3  •  **Arquivos:** `ft_abs.h`

**Funções permitidas:** nenhuma

---

## Objetivo

Escrever uma macro segura com parênteses.

## Tarefa

Crie a macro `ABS(Value)` que retorna o valor absoluto.

## Protótipo

```c
#define ABS(Value) ...
```

## Exemplo

```text
ABS(-42) -> 42
```

## Dica

`#define ABS(Value) ((Value) < 0 ? -(Value) : (Value))` — os parênteses externos são obrigatórios.

## Erros comuns

- Sem parênteses, quebra em expressões como ABS(a - b).
- Usar função em vez de macro.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C08/ex02`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
