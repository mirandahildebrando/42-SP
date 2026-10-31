"""C 01 - ponteiros, arrays e parâmetros por referência."""

HELPER_IMPRIME = """
static void	imprime(int *tab, int size)
{
	int	i;

	i = 0;
	while (i < size)
	{
		if (i)
			printf(" ");
		printf("%d", tab[i]);
		i++;
	}
	printf("\\n");
}
"""

LISTA = {
    "id": "C01",
    "nome": "C 01",
    "subtitulo": "ponteiros e arrays",
    "nivel": 0,
    "introducao": (
        "A lista que separa quem entendeu ponteiros de quem só decorou. "
        "Aqui você passa endereços, modifica valores na função chamadora e "
        "percorre arrays com aritmética de ponteiros. Desenhe a memória no papel "
        "antes de codar: vale mais que qualquer vídeo."
    ),
    "regras": [
        "Cabeçalho 42 em todos os arquivos.",
        "Nada de `main` nos exercícios de função.",
        "Use apenas `write` quando o exercício pedir saída (ft_putstr).",
        "Nunca acesse fora dos limites do array.",
        "Norminette: no máximo 25 linhas por função e 4 parâmetros.",
    ],
    "exercicios": [
        {
            "id": "ex00",
            "nome": "ft_ft",
            "arquivos": ["ft_ft.c"],
            "permitidas": [],
            "tipo": "funcao",
            "prototipo": "void ft_ft(int *nbr);",
            "decl": "void ft_ft(int *nbr);",
            "objetivo": "Entender que uma função pode alterar a variável do chamador.",
            "tarefa": "Escreva uma função que coloque o valor 42 no inteiro apontado por `nbr`.",
            "exemplo": "int n = 0; ft_ft(&n);  // n agora vale 42",
            "dica": "`*nbr = 42;` — o `*` acessa o valor apontado, não o endereço.",
            "erros": ["Fazer `nbr = 42` (muda o ponteiro local).", "Esquecer o `*`."],
            "casos": [
                {"nome": "zero_vira_42",
                 "codigo": "int n = 0; ft_ft(&n); printf(\"%d\\n\", n);",
                 "esperado": "42\n"},
                {"nome": "outro_valor",
                 "codigo": "int n = -7; ft_ft(&n); printf(\"%d\\n\", n);",
                 "esperado": "42\n"},
            ],
        },
        {
            "id": "ex01",
            "nome": "ft_ultimate_ft",
            "arquivos": ["ft_ultimate_ft.c"],
            "permitidas": [],
            "tipo": "funcao",
            "prototipo": "void ft_ultimate_ft(int *********nbr);",
            "decl": "void ft_ultimate_ft(int *********nbr);",
            "objetivo": "Seguir nove níveis de indireção sem se perder.",
            "tarefa": (
                "Escreva uma função que receba um ponteiro de ponteiro (nove "
                "vezes) e coloque 42 no inteiro final."
            ),
            "exemplo": "int n; ... int *********p9 = &p8; ft_ultimate_ft(p9); // n == 42",
            "dica": "São nove `*` antes de `nbr = 42`. Conte no papel, não no olho.",
            "erros": ["Errar a quantidade de asteriscos.", "Declarar os ponteiros na ordem errada."],
            "casos": [
                {"nome": "nove_niveis",
                 "codigo": (
                     "int n = 0;\n"
                     "int *p1 = &n;\n"
                     "int **p2 = &p1;\n"
                     "int ***p3 = &p2;\n"
                     "int ****p4 = &p3;\n"
                     "int *****p5 = &p4;\n"
                     "int ******p6 = &p5;\n"
                     "int *******p7 = &p6;\n"
                     "int ********p8 = &p7;\n"
                     "int *********p9 = &p8;\n"
                     "ft_ultimate_ft(p9);\n"
                     "printf(\"%d\\n\", n);"
                 ), "esperado": "42\n"},
            ],
        },
        {
            "id": "ex02",
            "nome": "ft_swap",
            "arquivos": ["ft_swap.c"],
            "permitidas": [],
            "tipo": "funcao",
            "prototipo": "void ft_swap(int *a, int *b);",
            "decl": "void ft_swap(int *a, int *b);",
            "objetivo": "Trocar dois valores usando uma variável temporária.",
            "tarefa": "Escreva uma função que troque os valores apontados por `a` e `b`.",
            "exemplo": "int a = 1, b = 2; ft_swap(&a, &b); // a == 2, b == 1",
            "dica": "Salve `*a` em um `int tmp` antes de sobrescrever.",
            "erros": [
                "Trocar os ponteiros em vez dos valores.",
                "Esquecer a variável temporária e perder um dos valores.",
            ],
            "casos": [
                {"nome": "1_e_2",
                 "codigo": "int a = 1, b = 2; ft_swap(&a, &b); printf(\"%d %d\\n\", a, b);",
                 "esperado": "2 1\n"},
                {"nome": "negativos",
                 "codigo": "int a = -42, b = 21; ft_swap(&a, &b); printf(\"%d %d\\n\", a, b);",
                 "esperado": "21 -42\n"},
            ],
        },
        {
            "id": "ex03",
            "nome": "ft_div_mod",
            "arquivos": ["ft_div_mod.c"],
            "permitidas": [],
            "tipo": "funcao",
            "prototipo": "void ft_div_mod(int a, int b, int *div, int *mod);",
            "decl": "void ft_div_mod(int a, int b, int *div, int *mod);",
            "objetivo": "Devolver dois resultados por parâmetros de saída.",
            "tarefa": (
                "Divida `a` por `b`, guarde o quociente em `*div` e o resto "
                "em `*mod`. Considere `b` diferente de zero."
            ),
            "exemplo": "42 / 5 -> div = 8, mod = 2",
            "dica": "Use `/` e `%` uma única vez cada; cuidado com números negativos (truncamento de C).",
            "erros": ["Inverter quociente e resto.", "Não escrever nos dois ponteiros."],
            "casos": [
                {"nome": "42_por_5",
                 "codigo": "int d, m; ft_div_mod(42, 5, &d, &m); printf(\"%d %d\\n\", d, m);",
                 "esperado": "8 2\n"},
                {"nome": "negativo",
                 "codigo": "int d, m; ft_div_mod(-7, 2, &d, &m); printf(\"%d %d\\n\", d, m);",
                 "esperado": "-3 -1\n"},
            ],
        },
        {
            "id": "ex04",
            "nome": "ft_ultimate_div_mod",
            "arquivos": ["ft_ultimate_div_mod.c"],
            "permitidas": [],
            "tipo": "funcao",
            "prototipo": "void ft_ultimate_div_mod(int *a, int *b);",
            "decl": "void ft_ultimate_div_mod(int *a, int *b);",
            "objetivo": "Escrever o resultado da divisão de volta nos próprios argumentos.",
            "tarefa": (
                "Divida o valor apontado por `a` pelo valor apontado por `b`. "
                "Coloque o quociente em `*a` e o resto em `*b`."
            ),
            "exemplo": "a = 42, b = 5  ->  a = 8, b = 2",
            "dica": "Guarde o divisor antes de alterar `*b`, ou use variáveis locais.",
            "erros": [
                "Sobrescrever `*b` antes de calcular o resto.",
                "Assumir que `b` continua com o valor original.",
            ],
            "casos": [
                {"nome": "42_5",
                 "codigo": "int a = 42, b = 5; ft_ultimate_div_mod(&a, &b); printf(\"%d %d\\n\", a, b);",
                 "esperado": "8 2\n"},
                {"nome": "100_7",
                 "codigo": "int a = 100, b = 7; ft_ultimate_div_mod(&a, &b); printf(\"%d %d\\n\", a, b);",
                 "esperado": "14 2\n"},
            ],
        },
        {
            "id": "ex05",
            "nome": "ft_putstr",
            "arquivos": ["ft_putstr.c"],
            "permitidas": ["write"],
            "tipo": "funcao",
            "prototipo": "void ft_putstr(char *str);",
            "decl": "void ft_putstr(char *str);",
            "objetivo": "Percorrer uma string até o terminador nulo.",
            "tarefa": "Escreva uma função que mostre, um a um, os caracteres de uma string.",
            "exemplo": "ft_putstr(\"42SP\");  ->  42SP",
            "dica": "`while (*str) write(1, str++, 1);`",
            "erros": ["Usar `printf` ou `puts`.", "Esquecer de avançar o ponteiro.", "Tentar imprimir o `\\0`."],
            "casos": [
                {"nome": "texto", "codigo": "ft_putstr(\"42SP\");", "esperado": "42SP"},
                {"nome": "vazia", "codigo": "ft_putstr(\"\");", "esperado": ""},
                {"nome": "com_espacos", "codigo": "ft_putstr(\"hello world\");", "esperado": "hello world"},
            ],
        },
        {
            "id": "ex06",
            "nome": "ft_strlen",
            "arquivos": ["ft_strlen.c"],
            "permitidas": [],
            "tipo": "funcao",
            "prototipo": "int ft_strlen(char *str);",
            "decl": "int ft_strlen(char *str);",
            "objetivo": "Contar bytes de uma string sem usar strlen.",
            "tarefa": "Escreva uma função que retorne o tamanho de uma string (sem contar o `\\0`).",
            "exemplo": "ft_strlen(\"42SP\") -> 4",
            "dica": "Um contador e um `while (str[i]) i++;`.",
            "erros": ["Contar o terminador nulo.", "Usar `strlen` (proibido)."],
            "casos": [
                {"nome": "vazia", "codigo": "printf(\"%d\\n\", ft_strlen(\"\"));", "esperado": "0\n"},
                {"nome": "42sp", "codigo": "printf(\"%d\\n\", ft_strlen(\"42SP\"));", "esperado": "4\n"},
                {"nome": "longa",
                 "codigo": "printf(\"%d\\n\", ft_strlen(\"abcdefghijklmnopqrstuvwxyz\"));",
                 "esperado": "26\n"},
            ],
        },
        {
            "id": "ex07",
            "nome": "ft_rev_int_tab",
            "arquivos": ["ft_rev_int_tab.c"],
            "permitidas": [],
            "tipo": "funcao",
            "prototipo": "void ft_rev_int_tab(int *tab, int size);",
            "decl": "void ft_rev_int_tab(int *tab, int size);\n" + HELPER_IMPRIME,
            "objetivo": "Manipular um array in-place com dois índices.",
            "tarefa": "Escreva uma função que inverta a ordem dos elementos de um array de inteiros.",
            "exemplo": "[1, 2, 3, 4] -> [4, 3, 2, 1]",
            "dica": "Use dois índices (`i = 0`, `j = size - 1`) e troque até se cruzarem.",
            "erros": ["Trocar apenas metade dos elementos.", "Estourar o array com size 0."],
            "casos": [
                {"nome": "quatro", "codigo": "int t[] = {1, 2, 3, 4}; ft_rev_int_tab(t, 4); imprime(t, 4);", "esperado": "4 3 2 1\n"},
                {"nome": "cinco", "codigo": "int t[] = {1, 2, 3, 4, 5}; ft_rev_int_tab(t, 5); imprime(t, 5);", "esperado": "5 4 3 2 1\n"},
                {"nome": "um", "codigo": "int t[] = {42}; ft_rev_int_tab(t, 1); imprime(t, 1);", "esperado": "42\n"},
                {"nome": "zero", "codigo": "int t[] = {1}; ft_rev_int_tab(t, 0); imprime(t, 1);", "esperado": "1\n"},
            ],
        },
        {
            "id": "ex08",
            "nome": "ft_sort_int_tab",
            "arquivos": ["ft_sort_int_tab.c"],
            "permitidas": [],
            "tipo": "funcao",
            "prototipo": "void ft_sort_int_tab(int *tab, int size);",
            "decl": "void ft_sort_int_tab(int *tab, int size);\n" + HELPER_IMPRIME,
            "objetivo": "Ordenar um array in-place (bubble/selection/insertion).",
            "tarefa": "Escreva uma função que ordene um array de inteiros em ordem crescente.",
            "exemplo": "[3, 1, 4, 1, 5] -> [1, 1, 3, 4, 5]",
            "dica": "Bubble sort é suficiente: dois loops e uma troca. Cuide do size 0.",
            "erros": [
                "Esquecer de repetir as passagens.",
                "Acessar `tab[j + 1]` quando j chega ao fim.",
                "Não tratar arrays já ordenados (não é erro, mas faça o loop terminar).",
            ],
            "casos": [
                {"nome": "desordenado", "codigo": "int t[] = {3, 1, 4, 1, 5}; ft_sort_int_tab(t, 5); imprime(t, 5);", "esperado": "1 1 3 4 5\n"},
                {"nome": "invertido", "codigo": "int t[] = {5, 4, 3, 2, 1}; ft_sort_int_tab(t, 5); imprime(t, 5);", "esperado": "1 2 3 4 5\n"},
                {"nome": "negativos", "codigo": "int t[] = {0, -5, 42, -42, 7}; ft_sort_int_tab(t, 5); imprime(t, 5);", "esperado": "-42 -5 0 7 42\n"},
                {"nome": "vazio", "codigo": "int t[] = {1}; ft_sort_int_tab(t, 0); imprime(t, 1);", "esperado": "1\n"},
            ],
        },
    ],
}
