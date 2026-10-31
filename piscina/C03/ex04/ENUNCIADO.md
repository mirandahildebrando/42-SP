# ex04 — ft_strstr

**Lista:** [C 03](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_strstr.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Encontrar a primeira ocorrência de uma substring.

## Tarefa

Procure `to_find` dentro de `str` e retorne o ponteiro para a primeira ocorrência. Se não encontrar, retorne `NULL`. Se `to_find` for vazia, retorne `str`.

## Protótipo

```c
char *ft_strstr(char *str, char *to_find);
```

## Exemplo

```text
ft_strstr("hello world", "world") -> ponteiro para 'w'
```

## Dica

Para cada posição de `str`, tente casar `to_find` inteira. Se `str` estiver no fim, pare.

## Erros comuns

- Retornar o índice em vez do ponteiro.
- Estourar ao comparar quando a substring é maior.
- Não tratar needle vazia.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C03/ex04`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
