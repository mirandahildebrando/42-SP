# ex09 — Illusions, not tricks, Michael...

**Lista:** [Shell 00](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `ft_magic`

**Funções permitidas:** nenhuma

---

## Objetivo

Escrever uma regra de magic file para detectar o byte 42.

## Tarefa

Crie o arquivo `ft_magic` no formato do comando `file`, capaz de detectar arquivos que tenham a string `42` a partir do 42º byte (offset 42).

## Protótipo

```c
ft_magic
```

## Exemplo

```text
file -m ft_magic arquivo42
arquivo42: 42
```

## Dica

A sintaxe é `offset tipo teste [mensagem]`. Comece com `42 string 42`.

## Erros comuns

- Usar offset 41 ou 43.
- Escrever `42 string "42"` com aspas que o magic não espera.
- Deixar o arquivo sem quebra de linha final.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette Shell00/ex09`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
