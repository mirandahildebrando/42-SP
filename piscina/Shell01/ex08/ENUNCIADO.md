# ex08 — add_chelou

**Lista:** [Shell 01](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `add_chelou.sh`

**Funções permitidas:** nenhuma

---

## Objetivo

Converter e somar números em bases exóticas.

## Tarefa

Crie `add_chelou.sh`, um script que leia `$FT_NBR1` na base `'\"?!`, `$FT_NBR2` na base `mrdoc`, some os dois valores e imprima o resultado na base `gtaio luSnemf`.

## Protótipo

```text
add_chelou.sh
```

## Exemplo

```text
FT_NBR1=... FT_NBR2=... ./add_chelou.sh
Salut
```

## Dica

Converta cada caractere para dígito, use uma calculadora de base (bc/awk) e mapeie a saída. O espaço faz parte da base final.

## Erros comuns

- Esquecer que o espaço é um dígito da base final.
- Tratar os caracteres especiais sem quoting.
- Usar base 10 na saída.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O script roda com `bash arquivo.sh` (ou `/bin/sh`).
- [ ] Permissões, conteúdo e saída seguem o enunciado.
- [ ] Testei com `moulinette Shell01/ex08`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
