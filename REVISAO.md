# Revisão rápida — o que cai e o que mais reprova

Use este arquivo nas revisões espaçadas. Ele não substitui os subjects: é um
mapa para você perceber o que esqueceu.

## Lista por lista

### C00 — write, loops e ASCII
- `write(1, &c, 1)`; `write` pode escrever menos que o pedido, mas nos
  exercícios simples um byte basta.
- Conversão caractere ↔ dígito: `c - '0'`.
- Loops com `while`, contadores e condições de parada.
- `ft_print_comb`/`ft_print_combn`: ordem crescente, sem repetição, formatação
  exata (vírgula, espaço, newline).
- **Erro clássico:** usar `printf`, `puts` ou `strlen` (proibidos).

### C01 — ponteiros e arrays
- `*p` acessa; `&x` endereço; `int **` é ponteiro para ponteiro.
- `ft_ultimate_ft`: nove níveis; desenhe antes.
- `ft_swap`: troque via ponteiros, sem variável global.
- `ft_div_mod`: quociente e resto; cuidado com negativo.
- `ft_rev_int_tab`/`ft_sort_int_tab`: índices e limites.
- **Erro clássico:** desreferenciar ponteiro nulo ou trocar ponteiros em vez
  de valores.

### C02 — strings e caracteres
- String em C termina em `\0`; `strlen` não conta o terminador.
- `ft_strcpy`/`ft_strncpy`: copie o `\0` quando couber; `strncpy` pode não
  terminar.
- `ft_str_is_*`: use `unsigned char` para classificar bytes acima de 127.
- `ft_strupcase`/`ft_strlowcase`: só letras.
- **Erro clássico:** escrever fora do buffer ou esquecer o `\0`.

### C03 — comparar, juntar, procurar
- `ft_strcmp`/`ft_strncmp`: retorno negativo, zero ou positivo; não precisa ser
  a diferença exata.
- `ft_strcat`/`ft_strncat`: destino precisa ter espaço; retorne `dest`.
- `ft_strstr`: se `needle` for vazio, retorne `haystack`.
- `ft_strlcat`: respeite o tamanho e sempre termine quando `size > 0`.
- **Erro clássico:** estourar o destino ou não tratar `size == 0`.

### C04 — números e bases
- `ft_strlen`, `ft_putnbr`, `ft_atoi`: sinais, espaços e limites.
- `INT_MIN` não pode ser negado em `int`; use `long long`.
- `ft_putnbr_base`: valide base (tamanho ≥ 2, sem repetição, sem `+`/`-`);
  trate `INT_MIN`.
- `ft_convert_base`: dois arquivos no C07; no C04, entenda o conceito.
- **Erro clássico:** overflow silencioso e base inválida.

### C05 — recursão e algoritmos
- `ft_recursive_factorial`, `ft_recursive_power`: caso base e propagação.
- `ft_fibonacci`: `n < 0` retorna `-1`; `fib(0)=0`, `fib(1)=1`.
- `ft_sqrt`: se não for quadrado perfeito, retorne `0`.
- `ft_is_prime`: 0 e 1 não são primos; teste até `i*i <= n`.
- `ft_ten_queens_puzzle`: backtracking; 724 soluções; formate com `write`.
- **Erro clássico:** recursão sem caso base e estouro de pilha.

### C06 — argc e argv
- `argc` conta o nome do programa; `argv[0]` é o nome.
- `ft_print_program_name`: `argv[0]` + newline.
- `ft_print_params`: um por linha; `ft_rev_params`: ordem inversa.
- `ft_sort_params`: compare com `strcmp`, troque ponteiros, imprima.
- **Erro clássico:** acessar `argv[argc]` ou esquecer newline.

### C07 — malloc, arrays e split
- `malloc(sizeof(type) * n)`; verifique `NULL`; `free` exatamente o que alocou.
- `ft_strdup`, `ft_range`, `ft_ultimate_range`: retorno e falha.
- `ft_concat_params`: soma tamanhos + separadores + `\0`.
- `ft_split`: conte palavras, aloque a matriz, trate erro no meio e libere.
- `ft_convert_base`: dois arquivos; `malloc` para o resultado.
- **Erro clássico:** vazamento, free de ponteiro não alocado e falta de `\0`.

### C08 — headers, macros e structs
- Header com include guard: `#ifndef`, `#define`, `#endif`.
- `ft.h` declara protótipos; não coloque implementação.
- Macros de `ft_abs.h`, `ft_boolean.h`, `ft_point.h`.
- `ft_stock_str.h`: struct com `char *str`, `int size`, `char *copy`.
- `ft_show_tab`: percorre o array até `str == NULL`; formatação exata.
- **Erro clássico:** incluir `.c`, duplicar símbolos ou não inicializar structs.

### Shell00 — arquivos, permissões, tar, git, find, file
- `z`: conteúdo exato, inclui newline.
- `testShell00.tar`: modo 0545, tamanho 40; o tar guarda os metadados.
- `exo2.tar`: permissões, hard link, symlink; `ln`/`ln -s`.
- `klist.txt`: no Windows use `klist-sim`.
- `midLS`: `ls -1tp`, vírgulas, sem cabeçalho.
- `git_commit.sh`: `git log --format=%H -5`.
- `git_ignore.sh`: `git ls-files --others --ignored --exclude-standard`.
- `diff`: `b` diferente de `a` e patch aplicável.
- `clean`: `find . \( -name '*~' -o -name '#*#' \) -print -delete`.
- `ft_magic`: `42 string 42`.

### Shell01 — grupos, find, contagem, MAC, quoting
- `print_groups.sh`: `id -Gn "$FT_USER" | tr ' ' ','` (sem newline no exemplo).
- `find_sh.sh`: `find . -type f -name '*.sh' -exec basename {} .sh \;`.
- `count_files.sh`: `find . | wc -l` (inclui `.`).
- `MAC.sh`: `ifconfig | grep ether | awk '{print $2}'`.
- `skip.sh`: `ls -l | awk 'NR % 2 == 1'`.
- `r_dwssap.sh`: cat → grep -v '^#' → linhas alternadas → cut → rev → sort -r
  → intervalo → `, ` → ponto final.
- `add_chelou.sh`: manual neste ambiente; entenda conversão de base e quoting.

## Norminette — checklist de 60 segundos

- [ ] Cabeçalho 42 com login e e-mail corretos.
- [ ] Tab no começo das linhas; sem espaços de indentação.
- [ ] Nenhuma linha passa de 80 colunas.
- [ ] Função com no máximo 25 linhas.
- [ ] No máximo 4 parâmetros.
- [ ] Variáveis declaradas no início do bloco.
- [ ] Uma instrução por linha; sem `for`? (permitido, mas cuidado com a Norma).
- [ ] Sem comentário dentro do corpo da função.
- [ ] Newline no fim do arquivo.
- [ ] No máximo 5 funções por arquivo.

## Funções proibidas

O corretor procura chamadas a `printf`, `puts`, `strlen`, `malloc` (quando não
permitido), `free` (quando não permitido) e outras funções da libc. Se o
subject diz “Allowed functions: write”, **somente `write`**.

`main` só é permitido nos exercícios de programa (C06, C07/ex04 etc.). Nos
exercícios de função, `main` reprova.

## Como revisar um erro

1. Leia a **primeira** linha da falha; não tente corrigir tudo de uma vez.
2. Se for Norma, corrija a Norma antes de testar lógica.
3. Se for teste, reproduza o caso no papel com entrada pequena.
4. Se for compilação, leia a primeira mensagem do GCC, não a última.
5. Se for segmentation fault, compile com `-g` e rode no `gdb`; ou reduza o caso.
6. Depois de corrigir, refaça o mesmo caso e um caso de borda.
7. Escreva em uma frase por que o erro aconteceu.

## Sinais de que você está pronto para a piscina

- [ ] Terminei C00–C06 sem consultar solução.
- [ ] Sei explicar ponteiro, array, string, malloc e recursão.
- [ ] Consigo escrever dentro da Norma sem olhar o checklist.
- [ ] Terminei pelo menos dois simulados completos.
- [ ] Meu último simulado ficou acima da meta e sem tempo estourado.
- [ ] Estou dormindo pelo menos 7 horas por noite.
