# ex02 — ft_rev_params

**Lista:** [C 06](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `ft_rev_params.c`

**Funções permitidas:** `write`

---

## Objetivo

Percorrer argv de trás para frente.

## Tarefa

Mostre todos os argumentos, um por linha, na ordem inversa.

## Protótipo

```c
int main(int argc, char **argv);
```

## Exemplo

```text
./a.out a b c  ->  c\nb\na\n
```

## Dica

Comece em `argc - 1` e vá até 1, decrementando.

## Erros comuns

- Incluir argv[0].
- Loop com índice sem sinal (unsigned) e `i >= 0`.

## Atenção

Este exercício é um **programa**: você deve entregar um `main`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C06/ex02`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
