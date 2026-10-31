# Shell 01 — grupos, find, contagem, MAC, quoting e pipelines

A segunda lista de shell mistura comandos do dia a dia com quoting difícil. O objetivo não é decorar: é entender o que cada pipe faz. Teste sempre com `bash -n script.sh` e execute em uma pasta de teste.

## Regras da lista

- Cada script deve funcionar com `/bin/sh`; no Windows, use o Git Bash.
- Não deixe arquivos extras na pasta do exercício.
- Leia as variáveis de ambiente com `$FT_USER`, `$FT_LINE1`, etc.
- Evite caminhos absolutos do Windows nos scripts.
- Alguns exercícios têm adaptação documentada para Windows.

## Exercícios

| # | Exercício | Arquivo(s) | Permitidas |
|---|---|---|---|
| ex00 | [Exam](ex00/ENUNCIADO.md) | `INSCRICAO.md` | — |
| ex01 | [print_groups](ex01/ENUNCIADO.md) | `print_groups.sh` | — |
| ex02 | [find_sh](ex02/ENUNCIADO.md) | `find_sh.sh` | — |
| ex03 | [count_files](ex03/ENUNCIADO.md) | `count_files.sh` | — |
| ex04 | [MAC](ex04/ENUNCIADO.md) | `MAC.sh` | — |
| ex05 | [Can you create it?](ex05/ENUNCIADO.md) | `MaRViN` | — |
| ex06 | [Skip](ex06/ENUNCIADO.md) | `skip.sh` | — |
| ex07 | [r_dwssap](ex07/ENUNCIADO.md) | `r_dwssap.sh` | — |
| ex08 | [add_chelou](ex08/ENUNCIADO.md) | `add_chelou.sh` | — |

## Como treinar esta lista

```sh
cd piscina/Shell01
moulinette .             # corrige a lista inteira
moulinette Shell01/ex00   # corrige um exercício
```

O progresso detalhado fica em [PROGRESSO.md](../PROGRESSO.md).

### Ordem recomendada

1. Leia o enunciado inteiro e escreva o protótipo no papel.
2. Implemente sem pressa; compile cedo para pegar erros de sintaxe.
3. Rode `norminette` e corrija a forma **antes** de depurar a lógica.
4. Rode `moulinette` e leia a primeira falha, não todas de uma vez.
5. Quando passar, refaça o exercício de memória no dia seguinte.

---

[Voltar para a piscina](../README.md) • [Progresso](../PROGRESSO.md)
