# ex01 — ft_print_alphabet

**Lista:** [C 00](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_print_alphabet.c`

**Funções permitidas:** `write`

---

## Objetivo

Imprimir o alfabeto minúsculo, em ordem.

## Tarefa

Escreva uma função que mostre o alfabeto em minúsculas, em ordem crescente, na saída padrão.

## Protótipo

```c
void ft_print_alphabet(void);
```

## Exemplo

```text
ft_print_alphabet();  ->  abcdefghijklmnopqrstuvwxyz
```

## Dica

Use um `char` começando em `'a'` e um `while (c <= 'z')`.

## Erros comuns

- Imprimir com `printf`.
- Esquecer de incrementar a variável (loop infinito).
- Usar uma string literal gigante em vez de um loop (passa, mas não aprende).

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C00/ex01`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
