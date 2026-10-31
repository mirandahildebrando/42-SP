# ex02 — find_sh

**Lista:** [Shell 01](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `find_sh.sh`

**Funções permitidas:** nenhuma

---

## Objetivo

Encontrar arquivos .sh e mostrar só o nome sem extensão.

## Tarefa

Crie `find_sh.sh`, um script que procure em todos os subdiretórios os arquivos terminados em `.sh` e mostre apenas o nome do arquivo, sem o `.sh`, um por linha.

## Protótipo

```text
find_sh.sh
```

## Exemplo

```text
./find_sh.sh | cat -e
find_sh$
file1$
```

## Dica

`find . -type f -name '*.sh'` e `basename` (ou `sed`) resolvem. Cuidado com o nome do próprio script.

## Erros comuns

- Incluir o caminho `./sub/` na saída.
- Incluir a extensão `.sh`.
- Procurar só na pasta atual.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O script roda com `bash arquivo.sh` (ou `/bin/sh`).
- [ ] Permissões, conteúdo e saída seguem o enunciado.
- [ ] Testei com `moulinette Shell01/ex02`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
