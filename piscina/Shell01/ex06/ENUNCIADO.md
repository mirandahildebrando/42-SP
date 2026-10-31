# ex06 — Skip

**Lista:** [Shell 01](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `skip.sh`

**Funções permitidas:** nenhuma

---

## Objetivo

Mostrar linhas alternadas de uma saída.

## Tarefa

Crie `skip.sh`, um script que execute `ls -l` e mostre uma linha sim, uma não, começando pela primeira linha.

## Protótipo

```text
skip.sh
```

## Exemplo

```text
./skip.sh | cat -e
total ...$
-rw...$
```

## Dica

`awk 'NR % 2 == 1'` ou `sed -n '1~2p'` (GNU sed).

## Erros comuns

- Começar pela segunda linha.
- Mostrar a saída inteira.
- Colocar `ls -l` dentro do arquivo sem imprimir na tela.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O script roda com `bash arquivo.sh` (ou `/bin/sh`).
- [ ] Permissões, conteúdo e saída seguem o enunciado.
- [ ] Testei com `moulinette Shell01/ex06`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
