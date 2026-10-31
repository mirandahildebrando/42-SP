# ex05 — ft_show_tab

**Lista:** [C 08](../README.md)  •  **Nível:** 3/3  •  **Arquivos:** `ft_show_tab.c`

**Funções permitidas:** `write`

---

## Objetivo

Percorrer um array de structs e imprimir todos os campos.

## Tarefa

Para cada elemento do array (até `str == NULL`), mostre a string, o tamanho e a cópia, cada um seguido de `\n`. Use apenas `write`.

## Protótipo

```c
void ft_show_tab(struct s_stock_str *par);
```

## Exemplo

```text
hello / 5 / HELLO (cada um em uma linha)
```

## Dica

Você pode reaproveitar um putstr e um putnbr. O fim do array é `par[i].str == NULL`.

## Erros comuns

- Parar no primeiro `str` vazio (use o ponteiro nulo, não o conteúdo).
- Imprimir `str` em vez de `copy` no terceiro campo.
- Esquecer o newline do tamanho.

> O arquivo `ft_stock_str.h` é **fornecido** e já está nesta pasta. Não é necessário entregá-lo, mas ele será usado na compilação.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C08/ex05`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
