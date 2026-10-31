# ex07 — ft_putnbr

**Lista:** [C 00](../README.md)  •  **Nível:** 0/3  •  **Arquivos:** `ft_putnbr.c`

**Funções permitidas:** `write`

---

## Objetivo

Imprimir um inteiro, incluindo o menor int possível.

## Tarefa

Escreva uma função que mostre o número recebido como argumento. Ela precisa funcionar com todos os valores de `int`, inclusive `INT_MIN` (-2147483648).

## Protótipo

```c
void ft_putnbr(int nb);
```

## Exemplo

```text
ft_putnbr(-42); -> -42
```

## Dica

O truque clássico: trate `INT_MIN` separadamente ou use `long`/`long long` para evitar overflow ao negar o número. Recursão resolve dígito a dígito.

## Erros comuns

- `-nb` com `INT_MIN` causa overflow (undefined behavior).
- Perder o sinal de menos.
- Ordem dos dígitos invertida.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C00/ex07`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
