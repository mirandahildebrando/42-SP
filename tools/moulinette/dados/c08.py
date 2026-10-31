"""C 08 - headers, macros, structs e arrays de structs."""

STOCK = """#ifndef FT_STOCK_STR_H
# define FT_STOCK_STR_H

typedef struct s_stock_str
{
	int		size;
	char	*str;
	char	*copy;
}	t_stock_str;

#endif
"""

LISTA = {
    "id": "C08",
    "nome": "C 08",
    "subtitulo": "headers, macros e structs",
    "nivel": 3,
    "introducao": (
        "A última lista de C da piscina junta tudo: arquivos de cabeçalho, "
        "include guards, macros, typedefs, structs e arrays de structs com "
        "alocação. É a ponte para o projeto libft. Aqui o `#include \"...\"` e "
        "os protótipos precisam estar perfeitos."
    ),
    "regras": [
        "Cabeçalho 42 em todos os arquivos (norminette com -R CheckForbiddenSourceHeader).",
        "Include guards em todos os headers: `#ifndef`, `#define`, `#endif`.",
        "Header não compila sozinho: apenas declara tipos e protótipos.",
        "Structs e typedefs exatamente como o subject pede.",
        "Nos exercícios 04 e 05, o header ft_stock_str.h é fornecido.",
    ],
    "exercicios": [
        {
            "id": "ex00",
            "nome": "ft.h",
            "arquivos": ["ft.h"],
            "permitidas": [],
            "tipo": "compilar",
            "prototipo": "ft.h com os cinco protótipos",
            "decl": (
                "void\tft_putchar(char c) { (void)c; }\n"
                "void\tft_swap(int *a, int *b) { (void)a; (void)b; }\n"
                "void\tft_putstr(char *str) { (void)str; }\n"
                "int\t\tft_strlen(char *str) { (void)str; return (0); }\n"
                "int\t\tft_strcmp(char *s1, char *s2) { (void)s1; (void)s2; return (0); }"
            ),
            "includes": ["\"ft.h\""],
            "objetivo": "Criar seu primeiro header e entender protótipos.",
            "tarefa": (
                "Crie `ft.h` com o include guard e os protótipos de: "
                "`ft_putchar`, `ft_swap`, `ft_putstr`, `ft_strlen` e `ft_strcmp`."
            ),
            "exemplo": "void ft_putchar(char c);\nint ft_strlen(char *str);",
            "dica": "O header só declara. As definições ficam nos .c. Teste incluindo o header em dois arquivos diferentes.",
            "erros": [
                "Esquecer o include guard (erro de redefinição).",
                "Colocar corpo de função no header.",
                "Trocar a ordem/tipo dos parâmetros.",
            ],
            "casos": [
                {"nome": "compila_e_inclui", "codigo": "printf(\"ok\\n\");", "esperado": "ok\n"},
            ],
        },
        {
            "id": "ex01",
            "nome": "ft_boolean.h",
            "arquivos": ["ft_boolean.h"],
            "permitidas": [],
            "tipo": "compilar",
            "norm_ignorar": ["MACRO_FUNC_FORBIDDEN", "PREPROC_CONSTANT", "TERNARY_FBIDDEN"],
            "prototipo": "ft_boolean.h com t_bool, TRUE, FALSE, SUCCESS, EVEN, EVEN_MSG, ODD_MSG",
            "decl": "",
            "includes": ["\"ft_boolean.h\""],
            "objetivo": "Definir tipos, macros e mensagens em um header.",
            "tarefa": (
                "Crie `ft_boolean.h` para compilar o main do subject. Ele precisa "
                "definir `t_bool` (int), `TRUE` (1), `FALSE` (0), `SUCCESS` (0), "
                "a macro `EVEN(nbr)` e as strings `EVEN_MSG` e `ODD_MSG` com as "
                "mensagens do enunciado, incluindo o `\\n`."
            ),
            "exemplo": "EVEN(42) -> verdadeiro; EVEN(41) -> falso",
            "dica": "EVEN pode ser `((nbr) % 2 == 0)`. Coloque parênteses em volta do argumento da macro.",
            "erros": [
                "Não incluir `<unistd.h>` se o main usar write (o main de teste inclui).",
                "Esquecer o `\\n` nas mensagens.",
                "Definir EVEN sem parênteses e quebrar com expressões.",
            ],
            "casos": [
                {"nome": "macros",
                 "codigo": "printf(\"%d|%d|%d\\n\", TRUE, FALSE, SUCCESS); printf(\"%d|%d\\n\", EVEN(42), EVEN(41)); printf(\"%s\", EVEN_MSG); printf(\"%s\", ODD_MSG);",
                 "esperado": "1|0|0\n1|0\nI have an even number of arguments.\nI have an odd number of arguments.\n"},
            ],
        },
        {
            "id": "ex02",
            "nome": "ft_abs.h",
            "arquivos": ["ft_abs.h"],
            "permitidas": [],
            "tipo": "compilar",
            "norm_ignorar": ["MACRO_FUNC_FORBIDDEN", "PREPROC_CONSTANT", "TERNARY_FBIDDEN"],
            "prototipo": "#define ABS(Value) ...",
            "decl": "",
            "includes": ["\"ft_abs.h\""],
            "objetivo": "Escrever uma macro segura com parênteses.",
            "tarefa": "Crie a macro `ABS(Value)` que retorna o valor absoluto.",
            "exemplo": "ABS(-42) -> 42",
            "dica": "`#define ABS(Value) ((Value) < 0 ? -(Value) : (Value))` — os parênteses externos são obrigatórios.",
            "erros": ["Sem parênteses, quebra em expressões como ABS(a - b).", "Usar função em vez de macro."],
            "casos": [
                {"nome": "valores",
                 "codigo": "printf(\"%d %d %d %d\\n\", ABS(-42), ABS(0), ABS(42), ABS(-2147483647));",
                 "esperado": "42 0 42 2147483647\n"},
            ],
        },
        {
            "id": "ex03",
            "nome": "ft_point.h",
            "arquivos": ["ft_point.h"],
            "permitidas": [],
            "tipo": "compilar",
            "prototipo": "typedef struct s_point { int x; int y; } t_point;",
            "decl": "void\tset_point(t_point *point)\n{\n\tpoint->x = 42;\n\tpoint->y = 21;\n}",
            "includes": ["\"ft_point.h\""],
            "objetivo": "Definir uma struct e um typedef em um header.",
            "tarefa": "Crie `ft_point.h` de forma que o main do subject compile e use `t_point` com os campos `x` e `y`.",
            "exemplo": "t_point p; set_point(&p); // p.x == 42, p.y == 21",
            "dica": "A struct precisa se chamar `s_point`? O subject usa apenas `t_point`; o typedef é o que importa. Use include guard.",
            "erros": ["Esquecer o typedef.", "Errar o nome dos campos.", "Declarar a struct dentro de uma função."],
            "casos": [
                {"nome": "set_point",
                 "codigo": "t_point p; set_point(&p); printf(\"%d %d\\n\", p.x, p.y);",
                 "esperado": "42 21\n"},
            ],
        },
        {
            "id": "ex04",
            "nome": "ft_strs_to_tab",
            "arquivos": ["ft_strs_to_tab.c"],
            "permitidas": ["malloc", "free"],
            "tipo": "funcao",
            "prototipo": "struct s_stock_str *ft_strs_to_tab(int ac, char **av);",
            "decl": "struct s_stock_str *ft_strs_to_tab(int ac, char **av);",
            "includes": ["\"ft_stock_str.h\""],
            "arquivos_providos": {"ft_stock_str.h": STOCK},
            "ignorar_norm": ["ft_stock_str.h"],
            "objetivo": "Transformar argv em um array de structs alocado.",
            "tarefa": (
                "Para cada uma das `ac` strings de `av`, crie uma struct com "
                "`size` (comprimento), `str` (ponteiro original) e `copy` (cópia "
                "alocada). O array retornado deve ter `ac + 1` elementos e o "
                "último deve ter `str = NULL`. Retorne NULL em erro."
            ),
            "exemplo": "av=[\"42\",\"SP\"] -> [{2,\"42\",\"42\"},{2,\"SP\",\"SP\"},{0,NULL,NULL}]",
            "dica": "Aloque `(ac + 1) * sizeof(t_stock_str)`. Para cada item, aloque `size + 1` e copie. Cuide do vazamento em caso de erro.",
            "erros": [
                "Esquecer o terminador `str = NULL`.",
                "Apontar `copy` para `str` em vez de alocar.",
                "Não tratar ac == 0.",
                "Esquecer o `\\0` da cópia.",
            ],
            "casos": [
                {"nome": "tres",
                 "codigo": "char *av[]={\"hello\",\"42\",\"world\"}; t_stock_str *tab=ft_strs_to_tab(3,av); if (!tab) printf(\"NULL\\n\"); else { for (int i=0;i<3;i++) printf(\"%d|%s|%s|%d\\n\",tab[i].size,tab[i].str,tab[i].copy,tab[i].copy!=tab[i].str); printf(\"END:%d\\n\",tab[3].str==NULL); }",
                 "esperado": "5|hello|hello|1\n2|42|42|1\n5|world|world|1\nEND:1\n"},
                {"nome": "zero",
                 "codigo": "char *av[]={NULL}; t_stock_str *tab=ft_strs_to_tab(0,av); if (!tab) printf(\"NULL\\n\"); else printf(\"END:%d\\n\",tab[0].str==NULL);",
                 "esperado": "END:1\n"},
                {"nome": "string_vazia",
                 "codigo": "char *av[]={\"\"}; t_stock_str *tab=ft_strs_to_tab(1,av); if (!tab) printf(\"NULL\\n\"); else printf(\"%d|[%s]|%d|END:%d\\n\",tab[0].size,tab[0].copy,tab[0].copy!=tab[0].str,tab[1].str==NULL);",
                 "esperado": "0|[]|1|END:1\n"},
            ],
        },
        {
            "id": "ex05",
            "nome": "ft_show_tab",
            "arquivos": ["ft_show_tab.c"],
            "permitidas": ["write"],
            "tipo": "funcao",
            "prototipo": "void ft_show_tab(struct s_stock_str *par);",
            "decl": "void ft_show_tab(struct s_stock_str *par);",
            "includes": ["\"ft_stock_str.h\""],
            "arquivos_providos": {"ft_stock_str.h": STOCK},
            "ignorar_norm": ["ft_stock_str.h"],
            "objetivo": "Percorrer um array de structs e imprimir todos os campos.",
            "tarefa": (
                "Para cada elemento do array (até `str == NULL`), mostre a "
                "string, o tamanho e a cópia, cada um seguido de `\\n`. Use "
                "apenas `write`."
            ),
            "exemplo": "hello / 5 / HELLO (cada um em uma linha)",
            "dica": "Você pode reaproveitar um putstr e um putnbr. O fim do array é `par[i].str == NULL`.",
            "erros": [
                "Parar no primeiro `str` vazio (use o ponteiro nulo, não o conteúdo).",
                "Imprimir `str` em vez de `copy` no terceiro campo.",
                "Esquecer o newline do tamanho.",
            ],
            "casos": [
                {"nome": "tres_elementos",
                 "codigo": "t_stock_str tab[4]; tab[0].size=5; tab[0].str=\"hello\"; tab[0].copy=\"HELLO\"; tab[1].size=2; tab[1].str=\"42\"; tab[1].copy=\"42\"; tab[2].size=0; tab[2].str=\"\"; tab[2].copy=\"\"; tab[3].str=NULL; ft_show_tab(tab);",
                 "esperado": "hello\n5\nHELLO\n42\n2\n42\n\n0\n\n"},
                {"nome": "copia_modificada",
                 "codigo": "t_stock_str tab[2]; tab[0].size=3; tab[0].str=\"abc\"; tab[0].copy=\"XYZ\"; tab[1].str=NULL; ft_show_tab(tab);",
                 "esperado": "abc\n3\nXYZ\n"},
            ],
        },
    ],
}
