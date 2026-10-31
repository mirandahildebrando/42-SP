"""Shell 00 - arquivos, permissões, tar, git, find e file."""

A = """STARWARS
Episode IV, A NEW HOPE It is a period of civil war.

Rebel spaceships, striking from a hidden base, have won their first victory against the evil
Galactic Empire.
During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate weapon, the
DEATH STAR,
an armored space station with enough power to destroy an entire planet.

Pursued by the Empire's sinister agents, Princess Leia races home aboard her starship, custodian of
the stolen plans that can save her people and restore freedom to the galaxy...

"""

LISTA = {
    "id": "Shell00",
    "nome": "Shell 00",
    "subtitulo": "arquivos, permissões, tar, git, find e file",
    "nivel": 1,
    "introducao": (
        "A lista de shell da piscina. Aqui não existe compilador: o que conta é "
        "o estado dos arquivos, as permissões, o conteúdo dos scripts e a saída "
        "dos comandos. Leia o enunciado inteiro e teste no Git Bash."
    ),
    "regras": [
        "Os scripts devem rodar com `/bin/sh` (no Windows, use o Git Bash).",
        "Não deixe arquivos extras na pasta do exercício.",
        "Permissões e nomes de arquivos fazem parte da nota.",
        "Use `man` e `--help`; entender o comando vale mais que decorar.",
        "Os exercícios com adaptação para Windows estão marcados no enunciado.",
    ],
    "exercicios": [
        {
            "id": "ex00",
            "nome": "Z",
            "arquivos": ["z"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "z",
            "prototipo": "z",
            "objetivo": "Criar um arquivo cujo conteúdo é exatamente Z e uma quebra de linha.",
            "tarefa": (
                "Crie o arquivo `z` com o caractere `Z` seguido de `\\n`. "
                "O comando `cat z` deve imprimir `Z` e nada mais."
            ),
            "exemplo": "cat z\nZ",
            "dica": "`printf 'Z\\n' > z` é o caminho mais curto. Evite `echo` se não souber como ele trata `\\n`.",
            "erros": [
                "Deixar um espaço depois do Z.",
                "Criar `Z` com maiúscula no nome do arquivo.",
                "Esquecer a quebra de linha final.",
            ],
        },
        {
            "id": "ex01",
            "nome": "testShell00",
            "arquivos": ["testShell00.tar"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "tar_test",
            "prototipo": "testShell00.tar",
            "objetivo": "Reproduzir permissões e tamanho de um arquivo dentro de um tar.",
            "tarefa": (
                "Crie um arquivo `testShell00` com **40 bytes** e permissão "
                "`-r--r-xr-x` (modo 0545). Depois gere `testShell00.tar` com "
                "`tar -cf testShell00.tar testShell00 .`. O conteúdo do arquivo "
                "não é avaliado, apenas nome, tamanho e modo."
            ),
            "exemplo": "ls -l\n-r--r-xr-x 1 hilde hilde 40 ... testShell00",
            "dica": (
                "`yes A | head -c 40 > testShell00` cria os 40 bytes. "
                "`chmod 545 testShell00` ajusta o modo. Se o Windows ignorar o "
                "chmod, use `tar --mode=545 -cf testShell00.tar testShell00 .`."
            ),
            "erros": [
                "Criar o tar antes de ajustar o modo.",
                "Usar 0444 em vez de 0545.",
                "Esquecer o ponto final do comando tar (ele inclui o diretório atual).",
            ],
        },
        {
            "id": "ex02",
            "nome": "Oh yeah, mooore...",
            "arquivos": ["exo2.tar"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "tar_exo2",
            "prototipo": "exo2.tar",
            "objetivo": "Criar uma árvore com permissões, tamanhos, hard link e symlink.",
            "tarefa": (
                "Crie os arquivos e diretórios abaixo com os modos e tamanhos "
                "indicados, depois rode `tar -cf exo2.tar *`:\n\n"
                "```text\n"
                "drwx--xr-x  test0/            (0715)\n"
                "-rwx--xr--  test1  4 bytes     (0714)\n"
                "dr-x---r--  test2/            (0504)\n"
                "-r-----r--  test3  1 byte      (0404, hard link)\n"
                "-rw-r----x  test4  2 bytes     (0641)\n"
                "-r-----r--  test5  1 byte      (0404, mesmo inode de test3)\n"
                "lrwxr-xr-x  test6 -> test0    (symlink)\n"
                "```\n\n"
                "O `ls -l` do subject mostra `test3` e `test5` com link count 2. "
                "No Git Bash, use `ln test3 test5`; se o Windows não criar hard "
                "link, crie dois arquivos de 1 byte com o mesmo conteúdo (o "
                "validador local aceita essa adaptação)."
            ),
            "exemplo": "ls -l\ntotal ...\ndrwx--xr-x ... test0\n-rwx--xr-- ... test1",
            "dica": (
                "Use `chmod` com modo octal: `chmod 715 test0`. Para os bytes, "
                "`head -c 4 /dev/zero > test1`, `head -c 1 /dev/zero > test3`, "
                "`head -c 2 /dev/zero > test4`. Crie o symlink com "
                "`ln -s test0 test6`."
            ),
            "erros": [
                "Colocar barra no nome dos diretórios ao criar (o `ls` mostra a barra, o nome não tem).",
                "Esquecer o hard link entre test3 e test5.",
                "Criar test6 como cópia em vez de symlink.",
            ],
        },
        {
            "id": "ex03",
            "nome": "Connect me!",
            "arquivos": ["klist.txt"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "klist",
            "prototipo": "klist.txt",
            "objetivo": "Entender tickets Kerberos e salvar a saída do klist.",
            "tarefa": (
                "No cluster da 42, obtenha um ticket Kerberos e rode "
                "`klist > klist.txt`. No Windows não há Kerberos configurado: "
                "use o simulador `klist-sim > klist.txt` (ele está no PATH do "
                "ambiente) ou, se tiver um ticket real, use `klist`."
            ),
            "exemplo": "klist-sim > klist.txt\ncat klist.txt",
            "dica": "O arquivo deve ter `Ticket cache`, `Default principal` e uma linha com `krbtgt`.",
            "erros": [
                "Salvar a saída de `klist` sem redirecionar.",
                "Criar um arquivo vazio.",
                "Confundir o nome do arquivo: é `klist.txt`, não `klist`.",
            ],
        },
        {
            "id": "ex04",
            "nome": "midLS",
            "arquivos": ["midLS"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "midls",
            "prototipo": "midLS (uma linha de comando)",
            "objetivo": "Listar arquivos por data, com vírgulas e barras nos diretórios.",
            "tarefa": (
                "Coloque no arquivo `midLS` **uma única linha de comando** que "
                "liste os arquivos e diretórios do diretório atual (sem ocultos "
                "e sem `.`/`..`), separados por vírgula, em ordem de data de "
                "modificação, com `/` no final dos diretórios. Não adicione "
                "cabeçalho, comentários ou um `main`."
            ),
            "exemplo": "arquivo_novo, pasta_nova/, arquivo_antigo",
            "dica": "`ls -1tp` já coloca `/` nos diretórios e ordena por data; depois use `sed`/`tr` para as vírgulas.",
            "erros": [
                "Usar `ls -l` e deixar o cabeçalho/total na saída.",
                "Esquecer a barra nos diretórios.",
                "Deixar uma vírgula sobrando no final (o validador tolera, mas o ideal é não deixar).",
            ],
        },
        {
            "id": "ex05",
            "nome": "GiT commit",
            "arquivos": ["git_commit.sh"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "git_commit",
            "prototipo": "git_commit.sh",
            "objetivo": "Escrever um script que mostra os 5 últimos commits.",
            "tarefa": (
                "Crie `git_commit.sh`, um script que exibe os IDs dos últimos "
                "5 commits do repositório atual, um por linha. Ele será testado "
                "em um repositório criado pelo corretor."
            ),
            "exemplo": "bash git_commit.sh | cat -e\nbaa23b...$",
            "dica": "`git log --format=%H -5` resolve. Não use caminho absoluto nem `cd` para outro repositório.",
            "erros": [
                "Mostrar a mensagem do commit em vez do hash.",
                "Mostrar mais ou menos de 5 commits.",
                "Assumir que o script roda na sua pasta, e não no repositório de teste.",
            ],
        },
        {
            "id": "ex06",
            "nome": "gitignore",
            "arquivos": ["git_ignore.sh"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "git_ignore",
            "prototipo": "git_ignore.sh",
            "objetivo": "Listar arquivos ignorados pelo Git.",
            "tarefa": (
                "Crie `git_ignore.sh`, um script que lista os arquivos existentes "
                "ignorados pelo repositório Git atual, um por linha."
            ),
            "exemplo": "bash git_ignore.sh | cat -e\n.DS_Store$\nmywork.c~$",
            "dica": "`git ls-files --others --ignored --exclude-standard` é o comando canônico.",
            "erros": [
                "Listar arquivos rastreados em vez de ignorados.",
                "Incluir diretórios vazios (o Git não os rastreia).",
                "Depender de um `.gitignore` específico da sua pasta.",
            ],
        },
        {
            "id": "ex07",
            "nome": "diff",
            "arquivos": ["b"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "diff_b",
            "arquivos_providos": {"a": A},
            "prototipo": "a  ->  b",
            "objetivo": "Criar uma versão modificada de um texto e testar diff/patch.",
            "tarefa": (
                "O arquivo `a` já está na pasta. Crie `b` como uma cópia "
                "modificada de `a` (uma ou mais mudanças de texto). "
                "`diff -u a b` deve gerar um patch que possa ser aplicado "
                "sobre uma cópia limpa de `a`. Não altere `a`."
            ),
            "exemplo": "diff -u a b > sw.diff\npatch a < sw.diff",
            "dica": "Copie `a` para `b` e mude uma palavra. Use `diff -u` para conferir e `patch` para testar a aplicação.",
            "erros": [
                "Deixar `b` idêntico a `a`.",
                "Modificar `a` em vez de criar `b`.",
                "Criar um patch que não aplica (por exemplo, mudando várias linhas sem contexto).",
            ],
        },
        {
            "id": "ex08",
            "nome": "clean",
            "arquivos": ["clean"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "clean",
            "prototipo": "clean (uma linha de comando)",
            "objetivo": "Encontrar e apagar arquivos temporários com um único comando find.",
            "tarefa": (
                "Coloque no arquivo `clean` uma única linha de comando que "
                "procure, a partir do diretório atual e em todos os "
                "subdiretórios, arquivos cujo nome termine em `~` ou comece e "
                "termine com `#`. O comando deve mostrar e apagar os arquivos. "
                "Não use `;`, `&&` ou `||`."
            ),
            "exemplo": "find . \\( -name '*~' -o -name '#*#' \\) -print -delete",
            "dica": "`find` aceita `-print` e `-delete`; a precedência do `-o` exige parênteses escapados.",
            "erros": [
                "Apagar só os arquivos do diretório atual.",
                "Esquecer de mostrar os nomes.",
                "Usar dois comandos separados por `;`.",
            ],
        },
        {
            "id": "ex09",
            "nome": "Illusions, not tricks, Michael...",
            "arquivos": ["ft_magic"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "magic",
            "prototipo": "ft_magic",
            "objetivo": "Escrever uma regra de magic file para detectar o byte 42.",
            "tarefa": (
                "Crie o arquivo `ft_magic` no formato do comando `file`, capaz "
                "de detectar arquivos que tenham a string `42` a partir do "
                "42º byte (offset 42)."
            ),
            "exemplo": "file -m ft_magic arquivo42\narquivo42: 42",
            "dica": "A sintaxe é `offset tipo teste [mensagem]`. Comece com `42 string 42`.",
            "erros": [
                "Usar offset 41 ou 43.",
                "Escrever `42 string \"42\"` com aspas que o magic não espera.",
                "Deixar o arquivo sem quebra de linha final.",
            ],
        },
    ],
}
