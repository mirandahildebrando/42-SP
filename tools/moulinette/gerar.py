#!/usr/bin/env python3
"""Gera a estrutura de pastas, enunciados e READMEs das listas.

Pode ser rodado quantas vezes quiser: não sobrescreve arquivos do aluno,
apenas os enunciados/READMEs e arquivos fornecidos que estiverem faltando.
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PISCINA = RAIZ / "piscina"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dados import LISTAS  # noqa: E402


def bloco(texto):
    return str(texto).strip()


def enunciado(lista, ex):
    arquivos = ", ".join(f"`{a}`" for a in ex.get("arquivos", []))
    permitidas = ", ".join(f"`{p}`" for p in ex.get("permitidas", [])) or "nenhuma"
    linhas = [
        f"# {ex['id']} — {ex['nome']}",
        "",
        f"**Lista:** [{lista['nome']}](../README.md)  •  "
        f"**Nível:** {lista['nivel']}/3  •  **Arquivos:** {arquivos}",
        "",
        f"**Funções permitidas:** {permitidas}",
        "",
        "---",
        "",
        "## Objetivo",
        "",
        bloco(ex["objetivo"]),
        "",
        "## Tarefa",
        "",
        bloco(ex["tarefa"]),
        "",
        "## Protótipo",
        "",
        "```" + ("text" if ex.get("tipo") == "shell" else "c"),
        bloco(ex["prototipo"]),
        "```",
        "",
    ]
    if ex.get("exemplo"):
        linhas += ["## Exemplo", "", "```text", bloco(ex["exemplo"]), "```", ""]
    if ex.get("dica"):
        linhas += ["## Dica", "", bloco(ex["dica"]), ""]
    if ex.get("erros"):
        linhas += ["## Erros comuns", ""]
        linhas += [f"- {e}" for e in ex["erros"]]
        linhas += [""]
    if ex.get("tipo") == "programa":
        linhas += [
            "## Atenção",
            "",
            "Este exercício é um **programa**: você deve entregar um `main`.",
            "",
        ]
    if ex.get("arquivos_providos"):
        for nome in ex["arquivos_providos"]:
            linhas += [
                f"> O arquivo `{nome}` é **fornecido** e já está nesta pasta. "
                "Não é necessário entregá-lo, mas ele será usado na compilação.",
                "",
            ]
    if ex.get("tipo") == "shell":
        checklist = [
            "- [ ] O arquivo tem exatamente o nome pedido.",
            "- [ ] O script roda com `bash arquivo.sh` (ou `/bin/sh`).",
            "- [ ] Permissões, conteúdo e saída seguem o enunciado.",
            "- [ ] Testei com `moulinette " + f"{lista['id']}/{ex['id']}" + "`.",
        ]
    else:
        checklist = [
            "- [ ] O arquivo tem exatamente o nome pedido.",
            "- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).",
            "- [ ] Compila com `gcc -Wall -Wextra -Werror`.",
            "- [ ] `norminette` passa sem erros.",
            "- [ ] Testei com `moulinette " + f"{lista['id']}/{ex['id']}" + "`.",
        ]
    linhas += [
        "## Checklist antes de testar",
        "",
        *checklist,
        "",
        "---",
        "",
        "*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, "
        "desenhe no papel e pergunte a um colega — na piscina, pedir ajuda "
        "faz parte do jogo.*",
        "",
    ]
    return "\n".join(linhas)


def readme_lista(lista):
    linhas = [
        f"# {lista['nome']} — {lista['subtitulo']}",
        "",
        bloco(lista["introducao"]),
        "",
        "## Regras da lista",
        "",
    ]
    linhas += [f"- {r}" for r in lista["regras"]]
    linhas += [
        "",
        "## Exercícios",
        "",
        "| # | Exercício | Arquivo(s) | Permitidas |",
        "|---|---|---|---|",
    ]
    for ex in lista["exercicios"]:
        arquivos = ", ".join(f"`{a}`" for a in ex.get("arquivos", []))
        permitidas = ", ".join(f"`{p}`" for p in ex.get("permitidas", [])) or "—"
        linhas.append(
            f"| {ex['id']} | [{ex['nome']}]({ex['id']}/ENUNCIADO.md) "
            f"| {arquivos} | {permitidas} |")
    linhas += [
        "",
        "## Como treinar esta lista",
        "",
        "```sh",
        f"cd piscina/{lista['id']}",
        "moulinette .             # corrige a lista inteira",
        f"moulinette {lista['id']}/ex00   # corrige um exercício",
        "```",
        "",
        "O progresso detalhado fica em [PROGRESSO.md](../PROGRESSO.md).",
        "",
        "### Ordem recomendada",
        "",
        "1. Leia o enunciado inteiro e escreva o protótipo no papel.",
        "2. Implemente sem pressa; compile cedo para pegar erros de sintaxe.",
        "3. Rode `norminette` e corrija a forma **antes** de depurar a lógica.",
        "4. Rode `moulinette` e leia a primeira falha, não todas de uma vez.",
        "5. Quando passar, refaça o exercício de memória no dia seguinte.",
        "",
        "---",
        "",
        "[Voltar para a piscina](../README.md) • "
        "[Progresso](../PROGRESSO.md)",
        "",
    ]
    return "\n".join(linhas)


def readme_piscina():
    linhas = [
        "# Piscina 42SP — ambiente de treino",
        "",
        "Este diretório contém as listas da piscina, enunciados em português e "
        "um corretor local que imita o essencial da Moulinette: cabeçalho 42, "
        "norminette, compilação com `-Wall -Wextra -Werror`, funções proibidas "
        "e testes de comportamento.",
        "",
        "## Comece por aqui",
        "",
        "1. Leia [COMO-TREINAR.md](COMO-TREINAR.md).",
        "2. Abra o terminal com `ABRIR-42.cmd` (na raiz do projeto).",
        "3. Rode `moulinette` para ver o painel.",
        "4. Entre em `C00/ex00`, leia o enunciado e crie o arquivo.",
        "",
        "## Listas",
        "",
        "| Lista | Tema | Exercícios |",
        "|---|---|---|",
    ]
    for lista in LISTAS:
        linhas.append(
            f"| [{lista['nome']}]({lista['id']}/README.md) | "
            f"{lista['subtitulo']} | {len(lista['exercicios'])} |")
    linhas += [
        "",
        "## Comandos",
        "",
        "```sh",
        "moulinette                  # painel de progresso",
        "moulinette C00              # corrige a lista C00",
        "moulinette C00/ex00         # corrige um exercício",
        "moulinette --pasta .        # corrige o exercício desta pasta",
        "exame exam00                # inicia um simulado de exame",
        "exame exam00 status         # tempo restante",
        "exame exam00 entregar       # corrige o simulado",
        "42header arquivo.c          # insere o cabeçalho 42",
        "```",
        "",
        "## Regras de convivência",
        "",
        "- O corretor é local: ele **não** substitui a Moulinette oficial.",
        "- Os testes são para aprender; não os leia antes de tentar resolver.",
        "- Não copie soluções de colegas nem gere código com IA durante a "
        "piscina oficial. Aqui, use tudo como ferramenta de estudo.",
        "- Se um teste parecer errado, anote o caso e me avise: o objetivo é "
        "que o ambiente fique fiel.",
        "",
        "## Estrutura",
        "",
        "```text",
        "piscina/",
        "├── C00/ ... C08/      listas de C",
        "├── Shell00/ Shell01/  listas de shell",
        "├── exames/            simulados e banco de exercícios",
        "├── COMO-TREINAR.md",
        "└── PROGRESSO.md       gerado pelo corretor",
        "```",
        "",
        "---",
        "",
        "Bom treino. A piscina é difícil, mas é feita de exercícios pequenos. "
        "Um por vez.",
        "",
    ]
    return "\n".join(linhas)


def como_treinar():
    return """# Como treinar (e passar)

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
"""


def main():
    PISCINA.mkdir(exist_ok=True)
    for lista in LISTAS:
        pasta_lista = PISCINA / lista["id"]
        pasta_lista.mkdir(exist_ok=True)
        (pasta_lista / "README.md").write_text(
            readme_lista(lista), encoding="utf-8", newline="\n")
        for ex in lista["exercicios"]:
            pasta = pasta_lista / ex["id"]
            pasta.mkdir(exist_ok=True)
            (pasta / "ENUNCIADO.md").write_text(
                enunciado(lista, ex), encoding="utf-8", newline="\n")
            for nome, conteudo in ex.get("arquivos_providos", {}).items():
                destino = pasta / nome
                if not destino.exists():
                    destino.write_text(conteudo, encoding="utf-8", newline="\n")
                    print(f"fornecido: {destino.relative_to(RAIZ)}")
        print(f"lista pronta: {lista['id']} ({len(lista['exercicios'])} exercícios)")
    (PISCINA / "README.md").write_text(
        readme_piscina(), encoding="utf-8", newline="\n")
    (PISCINA / "COMO-TREINAR.md").write_text(
        como_treinar(), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
