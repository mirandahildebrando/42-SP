# ex03 — ft_sort_params

**Lista:** [C 06](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `ft_sort_params.c`

**Funções permitidas:** `write`

---

## Objetivo

Ordenar strings usando strcmp e trocar ponteiros.

## Tarefa

Mostre os argumentos em ordem ASCII crescente, um por linha. Não é necessário ordenar o argv original: pode trocar ponteiros em uma cópia.

## Protótipo

```c
int main(int argc, char **argv);
```

## Exemplo

```text
./a.out banana Apple 42  ->  42\nApple\nbanana\n
```

## Dica

Bubble sort sobre os ponteiros de `argv` (a partir de 1), comparando com sua `ft_strcmp` ou com comparação própria.

## Erros comuns

- Usar `qsort` (proibido).
- Ordenar o argv[0].
- Comparar ponteiros em vez de conteúdo.

## Atenção

Este exercício é um **programa**: você deve entregar um `main`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C06/ex03`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
