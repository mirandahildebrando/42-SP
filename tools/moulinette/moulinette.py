#!/usr/bin/env python3
"""Moulinette local da Piscina 42SP.

Uso:
    python tools/moulinette/moulinette.py            # status geral
    python tools/moulinette/moulinette.py C00        # corrige a lista C00
    python tools/moulinette/moulinette.py C00/ex05   # corrige um exercício
    python tools/moulinette/moulinette.py --tudo     # corrige tudo
    python tools/moulinette/moulinette.py --pasta <pasta>  # exercício da pasta

Opções:
    --sem-norma     pula a norminette (iteração rápida)
    --verboso       mostra comandos e saídas completas
    --sem-cor       desliga cores
    --json          saída legível por máquina (status)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from itertools import combinations
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PISCINA = RAIZ / "piscina"
PROGRESSO = PISCINA / ".progresso.json"
BUILD = ".build"
EXE = "a.out.exe"

GCC = RAIZ / "tools" / "mingw64" / "bin" / "gcc.exe"
if not GCC.exists():
    _gcc = shutil.which("gcc")
    GCC = Path(_gcc) if _gcc else None
NORME = [sys.executable, "-m", "norminette", "--no-colors",
         "-R", "CheckForbiddenSourceHeader"]

FORBIDDEN = {
    "printf", "fprintf", "sprintf", "snprintf", "vprintf", "dprintf",
    "puts", "putchar", "fputs", "fputc", "perror",
    "strlen", "strcpy", "strncpy", "strcat", "strncat", "strcmp", "strncmp",
    "strstr", "strchr", "strrchr", "strdup", "strndup", "strjoin", "strtrim",
    "memcpy", "memset", "memmove", "memcmp", "strlcpy", "strlcat",
    "malloc", "calloc", "realloc", "free",
    "atoi", "atol", "atoll", "itoa", "strtol", "strtoul", "exit", "abort",
    "qsort", "bsearch", "abs", "labs", "pow", "sqrt", "floor", "ceil",
    "toupper", "tolower", "isalpha", "isdigit", "isalnum", "isspace",
    "isprint", "isupper", "islower", "ispunct", "isascii",
    "open", "close", "read", "rand", "srand", "time", "getchar", "scanf",
    "stdin", "stdout", "stderr", "errno", "FILE",
}

KEYWORDS = {
    "if", "else", "while", "for", "switch", "case", "return", "sizeof",
    "do", "break", "continue", "goto", "typedef", "struct", "union", "enum",
    "static", "const", "volatile", "unsigned", "signed", "int", "char",
    "void", "long", "short", "float", "double", "defined",
}

C_INCLUDES = """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <unistd.h>
"""


# ---------------------------------------------------------------------------
# cores e utilidades
# ---------------------------------------------------------------------------

class Cor:
    on = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None

    @classmethod
    def _c(cls, codigo, texto):
        return f"\033[{codigo}m{texto}\033[0m" if cls.on else texto

    @classmethod
    def verde(cls, t): return cls._c("1;32", t)

    @classmethod
    def vermelho(cls, t): return cls._c("1;31", t)

    @classmethod
    def amarelo(cls, t): return cls._c("1;33", t)

    @classmethod
    def ciano(cls, t): return cls._c("1;36", t)

    @classmethod
    def cinza(cls, t): return cls._c("2", t)

    @classmethod
    def negrito(cls, t): return cls._c("1", t)


def agora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def normalizar(texto):
    return texto.replace("\r\n", "\n").replace("\r", "\n")


def hash_pasta(pasta: Path, arquivos):
    h = hashlib.sha256()
    for nome in sorted(arquivos):
        p = pasta / nome
        if p.exists():
            h.update(nome.encode())
            h.update(p.read_bytes())
    return h.hexdigest()[:16]


def arquivos_fonte(pasta: Path, excluir=()):
    """Todos os .c/.h da pasta, exceto build e arquivos excluídos."""
    saida = []
    for p in sorted(pasta.iterdir()):
        if not p.is_file() or p.name in excluir:
            continue
        if p.suffix in {".c", ".h"} and not p.name.startswith("_"):
            saida.append(p.name)
    return saida


def ler_json(caminho: Path, padrao):
    try:
        return json.loads(caminho.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return padrao


def salvar_json(caminho: Path, dados):
    caminho.parent.mkdir(parents=True, exist_ok=True)
    tmp = caminho.with_suffix(caminho.suffix + ".tmp")
    tmp.write_text(json.dumps(dados, indent=2, ensure_ascii=False),
                   encoding="utf-8", newline="\n")
    tmp.replace(caminho)


# ---------------------------------------------------------------------------
# geração dos testes
# ---------------------------------------------------------------------------

GERADORES = {
    "comb3": lambda: ", ".join(
        "".join(str(d) for d in c) for c in combinations(range(10), 3)),
    "comb2": lambda: ", ".join(
        f"{a:02d} {b:02d}" for a in range(100) for b in range(a + 1, 100)),
}
for _n in range(1, 10):
    GERADORES[f"combn{_n}"] = (
        lambda n=_n: ", ".join(
            "".join(str(d) for d in c) for c in combinations(range(10), n)))


def esperado_caso(caso):
    if "gerador" in caso:
        return GERADORES[caso["gerador"]]()
    return caso.get("esperado", "")


def gerar_teste(meta):
    """Monta o main de teste com marcadores @@CASE:...@@ ... @@END@@."""
    decls = meta.get("decl", "")
    linhas_inc = []
    for inc in meta.get("includes", []):
        if inc.startswith('"') or inc.startswith("<"):
            linhas_inc.append(f"#include {inc}")
        else:
            linhas_inc.append(f'#include "{inc}"')
    includes = "\n".join(linhas_inc)
    partes = [
        C_INCLUDES,
        "#define _CASO(n) printf(\"\\n@@CASE:%s@@\\n\", (n))",
        "#define _FIM() printf(\"\\n@@END@@\\n\")",
        includes,
        decls,
        "",
        "int main(void)",
        "{",
        "\tsetvbuf(stdout, NULL, _IONBF, 0);",
    ]
    for caso in meta["casos"]:
        partes.append(f"\t_CASO(\"{caso['nome']}\");")
        partes.append("\t{")
        for linha in normalizar(caso["codigo"]).split("\n"):
            partes.append("\t\t" + linha)
        partes.append("\t}")
        partes.append("\t_FIM();")
    partes += ["\treturn (0);", "}", ""]
    return "\n".join(partes)


# ---------------------------------------------------------------------------
# análise de funções proibidas
# ---------------------------------------------------------------------------

def remover_comentarios_e_strings(texto):
    texto = re.sub(r"/\*.*?\*/", " ", texto, flags=re.S)
    texto = re.sub(r"//[^\n]*", " ", texto)
    texto = re.sub(r'"(?:\\.|[^"\\])*"', '""', texto)
    texto = re.sub(r"'(?:\\.|[^'\\])*'", "''", texto)
    return texto


def funcoes_definidas(texto):
    # Definições de função no começo de linha: tipo(s) + nome(...)
    padrao = re.compile(
        r"^[ \t]*(?:[A-Za-z_][A-Za-z0-9_ \t*]*[ \t*])"
        r"([A-Za-z_][A-Za-z0-9_]*)[ \t]*\([^;]*\)[ \t]*\{",
        re.M)
    return {m.group(1) for m in padrao.finditer(texto)}


def chamadas(texto):
    saida = {}
    for m in re.finditer(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(", texto):
        nome = m.group(1)
        if nome in KEYWORDS:
            continue
        saida[nome] = saida.get(nome, 0) + 1
    return saida


def verificar_proibidas(pasta: Path, arquivos, permitidas, permitir_main=False):
    problemas = []
    for nome in arquivos:
        if not nome.endswith(".c"):
            continue
        caminho = pasta / nome
        bruto = caminho.read_text(encoding="utf-8", errors="replace")
        codigo = remover_comentarios_e_strings(bruto)
        definidas = funcoes_definidas(codigo)
        for fn in sorted(chamadas(codigo)):
            if fn in definidas or fn in permitidas or fn not in FORBIDDEN:
                continue
            problemas.append(f"{nome}: função proibida `{fn}`")
        if not permitir_main and re.search(r"\bmain\s*\(", codigo):
            problemas.append(f"{nome}: `main` não é permitido neste exercício")
    return problemas


# ---------------------------------------------------------------------------
# norminette / compilação / execução
# ---------------------------------------------------------------------------

def rodar_norminette(pasta: Path, arquivos, verboso=False, ignorar=()):
    if not arquivos:
        return True, ""
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    cmd = NORME + arquivos
    try:
        r = subprocess.run(cmd, cwd=pasta, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=120,
                           env=env)
    except subprocess.TimeoutExpired:
        return False, "norminette travou (timeout)"
    saida = (r.stdout + r.stderr).strip()
    saida = re.sub(r"\x1b\[[0-9;]*m", "", saida)
    linhas = saida.splitlines()
    if ignorar:
        linhas = [l for l in linhas
                  if not any(regra in l for regra in ignorar)]
    relevantes = [l for l in linhas if "Error:" in l]
    ok = not relevantes
    if not ignorar:
        ok = ok and r.returncode == 0
    if ok and ignorar:
        saida = ""
    else:
        saida = "\n".join(linhas)
    if verboso:
        print(Cor.cinza("$ " + " ".join(cmd)))
        print(Cor.cinza(saida))
    return ok, saida


def compilar(pasta: Path, fontes, teste, verboso=False, timeout=60):
    build = pasta / BUILD
    if build.exists():
        shutil.rmtree(build, ignore_errors=True)
    build.mkdir(parents=True, exist_ok=True)
    exe = build / EXE
    cmd = [str(GCC), "-Wall", "-Wextra", "-Werror",
           "-I", str(pasta), "-I", str(build)]
    cmd += [str(pasta / f) for f in fontes if f.endswith(".c")]
    if teste is not None:
        arq_teste = build / "teste.c"
        arq_teste.write_text(teste, encoding="utf-8", newline="\n")
        cmd.append(str(arq_teste))
    cmd += ["-o", str(exe), "-lm"]
    if verboso:
        print(Cor.cinza("$ " + " ".join(cmd)))
    try:
        r = subprocess.run(cmd, cwd=pasta, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=timeout)
    except subprocess.TimeoutExpired:
        return False, exe, "compilação travou (timeout)"
    if r.returncode != 0:
        return False, exe, (r.stdout + r.stderr).strip()
    return True, exe, ""


def executar(exe: Path, pasta: Path, argv=None, timeout=30):
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    try:
        r = subprocess.run([str(exe)] + list(argv or []), cwd=pasta,
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=timeout, env=env)
        return r.returncode, normalizar(r.stdout), normalizar(r.stderr)
    except subprocess.TimeoutExpired:
        return "timeout", "", "timeout"
    except OSError as e:
        return "erro", "", str(e)


MARKER = re.compile(r"@@CASE:(.*?)@@\n(.*?)\n@@END@@\n", re.S)


def extrair_casos(saida):
    return {m.group(1): m.group(2) for m in MARKER.finditer(saida)}


def diff_curto(esperado, recebido, limite=160):
    esperado = normalizar(esperado)
    recebido = normalizar(recebido)
    if len(esperado) <= limite and len(recebido) <= limite:
        return f"esperado {esperado!r}\n      recebido {recebido!r}"
    i = 0
    while i < min(len(esperado), len(recebido)) and esperado[i] == recebido[i]:
        i += 1
    ini = max(0, i - 40)
    fim_e = min(len(esperado), i + 60)
    fim_r = min(len(recebido), i + 60)
    return (f"1ª diferença no byte {i}\n"
            f"      esperado ...{esperado[ini:fim_e]!r}\n"
            f"      recebido ...{recebido[ini:fim_r]!r}")


# ---------------------------------------------------------------------------
# correção de um exercício
# ---------------------------------------------------------------------------

def pasta_exercicio(lista, ex):
    base = PISCINA / lista["id"] / ex["id"]
    if lista.get("pasta"):
        base = PISCINA / lista["pasta"] / ex["id"]
    return base


def corrigir(lista, ex, sem_norma=False, verboso=False, pasta_override=None):
    pasta = Path(pasta_override) if pasta_override else pasta_exercicio(lista, ex)
    resultado = {
        "id": f"{lista['id']}/{ex['id']}",
        "nome": ex["nome"],
        "data": agora(),
        "status": "falhou",
        "detalhe": "",
        "casos": "",
    }
    if not pasta.exists():
        resultado["detalhe"] = f"pasta não encontrada: {pasta}"
        resultado["status"] = "falta"
        return resultado
    if ex.get("tipo") == "shell":
        from shell import corrigir_shell
        return corrigir_shell(lista, ex, sem_norma=sem_norma, verboso=verboso)

    arquivos = list(ex.get("arquivos", []))
    faltando = [a for a in arquivos if not (pasta / a).exists()]
    if faltando:
        resultado["detalhe"] = "arquivo(s) ausente(s): " + ", ".join(faltando)
        resultado["status"] = "falta"
        return resultado

    excluir = set(ex.get("ignorar_norm", [])) | set(ex.get("arquivos_providos", []))
    fontes = [a for a in arquivos if (pasta / a).exists()]
    fontes += [a for a in arquivos_fonte(pasta, excluir) if a not in fontes]

    if not sem_norma:
        ok, saida = rodar_norminette(pasta, fontes, verboso,
                                     ex.get("norm_ignorar", []))
        if not ok:
            resultado["status"] = "norma"
            linhas = [l for l in saida.splitlines() if l.strip()]
            resultado["detalhe"] = "norminette falhou:\n" + "\n".join(linhas[:14])
            return resultado

    proibidas = verificar_proibidas(pasta, fontes, set(ex.get("permitidas", [])),
                                    permitir_main=(ex.get("tipo") == "programa"))
    if proibidas:
        resultado["status"] = "proibida"
        resultado["detalhe"] = "\n".join(proibidas[:10])
        return resultado

    tipo = ex.get("tipo", "funcao")
    teste = None if tipo == "programa" else gerar_teste(ex)
    ok, exe, erro = compilar(pasta, fontes, teste, verboso)
    if not ok:
        resultado["status"] = "compila"
        resultado["detalhe"] = "compilação falhou:\n" + "\n".join(
            erro.splitlines()[:18])
        return resultado

    if tipo == "programa":
        ok, detalhe = rodar_casos_programa(pasta, exe, ex, verboso)
    else:
        ok, detalhe = rodar_casos_funcao(pasta, exe, ex, verboso)

    if ok:
        resultado["status"] = "validado"
        resultado["casos"] = f"{len(ex['casos'])}/{len(ex['casos'])}"
        resultado["hash"] = hash_pasta(pasta, fontes)
    else:
        resultado["status"] = "teste"
        resultado["detalhe"] = detalhe
    return resultado


def rodar_casos_funcao(pasta, exe, ex, verboso):
    timeout = max((c.get("timeout", 10) for c in ex["casos"]), default=10)
    codigo, saida, err = executar(exe, pasta, timeout=timeout)
    if verboso:
        print(Cor.cinza("--- stdout ---"))
        print(Cor.cinza(saida[:4000]))
        if err:
            print(Cor.cinza("--- stderr ---"))
            print(Cor.cinza(err[:2000]))
    obtidos = extrair_casos(saida)
    falhas = []
    for caso in ex["casos"]:
        nome = caso["nome"]
        if nome not in obtidos:
            falhas.append(f"caso `{nome}`: a função não produziu saída "
                          f"(travou? loop infinito? retorno antecipado?)")
            continue
        recebido = obtidos[nome]
        if caso.get("validador") == "ten_queens":
            ok, detalhe = validar_ten_queens(recebido, caso.get("retorno", 724))
            if not ok:
                falhas.append(f"caso `{nome}`: {detalhe}")
            continue
        esperado = esperado_caso(caso)
        if recebido != esperado:
            falhas.append(f"caso `{nome}`: " + diff_curto(esperado, recebido))
    if not falhas and codigo != 0:
        falhas.append(f"o programa terminou com código {codigo}")
    if falhas:
        return False, "\n".join(falhas[:6])
    return True, ""


def validar_ten_queens(saida, retorno_esperado):
    linhas = [l for l in saida.splitlines() if l.strip()]
    solucoes = [l for l in linhas if re.fullmatch(r"[0-9]{10}", l)]
    m = re.search(r"RET:(-?[0-9]+)", saida)
    if m is None:
        return False, "a função não imprimiu o retorno esperado (RET:...)"
    retorno = int(m.group(1))
    if retorno != retorno_esperado:
        return False, f"retorno {retorno}, esperado {retorno_esperado}"
    if len(solucoes) != retorno_esperado:
        return False, (f"{len(solucoes)} soluções impressas, "
                       f"esperado {retorno_esperado}")
    if len(set(solucoes)) != len(solucoes):
        return False, "há soluções repetidas"
    for linha in solucoes:
        colunas = [int(c) for c in linha]
        if sorted(colunas) != list(range(10)):
            return False, f"solução inválida (não é permutação 0-9): {linha}"
        for i in range(10):
            for j in range(i + 1, 10):
                if abs(i - j) == abs(colunas[i] - colunas[j]):
                    return False, f"rainhas se atacam na solução {linha}"
    return True, ""


def rodar_casos_programa(pasta, exe, ex, verboso):
    falhas = []
    for caso in ex["casos"]:
        argv = list(caso.get("argv", []))
        codigo, saida, err = executar(exe, pasta, argv=argv, timeout=20)
        esperado = caso.get("esperado", "")
        esperado = esperado.replace("{argv0}", str(exe))
        if caso.get("normalizar_argv0"):
            saida = saida.replace("\\", "/")
            esperado = esperado.replace("\\", "/")
        if verboso:
            print(Cor.cinza(f"$ {exe.name} {' '.join(argv)}"))
            print(Cor.cinza(saida[:2000]))
        if saida != esperado:
            falhas.append(f"caso `{caso['nome']}`: " + diff_curto(esperado, saida))
        if codigo != 0:
            falhas.append(f"caso `{caso['nome']}`: terminou com código {codigo}")
    if falhas:
        return False, "\n".join(falhas[:6])
    return True, ""


# ---------------------------------------------------------------------------
# status e progresso
# ---------------------------------------------------------------------------

def carregar_progresso():
    return ler_json(PROGRESSO, {})


def arquivos_do_exercicio(lista, ex):
    pasta = pasta_exercicio(lista, ex)
    if not pasta.exists():
        return []
    if ex.get("tipo") == "shell":
        return [a for a in ex.get("arquivos", []) if (pasta / a).exists()]
    excluir = set(ex.get("ignorar_norm", [])) | set(ex.get("arquivos_providos", []))
    return [a for a in arquivos_fonte(pasta, excluir)]


def estado_exercicio(lista, ex, progresso):
    chave = f"{lista['id']}/{ex['id']}"
    pasta = pasta_exercicio(lista, ex)
    faltando = [a for a in ex.get("arquivos", []) if not (pasta / a).exists()]
    if faltando:
        return "pendente"
    reg = progresso.get(chave)
    if reg and reg.get("status") == "manual":
        return "manual"
    if not reg or reg.get("status") != "validado":
        return "falhou" if reg and reg.get("status") in {"falhou", "teste",
                                                         "compila", "norma",
                                                         "proibida"} else "pendente"
    if reg.get("hash") != hash_pasta(pasta, arquivos_do_exercicio(lista, ex)):
        return "alterado"
    return "validado"


ICONES = {
    "validado": ("[OK]", Cor.verde),
    "alterado": ("[??]", Cor.amarelo),
    "falhou": ("[XX]", Cor.vermelho),
    "manual": ("[M]", Cor.ciano),
    "pendente": ("[  ]", Cor.cinza),
}


def barra(feitos, total, largura=22):
    cheio = int(round(largura * feitos / total)) if total else 0
    return "#" * cheio + "-" * (largura - cheio)


def status(como_json=False):
    from dados import LISTAS

    progresso = carregar_progresso()
    linhas = []
    total_geral = 0
    feitos_geral = 0
    pontos = 0
    proximos = []

    for lista in LISTAS:
        exs = lista["exercicios"]
        total = len(exs)
        feitos = 0
        pend = []
        for ex in exs:
            estado = estado_exercicio(lista, ex, progresso)
            if estado == "validado":
                feitos += 1
                pontos += 100
            else:
                pend.append(ex)
        total_geral += total
        feitos_geral += feitos
        linhas.append({
            "id": lista["id"],
            "nome": lista["nome"],
            "feitos": feitos,
            "total": total,
            "estados": {ex["id"]: estado_exercicio(lista, ex, progresso)
                        for ex in exs},
        })
        if pend:
            proximos.append((lista, pend[0]))

    if como_json:
        print(json.dumps({
            "total": total_geral, "feitos": feitos_geral,
            "pontos": pontos, "listas": linhas,
        }, indent=2, ensure_ascii=False))
        return

    print()
    print(Cor.ciano("  PISCINA 42SP  ") + Cor.negrito("— painel de treino"))
    print(Cor.cinza(f"  {agora()}"))
    print()
    for item in linhas:
        if item["total"] == 0:
            continue
        c = Cor.verde if item["feitos"] == item["total"] else Cor.amarelo
        pct = 100 * item["feitos"] // item["total"] if item["total"] else 0
        est = item["estados"].values()
        n_alt = sum(1 for e in est if e == "alterado")
        n_fal = sum(1 for e in est if e == "falhou")
        extra = ""
        if n_alt:
            extra += Cor.amarelo(f" {n_alt} alterado(s)")
        if n_fal:
            extra += Cor.vermelho(f" {n_fal} falhando")
        print(f"  {item['id']:<8} {c(barra(item['feitos'], item['total']))} "
              f"{item['feitos']:>2}/{item['total']:<2} {pct:>3}%{extra}")
    print()
    pct = 100 * feitos_geral // total_geral if total_geral else 0
    print(f"  Total: {Cor.negrito(f'{feitos_geral}/{total_geral}')} "
          f"({pct}%)  •  {Cor.amarelo(f'{pontos} XP')}")
    if proximos:
        print()
        print(Cor.negrito("  Próximos passos:"))
        for lista, ex in proximos[:4]:
            print(f"    - {lista['id']}/{ex['id']}  {ex['nome']}")
    print()
    print(Cor.cinza("  Teste:  moulinette C00        (lista inteira)"))
    print(Cor.cinza("          moulinette C00/ex00    (um exercício)"))
    print(Cor.cinza("          moulinette --pasta .   (exercício da pasta atual)"))
    print()
    gerar_progresso_md(linhas, feitos_geral, total_geral, pontos)


def gerar_progresso_md(linhas, feitos, total, pontos):
    from dados import LISTAS

    progresso = carregar_progresso()
    md = ["# Progresso da Piscina", "",
          f"Atualizado em **{agora()}**.", "",
          f"**{feitos}/{total} exercícios validados** • **{pontos} XP**", ""]
    for lista, item in zip(LISTAS, linhas):
        if item["total"] == 0:
            continue
        md.append(f"## {lista['nome']} — {item['feitos']}/{item['total']}")
        md.append("")
        md.append("| Exercício | Nome | Status |")
        md.append("|---|---|---|")
        simbolos = {"validado": "OK", "alterado": "ALTERADO",
                    "falhou": "FALHANDO", "manual": "MANUAL",
                    "pendente": "—"}
        for ex in lista["exercicios"]:
            estado = item["estados"][ex["id"]]
            md.append(f"| {ex['id']} | {ex['nome']} | {simbolos[estado]} |")
        md.append("")
        pend = [ex for ex in lista["exercicios"]
                if item["estados"][ex["id"]] != "validado"]
        if pend:
            md.append(f"Próximo: **{pend[0]['id']} — {pend[0]['nome']}**")
            md.append("")
    (PISCINA / "PROGRESSO.md").write_text("\n".join(md) + "\n",
                                          encoding="utf-8", newline="\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def resolver_alvo(alvo):
    from dados import LISTAS, MAPA

    if alvo in MAPA:
        return [MAPA[alvo]]
    lista = next((l for l in LISTAS if l["id"].lower() == alvo.lower()), None)
    if lista:
        return [(lista, ex) for ex in lista["exercicios"]]
    # tenta achar pelo nome do exercício (ex00, ft_putchar, ...)
    achados = []
    for chave, (l, ex) in MAPA.items():
        if ex["nome"].lower() == alvo.lower() or ex["id"].lower() == alvo.lower():
            achados.append((l, ex))
    if len(achados) == 1:
        return achados
    return []


def resolver_pasta(caminho):
    from dados import LISTAS

    p = Path(caminho).resolve()
    for _ in range(12):
        for lista in LISTAS:
            for ex in lista["exercicios"]:
                if pasta_exercicio(lista, ex).resolve() == p:
                    return lista, ex
        if p.parent == p:
            break
        p = p.parent
    return None, None


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("alvo", nargs="?", help="C00, C00/ex00, ft_putchar...")
    ap.add_argument("--tudo", action="store_true", help="corrige tudo")
    ap.add_argument("--pasta", help="corrige o exercício que contém esta pasta")
    ap.add_argument("--sem-norma", action="store_true")
    ap.add_argument("--verboso", action="store_true")
    ap.add_argument("--sem-cor", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.sem_cor:
        Cor.on = False
    if GCC is None:
        print("GCC não encontrado. Rode novamente o setup ou abra o terminal com ABRIR-42.cmd.")
        return 2

    from dados import LISTAS

    if args.pasta:
        lista, ex = resolver_pasta(args.pasta)
        if not ex:
            print(Cor.vermelho("Pasta fora da piscina. Passe C00/ex00 ou uma pasta dentro de piscina/."))
            return 2
        alvos = [(lista, ex)]
    elif args.tudo:
        alvos = [(l, ex) for l in LISTAS for ex in l["exercicios"]]
    elif args.alvo:
        alvos = resolver_alvo(args.alvo)
        if not alvos:
            print(Cor.vermelho(f"Não encontrei: {args.alvo}"))
            return 2
    else:
        status(como_json=args.json)
        return 0

    progresso = carregar_progresso()
    resultados = []
    for lista, ex in alvos:
        print()
        print(Cor.ciano(f"== {lista['id']}/{ex['id']} — {ex['nome']} =="))
        r = corrigir(lista, ex, sem_norma=args.sem_norma, verboso=args.verboso)
        progresso[r["id"]] = r
        resultados.append(r)
        cor = {"validado": Cor.verde, "falhou": Cor.vermelho,
               "falta": Cor.amarelo, "norma": Cor.amarelo,
               "compila": Cor.vermelho, "teste": Cor.vermelho,
               "manual": Cor.ciano,
               "proibida": Cor.vermelho}.get(r["status"], Cor.amarelo)
        rotulo = {"validado": "VALIDADO", "falhou": "FALHOU",
                  "falta": "FALTAM ARQUIVOS", "norma": "NORMA",
                  "compila": "NÃO COMPILA", "teste": "TESTES",
                  "manual": "MANUAL",
                  "proibida": "FUNÇÃO PROIBIDA"}.get(r["status"], r["status"])
        print("  " + cor(f"[{rotulo}]") + (f"  {r['casos']}" if r.get("casos") else ""))
        if r.get("detalhe"):
            for linha in r["detalhe"].splitlines():
                print("    " + linha)

    salvar_json(PROGRESSO, progresso)

    # resumo quando foi uma lista/tudo
    if len(alvos) > 1:
        ok = sum(1 for r in resultados if r["status"] == "validado")
        print()
        print(Cor.negrito(f"Resumo: {ok}/{len(resultados)} exercícios validados."))
        pendentes = [r for r in resultados if r["status"] != "validado"]
        if pendentes:
            print("Para revisar: " + ", ".join(r["id"] for r in pendentes[:8]))
        status()

    return 0 if all(r["status"] == "validado" for r in resultados) else 1


if __name__ == "__main__":
    sys.exit(main())
