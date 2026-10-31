# ex00 — ft_print_program_name

**Lista:** [C 06](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `ft_print_program_name.c`

**Funções permitidas:** `write`

---

## Objetivo

Entender que argv[0] é o nome do programa.

## Tarefa

Mostre o nome do programa (`argv[0]`) seguido de uma quebra de linha.

## Protótipo

```c
int main(int argc, char **argv);
```

## Exemplo

```text
./a.out  ->  ./a.out
```

## Dica

Imprima exatamente `argv[0]`, sem hardcode.

## Erros comuns

- Imprimir um nome fixo.
- Esquecer a quebra de linha.
- Imprimir argv[1].

## Atenção

Este exercício é um **programa**: você deve entregar um `main`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C06/ex00`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
