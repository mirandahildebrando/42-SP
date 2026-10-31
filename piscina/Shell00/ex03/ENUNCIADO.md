# ex03 — Connect me!

**Lista:** [Shell 00](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `klist.txt`

**Funções permitidas:** nenhuma

---

## Objetivo

Entender tickets Kerberos e salvar a saída do klist.

## Tarefa

No cluster da 42, obtenha um ticket Kerberos e rode `klist > klist.txt`. No Windows não há Kerberos configurado: use o simulador `klist-sim > klist.txt` (ele está no PATH do ambiente) ou, se tiver um ticket real, use `klist`.

## Protótipo

```c
klist.txt
```

## Exemplo

```text
klist-sim > klist.txt
cat klist.txt
```

## Dica

O arquivo deve ter `Ticket cache`, `Default principal` e uma linha com `krbtgt`.

## Erros comuns

- Salvar a saída de `klist` sem redirecionar.
- Criar um arquivo vazio.
- Confundir o nome do arquivo: é `klist.txt`, não `klist`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette Shell00/ex03`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
