# ex07 — ft_find_next_prime

**Lista:** [C 05](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `ft_find_next_prime.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Reaproveitar is_prime para achar o próximo primo.

## Tarefa

Retorne o menor primo maior ou igual a `nb`.

## Protótipo

```c
int ft_find_next_prime(int nb);
```

## Exemplo

```text
ft_find_next_prime(4) -> 5; (17) -> 17
```

## Dica

Chame sua `ft_is_prime` (definida no mesmo arquivo) em um loop a partir de `nb`, com caso especial para valores < 2.

## Erros comuns

- Retornar o primo estritamente maior em vez de >=
- Loop infinito para nb negativo.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C05/ex07`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
