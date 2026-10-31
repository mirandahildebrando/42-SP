# ex00 — ft_strcpy

**Lista:** [C 02](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_strcpy.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Copiar uma string inteira, incluindo o terminador nulo.

## Tarefa

Copie `src` para `dest` e retorne `dest`.

## Protótipo

```c
char *ft_strcpy(char *dest, char *src);
```

## Exemplo

```text
ft_strcpy(dest, "42"); // dest contém '4','2','\0'
```

## Dica

Copie primeiro, teste o `\0` depois: `dest[i] = src[i];` e incremente.

## Erros comuns

- Esquecer de copiar o `\0`.
- Retornar `src` em vez de `dest`.
- Estourar `dest`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C02/ex00`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
