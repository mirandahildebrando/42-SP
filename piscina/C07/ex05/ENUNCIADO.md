# ex05 — ft_split

**Lista:** [C 07](../README.md)  •  **Nível:** 3/3  •  **Arquivos:** `ft_split.c`

**Funções permitidas:** `malloc`, `free`

---

## Objetivo

Separar uma string em palavras, alocando o array e cada token.

## Tarefa

Divida `str` em palavras usando qualquer caractere de `charset` como separador. Retorne um array de strings terminado por NULL. Não gere tokens vazios.

## Protótipo

```c
char **ft_split(char *str, char *charset);
```

## Exemplo

```text
ft_split("  hello   world  ", " ") -> ["hello","world",NULL]
```

## Dica

Conte as palavras, aloque `count + 1` ponteiros, depois aloque cada palavra. Separe em funções auxiliares para passar na Norma.

## Erros comuns

- Criar token vazio entre separadores consecutivos.
- Esquecer o NULL final.
- Não alocar `len + 1` de cada token.
- Vazar memória em caso de erro.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C07/ex05`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
