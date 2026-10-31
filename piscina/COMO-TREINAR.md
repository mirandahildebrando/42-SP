# Como treinar (e passar)

## O ciclo de um exercício

1. **Leia o enunciado inteiro** antes de abrir o editor. Marque no papel:
   entrada, saída, casos especiais e funções permitidas.
2. **Escreva o protótipo** e um esboço em pseudocódigo.
3. **Implemente em pedaços pequenos.** Compile cedo:
   ```sh
   gcc -Wall -Wextra -Werror ft_ex.c -o a.out
   ```
4. **Rode a norminette.** Corrija tabs, linhas longas e funções grandes
   antes de perder tempo depurando lógica.
5. **Rode o corretor**:
   ```sh
   moulinette C00/ex00
   ```
6. Se falhar, leia **a primeira** mensagem. Corrija, rode de novo.
7. Quando passar, escreva em uma frase o que aprendeu. No dia seguinte,
   refaça de memória.

## A regra dos 30 minutos

Travar faz parte. Mas travar 2 horas em um exercício é desperdício.

- 30 min sem progresso: releia o enunciado em voz alta, desenhe a memória.
- 45 min: peça uma dica a um colega (sem pedir código).
- 60 min: peça para alguém revisar seu raciocínio.
- Só depois de tentar de verdade, consulte uma solução — e reescreva sem olhar.

## Como estudar com o corretor

- `moulinette C00` corrige a lista toda, mas **não faça isso antes de tentar**.
- `--sem-norma` serve para testar lógica rápido, não para entregar.
- `--verboso` mostra o que o teste viu; use quando a mensagem não bastar.
- O painel (`moulinette`) marca `ALTERADO` quando você mexe em algo já validado.

## Norminette: o que mais reprova

- Cabeçalho 42 ausente ou inválido.
- Espaços em vez de tabs na indentação.
- Linha com mais de 80 colunas.
- Função com mais de 25 linhas.
- Mais de 4 parâmetros.
- Variável declarada no meio da função.
- Comentário dentro de função (a Norma só permite no corpo? evite).
- Falta de newline no fim do arquivo.
- Mais de 5 funções por arquivo.

Rode `norminette arquivo.c` a cada 10 minutos, não só no final.

## Exames

Os simulados ficam em `piscina/exames/`. O fluxo é:

```sh
exame exam00              # cria a sessão e começa o cronômetro
exame exam00 status       # quanto falta
exame exam00 entregar     # corrige tudo e gera o resultado
```

Durante o simulado, não leia os testes nem o gabarito. A nota baixa é
informação: mostra o que revisar.

## Na piscina oficial

- Durma. Cansaço derruba mais gente que ponteiro.
- Faça os exercícios fáceis primeiro; a nota é acumulativa.
- Valide com os colegas (avaliação por pares) e aceite críticas.
- Não copie código e não use IA para resolver durante a piscina. As regras
  da 42 são rígidas e a expulsão é real.
- Pergunte "por quê", não "qual é a resposta".
