# ex01 — ft_strncpy

**Lista:** [C 02](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_strncpy.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Copiar no máximo n bytes e completar com zeros se necessário.

## Tarefa

Copie até `n` caracteres de `src` para `dest`. Se `src` tiver menos de `n` caracteres, complete o restante com `\0`. Se `src` tiver `n` ou mais, não adicione terminador. Retorne `dest`.

## Protótipo

```c
char *ft_strncpy(char *dest, char *src, unsigned int n);
```

## Exemplo

```text
n=5, src="abc" -> 'a','b','c','\0','\0'
```

## Dica

Use um índice e dois loops: um copiando e outro preenchendo com zero.

## Erros comuns

- Sempre adicionar `\0` no fim (strncpy não garante isso).
- Copiar n+1 bytes.
- Esquecer de retornar `dest`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C02/ex01`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
