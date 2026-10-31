# ex07 — diff

**Lista:** [Shell 00](../README.md)  •  **Nível:** 1/3  •  **Arquivos:** `b`

**Funções permitidas:** nenhuma

---

## Objetivo

Criar uma versão modificada de um texto e testar diff/patch.

## Tarefa

O arquivo `a` já está na pasta. Crie `b` como uma cópia modificada de `a` (uma ou mais mudanças de texto). `diff -u a b` deve gerar um patch que possa ser aplicado sobre uma cópia limpa de `a`. Não altere `a`.

## Protótipo

```text
a  ->  b
```

## Exemplo

```text
diff -u a b > sw.diff
patch a < sw.diff
```

## Dica

Copie `a` para `b` e mude uma palavra. Use `diff -u` para conferir e `patch` para testar a aplicação.

## Erros comuns

- Deixar `b` idêntico a `a`.
- Modificar `a` em vez de criar `b`.
- Criar um patch que não aplica (por exemplo, mudando várias linhas sem contexto).

> O arquivo `a` é **fornecido** e já está nesta pasta. Não é necessário entregá-lo, mas ele será usado na compilação.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O script roda com `bash arquivo.sh` (ou `/bin/sh`).
- [ ] Permissões, conteúdo e saída seguem o enunciado.
- [ ] Testei com `moulinette Shell00/ex07`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
