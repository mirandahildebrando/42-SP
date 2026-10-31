# ex01 — print_groups

**Lista:** [Shell 01](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `print_groups.sh`

**Funções permitidas:** nenhuma

---

## Objetivo

Listar os grupos de um usuário separados por vírgula.

## Tarefa

Escreva uma linha de comando que mostre os grupos do login contido em `$FT_USER`, separados por vírgula e sem espaços. No Windows, o comando `id` é simulado pelo ambiente para que o exercício possa ser corrigido.

## Protótipo

```c
print_groups.sh
```

## Exemplo

```text
FT_USER=nours ./print_groups.sh
god,root,admin,master,nours,bocal
```

## Dica

`id -Gn` lista os nomes dos grupos; `tr ' ' ','` troca espaços por vírgulas.

## Erros comuns

- Deixar espaço depois da vírgula.
- Deixar uma quebra de linha no final.
- Usar `$USER` em vez de `$FT_USER`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette Shell01/ex01`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
