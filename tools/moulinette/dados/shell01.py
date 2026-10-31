"""Shell 01 - grupos, find, count, MAC, nomes e texto."""

LISTA = {
    "id": "Shell01",
    "nome": "Shell 01",
    "subtitulo": "grupos, find, contagem, MAC, quoting e pipelines",
    "nivel": 2,
    "introducao": (
        "A segunda lista de shell mistura comandos do dia a dia com quoting "
        "difícil. O objetivo não é decorar: é entender o que cada pipe faz. "
        "Teste sempre com `bash -n script.sh` e execute em uma pasta de teste."
    ),
    "regras": [
        "Cada script deve funcionar com `/bin/sh`; no Windows, use o Git Bash.",
        "Não deixe arquivos extras na pasta do exercício.",
        "Leia as variáveis de ambiente com `$FT_USER`, `$FT_LINE1`, etc.",
        "Evite caminhos absolutos do Windows nos scripts.",
        "Alguns exercícios têm adaptação documentada para Windows.",
    ],
    "exercicios": [
        {
            "id": "ex00",
            "nome": "Exam",
            "arquivos": ["INSCRICAO.md"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "inscricao",
            "prototipo": "INSCRICAO.md",
            "objetivo": "Não esquecer a inscrição no exame oficial.",
            "tarefa": (
                "Este exercício é administrativo no subject original. Quando "
                "estiver inscrito no evento **e** no projeto Exam00, crie "
                "`INSCRICAO.md` com exatamente estas duas linhas:\n\n"
                "```text\n"
                "evento: ok\n"
                "projeto: ok\n"
                "```\n\n"
                "Na piscina, faça isso no primeiro dia; sem inscrição você "
                "não pode fazer o exame."
            ),
            "exemplo": "cat INSCRICAO.md\nevento: ok\nprojeto: ok",
            "dica": "O calendário e o projeto aparecem separados na intranet. Confirme os dois.",
            "erros": [
                "Inscrever-se só no evento e esquecer o projeto.",
                "Deixar para a última hora.",
            ],
        },
        {
            "id": "ex01",
            "nome": "print_groups",
            "arquivos": ["print_groups.sh"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "groups",
            "prototipo": "print_groups.sh",
            "objetivo": "Listar os grupos de um usuário separados por vírgula.",
            "tarefa": (
                "Escreva uma linha de comando que mostre os grupos do login "
                "contido em `$FT_USER`, separados por vírgula e sem espaços. "
                "No Windows, o comando `id` é simulado pelo ambiente para que "
                "o exercício possa ser corrigido."
            ),
            "exemplo": "FT_USER=nours ./print_groups.sh\ngod,root,admin,master,nours,bocal",
            "dica": "`id -Gn` lista os nomes dos grupos; `tr ' ' ','` troca espaços por vírgulas.",
            "erros": [
                "Deixar espaço depois da vírgula.",
                "Deixar uma quebra de linha no final.",
                "Usar `$USER` em vez de `$FT_USER`.",
            ],
        },
        {
            "id": "ex02",
            "nome": "find_sh",
            "arquivos": ["find_sh.sh"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "find_sh",
            "prototipo": "find_sh.sh",
            "objetivo": "Encontrar arquivos .sh e mostrar só o nome sem extensão.",
            "tarefa": (
                "Crie `find_sh.sh`, um script que procure em todos os "
                "subdiretórios os arquivos terminados em `.sh` e mostre apenas "
                "o nome do arquivo, sem o `.sh`, um por linha."
            ),
            "exemplo": "./find_sh.sh | cat -e\nfind_sh$\nfile1$",
            "dica": "`find . -type f -name '*.sh'` e `basename` (ou `sed`) resolvem. Cuidado com o nome do próprio script.",
            "erros": [
                "Incluir o caminho `./sub/` na saída.",
                "Incluir a extensão `.sh`.",
                "Procurar só na pasta atual.",
            ],
        },
        {
            "id": "ex03",
            "nome": "count_files",
            "arquivos": ["count_files.sh"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "count_files",
            "prototipo": "count_files.sh",
            "objetivo": "Contar arquivos e diretórios recursivamente, incluindo o ponto.",
            "tarefa": (
                "Crie `count_files.sh`, um script que conte e mostre o número "
                "de arquivos regulares e diretórios no diretório atual e em "
                "todos os subdiretórios, incluindo o diretório inicial `.`."
            ),
            "exemplo": "./count_files.sh | cat -e\n42$",
            "dica": "`find . | wc -l` conta todas as entradas, inclusive `.`. A saída deve ser só o número.",
            "erros": [
                "Contar apenas arquivos regulares.",
                "Não incluir o diretório inicial.",
                "Deixar espaços antes do número.",
            ],
        },
        {
            "id": "ex04",
            "nome": "MAC",
            "arquivos": ["MAC.sh"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "mac",
            "prototipo": "MAC.sh",
            "objetivo": "Extrair endereços MAC de uma saída de ifconfig.",
            "tarefa": (
                "Crie `MAC.sh`, um script que mostre os endereços MAC da "
                "máquina, um por linha. No Windows, `ifconfig` é simulado pelo "
                "ambiente com uma saída no formato Linux."
            ),
            "exemplo": "./MAC.sh\n00:11:22:33:44:55",
            "dica": "`ifconfig | grep ether | awk '{print $2}'` é a solução clássica.",
            "erros": [
                "Mostrar a linha inteira em vez do endereço.",
                "Incluir interfaces sem MAC.",
                "Deixar cabeçalhos ou linhas vazias.",
            ],
        },
        {
            "id": "ex05",
            "nome": "Can you create it?",
            "arquivos": ["MaRViN"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "marvin",
            "prototipo": "MaRViN (arquivo)",
            "objetivo": "Criar um arquivo com conteúdo exato e nome difícil.",
            "tarefa": (
                "O subject original pede um nome com `?`, `*`, `\"` e `\\`, "
                "que o NTFS do Windows não aceita. **Adaptação local:** crie "
                "um arquivo chamado `MaRViN` contendo exatamente os dois "
                "caracteres `42`, sem quebra de linha. Na piscina oficial, "
                "você fará o nome completo com quoting."
            ),
            "exemplo": "printf 42 > MaRViN\nwc -c MaRViN\n2 MaRViN",
            "dica": "`printf 42 > MaRViN` grava dois bytes. Confira com `xxd` ou `wc -c`.",
            "erros": [
                "Usar `echo 42`, que acrescenta uma quebra de linha.",
                "Criar `marvin` minúsculo.",
                "Deixar um espaço ou newline no conteúdo.",
            ],
        },
        {
            "id": "ex06",
            "nome": "Skip",
            "arquivos": ["skip.sh"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "skip",
            "prototipo": "skip.sh",
            "objetivo": "Mostrar linhas alternadas de uma saída.",
            "tarefa": (
                "Crie `skip.sh`, um script que execute `ls -l` e mostre uma "
                "linha sim, uma não, começando pela primeira linha."
            ),
            "exemplo": "./skip.sh | cat -e\ntotal ...$\n-rw...$",
            "dica": "`awk 'NR % 2 == 1'` ou `sed -n '1~2p'` (GNU sed).",
            "erros": [
                "Começar pela segunda linha.",
                "Mostrar a saída inteira.",
                "Colocar `ls -l` dentro do arquivo sem imprimir na tela.",
            ],
        },
        {
            "id": "ex07",
            "nome": "r_dwssap",
            "arquivos": ["r_dwssap.sh"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "r_dwssap",
            "prototipo": "r_dwssap.sh",
            "objetivo": "Transformar /etc/passwd em uma lista de logins invertidos.",
            "tarefa": (
                "Crie `r_dwssap.sh`, um script que leia `/etc/passwd`, remova "
                "comentários, pegue as linhas alternadas começando pela "
                "segunda, inverta cada login, ordene em ordem alfabética "
                "reversa, mantenha apenas entre `$FT_LINE1` e `$FT_LINE2` e "
                "separe por `, `, terminando com `.`."
            ),
            "exemplo": "FT_LINE1=7 FT_LINE2=15 ./r_dwssap.sh\nsstq_, sorebrek_brk_, soibten_, ....",
            "dica": "Monte o pipeline em etapas e teste cada uma. `cut -d: -f1`, `rev`, `sort -r`, `sed -n`, `paste -sd, -`.",
            "erros": [
                "Inverter a linha inteira em vez do login.",
                "Esquecer de remover os comentários antes de alternar linhas.",
                "Deixar a vírgula final ou o ponto final de fora.",
            ],
        },
        {
            "id": "ex08",
            "nome": "add_chelou",
            "arquivos": ["add_chelou.sh"],
            "permitidas": [],
            "tipo": "shell",
            "validador": "add_chelou",
            "prototipo": "add_chelou.sh",
            "objetivo": "Converter e somar números em bases exóticas.",
            "tarefa": (
                "Crie `add_chelou.sh`, um script que leia `$FT_NBR1` na base "
                "`'\\\"?!`, `$FT_NBR2` na base `mrdoc`, some os dois valores e "
                "imprima o resultado na base `gtaio luSnemf`."
            ),
            "exemplo": "FT_NBR1=... FT_NBR2=... ./add_chelou.sh\nSalut",
            "dica": "Converta cada caractere para dígito, use uma calculadora de base (bc/awk) e mapeie a saída. O espaço faz parte da base final.",
            "erros": [
                "Esquecer que o espaço é um dígito da base final.",
                "Tratar os caracteres especiais sem quoting.",
                "Usar base 10 na saída.",
            ],
        },
    ],
}
