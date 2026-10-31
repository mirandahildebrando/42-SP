# ex06 — gitignore

**Lista:** [Shell 00](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `git_ignore.sh`

**Funções permitidas:** nenhuma

---

## Objetivo

Listar arquivos ignorados pelo Git.

## Tarefa

Crie `git_ignore.sh`, um script que lista os arquivos existentes ignorados pelo repositório Git atual, um por linha.

## Protótipo

```text
git_ignore.sh
```

## Exemplo

```text
bash git_ignore.sh | cat -e
.DS_Store$
mywork.c~$
```

## Dica

`git ls-files --others --ignored --exclude-standard` é o comando canônico.

## Erros comuns

- Listar arquivos rastreados em vez de ignorados.
- Incluir diretórios vazios (o Git não os rastreia).
- Depender de um `.gitignore` específico da sua pasta.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O script roda com `bash arquivo.sh` (ou `/bin/sh`).
- [ ] Permissões, conteúdo e saída seguem o enunciado.
- [ ] Testei com `moulinette Shell00/ex06`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
