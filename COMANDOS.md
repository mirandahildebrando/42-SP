# Comandos do dia a dia

## Abrir o ambiente

| O que fazer | Como |
|---|---|
| Terminal completo (recomendado) | duplo clique em `ABRIR-42.cmd` |
| Corrigir pelo Prompt de Comando | `TESTAR.cmd C00/ex00` |
| Corrigir a pasta atual | `TESTAR.cmd --pasta .` |
| Rodar norminette em um arquivo | `NORMINETTE.cmd piscina\C00\ex00\ft_putchar.c` |
| Inserir cabeçalho | `42HEADER.cmd piscina\C00\ex00\ft_putchar.c` |
| Simulador pelo Prompt | `EXAME.cmd iniciar exam00` |

Dentro do Git Bash, os mesmos comandos ficam disponíveis sem `.cmd`.

## Corretor

```sh
moulinette                       # painel de progresso
moulinette C00                   # corrige a lista inteira
moulinette C00/ex00              # corrige um exercício
moulinette --pasta .             # descobre o exercício pela pasta atual
moulinette --tudo                # todas as listas (C + Shell)
moulinette --verboso C00/ex00    # mostra a saída dos testes
moulinette --sem-norma C00/ex00  # testa lógica sem a Norma (não é entrega)
moulinette --json C00/ex00       # saída em JSON
moulinette --sem-cor C00         # sem cores (útil em logs)
```

Os estados do painel:

- `OK`: passou em tudo e o arquivo não mudou desde a correção.
- `??`: passou, mas você editou o arquivo depois; corrija de novo.
- `XX`: falhou, não compila, quebrou a Norma ou usou função proibida.
- `M`: exercício manual (só o Shell01/ex08).
- `[ ]`: ainda não corrigido.

## Norminette

```sh
norminette ft_putchar.c
norminette .
```

Dentro do corretor, a norminette roda com `-R CheckForbiddenSourceHeader`.
Corrija primeiro os erros de Norma; eles escondem erros de lógica.

## Cabeçalho 42

```sh
42header ft_putchar.c
```

O cabeçalho usa o login e o e-mail de `42.config`. Se mudar de login, edite
`42.config` antes de gerar novos arquivos.

## Compilar à mão

```sh
gcc -Wall -Wextra -Werror ft_putchar.c -o a.out
./a.out
```

Para um exercício com `main`:

```sh
gcc -Wall -Wextra -Werror main.c ft_ex.c -o programa
./programa
```

Nunca deixe `a.out`, `.o` ou `.build` na pasta de entrega.

## Exames

```sh
exame                         # lista exames e melhores notas
exame iniciar exam00          # abre uma sessão com cronômetro
exame iniciar exam01 --semente 42
exame status                  # tempo restante e arquivos
exame entregar                # corrige e encerra
exame resultado               # relatório da última sessão
exame historico               # todos os resultados
exame cancelar                # cancela a sessão aberta
exame abrir                   # abre a pasta no Explorer
```

Uma sessão por vez. Se o tempo acabar, o relatório marca `ATRASADO`; entregue
mesmo assim para aprender com os erros.

## Git Bash: comandos que ajudam

```sh
pwd                 # onde estou
ls -la              # arquivos, incluindo ocultos
cat arquivo         # conteúdo
cd ..               # subir um nível
find . -type f      # listar arquivos recursivamente
file arquivo        # tipo do arquivo
tar -tf arquivo.tar # listar conteúdo de um tar
chmod 545 arquivo   # permissões (quando o NTFS permitir)
```

## Limpar o progresso

O progresso fica em `piscina/.progresso.json`. Para começar do zero:

```sh
rm piscina/.progresso.json piscina/PROGRESSO.md
```

O `PROGRESSO.md` é gerado novamente na próxima correção.

## Problemas comuns

- **`python` abre a Microsoft Store**: use `ABRIR-42.cmd` ou os `.cmd`; eles
  apontam para o Python 3.12 instalado.
- **Acentos estranhos no Prompt**: rode `chcp 65001` ou use o Git Bash.
- **Norminette reclama do cabeçalho**: gere com `42header`; não copie um
  cabeçalho de outro login.
- **`Permission denied` ao rodar script**: use `bash script.sh` ou
  `chmod +x script.sh`.
- **Tar com modo errado**: use `tar --mode=545` (veja o enunciado do Shell00).
