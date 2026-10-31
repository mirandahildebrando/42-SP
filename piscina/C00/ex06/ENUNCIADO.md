# ex06 — ft_print_comb2

**Lista:** [C 00](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_print_comb2.c`

**Funções permitidas:** `write`

---

## Objetivo

Gerar todos os pares de números de 00 a 99.

## Tarefa

Escreva uma função que mostre todas as combinações de dois números entre 00 e 99, em ordem crescente, no formato `XX XX`, separadas por `, `. O primeiro número é sempre menor que o segundo.

## Protótipo

```c
void ft_print_comb2(void);
```

## Exemplo

```text
00 01, 00 02, ..., 00 99, 01 02, ..., 98 99
```

## Dica

Dois loops de 0 a 99 com `a < b`. Para imprimir dois dígitos, use divisão e módulo por 10. Cuidado com o separador: imprima antes do par, exceto no primeiro.

## Erros comuns

- Imprimir `00 00`.
- Esquecer o zero à esquerda.
- Vírgula sobrando no final.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C00/ex06`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
