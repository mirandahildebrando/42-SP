# ex01 — ft_print_params

**Lista:** [C 06](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `ft_print_params.c`

**Funções permitidas:** `write`

---

## Objetivo

Percorrer argv e imprimir cada argumento.

## Tarefa

Mostre todos os argumentos recebidos, um por linha, na ordem original.

## Protótipo

```c
int main(int argc, char **argv);
```

## Exemplo

```text
./a.out hello 42  ->  hello\n42\n
```

## Dica

Comece em `i = 1` e vá até `i < argc`. Cada argumento termina com `\n`.

## Erros comuns

- Imprimir argv[0].
- Não colocar newline.
- Acessar argv[argc] como string.

## Atenção

Este exercício é um **programa**: você deve entregar um `main`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C06/ex01`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
