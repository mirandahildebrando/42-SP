# Shell 00 — arquivos, permissões, tar, git, find e file

A lista de shell da piscina. Aqui não existe compilador: o que conta é o estado dos arquivos, as permissões, o conteúdo dos scripts e a saída dos comandos. Leia o enunciado inteiro e teste no Git Bash.

## Regras da lista

- Os scripts devem rodar com `/bin/sh` (no Windows, use o Git Bash).
- Não deixe arquivos extras na pasta do exercício.
- Permissões e nomes de arquivos fazem parte da nota.
- Use `man` e `--help`; entender o comando vale mais que decorar.
- Os exercícios com adaptação para Windows estão marcados no enunciado.

## Exercícios

| # | Exercício | Arquivo(s) | Permitidas |
|---|---|---|---|
| ex00 | [Z](ex00/ENUNCIADO.md) | `z` | — |
| ex01 | [testShell00](ex01/ENUNCIADO.md) | `testShell00.tar` | — |
| ex02 | [Oh yeah, mooore...](ex02/ENUNCIADO.md) | `exo2.tar` | — |
| ex03 | [Connect me!](ex03/ENUNCIADO.md) | `klist.txt` | — |
| ex04 | [midLS](ex04/ENUNCIADO.md) | `midLS` | — |
| ex05 | [GiT commit](ex05/ENUNCIADO.md) | `git_commit.sh` | — |
| ex06 | [gitignore](ex06/ENUNCIADO.md) | `git_ignore.sh` | — |
| ex07 | [diff](ex07/ENUNCIADO.md) | `b` | — |
| ex08 | [clean](ex08/ENUNCIADO.md) | `clean` | — |
| ex09 | [Illusions, not tricks, Michael...](ex09/ENUNCIADO.md) | `ft_magic` | — |

## Como treinar esta lista

```sh
cd piscina/Shell00
moulinette .             # corrige a lista inteira
moulinette Shell00/ex00   # corrige um exercício
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
