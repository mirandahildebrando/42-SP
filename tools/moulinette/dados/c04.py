"""C 04 - números, bases e conversões."""

LISTA = {
    "id": "C04",
    "nome": "C 04",
    "subtitulo": "números e bases",
    "nivel": 1,
    "introducao": (
        "A lista da aritmética de caracteres. Você vai converter texto em "
        "inteiro, inteiro em texto e transitar entre bases numéricas. É também "
        "onde `INT_MIN` aparece para lembrar que `-2147483648` não cabe positivo "
        "em um `int`."
    ),
    "regras": [
        "Cabeçalho 42 e Norminette.",
        "Só `write` nos exercícios de saída; nada de `printf`.",
        "Bases válidas têm pelo menos 2 caracteres, sem repetição, sem `+`, `-` ou espaços.",
        "Cuidado com overflow: negue depois de converter para `long` ou trate `INT_MIN`.",
    ],
    "exercicios": [
        {
            "id": "ex00",
            "nome": "ft_strlen",
            "arquivos": ["ft_strlen.c"],
            "permitidas": [],
            "tipo": "funcao",
            "prototipo": "int ft_strlen(char *str);",
            "decl": "int ft_strlen(char *str);",
            "objetivo": "Reescrever strlen mais uma vez, agora com confiança.",
            "tarefa": "Retorne o número de caracteres de `str`, sem contar o `\\0`.",
            "exemplo": "ft_strlen(\"42SP\") -> 4",
            "dica": "Se já fez na C01, escreva de memória e confira os casos vazios.",
            "erros": ["Contar o terminador.", "Usar strlen."],
            "casos": [
                {"nome": "vazia", "codigo": "printf(\"%d\\n\", ft_strlen(\"\"));", "esperado": "0\n"},
                {"nome": "42", "codigo": "printf(\"%d\\n\", ft_strlen(\"42\"));", "esperado": "2\n"},
                {"nome": "longa", "codigo": "printf(\"%d\\n\", ft_strlen(\"A piscina da 42SP\"));", "esperado": "17\n"},
            ],
        },
        {
            "id": "ex01",
            "nome": "ft_putstr",
            "arquivos": ["ft_putstr.c"],
            "permitidas": ["write"],
            "tipo": "funcao",
            "prototipo": "void ft_putstr(char *str);",
            "decl": "void ft_putstr(char *str);",
            "objetivo": "Imprimir uma string com write.",
            "tarefa": "Mostre a string recebida, caractere por caractere.",
            "exemplo": "ft_putstr(\"42SP\") -> 42SP",
            "dica": "Pare no `\\0`; não tente imprimi-lo.",
            "erros": ["Usar printf.", "Loop infinito por não avançar o ponteiro."],
            "casos": [
                {"nome": "texto", "codigo": "ft_putstr(\"42SP\");", "esperado": "42SP"},
                {"nome": "vazia", "codigo": "ft_putstr(\"\");", "esperado": ""},
            ],
        },
        {
            "id": "ex02",
            "nome": "ft_putnbr",
            "arquivos": ["ft_putnbr.c"],
            "permitidas": ["write"],
            "tipo": "funcao",
            "prototipo": "void ft_putnbr(int nb);",
            "decl": "void ft_putnbr(int nb);",
            "objetivo": "Imprimir um inteiro completo, sem printf.",
            "tarefa": "Mostre o inteiro `nb`, incluindo sinal e `INT_MIN`.",
            "exemplo": "ft_putnbr(-42) -> -42",
            "dica": "Recursão: divida por 10, imprima o resto depois, e trate o negativo antes.",
            "erros": ["Overflow em `-nb` com INT_MIN.", "Ordem dos dígitos invertida."],
            "casos": [
                {"nome": "zero", "codigo": "ft_putnbr(0);", "esperado": "0"},
                {"nome": "positivo", "codigo": "ft_putnbr(42);", "esperado": "42"},
                {"nome": "negativo", "codigo": "ft_putnbr(-42);", "esperado": "-42"},
                {"nome": "int_min", "codigo": "ft_putnbr(INT_MIN);", "esperado": "-2147483648"},
            ],
        },
        {
            "id": "ex03",
            "nome": "ft_atoi",
            "arquivos": ["ft_atoi.c"],
            "permitidas": [],
            "tipo": "funcao",
            "prototipo": "int ft_atoi(char *str);",
            "decl": "int ft_atoi(char *str);",
            "objetivo": "Converter texto em inteiro como a função atoi.",
            "tarefa": (
                "Converta a string para `int`. Ignore espaços no início, aceite "
                "um sinal `+` ou `-` e pare no primeiro caractere que não for "
                "dígito. Sem dígitos, retorne 0."
            ),
            "exemplo": "ft_atoi(\"  -42abc\") -> -42",
            "dica": "Acumule `result = result * 10 + (c - '0')` e aplique o sinal no final.",
            "erros": [
                "Não pular espaços iniciais.",
                "Aceitar letras no meio sem parar.",
                "Esquecer o sinal negativo.",
                "Estourar com INT_MIN.",
            ],
            "casos": [
                {"nome": "simples", "codigo": "printf(\"%d\\n\", ft_atoi(\"42\"));", "esperado": "42\n"},
                {"nome": "espacos_sinal", "codigo": "printf(\"%d\\n\", ft_atoi(\"   -42\"));", "esperado": "-42\n"},
                {"nome": "mais", "codigo": "printf(\"%d\\n\", ft_atoi(\"+42\"));", "esperado": "42\n"},
                {"nome": "para_na_letra", "codigo": "printf(\"%d\\n\", ft_atoi(\"123abc\"));", "esperado": "123\n"},
                {"nome": "sem_digito", "codigo": "printf(\"%d\\n\", ft_atoi(\"abc\"));", "esperado": "0\n"},
                {"nome": "tabs", "codigo": "printf(\"%d\\n\", ft_atoi(\" \\t\\n -42\"));", "esperado": "-42\n"},
                {"nome": "int_max", "codigo": "printf(\"%d\\n\", ft_atoi(\"2147483647\"));", "esperado": "2147483647\n"},
                {"nome": "int_min", "codigo": "printf(\"%d\\n\", ft_atoi(\"-2147483648\"));", "esperado": "-2147483648\n"},
            ],
        },
        {
            "id": "ex04",
            "nome": "ft_putnbr_base",
            "arquivos": ["ft_putnbr_base.c"],
            "permitidas": ["write"],
            "tipo": "funcao",
            "prototipo": "void ft_putnbr_base(int nbr, char *base);",
            "decl": "void ft_putnbr_base(int nbr, char *base);",
            "objetivo": "Imprimir um número em qualquer base.",
            "tarefa": (
                "Mostre `nbr` na base representada por `base`. A base define os "
                "símbolos e o tamanho. Números negativos começam com `-`. "
                "Considere a base sempre válida."
            ),
            "exemplo": "42 na base \"01\" -> 101010; -42 na base decimal -> -42",
            "dica": "Descubra o tamanho da base, trate o sinal e use recursão com `% base_len` e `/ base_len`.",
            "erros": [
                "Assumir base 10.",
                "Não tratar negativo.",
                "Overflow com INT_MIN.",
                "Imprimir o dígito antes da recursão (ordem invertida).",
            ],
            "casos": [
                {"nome": "decimal", "codigo": "ft_putnbr_base(42, \"0123456789\");", "esperado": "42"},
                {"nome": "negativo", "codigo": "ft_putnbr_base(-42, \"0123456789\");", "esperado": "-42"},
                {"nome": "binario", "codigo": "ft_putnbr_base(42, \"01\");", "esperado": "101010"},
                {"nome": "hex", "codigo": "ft_putnbr_base(255, \"0123456789ABCDEF\");", "esperado": "FF"},
                {"nome": "poney", "codigo": "ft_putnbr_base(668, \"poneyvif\");", "esperado": "oney"},
                {"nome": "zero_poney", "codigo": "ft_putnbr_base(0, \"poneyvif\");", "esperado": "p"},
                {"nome": "int_min", "codigo": "ft_putnbr_base(INT_MIN, \"0123456789\");", "esperado": "-2147483648"},
            ],
        },
        {
            "id": "ex05",
            "nome": "ft_atoi_base",
            "arquivos": ["ft_atoi_base.c"],
            "permitidas": [],
            "tipo": "funcao",
            "prototipo": "int ft_atoi_base(char *str, char *base);",
            "decl": "int ft_atoi_base(char *str, char *base);",
            "objetivo": "Ler um número escrito em qualquer base.",
            "tarefa": (
                "Converta `str`, escrita na base `base`, para `int`. Ignore "
                "espaços iniciais, aceite sinais e pare no primeiro caractere "
                "que não pertence à base. Considere a base válida."
            ),
            "exemplo": "ft_atoi_base(\"  -2A\", \"0123456789ABCDEF\") -> -42",
            "dica": "Para cada caractere, ache o índice dele na base. Se não existir, pare. Acumule com `result = result * base_len + índice`.",
            "erros": [
                "Não achar o índice corretamente (base arbitrária).",
                "Confundir o valor do caractere com o índice.",
                "Ignorar o sinal.",
            ],
            "casos": [
                {"nome": "decimal", "codigo": "printf(\"%d\\n\", ft_atoi_base(\"42\", \"0123456789\"));", "esperado": "42\n"},
                {"nome": "hex_negativo", "codigo": "printf(\"%d\\n\", ft_atoi_base(\"  -2A\", \"0123456789ABCDEF\"));", "esperado": "-42\n"},
                {"nome": "binario", "codigo": "printf(\"%d\\n\", ft_atoi_base(\"101\", \"01\"));", "esperado": "5\n"},
                {"nome": "poney", "codigo": "printf(\"%d\\n\", ft_atoi_base(\"poney\", \"poneyvif\"));", "esperado": "668\n"},
                {"nome": "hex_255", "codigo": "printf(\"%d\\n\", ft_atoi_base(\"ff\", \"0123456789abcdef\"));", "esperado": "255\n"},
                {"nome": "invalido_para", "codigo": "printf(\"%d\\n\", ft_atoi_base(\"xyz\", \"0123456789\"));", "esperado": "0\n"},
                {"nome": "sinais", "codigo": "printf(\"%d\\n\", ft_atoi_base(\"--+42\", \"0123456789\"));", "esperado": "42\n"},
                {"nome": "vazia", "codigo": "printf(\"%d\\n\", ft_atoi_base(\"\", \"0123456789\"));", "esperado": "0\n"},
            ],
        },
    ],
}
