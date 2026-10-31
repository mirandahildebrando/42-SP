# ex06 — ft_is_prime

**Lista:** [C 05](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `ft_is_prime.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Teste de primalidade eficiente.

## Tarefa

Retorne 1 se `nb` for primo e 0 caso contrário.

## Protótipo

```c
int ft_is_prime(int nb);
```

## Exemplo

```text
ft_is_prime(17) -> 1; ft_is_prime(25) -> 0
```

## Dica

Teste divisores de 2 até a raiz quadrada. Trate 0, 1 e negativos como não primos.

## Erros comuns

- Testar até nb (lento).
- Considerar 2 não primo.
- Overflow no loop de divisores.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C05/ex06`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
