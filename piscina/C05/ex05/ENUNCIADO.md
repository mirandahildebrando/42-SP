# ex05 — ft_sqrt

**Lista:** [C 05](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `ft_sqrt.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Raiz quadrada inteira exata.

## Tarefa

Retorne a raiz quadrada inteira de `nb` se ela existir; caso contrário, retorne 0. Negativos retornam 0.

## Protótipo

```c
int ft_sqrt(int nb);
```

## Exemplo

```text
ft_sqrt(16) -> 4; ft_sqrt(15) -> 0
```

## Dica

Percorra `i` de 0 até `i * i <= nb`, mas cuidado com overflow em `i * i`. Use `i <= nb / i`.

## Erros comuns

- Usar `sqrt` (proibido).
- Overflow em i * i.
- Retornar aproximação em vez de 0.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C05/ex05`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
