# ex02 — ft_str_is_alpha

**Lista:** [C 02](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_str_is_alpha.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Reconhecer letras ASCII.

## Tarefa

Retorne 1 se a string contiver apenas letras (a-z, A-Z), e 0 caso contrário. String vazia retorna 1.

## Protótipo

```c
int ft_str_is_alpha(char *str);
```

## Exemplo

```text
ft_str_is_alpha("abcXYZ") -> 1; ("abc1") -> 0
```

## Dica

Compare faixas: `(c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')`.

## Erros comuns

- Aceitar dígitos.
- Retornar 0 para string vazia.
- Usar `isalpha` (proibido).

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C02/ex02`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
