# Simulador de exames

Os simulados existem para treinar **tempo**, **leitura de subject** e **entrega**,
não para substituir a avaliação oficial.

## Como funciona

Cada sessão cria uma pasta em `exames/sessoes/` com quatro exercícios sorteados
do currículo. Os arquivos são cópias: você pode editar à vontade, mas o
resultado não altera seu progresso normal em `piscina/`.

O tempo começa a contar no `exame iniciar`. O simulador não bloqueia o editor
quando o tempo acaba; ele marca a entrega como `ATRASADO`. Seja honesto: pare de
codar no limite e entregue.

## Exames

| ID | Tema | Duração | Meta local |
|---|---|---|---|
| `exam00` | primeiras listas, funções e loops | 2h | 75% |
| `exam01` | strings, ponteiros e programas | 3h | 75% |
| `exam02` | malloc, listas e arquivos | 4h | 80% |
| `exam03` | argv, bases e funções maiores | 4h | 80% |
| `final` | tudo junto, na véspera | 5h | 90% |

A meta é local. Na 42, o critério oficial é a Moulinette e o regulamento do
exame; não presuma que 75% aqui é aprovação garantida.

## Comandos

```sh
exame                         # lista exames e melhores notas
exame iniciar exam00          # abre sessão
exame iniciar exam00 --semente 42   # repete o mesmo sorteio
exame status                  # tempo restante e arquivos
exame entregar                # corrige e encerra
exame resultado               # relatório da última sessão
exame historico               # todas as notas
exame abrir                   # abre a pasta no Explorer
exame cancelar                # cancela a sessão aberta
```

## O que é corrigido

- Cabeçalho 42 e norminette.
- Funções proibidas (incluindo `main` em exercício de função).
- Compilação com `-Wall -Wextra -Werror`.
- Testes de comportamento dos casos do currículo.
- Tempo usado e atraso.

A nota é a média dos quatro exercícios; cada exercício vale 100 somente se
passar em tudo. Um erro de Norma zera o exercício, como acontece nas entregas
da piscina.

## Ética

- Não consulte os testes, soluções ou IA durante o simulado.
- Não abra outra sessão para “espiar” os exercícios.
- Se travar, use o tempo como usaria no exame: leia de novo, faça um caso
  pequeno, deixe para depois e volte.
- Ao terminar, estude cada erro na pasta principal antes de repetir o exame.

## Onde ficam os resultados

- `exames/sessoes/<data>_<exame>/sessao.json`: respostas, notas e relatório.
- `exames/historico.json`: histórico resumido.

Esses arquivos são ignorados pelo Git. Se quiser começar do zero, apague a
pasta `exames/sessoes` e o `historico.json` (com o ambiente fechado).
