# ex03 — ft_strncat

**Lista:** [C 03](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_strncat.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Concatenar limitando o número de bytes da origem.

## Tarefa

Acrescente no máximo `nb` caracteres de `src` ao final de `dest`, sempre terminando com `\0`, e retorne `dest`.

## Protótipo

```c
char *ft_strncat(char *dest, char *src, unsigned int nb);
```

## Exemplo

```text
dest="hello", src=" world", nb=3 -> "hello wo"
```

## Dica

Copie o loop de strcat com uma condição extra `i < nb`; feche o `\0` depois.

## Erros comuns

- Copiar nb+1 bytes.
- Não terminar com `\0` quando nb < tamanho de src.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C03/ex03`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
