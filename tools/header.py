#!/usr/bin/env python3
"""Gera o cabeçalho 42 nos arquivos .c/.h.

Uso:
    python tools/header.py arquivo.c [arquivo.h ...]
    python tools/header.py .            # todos os .c/.h da pasta (recursivo)

O login/email vêm de 42.config na raiz do projeto.
"""

from __future__ import annotations

import configparser
import sys
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CONFIG = RAIZ / "42.config"


def config():
    login = "hilde"
    email = None
    if CONFIG.exists():
        cp = configparser.ConfigParser()
        cp.read(CONFIG, encoding="utf-8")
        login = cp.get("aluno", "login", fallback=login)
        email = cp.get("aluno", "email", fallback=None)
    if not email:
        email = f"{login}@student.42sp.org.br"
    return login, email


SUF_BY = "+#+  +:+       +#+        */"
SUF_L6 = "+#+#+#+#+#+   +#+           */"
SUF_CRIADO = "#+#    #+#             */"
SUF_UPDATE = "###   ########.fr       */"


def linha_direita(prefixo, sufixo):
    if len(prefixo) + len(sufixo) > 80:
        prefixo = prefixo[:80 - len(sufixo) - 1]
    return prefixo + " " * (80 - len(prefixo) - len(sufixo)) + sufixo


def cabecalho(nome, login, email, criado=None):
    agora = datetime.now()
    if criado is None:
        criado = agora
    data_c = criado.strftime("%Y/%m/%d %H:%M:%S")
    data_u = agora.strftime("%Y/%m/%d %H:%M:%S")
    nome = Path(nome).name
    linhas = [
        "/* " + "*" * 74 + " */",
        "/*" + " " * 76 + "*/",
        "/*" + " " * 56 + ":::      ::::::::   */",
        linha_direita("/*   " + nome.ljust(51), ":+:      :+:    :+:   */"),
        "/*" + " " * 52 + "+:+ +:+         +:+     */",
        linha_direita(f"/*   By: {login} <{email}>", SUF_BY),
        "/*" + " " * 48 + SUF_L6,
        linha_direita(f"/*   Created: {data_c} by {login}", SUF_CRIADO),
        linha_direita(f"/*   Updated: {data_u} by {login}", SUF_UPDATE),
        "/*" + " " * 76 + "*/",
        "/* " + "*" * 74 + " */",
    ]
    return "\n".join(linhas) + "\n"


def tem_cabecalho(texto):
    return "/* By:" in texto and "Created:" in texto


def processar(p: Path):
    try:
        texto = p.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        print(f"[erro] {p}: não é UTF-8")
        return False
    if tem_cabecalho(texto):
        print(f"[ok]   {p.name}: já possui cabeçalho")
        return True
    login, email = config()
    corpo = texto.lstrip("\n")
    p.write_text(cabecalho(p.name, login, email) + "\n" + corpo,
                 encoding="utf-8", newline="\n")
    print(f"[novo] {p.name}: cabeçalho inserido (login: {login})")
    return True


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    arquivos = []
    for arg in args:
        p = Path(arg)
        if p.is_dir():
            arquivos += [x for x in p.rglob("*")
                         if x.is_file() and x.suffix in {".c", ".h"}]
        elif p.is_file():
            arquivos.append(p)
        else:
            print(f"[erro] não encontrado: {p}")
    if not arquivos:
        print("Nenhum .c/.h encontrado.")
        return 1
    for p in sorted(set(arquivos)):
        processar(p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
