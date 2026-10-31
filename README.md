# Piscina 42SP — ambiente de treino no Windows

Ambiente local para estudar as listas da Piscina 42SP antes da piscina de
**16/11/2026**. O objetivo é chegar sabendo ler um subject, escrever C dentro da
Norma, testar o próprio código e administrar o tempo de exame.

> Este material é de treino. Na piscina oficial, siga as regras da 42: não copie
> código e não use IA para resolver os exercícios.

## Comece agora

1. Dê dois cliques em **`ABRIR-42.cmd`**. Ele abre o Git Bash já com GCC,
   norminette, `moulinette`, `42header` e `exame` no PATH.
2. Entre no primeiro exercício:
   ```sh
   cd piscina/C00/ex00
   ```
3. Leia o `ENUNCIADO.md` inteiro e crie o arquivo pedido.
4. Insira o cabeçalho e teste:
   ```sh
   42header ft_putchar.c
   moulinette --pasta .
   ```
5. Quando terminar a lista:
   ```sh
   moulinette C00
   ```

Se preferir o Prompt de Comando do Windows, use `TESTAR.cmd C00/ex00` ou
`TESTAR.cmd --pasta piscina\C00\ex00`.

## O que está pronto

| Parte | Situação |
|---|---|
| Listas **C00 a C08** | 65 exercícios com enunciado em português, testes e corretor |
| Validação das soluções de referência | **65/65 exercícios C passando** |
| **Shell00 e Shell01** | 19 exercícios adaptados ao Windows; 18 com validador automático |
| Simulador de exames | `exam00` a `exam03` + `final`, com cronômetro e relatório |
| Norminette | 3.3.60, com cabeçalho 42 e regras da Piscina |
| Launchers | `ABRIR-42.cmd`, `TESTAR.cmd`, `NORMINETTE.cmd`, `42HEADER.cmd`, `EXAME.cmd` |

O único exercício sem correção automática é o **Shell01/ex08 (`add_chelou`)**:
o subject oficial depende de `bc` e de variáveis com quoting muito específico,
que o Git Bash do Windows não reproduz com fidelidade. Ele está marcado como
**MANUAL** no painel; confira o exemplo no enunciado.

## Comandos principais

```sh
moulinette                  # painel de progresso
moulinette C00              # corrige a lista C00
moulinette C00/ex00         # corrige um exercício
moulinette --pasta .        # corrige o exercício da pasta atual
moulinette --tudo           # corrige todas as listas
moulinette --verboso C00/ex00
moulinette --sem-norma C00/ex00   # só para depurar lógica
```

```sh
exame                       # lista os simulados
exame iniciar exam00        # cria uma sessão cronometrada
exame status                # tempo restante e arquivos
exame entregar              # corrige, encerra e gera relatório
exame historico
```

```sh
norminette arquivo.c        # dentro do Git Bash
42header arquivo.c
gcc -Wall -Wextra -Werror arquivo.c -o a.out
```

Veja a lista completa em [COMANDOS.md](COMANDOS.md) e o cronograma em
[PLANO-16-DIAS.md](PLANO-16-DIAS.md).

## Estrutura

```text
SP42/
├─ ABRIR-42.cmd          terminal pronto (recomendado)
├─ TESTAR.cmd            corretor pelo Prompt de Comando
├─ NORMINETTE.cmd
├─ 42HEADER.cmd
├─ piscina/
│  ├─ C00/ ... C08/      enunciados e pastas dos exercícios
│  ├─ Shell00/ Shell01/
│  ├─ README.md
│  └─ COMO-TREINAR.md
├─ exames/
│  ├─ README.md
│  ├─ sessoes/           criado ao iniciar um simulado (ignorado pelo Git)
│  └─ historico.json     criado ao entregar (ignorado pelo Git)
├─ tools/
│  ├─ mingw64/           GCC 16.2.0 + mingw32-make
│  ├─ moulinette/        motor do corretor e currículo
│  ├─ shell/             42rc e stubs de comandos do Windows
│  ├─ exame/             simulador
│  └─ validacao/         soluções de referência (material interno)
├─ PLANO-16-DIAS.md
├─ REVISAO.md
└─ COMANDOS.md
```

## Adaptações inevitáveis no Windows

- O Git Bash não traz `rev`, `bc` nem Kerberos. `rev` e um `klist` simulado são
  fornecidos em `tools/shell/bin`; `bc` não está disponível.
- O nome do arquivo do Shell01/ex05 com `?*"` não é criável no NTFS. O exercício
  local usa `MaRViN`; o enunciado explica a adaptação.
- `chmod` pode não ser aplicado pelo NTFS. No Shell00/ex01, se o tar sair com
  modo errado, use `tar --mode=545 -cf testShell00.tar testShell00 .`.
- O Shell01/ex07 usa um `/etc/passwd` simulado para que o pipeline possa ser
  corrigido no Windows.
- O Shell01/ex08 é manual.

## Regras de estudo

- Leia o subject antes de codar; não abra os testes antes de tentar.
- Rode a norminette a cada bloco, não só no fim.
- Se travar 45 minutos, peça uma dica (sem pedir código) ou releia o enunciado.
- Ao passar, explique em voz alta o que o exercício ensina. Se não conseguir
  explicar, ainda não aprendeu.
- No dia seguinte, refaça de memória um exercício do dia anterior.
- Durma. A piscina é uma maratona, não uma prova de resistência sem sono.

Bom treino. A piscina é difícil, mas é feita de exercícios pequenos: um por vez.
