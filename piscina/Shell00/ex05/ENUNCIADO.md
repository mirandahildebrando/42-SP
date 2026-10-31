# ex05 — GiT commit

**Lista:** [Shell 00](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `git_commit.sh`

**Funções permitidas:** nenhuma

---

## Objetivo

Escrever um script que mostra os 5 últimos commits.

## Tarefa

Crie `git_commit.sh`, um script que exibe os IDs dos últimos 5 commits do repositório atual, um por linha. Ele será testado em um repositório criado pelo corretor.

## Protótipo

```text
git_commit.sh
```

## Exemplo

```text
bash git_commit.sh | cat -e
baa23b...$
```

## Dica

`git log --format=%H -5` resolve. Não use caminho absoluto nem `cd` para outro repositório.

## Erros comuns

- Mostrar a mensagem do commit em vez do hash.
- Mostrar mais ou menos de 5 commits.
- Assumir que o script roda na sua pasta, e não no repositório de teste.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O script roda com `bash arquivo.sh` (ou `/bin/sh`).
- [ ] Permissões, conteúdo e saída seguem o enunciado.
- [ ] Testei com `moulinette Shell00/ex05`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
