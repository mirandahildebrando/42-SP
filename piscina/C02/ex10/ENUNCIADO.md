# ex10 — ft_strlcpy

**Lista:** [C 02](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_strlcpy.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Cópia segura com tamanho de destino e retorno do tamanho da origem.

## Tarefa

Copie no máximo `size - 1` caracteres de `src` para `dest` e termine com `\0` se `size > 0`. Retorne o tamanho de `src`. Se `size` for 0, não escreva nada em `dest`.

## Protótipo

```c
unsigned int ft_strlcpy(char *dest, char *src, unsigned int size);
```

## Exemplo

```text
size=4, src="hello" -> dest="hel", retorno=5
```

## Dica

Calcule o tamanho de `src` primeiro. Copie enquanto houver espaço e depois feche com `\0`.

## Erros comuns

- Escrever em `dest` quando size == 0.
- Retornar o número de bytes copiados em vez do tamanho de `src`.
- Deixar `dest` sem terminador quando size > 0.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C02/ex10`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
