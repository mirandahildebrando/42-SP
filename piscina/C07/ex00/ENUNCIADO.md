# ex00 — ft_strdup

**Lista:** [C 07](../README.md)  •  **Nível:** 3/3  •  **Arquivos:** `ft_strdup.c`

**Funções permitidas:** `malloc`

---

## Objetivo

Duplicar uma string em memória nova.

## Tarefa

Aloque memória suficiente, copie `src` (com `\0`) e retorne o novo ponteiro.

## Protótipo

```c
char *ft_strdup(char *src);
```

## Exemplo

```text
ft_strdup("42") -> novo bloco contendo "42"
```

## Dica

Conte o tamanho primeiro, aloque `len + 1`, depois copie.

## Erros comuns

- Alocar `len` e esquecer o `\0`.
- Retornar `src` sem alocar.
- Não verificar malloc.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C07/ex00`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
