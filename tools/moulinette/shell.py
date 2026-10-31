#!/usr/bin/env python3
"""Validadores locais das listas de Shell.

Cada validador recebe a pasta do exercício e devolve (ok, detalhe). Os testes
criam uma pasta temporária em .build/shell para não sujar os arquivos do aluno.
"""

from __future__ import annotations

import hashlib
import os
import re
import shutil
import subprocess
import tarfile
import time
from pathlib import Path, PurePosixPath

RAIZ = Path(__file__).resolve().parents[2]
BASH = Path(os.environ.get("SP42_BASH", r"C:\Program Files\Git\bin\bash.exe"))
if not BASH.exists():
    _bash = shutil.which("bash")
    BASH = Path(_bash) if _bash else None

PYTHON = Path(os.environ.get("SP42_PYTHON", "")) if os.environ.get("SP42_PYTHON") else None


def _env(extra=None):
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    env["SP42"] = str(RAIZ)
    env["PATH"] = (str(RAIZ / "tools" / "shell" / "bin") + os.pathsep
                   + str(RAIZ / "tools" / "mingw64" / "bin") + os.pathsep
                   + env.get("PATH", ""))
    if PYTHON:
        env["PY"] = str(PYTHON)
    if extra:
        env.update({k: str(v) for k, v in extra.items()})
    return env


def _posix(p):
    s = Path(p).as_posix()
    if re.match(r"^[A-Za-z]:/", s):
        return "/" + s[0].lower() + s[2:]
    return s


def _bash(comando, cwd, env=None, timeout=30):
    if BASH is None:
        return 127, "", "Git Bash não encontrado"
    prefixo = (f'export PATH="{_posix(RAIZ / "tools" / "shell" / "bin")}:'
               f'{_posix(RAIZ / "tools" / "mingw64" / "bin")}:$PATH"; ')
    try:
        r = subprocess.run([str(BASH), "-c", prefixo + comando], cwd=str(cwd),
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=timeout, env=_env(env))
        return r.returncode, r.stdout.replace("\r\n", "\n"), r.stderr.replace("\r\n", "\n")
    except subprocess.TimeoutExpired:
        return "timeout", "", "tempo esgotado"
    except OSError as e:
        return "erro", "", str(e)


def _script(pasta, nome, env=None, timeout=30):
    return _bash(f'bash "{Path(pasta / nome).as_posix()}"', pasta, env, timeout)


def _script_cwd(pasta_script, cwd, nome, env=None, timeout=30):
    return _bash(f'bash "{Path(pasta_script / nome).as_posix()}"',
                 cwd, env, timeout)


def _fixture(pasta):
    base = pasta / ".build" / "shell"
    if base.exists():
        shutil.rmtree(base, ignore_errors=True)
    base.mkdir(parents=True, exist_ok=True)
    return base


def _texto(p):
    return (p / "midLS").read_text(encoding="utf-8", errors="replace") if False else ""


def _hash(pasta, arquivos):
    h = hashlib.sha256()
    for nome in sorted(arquivos):
        p = pasta / nome
        if p.exists():
            h.update(nome.encode())
            h.update(p.read_bytes())
    return h.hexdigest()[:16]


# ---------------------------------------------------------------------------
# Shell 00
# ---------------------------------------------------------------------------

def val_z(pasta):
    p = pasta / "z"
    dados = p.read_bytes()
    if dados == b"Z\n":
        return True, ""
    return False, f"o arquivo z tem {len(dados)} byte(s): {dados!r}; esperado b'Z\\n'"


def _membros_tar(caminho):
    membros = {}
    with tarfile.open(caminho, "r:*") as tf:
        for m in tf.getmembers():
            if m.name in {".", "./"}:
                continue
            nome = PurePosixPath(m.name).name
            antigo = membros.get(nome)
            # `tar -cf ... testShell00 .` insere o arquivo duas vezes (uma
            # como hard link de `./`); prefira a entrada regular.
            if antigo is None or (not antigo.isreg() and m.isreg()):
                membros[nome] = m
    return membros


def val_tar_test(pasta):
    caminho = pasta / "testShell00.tar"
    try:
        membros = _membros_tar(caminho)
    except (tarfile.TarError, OSError) as e:
        return False, f"não consegui abrir testShell00.tar: {e}"
    m = membros.get("testShell00")
    if m is None:
        return False, "o tar não contém o arquivo testShell00"
    if not m.isreg():
        return False, "testShell00 não é um arquivo regular no tar"
    modo = m.mode & 0o777
    if modo not in (0o545, 0o444):
        return False, f"modo de testShell00 é {modo:04o}, esperado 0545 (ou 0444 no fallback do Windows)"
    if m.size != 40:
        return False, f"tamanho de testShell00 é {m.size}, esperado 40"
    aviso = "" if modo == 0o545 else "modo 0545 não é preservado pelo NTFS; aceito 0444 como fallback"
    return True, aviso


def _conteudo_tar(tf, m):
    f = tf.extractfile(m)
    return f.read() if f is not None else b""


def val_tar_exo2(pasta):
    caminho = pasta / "exo2.tar"
    try:
        with tarfile.open(caminho, "r:*") as tf:
            membros = {PurePosixPath(m.name).name: m for m in tf.getmembers()
                       if m.name not in {".", "./"}}
            esperado = {
                "test0": ("dir", 0o715),
                "test1": ("file", 0o714),
                "test2": ("dir", 0o504),
                "test3": ("file", 0o404),
                "test4": ("file", 0o641),
                "test5": ("file", 0o404),
            }
            fallback = []
            for nome, (tipo, modo) in esperado.items():
                m = membros.get(nome)
                if m is None:
                    return False, f"o tar não contém {nome}"
                if tipo == "dir" and not m.isdir():
                    return False, f"{nome} deveria ser diretório"
                if tipo == "file" and not (m.isfile() or m.islnk()):
                    return False, f"{nome} deveria ser arquivo regular"
                modo_windows = {(0o755 if tipo == "dir" else 0o644), 0o444}
                if (m.mode & 0o777) not in ({modo} | modo_windows):
                    return False, (f"modo de {nome} é {m.mode & 0o777:04o}, "
                                   f"esperado {modo:04o} (ou fallback do Windows)")
                if (m.mode & 0o777) != modo:
                    fallback.append(nome)
            if membros["test1"].size != 4:
                return False, f"test1 tem {membros['test1'].size} bytes, esperado 4"
            if membros["test3"].size != 1:
                return False, f"test3 tem {membros['test3'].size} bytes, esperado 1"
            if membros["test4"].size != 2:
                return False, f"test4 tem {membros['test4'].size} bytes, esperado 2"
            m6 = membros.get("test6")
            if m6 is None or not (m6.issym() or m6.isdir()):
                return False, "test6 deveria ser um symlink (ou uma pasta no fallback do Windows)"
            if m6.issym() and PurePosixPath(m6.linkname).name != "test0":
                return False, f"test6 aponta para {m6.linkname!r}, esperado test0"
            if m6.isdir() and not m6.issym():
                fallback.append("test6")
            m5 = membros["test5"]
            c3 = _conteudo_tar(tf, membros["test3"])
            c5 = _conteudo_tar(tf, m5)
            if not (m5.islnk() and PurePosixPath(m5.linkname).name == "test3"):
                if c5 != c3:
                    return False, "test5 não é hard link de test3 (conteúdo diferente)"
    except (tarfile.TarError, OSError) as e:
        return False, f"não consegui abrir exo2.tar: {e}"
    if fallback:
        return True, ("modo/symlink Unix não preservado pelo NTFS; "
                      "fallback Windows aceito em: " + ", ".join(fallback))
    return True, ""


def val_klist(pasta):
    texto = (pasta / "klist.txt").read_text(encoding="utf-8", errors="replace")
    if "Ticket cache" not in texto or "Default principal" not in texto:
        return False, "klist.txt não parece uma saída de klist (faltam Ticket cache/Default principal)"
    if "krbtgt" not in texto:
        return False, "klist.txt não contém um ticket krbtgt"
    return True, ""


def _fixture_midls(base):
    agora = time.time()
    entradas = [
        ("antigo.txt", agora - 500, False),
        ("dir_antigo", agora - 400, True),
        ("meio.txt", agora - 300, False),
        ("dir_novo", agora - 200, True),
        ("novo.txt", agora - 100, False),
    ]
    for nome, quando, eh_dir in entradas:
        p = base / nome
        if eh_dir:
            p.mkdir()
        else:
            p.write_text(nome, encoding="utf-8")
        os.utime(p, (quando, quando))
    (base / ".oculto").write_text("nao listar", encoding="utf-8")
    return ["novo.txt", "dir_novo/", "meio.txt", "dir_antigo/", "antigo.txt"]


def val_midls(pasta):
    bruto = (pasta / "midLS").read_text(encoding="utf-8", errors="replace")
    linhas = [l.strip() for l in bruto.splitlines() if l.strip()]
    if len(linhas) != 1:
        return False, "midLS deve conter uma única linha de comando"
    if any(x in linhas[0] for x in (";", "&&", "||")):
        return False, "midLS deve ser um único comando (sem ;, && ou ||)"
    base = _fixture(pasta)
    esperado = _fixture_midls(base)
    codigo, saida, err = _bash(linhas[0], base, timeout=20)
    if codigo != 0:
        return False, f"o comando de midLS falhou: {err.strip() or saida.strip()}"
    itens = [x.strip() for x in re.split(r"[,\n]", saida) if x.strip()]
    if itens != esperado:
        return False, ("ordem/conteúdo errado.\n"
                       f"esperado: {esperado}\nrecebido: {itens}")
    return True, ""


def _git(pasta, *args, env=None):
    return _bash("git " + " ".join(args), pasta, env, timeout=30)


def val_git_commit(pasta):
    base = _fixture(pasta)
    _git(base, "init", "-q")
    _git(base, "config", "user.email", "teste@42sp.org.br")
    _git(base, "config", "user.name", "teste")
    for i in range(6):
        (base / "arq.txt").write_text(str(i), encoding="utf-8")
        _git(base, "add", ".")
        _git(base, f"commit -q -m c{i}")
    _, esperado, _ = _git(base, "log", "-5", "--format=%H")
    codigo, saida, err = _script_cwd(pasta, base, "git_commit.sh", timeout=30)
    if codigo != 0:
        return False, f"git_commit.sh falhou: {err.strip() or saida.strip()}"
    obtido = [l.strip() for l in saida.splitlines() if l.strip()]
    alvo = [l.strip() for l in esperado.splitlines() if l.strip()]
    if obtido != alvo:
        return False, f"esperado:\n{esperado}recebido:\n{saida}"
    return True, ""


def val_git_ignore(pasta):
    base = _fixture(pasta)
    (base / ".gitignore").write_text("*.log\nignored/\n", encoding="utf-8")
    _git(base, "init", "-q")
    _git(base, "config", "user.email", "teste@42sp.org.br")
    _git(base, "config", "user.name", "teste")
    _git(base, "add", ".gitignore")
    _git(base, "commit", "-q", "-m", "base")
    (base / "a.log").write_text("l", encoding="utf-8")
    (base / "importante.txt").write_text("k", encoding="utf-8")
    (base / "ignored").mkdir()
    (base / "ignored" / "x").write_text("x", encoding="utf-8")
    (base / "sub").mkdir()
    (base / "sub" / "c.log").write_text("c", encoding="utf-8")
    _, esperado, _ = _git(base, "ls-files", "--others", "--ignored",
                          "--exclude-standard")
    codigo, saida, err = _script_cwd(pasta, base, "git_ignore.sh", timeout=30)
    if codigo != 0:
        return False, f"git_ignore.sh falhou: {err.strip() or saida.strip()}"
    obtido = {l.strip().replace("\\", "/").lstrip("./")
              for l in saida.splitlines() if l.strip()}
    alvo = {l.strip().replace("\\", "/").lstrip("./")
            for l in esperado.splitlines() if l.strip()}
    if obtido != alvo:
        return False, f"esperado: {sorted(alvo)}\nrecebido: {sorted(obtido)}"
    return True, ""


def val_diff_b(pasta):
    a = (pasta / "a").read_text(encoding="utf-8", errors="replace")
    b = (pasta / "b").read_text(encoding="utf-8", errors="replace")
    if a == b:
        return False, "b é idêntico a a; crie uma diferença"
    base = _fixture(pasta)
    (base / "a").write_text(a, encoding="utf-8", newline="\n")
    (base / "b").write_text(b, encoding="utf-8", newline="\n")
    codigo, diff, err = _bash("diff -u a b > sw.diff", base)
    if codigo not in (0, 1):
        return False, f"diff falhou: {err.strip()}"
    if not (base / "sw.diff").read_text(encoding="utf-8", errors="replace").strip():
        return False, "diff não produziu nenhuma diferença"
    codigo, saida, err = _bash("patch --dry-run -p0 a < sw.diff", base)
    if codigo != 0:
        return False, f"o patch de b não aplica em a: {err.strip() or saida.strip()}"
    return True, ""


def val_clean(pasta):
    bruto = (pasta / "clean").read_text(encoding="utf-8", errors="replace")
    linhas = [l.strip() for l in bruto.splitlines() if l.strip()]
    if len(linhas) != 1:
        return False, "clean deve conter uma única linha de comando"
    if any(x in linhas[0] for x in (";", "&&", "||")):
        return False, "use um único comando find (sem ;, && ou ||)"
    base = _fixture(pasta)
    alvos = [base / "lixo~", base / "#temp#", base / ".oculto~",
             base / "sub" / "lixo2~", base / "sub" / "#x#"]
    (base / "sub").mkdir()
    for p in alvos:
        p.write_text("x", encoding="utf-8")
    (base / "manter.txt").write_text("ok", encoding="utf-8")
    codigo, saida, err = _bash(linhas[0], base, timeout=20)
    if codigo != 0:
        return False, f"comando de clean falhou: {err.strip() or saida.strip()}"
    restantes = [p.relative_to(base).as_posix() for p in alvos if p.exists()]
    if restantes:
        return False, "arquivos não apagados: " + ", ".join(restantes)
    if "lixo~" not in saida or "#temp#" not in saida:
        return False, "o comando deve mostrar os nomes encontrados (use -print)"
    return True, ""


def val_magic(pasta):
    bruto = (pasta / "ft_magic").read_text(encoding="utf-8", errors="replace")
    linhas = [l.strip() for l in bruto.splitlines() if l.strip()]
    if not any(re.match(r"^42\s+string\s+42(?:\s|$)", l) for l in linhas):
        return False, "ft_magic deve ter uma linha como `42 string 42`"
    base = _fixture(pasta)
    shutil.copyfile(pasta / "ft_magic", base / "ft_magic")
    alvo = base / "alvo42"
    alvo.write_bytes(b"A" * 41 + b"42\n")
    codigo, saida, err = _bash('file -m ft_magic alvo42', base, timeout=20)
    if codigo != 0:
        return False, f"file -m falhou: {err.strip()}"
    if "42" not in saida and "data" in saida.lower():
        return False, f"file não reconheceu o formato: {saida.strip()}"
    return True, ""


# ---------------------------------------------------------------------------
# Shell 01
# ---------------------------------------------------------------------------

def val_inscricao(pasta):
    texto = (pasta / "INSCRICAO.md").read_text(encoding="utf-8", errors="replace")
    baixo = texto.lower()
    if "evento:" not in baixo or "projeto:" not in baixo:
        return False, "INSCRICAO.md deve ter as linhas evento: ok e projeto: ok"
    if "ok" not in baixo:
        return False, "marque evento e projeto com ok"
    return True, ""


def val_groups(pasta):
    for usuario, esperado in [
        ("nours", "god,root,admin,master,nours,bocal"),
        ("daemon", "daemon,bin"),
    ]:
        codigo, saida, err = _script(pasta, "print_groups.sh",
                                     {"FT_USER": usuario}, timeout=20)
        if codigo != 0:
            return False, f"print_groups.sh falhou com FT_USER={usuario}: {err.strip()}"
        if saida.rstrip("\n") != esperado:
            return False, (f"FT_USER={usuario}: esperado {esperado!r}, "
                           f"recebido {saida.rstrip(chr(10))!r}")
    return True, ""


def _fixture_find(base):
    (base / "find_sh.sh").write_text("", encoding="utf-8")
    for nome in ("file1.sh", "file2.sh", "file3.sh"):
        (base / nome).write_text("", encoding="utf-8")
    (base / "sub").mkdir()
    (base / "sub" / "file4.sh").write_text("", encoding="utf-8")
    (base / "not_sh.txt").write_text("", encoding="utf-8")
    (base / "upper.SH").write_text("", encoding="utf-8")


def val_find_sh(pasta):
    base = _fixture(pasta)
    _fixture_find(base)
    codigo, saida, err = _script_cwd(pasta, base, "find_sh.sh", timeout=20)
    if codigo != 0:
        return False, f"find_sh.sh falhou: {err.strip() or saida.strip()}"
    obtido = sorted(l.strip() for l in saida.splitlines() if l.strip())
    esperado = sorted(["find_sh", "file1", "file2", "file3", "file4"])
    if obtido != esperado:
        return False, f"esperado: {esperado}\nrecebido: {obtido}"
    return True, ""


def val_count_files(pasta):
    base = _fixture(pasta)
    (base / "a").write_text("", encoding="utf-8")
    (base / "b").write_text("", encoding="utf-8")
    (base / "dir").mkdir()
    (base / "dir" / "c").write_text("", encoding="utf-8")
    (base / "dir" / "sub").mkdir()
    (base / "dir" / "sub" / "d").write_text("", encoding="utf-8")
    esperado = len(list(base.rglob("*"))) + 1
    codigo, saida, err = _script_cwd(pasta, base, "count_files.sh", timeout=20)
    if codigo != 0:
        return False, f"count_files.sh falhou: {err.strip() or saida.strip()}"
    numeros = re.findall(r"-?\d+", saida)
    if not numeros or int(numeros[-1]) != esperado:
        return False, f"esperado {esperado}, recebido {saida.strip()!r}"
    return True, ""


def val_mac(pasta):
    codigo, saida, err = _script(pasta, "MAC.sh", timeout=20)
    if codigo != 0:
        return False, f"MAC.sh falhou: {err.strip() or saida.strip()}"
    obtido = [l.strip() for l in saida.splitlines() if l.strip()]
    esperado = ["00:11:22:33:44:55", "66:77:88:99:aa:bb"]
    if obtido != esperado:
        return False, f"esperado: {esperado}\nrecebido: {obtido}"
    return True, ""


def val_marvin(pasta):
    dados = (pasta / "MaRViN").read_bytes()
    if dados != b"42":
        return False, f"MaRViN deve ter exatamente os bytes b'42'; recebido {dados!r}"
    return True, ""


def val_skip(pasta):
    base = _fixture(pasta)
    for nome in ("a", "b", "c", "d"):
        (base / nome).write_text(nome, encoding="utf-8")
    _, ls, _ = _bash("ls -l", base)
    esperado = "\n".join(ls.splitlines()[::2]) + "\n"
    codigo, saida, err = _script_cwd(pasta, base, "skip.sh", timeout=20)
    if codigo != 0:
        return False, f"skip.sh falhou: {err.strip() or saida.strip()}"
    if saida.replace("\r\n", "\n") != esperado:
        return False, f"esperado:\n{esperado}recebido:\n{saida}"
    return True, ""


FAKE_PASSWD = """root:x:0:0:root:/root:/bin/bash
# comentario
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
# outro comentario
nours:x:1000:1000:Nours:/home/nours:/bin/bash
hilde:x:1001:1001:Hilde:/home/hilde:/bin/bash
ftp:x:1002:1002:FTP:/srv/ftp:/usr/sbin/nologin
www:x:1003:1003:WWW:/var/www:/usr/sbin/nologin
nobody:x:65534:65534:Nobody:/nonexistent:/usr/sbin/nologin
backup:x:1004:1004:Backup:/var/backups:/bin/sh
sync:x:1005:1005:sync:/bin:/bin/sync
games:x:1006:1006:games:/usr/games:/usr/sbin/nologin
"""


def val_r_dwssap(pasta):
    base = _fixture(pasta)
    (base / "passwd-fake").write_text(FAKE_PASSWD, encoding="utf-8",
                                      newline="\n")
    fake = _posix(base / "passwd-fake")
    env_bash = base / "bash_env"
    env_bash.write_text(
        'cat() { if [ "$1" = "/etc/passwd" ]; then /usr/bin/cat "' + fake
        + '"; else /usr/bin/cat "$@"; fi; }\n',
        encoding="utf-8", newline="\n")
    linhas = [l for l in FAKE_PASSWD.splitlines() if l and not l.startswith("#")]
    logins = [l.split(":")[0][::-1] for l in linhas[1::2]]
    logins.sort(reverse=True)
    ini, fim = 1, 5
    esperado = ", ".join(logins[ini - 1:fim]) + "."
    codigo, saida, err = _script_cwd(
        pasta, base, "r_dwssap.sh",
        {"FT_LINE1": str(ini), "FT_LINE2": str(fim),
         "BASH_ENV": _posix(env_bash)}, timeout=20)
    if codigo != 0:
        return False, f"r_dwssap.sh falhou: {err.strip() or saida.strip()}"
    if saida.rstrip("\n").rstrip("\r") != esperado:
        return False, f"esperado: {esperado!r}\nrecebido: {saida.rstrip()!r}"
    return True, ""


def val_add_chelou(pasta):
    # Deixado como conferência manual: o subject original depende de bc e de
    # variáveis com caracteres que o cmd/PowerShell alteram.
    return None, ("exercício manual: confira a saída esperada no enunciado; "
                  "o bc não faz parte do Git Bash e o validador automático "
                  "deste caso fica para uma revisão futura")


VALIDADORES = {
    "z": val_z,
    "tar_test": val_tar_test,
    "tar_exo2": val_tar_exo2,
    "klist": val_klist,
    "midls": val_midls,
    "git_commit": val_git_commit,
    "git_ignore": val_git_ignore,
    "diff_b": val_diff_b,
    "clean": val_clean,
    "magic": val_magic,
    "inscricao": val_inscricao,
    "groups": val_groups,
    "find_sh": val_find_sh,
    "count_files": val_count_files,
    "mac": val_mac,
    "marvin": val_marvin,
    "skip": val_skip,
    "r_dwssap": val_r_dwssap,
    "add_chelou": val_add_chelou,
}


def corrigir_shell(lista, ex, sem_norma=False, verboso=False):
    from datetime import datetime
    pasta = RAIZ / "piscina" / lista["id"] / ex["id"]
    resultado = {
        "id": f"{lista['id']}/{ex['id']}",
        "nome": ex["nome"],
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "falhou",
        "detalhe": "",
        "casos": "",
    }
    if not pasta.exists():
        resultado["status"] = "falta"
        resultado["detalhe"] = f"pasta não encontrada: {pasta}"
        return resultado
    faltando = [a for a in ex.get("arquivos", []) if not (pasta / a).exists()]
    if faltando:
        resultado["status"] = "falta"
        resultado["detalhe"] = "arquivo(s) ausente(s): " + ", ".join(faltando)
        return resultado
    validador = VALIDADORES.get(ex.get("validador"))
    if validador is None:
        resultado["status"] = "manual"
        resultado["detalhe"] = "sem validador automático"
        return resultado
    try:
        ok, detalhe = validador(pasta)
    except Exception as e:  # noqa: BLE001 - queremos mostrar o erro ao aluno
        ok, detalhe = False, f"erro no validador: {type(e).__name__}: {e}"
    if ok:
        resultado["status"] = "validado"
        resultado["casos"] = "shell"
        resultado["hash"] = _hash(pasta, ex.get("arquivos", []))
        if detalhe:
            resultado["detalhe"] = detalhe
    elif ok is None:
        resultado["status"] = "manual"
        resultado["detalhe"] = detalhe
    else:
        resultado["status"] = "teste"
        resultado["detalhe"] = detalhe
    if verboso:
        print(f"[shell] {resultado['id']}: {resultado['status']}")
    return resultado
