# ex08 — ft_strlowcase

**Lista:** [C 02](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_strlowcase.c`

**Funções permitidas:** nenhuma

---

## Objetivo

Transformar maiúsculas em minúsculas in-place.

## Tarefa

Passe todas as letras maiúsculas para minúsculas. Retorne a própria string.

## Protótipo

```c
char *ft_strlowcase(char *str);
```

## Exemplo

```text
ft_strlowcase("HeLLo 42!") -> "hello 42!"
```

## Dica

Se estiver entre 'A' e 'Z', some 32.

## Erros comuns

- Transformar símbolos.
- Esquecer de retornar `str`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C02/ex08`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
