# Como treinar (e passar)

## O ciclo de um exercício

1. **Leia o enunciado inteiro** antes de abrir o editor. Anote no papel:
   entrada, saída, casos especiais, arquivos a entregar e funções permitidas.
2. **Escreva o protótipo** e um esboço em pseudocódigo.
3. **Implemente em pedaços pequenos.** Compile cedo:
   ```sh
   gcc -Wall -Wextra -Werror ft_ex.c -o a.out
   ```
4. **Rode a norminette.** Corrija tabs, linhas longas e funções grandes antes
   de perder tempo depurando lógica.
5. **Rode o corretor:**
   ```sh
   moulinette --pasta .
   ```
6. Se falhar, leia **a primeira** mensagem. Corrija, rode de novo.
7. Quando passar, escreva em uma frase o que aprendeu. No dia seguinte, refaça
   de memória.

## A regra dos 45 minutos

Travar faz parte. Mas travar 2 horas em um exercício é desperdício.

- 30 min sem progresso: releia o enunciado em voz alta, desenhe a memória.
- 45 min: peça uma dica a um colega (sem pedir código).
- 60 min: peça para alguém revisar seu raciocínio.
- Só depois de tentar de verdade, consulte uma solução — e reescreva sem olhar.

## Como estudar com o corretor

- `moulinette C00` corrige a lista toda, mas **não faça isso antes de tentar**.
- `--sem-norma` serve para testar lógica rápido, não para entregar.
- `--verboso` mostra o que o teste viu; use quando a mensagem não bastar.
- O painel marca `ALTERADO` quando você mexe em algo já validado.
- O estado `M` é exercício manual (Shell01/ex08).

## Norminette: o que mais reprova

- Cabeçalho 42 ausente ou inválido.
- Espaços em vez de tabs na indentação.
- Linha com mais de 80 colunas.
- Função com mais de 25 linhas.
- Mais de 4 parâmetros.
- Variável declarada no meio da função.
- Comentário dentro de função (evite; a Norma restringe).
- Falta de newline no fim do arquivo.
- Mais de 5 funções por arquivo.

Rode `norminette arquivo.c` a cada 10 minutos, não só no final.

## Exames

O simulador fica na raiz do projeto. O fluxo é:

```sh
exame iniciar exam00
exame status
exame entregar
```

Durante o simulado, não leia os testes nem o gabarito. A nota baixa é
informação: mostra o que revisar. Veja `../exames/README.md` e
`../PLANO-16-DIAS.md`.

## Na piscina oficial

- Durma. Cansaço derruba mais gente que ponteiro.
- Faça os exercícios fáceis primeiro; a nota é acumulativa.
- Valide com os colegas (avaliação por pares) e aceite críticas.
- Não copie código e não use IA para resolver durante a piscina. As regras da
  42 são rígidas e a expulsão é real.
- Pergunte “por quê”, não “qual é a resposta”.
- Inscreva-se no **evento** e no **projeto Exam00** no primeiro dia.

## O que fazer quando um teste falha

1. Leia o caso que falhou e reproduza no papel com uma entrada pequena.
2. Verifique o `\0` das strings e os limites dos arrays.
3. Verifique se a função foi chamada com o tipo certo.
4. Se for Norma, corrija a Norma antes de mexer na lógica.
5. Explique a correção em voz alta. Se não conseguir explicar, ainda não
   entendeu.

## Rotina semanal recomendada

- 4 a 5 dias por semana, 2 a 4 horas por dia.
- Um dia para revisar exercícios antigos sem consultar.
- Um simulado no fim de cada fase.
- Um dia leve antes da piscina; chegar descansado vale mais que um exercício
  extra.
