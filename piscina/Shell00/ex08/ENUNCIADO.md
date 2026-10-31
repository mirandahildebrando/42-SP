# ex08 — clean

**Lista:** [Shell 00](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `clean`

**Funções permitidas:** nenhuma

---

## Objetivo

Encontrar e apagar arquivos temporários com um único comando find.

## Tarefa

Coloque no arquivo `clean` uma única linha de comando que procure, a partir do diretório atual e em todos os subdiretórios, arquivos cujo nome termine em `~` ou comece e termine com `#`. O comando deve mostrar e apagar os arquivos. Não use `;`, `&&` ou `||`.

## Protótipo

```text
clean (uma linha de comando)
```

## Exemplo

```text
find . \( -name '*~' -o -name '#*#' \) -print -delete
```

## Dica

`find` aceita `-print` e `-delete`; a precedência do `-o` exige parênteses escapados.

## Erros comuns

- Apagar só os arquivos do diretório atual.
- Esquecer de mostrar os nomes.
- Usar dois comandos separados por `;`.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O script roda com `bash arquivo.sh` (ou `/bin/sh`).
- [ ] Permissões, conteúdo e saída seguem o enunciado.
- [ ] Testei com `moulinette Shell00/ex08`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
