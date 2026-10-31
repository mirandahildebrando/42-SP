# ex02 — ft_ultimate_range

**Lista:** [C 07](../README.md)  •  **Nível:** 3/3  •  **Arquivos:** `ft_ultimate_range.c`

**Funções permitidas:** `malloc`

---

## Objetivo

Devolver o array por ponteiro e o tamanho pelo retorno.

## Tarefa

Aloque o array `min..max-1`, guarde o ponteiro em `*range` e retorne o tamanho. Se `min >= max`, coloque NULL em `*range` e retorne 0. Se malloc falhar, retorne -1.

## Protótipo

```c
int ft_ultimate_range(int **range, int min, int max);
```

## Exemplo

```text
ft_ultimate_range(&t, 1, 5) -> 4; t = [1,2,3,4]
```

## Dica

Você já sabe fazer ft_range; agora escreva no ponteiro de ponteiro.

## Erros comuns

- Retornar o ponteiro em vez do tamanho.
- Não setar *range quando vazio.
- Retornar -1 para faixa vazia.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C07/ex02`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
