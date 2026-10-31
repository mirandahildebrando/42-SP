# ex07 — ft_strupcase

**Lista:** [C 02](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_strupcase.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Transformar minúsculas em maiúsculas in-place.

## Tarefa

Passe todas as letras minúsculas para maiúsculas. Retorne a própria string.

## Protótipo

```c
char *ft_strupcase(char *str);
```

## Exemplo

```text
ft_strupcase("HeLLo 42!") -> "HELLO 42!"
```

## Dica

Se estiver entre 'a' e 'z', subtraia 32 (`'a' - 'A'`).

## Erros comuns

- Transformar dígitos ou pontuação.
- Retornar uma cópia em vez do ponteiro original.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C02/ex07`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
