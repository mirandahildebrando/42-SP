# ex02 — ft_strcat

**Lista:** [C 03](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_strcat.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Concatenar strings no destino.

## Tarefa

Acrescente `src` ao final de `dest` e retorne `dest`.

## Protótipo

```c
char *ft_strcat(char *dest, char *src);
```

## Exemplo

```text
dest="hello", src=" world" -> "hello world"
```

## Dica

Ande até o `\0` de `dest` e copie `src` a partir dali, incluindo o terminador.

## Erros comuns

- Sobrescrever o início de `dest`.
- Esquecer o `\0`.
- Não retornar `dest`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C03/ex02`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
