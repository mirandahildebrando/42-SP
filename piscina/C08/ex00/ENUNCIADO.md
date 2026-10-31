# ex00 — ft.h

**Lista:** [C 08](../README.md)  •  **Nível:** 3/3  •  **Arquivos:** `ft.h`

**Funções permitidas:** nenhuma

---

## Objetivo

Criar seu primeiro header e entender protótipos.

## Tarefa

Crie `ft.h` com o include guard e os protótipos de: `ft_putchar`, `ft_swap`, `ft_putstr`, `ft_strlen` e `ft_strcmp`.

## Protótipo

```c
ft.h com os cinco protótipos
```

## Exemplo

```text
void ft_putchar(char c);
int ft_strlen(char *str);
```

## Dica

O header só declara. As definições ficam nos .c. Teste incluindo o header em dois arquivos diferentes.

## Erros comuns

- Esquecer o include guard (erro de redefinição).
- Colocar corpo de função no header.
- Trocar a ordem/tipo dos parâmetros.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette C08/ex00`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
