"""C 06 - argumentos de linha de comando."""

LISTA = {
    "id": "C06",
    "nome": "C 06",
    "subtitulo": "argc e argv",
    "nivel": 2,
    "introducao": (
        "Pela primeira vez você entrega programas completos, com `main`. "
        "`argc` é a quantidade de argumentos (incluindo o nome do programa) e "
        "`argv` é o array de strings. Todo programa aqui usa `write`; nada de "
        "`printf`."
    ),
    "regras": [
        "Cabeçalho 42 e Norminette.",
        "Agora sim: `int main(int argc, char **argv)` é obrigatório.",
        "Use apenas `write`.",
        "Não acesse `argv` fora de `0 .. argc - 1`.",
    ],
    "exercicios": [
        {
            "id": "ex00",
            "nome": "ft_print_program_name",
            "arquivos": ["ft_print_program_name.c"],
            "permitidas": ["write"],
            "tipo": "programa",
            "prototipo": "int main(int argc, char **argv);",
            "decl": "",
            "objetivo": "Entender que argv[0] é o nome do programa.",
            "tarefa": "Mostre o nome do programa (`argv[0]`) seguido de uma quebra de linha.",
            "exemplo": "./a.out  ->  ./a.out",
            "dica": "Imprima exatamente `argv[0]`, sem hardcode.",
            "erros": ["Imprimir um nome fixo.", "Esquecer a quebra de linha.", "Imprimir argv[1]."],
            "casos": [
                {"nome": "nome_do_programa", "argv": [], "esperado": "{argv0}\n",
                 "normalizar_argv0": True},
            ],
        },
        {
            "id": "ex01",
            "nome": "ft_print_params",
            "arquivos": ["ft_print_params.c"],
            "permitidas": ["write"],
            "tipo": "programa",
            "prototipo": "int main(int argc, char **argv);",
            "decl": "",
            "objetivo": "Percorrer argv e imprimir cada argumento.",
            "tarefa": "Mostre todos os argumentos recebidos, um por linha, na ordem original.",
            "exemplo": "./a.out hello 42  ->  hello\\n42\\n",
            "dica": "Comece em `i = 1` e vá até `i < argc`. Cada argumento termina com `\\n`.",
            "erros": ["Imprimir argv[0].", "Não colocar newline.", "Acessar argv[argc] como string."],
            "casos": [
                {"nome": "tres_args", "argv": ["hello", "42", "a b"],
                 "esperado": "hello\n42\na b\n"},
                {"nome": "sem_args", "argv": [], "esperado": ""},
                {"nome": "um_arg", "argv": ["42SP"], "esperado": "42SP\n"},
            ],
        },
        {
            "id": "ex02",
            "nome": "ft_rev_params",
            "arquivos": ["ft_rev_params.c"],
            "permitidas": ["write"],
            "tipo": "programa",
            "prototipo": "int main(int argc, char **argv);",
            "decl": "",
            "objetivo": "Percorrer argv de trás para frente.",
            "tarefa": "Mostre todos os argumentos, um por linha, na ordem inversa.",
            "exemplo": "./a.out a b c  ->  c\\nb\\na\\n",
            "dica": "Comece em `argc - 1` e vá até 1, decrementando.",
            "erros": ["Incluir argv[0].", "Loop com índice sem sinal (unsigned) e `i >= 0`."],
            "casos": [
                {"nome": "tres_args", "argv": ["a", "b", "c"],
                 "esperado": "c\nb\na\n"},
                {"nome": "sem_args", "argv": [], "esperado": ""},
            ],
        },
        {
            "id": "ex03",
            "nome": "ft_sort_params",
            "arquivos": ["ft_sort_params.c"],
            "permitidas": ["write"],
            "tipo": "programa",
            "prototipo": "int main(int argc, char **argv);",
            "decl": "",
            "objetivo": "Ordenar strings usando strcmp e trocar ponteiros.",
            "tarefa": (
                "Mostre os argumentos em ordem ASCII crescente, um por linha. "
                "Não é necessário ordenar o argv original: pode trocar ponteiros "
                "em uma cópia."
            ),
            "exemplo": "./a.out banana Apple 42  ->  42\\nApple\\nbanana\\n",
            "dica": "Bubble sort sobre os ponteiros de `argv` (a partir de 1), comparando com sua `ft_strcmp` ou com comparação própria.",
            "erros": ["Usar `qsort` (proibido).", "Ordenar o argv[0].", "Comparar ponteiros em vez de conteúdo."],
            "casos": [
                {"nome": "mistura", "argv": ["banana", "Apple", "42", "apple", "!"],
                 "esperado": "!\n42\nApple\napple\nbanana\n"},
                {"nome": "ja_ordenado", "argv": ["a", "b", "c"],
                 "esperado": "a\nb\nc\n"},
                {"nome": "um_arg", "argv": ["42"], "esperado": "42\n"},
            ],
        },
    ],
}
