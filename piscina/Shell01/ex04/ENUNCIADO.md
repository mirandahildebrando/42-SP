# ex04 — MAC

**Lista:** [Shell 01](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `MAC.sh`

**Funções permitidas:** nenhuma

---

## Objetivo

Extrair endereços MAC de uma saída de ifconfig.

## Tarefa

Crie `MAC.sh`, um script que mostre os endereços MAC da máquina, um por linha. No Windows, `ifconfig` é simulado pelo ambiente com uma saída no formato Linux.

## Protótipo

```c
MAC.sh
```

## Exemplo

```text
./MAC.sh
00:11:22:33:44:55
```

## Dica

`ifconfig | grep ether | awk '{print $2}'` é a solução clássica.

## Erros comuns

- Mostrar a linha inteira em vez do endereço.
- Incluir interfaces sem MAC.
- Deixar cabeçalhos ou linhas vazias.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette Shell01/ex04`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
