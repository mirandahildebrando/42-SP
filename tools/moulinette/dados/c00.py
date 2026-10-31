"""C 00 - primeiros passos com write, loops e ASCII."""

from itertools import combinations


def _comb(n, tamanho):
    return ", ".join("".join(str(d) for d in c)
                     for c in combinations(range(10), tamanho))


LISTA = {
    "id": "C00",
    "nome": "C 00",
    "subtitulo": "write, loops e ASCII",
    "nivel": 0,
    "introducao": (
        "A primeira lista da piscina. Aqui você aprende a usar apenas `write` "
        "para falar com o terminal, a construir loops simples e a pensar em "
        "cada caractere como um byte. Não use `printf`, `puts` ou funções da "
        "libc: a graça é fazer tudo na mão."
    ),
    "regras": [
        "Todos os arquivos precisam do cabeçalho 42 (rode `42header arquivo.c`).",
        "Norminette deve passar: tabs, 25 linhas por função, 80 colunas, etc.",
        "Compile com `gcc -Wall -Wextra -Werror`.",
        "Nenhum `main` nos exercícios de função.",
        "Só é permitido usar `write` (e mais nada da libc).",
    ],
    "exercicios": [
        {
            "id": "ex00",
            "nome": "ft_putchar",
            "arquivos": ["ft_putchar.c"],
            "permitidas": ["write"],
            "tipo": "funcao",
            "prototipo": "void ft_putchar(char c);",
            "decl": "void ft_putchar(char c);",
            "objetivo": "Escrever um único caractere na saída padrão.",
            "tarefa": (
                "Escreva uma função que receba um caractere e o envie para a "
                "saída padrão usando `write(1, &c, 1)`."
            ),
            "exemplo": "ft_putchar('A');  ->  A",
            "dica": (
                "`write` recebe o endereço do byte: `write(1, &c, 1)`. "
                "Confira o retorno de `write`? Na piscina, o retorno é ignorado "
                "sem problema."
            ),
            "erros": [
                "Usar `printf` ou `putchar` (proibido).",
                "Esquecer o `#include <unistd.h>`.",
                "Passar `c` em vez de `&c` para `write`.",
            ],
            "casos": [
                {"nome": "letra_A", "codigo": "ft_putchar('A');", "esperado": "A"},
                {"nome": "quebra_linha", "codigo": "ft_putchar('\\n');", "esperado": "\n"},
                {"nome": "zero", "codigo": "ft_putchar('0');", "esperado": "0"},
                {"nome": "til", "codigo": "ft_putchar('~');", "esperado": "~"},
            ],
        },
        {
            "id": "ex01",
            "nome": "ft_print_alphabet",
            "arquivos": ["ft_print_alphabet.c"],
            "permitidas": ["write"],
            "tipo": "funcao",
            "prototipo": "void ft_print_alphabet(void);",
            "decl": "void ft_print_alphabet(void);",
            "objetivo": "Imprimir o alfabeto minúsculo, em ordem.",
            "tarefa": (
                "Escreva uma função que mostre o alfabeto em minúsculas, em "
                "ordem crescente, na saída padrão."
            ),
            "exemplo": "ft_print_alphabet();  ->  abcdefghijklmnopqrstuvwxyz",
            "dica": "Use um `char` começando em `'a'` e um `while (c <= 'z')`.",
            "erros": [
                "Imprimir com `printf`.",
                "Esquecer de incrementar a variável (loop infinito).",
                "Usar uma string literal gigante em vez de um loop (passa, mas não aprende).",
            ],
            "casos": [
                {"nome": "alfabeto", "codigo": "ft_print_alphabet();",
                 "esperado": "abcdefghijklmnopqrstuvwxyz"},
            ],
        },
        {
            "id": "ex02",
            "nome": "ft_print_reverse_alphabet",
            "arquivos": ["ft_print_reverse_alphabet.c"],
            "permitidas": ["write"],
            "tipo": "funcao",
            "prototipo": "void ft_print_reverse_alphabet(void);",
            "decl": "void ft_print_reverse_alphabet(void);",
            "objetivo": "Imprimir o alfabeto minúsculo de trás para frente.",
            "tarefa": (
                "Escreva uma função que mostre o alfabeto em minúsculas, em "
                "ordem decrescente, na saída padrão."
            ),
            "exemplo": "ft_print_reverse_alphabet();  ->  zyxwvutsrqponmlkjihgfedcba",
            "dica": "Comece em `'z'` e decremente até `'a'`.",
            "erros": ["Loop que nunca termina.", "Imprimir na ordem errada."],
            "casos": [
                {"nome": "invertido", "codigo": "ft_print_reverse_alphabet();",
                 "esperado": "zyxwvutsrqponmlkjihgfedcba"},
            ],
        },
        {
            "id": "ex03",
            "nome": "ft_print_numbers",
            "arquivos": ["ft_print_numbers.c"],
            "permitidas": ["write"],
            "tipo": "funcao",
            "prototipo": "void ft_print_numbers(void);",
            "decl": "void ft_print_numbers(void);",
            "objetivo": "Imprimir os dígitos de 0 a 9.",
            "tarefa": "Escreva uma função que mostre os dígitos de 0 a 9, em ordem.",
            "exemplo": "ft_print_numbers();  ->  0123456789",
            "dica": "Comece em `'0'` e vá até `'9'`.",
            "erros": ["Confundir o caractere `'0'` com o número 0.", "Usar `printf`."],
            "casos": [
                {"nome": "digitos", "codigo": "ft_print_numbers();",
                 "esperado": "0123456789"},
            ],
        },
        {
            "id": "ex04",
            "nome": "ft_is_negative",
            "arquivos": ["ft_is_negative.c"],
            "permitidas": ["write"],
            "tipo": "funcao",
            "prototipo": "void ft_is_negative(int n);",
            "decl": "void ft_is_negative(int n);",
            "objetivo": "Classificar um inteiro como negativo ou não.",
            "tarefa": (
                "Escreva uma função que mostre `N` se o inteiro recebido for "
                "negativo e `P` caso contrário. Zero é não-negativo."
            ),
            "exemplo": "ft_is_negative(-42); -> N\nft_is_negative(0); -> P",
            "dica": "Use um `if (n < 0)` e dois `write`, um em cada caminho.",
            "erros": [
                "Tratar zero como negativo.",
                "Usar `printf`.",
                "Escrever os dois caracteres sempre.",
            ],
            "casos": [
                {"nome": "menos_um", "codigo": "ft_is_negative(-1);", "esperado": "N"},
                {"nome": "zero", "codigo": "ft_is_negative(0);", "esperado": "P"},
                {"nome": "positivo", "codigo": "ft_is_negative(42);", "esperado": "P"},
                {"nome": "int_min", "codigo": "ft_is_negative(INT_MIN);", "esperado": "N"},
            ],
        },
        {
            "id": "ex05",
            "nome": "ft_print_comb",
            "arquivos": ["ft_print_comb.c"],
            "permitidas": ["write"],
            "tipo": "funcao",
            "prototipo": "void ft_print_comb(void);",
            "decl": "void ft_print_comb(void);",
            "objetivo": "Gerar todas as combinações crescentes de 3 dígitos.",
            "tarefa": (
                "Escreva uma função que mostre todas as combinações diferentes "
                "de três dígitos em ordem crescente, separadas por `, `, sem "
                "repetir a mesma combinação em ordem diferente. A menor é `012` "
                "e a maior é `789`."
            ),
            "exemplo": "012, 013, 014, ..., 789",
            "dica": (
                "Três loops aninhados (a < b < c). Para imprimir os três dígitos "
                "sem repetir código, crie uma função auxiliar `ft_putchar` no "
                "mesmo arquivo (permitido)."
            ),
            "erros": [
                "Imprimir vírgula depois da última combinação.",
                "Gerar combinações repetidas (ex.: 012 e 021).",
                "Usar `printf`.",
            ],
            "casos": [
                {"nome": "comb3", "codigo": "ft_print_comb();", "gerador": "comb3"},
            ],
        },
        {
            "id": "ex06",
            "nome": "ft_print_comb2",
            "arquivos": ["ft_print_comb2.c"],
            "permitidas": ["write"],
            "tipo": "funcao",
            "prototipo": "void ft_print_comb2(void);",
            "decl": "void ft_print_comb2(void);",
            "objetivo": "Gerar todos os pares de números de 00 a 99.",
            "tarefa": (
                "Escreva uma função que mostre todas as combinações de dois "
                "números entre 00 e 99, em ordem crescente, no formato "
                "`XX XX`, separadas por `, `. O primeiro número é sempre menor "
                "que o segundo."
            ),
            "exemplo": "00 01, 00 02, ..., 00 99, 01 02, ..., 98 99",
            "dica": (
                "Dois loops de 0 a 99 com `a < b`. Para imprimir dois dígitos, "
                "use divisão e módulo por 10. Cuidado com o separador: imprima "
                "antes do par, exceto no primeiro."
            ),
            "erros": [
                "Imprimir `00 00`.",
                "Esquecer o zero à esquerda.",
                "Vírgula sobrando no final.",
            ],
            "casos": [
                {"nome": "comb2", "codigo": "ft_print_comb2();", "gerador": "comb2"},
            ],
        },
        {
            "id": "ex07",
            "nome": "ft_putnbr",
            "arquivos": ["ft_putnbr.c"],
            "permitidas": ["write"],
            "tipo": "funcao",
            "prototipo": "void ft_putnbr(int nb);",
            "decl": "void ft_putnbr(int nb);",
            "objetivo": "Imprimir um inteiro, incluindo o menor int possível.",
            "tarefa": (
                "Escreva uma função que mostre o número recebido como "
                "argumento. Ela precisa funcionar com todos os valores de `int`, "
                "inclusive `INT_MIN` (-2147483648)."
            ),
            "exemplo": "ft_putnbr(-42); -> -42",
            "dica": (
                "O truque clássico: trate `INT_MIN` separadamente ou use "
                "`long`/`long long` para evitar overflow ao negar o número. "
                "Recursão resolve dígito a dígito."
            ),
            "erros": [
                "`-nb` com `INT_MIN` causa overflow (undefined behavior).",
                "Perder o sinal de menos.",
                "Ordem dos dígitos invertida.",
            ],
            "casos": [
                {"nome": "zero", "codigo": "ft_putnbr(0);", "esperado": "0"},
                {"nome": "positivo", "codigo": "ft_putnbr(42);", "esperado": "42"},
                {"nome": "negativo", "codigo": "ft_putnbr(-42);", "esperado": "-42"},
                {"nome": "int_max", "codigo": "ft_putnbr(INT_MAX);", "esperado": "2147483647"},
                {"nome": "int_min", "codigo": "ft_putnbr(INT_MIN);", "esperado": "-2147483648"},
            ],
        },
        {
            "id": "ex08",
            "nome": "ft_print_combn",
            "arquivos": ["ft_print_combn.c"],
            "permitidas": ["write"],
            "tipo": "funcao",
            "prototipo": "void ft_print_combn(int n);",
            "decl": "void ft_print_combn(int n);",
            "objetivo": "Generalizar ft_print_comb para qualquer n de 1 a 9.",
            "tarefa": (
                "Escreva uma função que mostre todas as combinações de `n` "
                "dígitos em ordem crescente, separadas por `, `, sem repetição. "
                "`n` estará entre 1 e 9."
            ),
            "exemplo": "n=2 -> 01, 02, ..., 89\nn=3 -> 012, 013, ..., 789",
            "dica": (
                "Recursão é o caminho natural: escolha o próximo dígito sempre "
                "maior que o anterior. Guarde os dígitos em um array de 10 e "
                "imprima quando o array estiver cheio. Para o separador, imprima "
                "antes de cada combinação, exceto na primeira."
            ),
            "erros": [
                "Não tratar n=1.",
                "Estourar o buffer de dígitos.",
                "Separador errado ou combinações fora de ordem.",
            ],
            "casos": [
                {"nome": "n1", "codigo": "ft_print_combn(1);", "gerador": "combn1"},
                {"nome": "n2", "codigo": "ft_print_combn(2);", "gerador": "combn2"},
                {"nome": "n3", "codigo": "ft_print_combn(3);", "gerador": "combn3"},
                {"nome": "n5", "codigo": "ft_print_combn(5);", "gerador": "combn5"},
                {"nome": "n9", "codigo": "ft_print_combn(9);", "gerador": "combn9", "timeout": 60},
            ],
        },
    ],
}
