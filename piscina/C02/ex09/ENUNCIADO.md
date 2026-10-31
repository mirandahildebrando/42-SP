# ex09 — ft_strcapitalize

**Lista:** [C 02](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_strcapitalize.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Capitalizar palavras de forma inteligente.

## Tarefa

Coloque a primeira letra de cada palavra em maiúscula e as demais em minúscula. Uma palavra é uma sequência de caracteres alfanuméricos. Se o primeiro caractere for um dígito, a palavra não é capitalizada.

## Protótipo

```c
char *ft_strcapitalize(char *str);
```

## Exemplo

```text
"salut, comment tu vas ? 42mots quarante-deux; cinquante+et+un"
-> "Salut, Comment Tu Vas ? 42mots Quarante-Deux; Cinquante+Et+Un"
```

## Dica

Use uma flag `in_word` ou verifique o caractere anterior: se não for alfanumérico, o próximo caractere inicia palavra. Comece uma palavra com maiúscula e as demais com minúscula.

## Erros comuns

- Capitalizar letras depois de dígitos na mesma palavra (42mots vira 42Mots).
- Não baixar as maiúsculas do meio da palavra.
- Tratar `-` ou `+` como parte da palavra.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C02/ex09`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
