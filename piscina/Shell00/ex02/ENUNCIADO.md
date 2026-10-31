# ex02 — Oh yeah, mooore...

**Lista:** [Shell 00](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `exo2.tar`

**Funções permitidas:** nenhuma

---

## Objetivo

Criar uma árvore com permissões, tamanhos, hard link e symlink.

## Tarefa

Crie os arquivos e diretórios abaixo com os modos e tamanhos indicados, depois rode `tar -cf exo2.tar *`:

```text
drwx--xr-x  test0/            (0715)
-rwx--xr--  test1  4 bytes     (0714)
dr-x---r--  test2/            (0504)
-r-----r--  test3  1 byte      (0404, hard link)
-rw-r----x  test4  2 bytes     (0641)
-r-----r--  test5  1 byte      (0404, mesmo inode de test3)
lrwxr-xr-x  test6 -> test0    (symlink)
```

O `ls -l` do subject mostra `test3` e `test5` com link count 2. No Git Bash, use `ln test3 test5`; se o Windows não criar hard link, crie dois arquivos de 1 byte com o mesmo conteúdo (o validador local aceita essa adaptação).

## Protótipo

```c
exo2.tar
```

## Exemplo

```text
ls -l
total ...
drwx--xr-x ... test0
-rwx--xr-- ... test1
```

## Dica

Use `chmod` com modo octal: `chmod 715 test0`. Para os bytes, `head -c 4 /dev/zero > test1`, `head -c 1 /dev/zero > test3`, `head -c 2 /dev/zero > test4`. Crie o symlink com `ln -s test0 test6`.

## Erros comuns

- Colocar barra no nome dos diretórios ao criar (o `ls` mostra a barra, o nome não tem).
- Esquecer o hard link entre test3 e test5.
- Criar test6 como cópia em vez de symlink.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette Shell00/ex02`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
