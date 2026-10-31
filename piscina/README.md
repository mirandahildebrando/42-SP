# Piscina 42SP — ambiente de treino

Este diretório contém as listas da piscina, enunciados em português e um corretor local que imita o essencial da Moulinette: cabeçalho 42, norminette, compilação com `-Wall -Wextra -Werror`, funções proibidas e testes de comportamento.

## Comece por aqui

1. Leia [COMO-TREINAR.md](COMO-TREINAR.md).
2. Abra o terminal com `ABRIR-42.cmd` (na raiz do projeto).
3. Rode `moulinette` para ver o painel.
4. Entre em `C00/ex00`, leia o enunciado e crie o arquivo.

## Listas

| Lista | Tema | Exercícios |
|---|---|---|
| [C 00](C00/README.md) | write, loops e ASCII | 9 |
| [C 01](C01/README.md) | ponteiros e arrays | 9 |
| [C 02](C02/README.md) | strings e caracteres | 11 |
| [C 03](C03/README.md) | comparar, juntar, procurar | 5 |
| [C 04](C04/README.md) | números e bases | 6 |
| [C 05](C05/README.md) | recursão e algoritmos | 9 |
| [C 06](C06/README.md) | argc e argv | 4 |
| [C 07](C07/README.md) | malloc, arrays e split | 6 |
| [C 08](C08/README.md) | headers, macros e structs | 6 |
| [Shell 00](Shell00/README.md) | arquivos, permissões, tar, git, find e file | 10 |
| [Shell 01](Shell01/README.md) | grupos, find, contagem, MAC, quoting e pipelines | 9 |

## Comandos

```sh
moulinette                  # painel de progresso
moulinette C00              # corrige a lista C00
moulinette C00/ex00         # corrige um exercício
moulinette --pasta .        # corrige o exercício desta pasta
exame exam00                # inicia um simulado de exame
exame exam00 status         # tempo restante
exame exam00 entregar       # corrige o simulado
42header arquivo.c          # insere o cabeçalho 42
```

## Regras de convivência

- O corretor é local: ele **não** substitui a Moulinette oficial.
- Os testes são para aprender; não os leia antes de tentar resolver.
- Não copie soluções de colegas nem gere código com IA durante a piscina oficial. Aqui, use tudo como ferramenta de estudo.
- Se um teste parecer errado, anote o caso e me avise: o objetivo é que o ambiente fique fiel.

## Estrutura

```text
piscina/
├── C00/ ... C08/      listas de C
├── Shell00/ Shell01/  listas de shell
├── exames/            simulados e banco de exercícios
├── COMO-TREINAR.md
└── PROGRESSO.md       gerado pelo corretor
```

---

Bom treino. A piscina é difícil, mas é feita de exercícios pequenos. Um por vez.
