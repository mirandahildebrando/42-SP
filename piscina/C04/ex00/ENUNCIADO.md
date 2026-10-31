# ex00 — ft_strlen

**Lista:** [C 04](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_strlen.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Reescrever strlen mais uma vez, agora com confiança.

## Tarefa

Retorne o número de caracteres de `str`, sem contar o `\0`.

## Protótipo

```c
int ft_strlen(char *str);
```

## Exemplo

```text
ft_strlen("42SP") -> 4
```

## Dica

Se já fez na C01, escreva de memória e confira os casos vazios.

## Erros comuns

- Contar o terminador.
- Usar strlen.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C04/ex00`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
