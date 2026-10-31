# Plano de 16 dias — 31/10 a 15/11/2026

A piscina começa em **segunda, 16/11/2026**. Este plano usa os 16 dias que
restam. Ele é uma referência: se um dia render menos, não compense virando a
noite. Constância vale mais que uma maratona isolada.

## Meta do plano

- Terminar **C00 a C08** até **quinta, 12/11**.
- Fazer **Shell00 e Shell01** em paralelo, sem deixar para o fim.
- Fazer pelo menos **um simulado completo por fase**.
- Chegar em 15/11 descansado, com o ambiente testado e sem exercício novo
  pendente.

## Rotina diária (4 horas)

| Bloco | Tempo | O que fazer |
|---|---|---|
| Revisão | 15 min | refaça de memória um exercício do dia anterior |
| Leitura | 25 min | leia o subject, anote entradas, saídas e casos especiais |
| Código | 2h | implemente em pedaços pequenos; compile cedo |
| Norma + testes | 40 min | norminette, `moulinette --pasta .`, corrija a primeira falha |
| Diário | 20 min | escreva o que aprendeu e o que ainda confunde |

Se tiver só 2 horas, faça: 10 min de revisão + 50 min de código + 20 min de
Norma/testes + 10 min de diário. O importante é não pular a correção.

## Calendário

### Semana 1 — fundamentos e strings

**Sábado 31/10 — C00 (1/2) + Shell00 (1/2)**
- C00/ex00 a ex04.
- Shell00/ex00 e ex01.
- Teste o ambiente com `moulinette --pasta .` e `42header`.

**Domingo 01/11 — C00 (2/2) + Shell00 (2/2)**
- C00/ex05 a ex08.
- Shell00/ex02 a ex04.
- Se travar em `ft_print_combn`, desenhe a recursão no papel antes de codar.

**Segunda 02/11 — C01 + Shell00 (3/3)**
- C01/ex00 a ex08 (ponteiros, arrays, swap).
- Shell00/ex05 e ex06.
- Revise `ft_ultimate_ft`: desenhe os níveis de ponteiro.

**Terça 03/11 — C02 (1/2) + Shell00 (4/4)**
- C02/ex00 a ex05.
- Shell00/ex07 a ex09.
- Leia sobre `unsigned char` em `ft_str_is_*`.

**Quarta 04/11 — C02 (2/2) + Exam00**
- C02/ex06 a ex10.
- Faça o **exam00** (2h) sem consultar os testes.
- Corrija e anote os erros.

### Semana 2 — números, recursão e memória

**Quinta 05/11 — C03 + Shell01 (1/2)**
- C03/ex00 a ex04.
- Shell01/ex00 a ex03.
- Compare `strcmp`, `strncmp` e `strstr` com calma.

**Sexta 06/11 — C04 + Shell01 (2/2)**
- C04/ex00 a ex05 (bases, `INT_MIN`, `long long`).
- Shell01/ex04 a ex06.
- Teste `ft_putnbr_base` com base inválida e número negativo.

**Sábado 07/11 — C05 (1/2) + Exam01**
- C05/ex00 a ex04.
- Faça o **exam01** (3h).
- Revise recursão: caso base, chamada, retorno.

**Domingo 08/11 — C05 (2/2) + revisão**
- C05/ex05 a ex08.
- Shell01/ex07 (r_dwssap).
- Refaça dois exercícios de C04 sem olhar.

### Semana 3 — argc/argv, malloc e structs

**Segunda 09/11 — C06 + revisão**
- C06/ex00 a ex03.
- Revise C03 e C04: os erros mais comuns voltam aqui.

**Terça 10/11 — C07 (1/2)**
- C07/ex00 a ex02.
- Comece `ft_split` no papel: quantos `malloc`, quem libera o quê.

**Quarta 11/11 — C07 (2/2)**
- C07/ex03 a ex05.
- Leia o enunciado de `ft_convert_base` (dois arquivos) com atenção.

**Quinta 12/11 — C08**
- C08/ex00 a ex05.
- Revise header, include guard, macros e `struct`.

**Sexta 13/11 — Exam02 + revisão**
- Faça o **exam02** (4h).
- Corrija e refaça pelo menos um exercício que falhou.

**Sábado 14/11 — Exam03 + revisão dirigida**
- Faça o **exam03** (4h).
- À tarde, revise os pontos fracos do histórico de exames.
- Não comece exercício novo.

**Domingo 15/11 — Simulado final + descanso**
- Faça o **final** (5h) no período da manhã.
- Corrija, leia os erros e feche o caderno.
- À noite: prepare material, confira login/ambiente e **durma cedo**.

## O que fazer se atrasar

1. Priorize **C00 a C06**, depois C07/C08. As primeiras listas são a base dos
   exames.
2. Se faltar tempo para Shell, faça pelo menos Shell00/ex00 a ex04 e
   Shell01/ex01 a ex03.
3. Não substitua sono por mais exercícios na véspera. Cansaço produz erro bobo
   em ponteiro, que custa mais que um exercício novo.

## Como medir se você está pronto

- Você lê um subject e consegue listar os casos de teste antes de codar.
- Você escreve uma função de até 25 linhas sem estourar a Norma.
- Você explica `malloc`/`free`, ponteiro para ponteiro e recursão sem consultar.
- Você termina um exam00 em menos de 2h e um exam02 em menos de 4h.
- Você identifica rapidamente um `segmentation fault` com `gdb`/`valgrind`?
  No Windows, use `gcc -g` e `gdb`; o hábito de investigar é o que importa.

## Na semana da piscina

- A piscina oficial começa em **16/11/2026** e vai até **11/12/2026**.
- Confirme na intranet os dias e horários de exame; eles podem mudar.
- Faça a inscrição no **evento** e no **projeto Exam00** no primeiro dia.
- Durante a piscina, nada de IA ou código de colega. Peça dicas, não respostas.
- Avalie os colegas com seriedade; a avaliação por pares também ensina.

Bom treino. O plano é um mapa, não uma prisão: se um exercício exigir mais
tempo, entenda o porquê antes de seguir.
