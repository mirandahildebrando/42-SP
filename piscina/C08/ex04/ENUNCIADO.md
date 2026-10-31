# ex04 — ft_strs_to_tab

**Lista:** [C 08](../README.md)  •  **Nível:** 3/3  •  **Arquivos:** `ft_strs_to_tab.c`

**Funções permitidas:** `malloc`, `free`

---

## Objetivo

Transformar argv em um array de structs alocado.

## Tarefa

Para cada uma das `ac` strings de `av`, crie uma struct com `size` (comprimento), `str` (ponteiro original) e `copy` (cópia alocada). O array retornado deve ter `ac + 1` elementos e o último deve ter `str = NULL`. Retorne NULL em erro.

## Protótipo

```c
struct s_stock_str *ft_strs_to_tab(int ac, char **av);
```

## Exemplo

```text
av=["42","SP"] -> [{2,"42","42"},{2,"SP","SP"},{0,NULL,NULL}]
```

## Dica

Aloque `(ac + 1) * sizeof(t_stock_str)`. Para cada item, aloque `size + 1` e copie. Cuide do vazamento em caso de erro.

## Erros comuns

- Esquecer o terminador `str = NULL`.
- Apontar `copy` para `str` em vez de alocar.
- Não tratar ac == 0.
- Esquecer o `\0` da cópia.

> O arquivo `ft_stock_str.h` é **fornecido** e já está nesta pasta. Não é necessário entregá-lo, mas ele será usado na compilação.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C08/ex04`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
