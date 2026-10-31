# ex03 — ft_atoi

**Lista:** [C 04](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_atoi.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Converter texto em inteiro como a função atoi.

## Tarefa

Converta a string para `int`. Ignore espaços no início, aceite um sinal `+` ou `-` e pare no primeiro caractere que não for dígito. Sem dígitos, retorne 0.

## Protótipo

```c
int ft_atoi(char *str);
```

## Exemplo

```text
ft_atoi("  -42abc") -> -42
```

## Dica

Acumule `result = result * 10 + (c - '0')` e aplique o sinal no final.

## Erros comuns

- Não pular espaços iniciais.
- Aceitar letras no meio sem parar.
- Esquecer o sinal negativo.
- Estourar com INT_MIN.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C04/ex03`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
