# ex03 — ft_strjoin

**Lista:** [C 07](../README.md)  •  **Nível:** 3/3  •  **Arquivos:** `ft_strjoin.c`

**Funções permitidas:** `malloc`

---

## Objetivo

Juntar várias strings com um separador, alocando o resultado.

## Tarefa

Junte as `size` strings de `strs`, inserindo `sep` entre elas. Retorne uma string alocada. Se `size == 0`, retorne uma string vazia alocada (não NULL).

## Protótipo

```c
char *ft_strjoin(int size, char **strs, char *sep);
```

## Exemplo

```text
["42","SP","!"], sep="-" -> "42-SP-!"
```

## Dica

Calcule o tamanho total primeiro (incluindo separadores e `\0`), aloque uma vez e copie.

## Erros comuns

- Esquecer o `\0`.
- Separador depois da última string.
- Retornar NULL para size 0.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C07/ex03`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
