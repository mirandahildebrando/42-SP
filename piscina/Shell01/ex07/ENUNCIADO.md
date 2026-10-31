# ex07 — r_dwssap

**Lista:** [Shell 01](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `r_dwssap.sh`

**Funções permitidas:** nenhuma

---

## Objetivo

Transformar /etc/passwd em uma lista de logins invertidos.

## Tarefa

Crie `r_dwssap.sh`, um script que leia `/etc/passwd`, remova comentários, pegue as linhas alternadas começando pela segunda, inverta cada login, ordene em ordem alfabética reversa, mantenha apenas entre `$FT_LINE1` e `$FT_LINE2` e separe por `, `, terminando com `.`.

## Protótipo

```c
r_dwssap.sh
```

## Exemplo

```text
FT_LINE1=7 FT_LINE2=15 ./r_dwssap.sh
sstq_, sorebrek_brk_, soibten_, ....
```

## Dica

Monte o pipeline em etapas e teste cada uma. `cut -d: -f1`, `rev`, `sort -r`, `sed -n`, `paste -sd, -`.

## Erros comuns

- Inverter a linha inteira em vez do login.
- Esquecer de remover os comentários antes de alternar linhas.
- Deixar a vírgula final ou o ponto final de fora.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette Shell01/ex07`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
