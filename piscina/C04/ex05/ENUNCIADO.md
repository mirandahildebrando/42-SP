# ex05 — ft_atoi_base

**Lista:** [C 04](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_atoi_base.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Ler um número escrito em qualquer base.

## Tarefa

Converta `str`, escrita na base `base`, para `int`. Ignore espaços iniciais, aceite sinais e pare no primeiro caractere que não pertence à base. Considere a base válida.

## Protótipo

```c
int ft_atoi_base(char *str, char *base);
```

## Exemplo

```text
ft_atoi_base("  -2A", "0123456789ABCDEF") -> -42
```

## Dica

Para cada caractere, ache o índice dele na base. Se não existir, pare. Acumule com `result = result * base_len + índice`.

## Erros comuns

- Não achar o índice corretamente (base arbitrária).
- Confundir o valor do caractere com o índice.
- Ignorar o sinal.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C04/ex05`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
