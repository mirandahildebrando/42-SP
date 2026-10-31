#!/usr/bin/env python3
"""Simulador local de exames da Piscina 42SP.

Uso:
    exame                      # lista os exames e os melhores resultados
    exame iniciar exam00       # abre uma sessão cronometrada
    exame status               # tempo restante e exercícios da sessão
    exame entregar             # corrige e encerra a sessão
    exame resultado [sessao]   # relatório de uma sessão entregue
    exame historico            # todos os resultados
    exame abrir [sessao]       # abre a pasta no Explorer
"""

from __future__ import annotations

import argparse
import json
import os
import random
import shutil
import sys
from datetime import datetime, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PISCINA = RAIZ / "piscina"
BASE = RAIZ / "exames"
SESSOES = BASE / "sessoes"
HISTORICO = BASE / "historico.json"

sys.path.insert(0, str(RAIZ / "tools" / "moulinette"))
sys.path.insert(0, str(RAIZ / "tools" / "exame"))

from dados import MAPA, lista_por_id  # noqa: E402
from definicoes import EXAMES  # noqa: E402
from moulinette import corrigir  # noqa: E402


def agora():
    return datetime.now().astimezone()


def iso(dt):
    return dt.isoformat(timespec="seconds")


def ler_json(p, padrao=None):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return padrao


def salvar_json(p, dados):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n",
                 encoding="utf-8", newline="\n")


def listar_sessoes():
    if not SESSOES.exists():
        return []
    return sorted((p for p in SESSOES.iterdir()
                   if p.is_dir() and (p / "sessao.json").exists()),
                  key=lambda p: p.name, reverse=True)


def achar_sessao(arg=None, apenas_aberta=False):
    sessoes = listar_sessoes()
    if arg:
        for p in sessoes:
            if p.name == arg or p.name.endswith(arg) or p.name.startswith(arg):
                return p
        tentativa = Path(arg)
        if tentativa.exists() and (tentativa / "sessao.json").exists():
            return tentativa
        return None
    if apenas_aberta:
        for p in sessoes:
            if (ler_json(p / "sessao.json", {}) or {}).get("status") == "aberta":
                return p
        return None
    return sessoes[0] if sessoes else None


def fmt_tempo(minutos):
    minutos = int(round(minutos))
    sinal = "-" if minutos < 0 else ""
    minutos = abs(minutos)
    return f"{sinal}{minutos // 60:02d}h{minutos % 60:02d}"


def restante(sessao):
    inicio = datetime.fromisoformat(sessao["inicio"])
    fim = inicio + timedelta(minutes=int(sessao["duracao"]))
    return (fim - agora()).total_seconds() / 60.0, fim


def cmd_listar(_args):
    historico = ler_json(HISTORICO, []) or []
    print("Exames disponíveis\n")
    print(f"{'ID':8} {'Duração':8} {'Meta':5} {'Melhor':7} Título")
    print("-" * 78)
    for nome, d in EXAMES.items():
        notas = [h.get("nota") for h in historico
                 if h.get("exame") == nome and isinstance(h.get("nota"), (int, float))]
        melhor = f"{max(notas):.0f}%" if notas else "—"
        print(f"{nome:8} {d['duracao']:>5} min {d['meta']:>4}% {melhor:>7} {d['titulo']}")
    print("\nExemplo: exame iniciar exam00")
    print("Depois:  exame status   |   exame entregar")
    return 0


def _copiar_exercicio(chave, destino):
    lista_id, ex_id = chave.split("/")
    origem = PISCINA / lista_id / ex_id
    if not origem.exists():
        raise FileNotFoundError(f"exercício não encontrado: {origem}")
    shutil.copytree(
        origem, destino,
        ignore=shutil.ignore_patterns(".build", "__pycache__", "*.o", "*.exe",
                                      ".progresso.json", "PROGRESSO.md"),
    )


def cmd_iniciar(args):
    nome = args.exame
    if nome not in EXAMES:
        print(f"exame desconhecido: {nome}")
        print("Use um destes: " + ", ".join(EXAMES))
        return 2
    aberta = achar_sessao(apenas_aberta=True)
    if aberta and not args.forcar:
        s = ler_json(aberta / "sessao.json", {}) or {}
        print(f"Já existe uma sessão aberta: {aberta.name}")
        print(f"Termine com `exame entregar` ou use `exame iniciar {nome} --forcar`.")
        return 1

    d = EXAMES[nome]
    rng = random.Random(args.semente)
    pool = list(dict.fromkeys(d["pool"]))
    if d["n"] > len(pool):
        print("definição inválida: poucos exercícios no pool")
        return 2
    escolhidos = rng.sample(pool, d["n"])

    inicio = agora()
    base_nome = inicio.strftime("%Y-%m-%d_%H-%M-%S") + "_" + nome
    sessao_dir = SESSOES / base_nome
    n = 1
    while sessao_dir.exists():
        n += 1
        sessao_dir = SESSOES / f"{base_nome}_{n}"
    sessao_dir.mkdir(parents=True)

    exercicios = []
    for i, chave in enumerate(escolhidos):
        slot = f"ex{i:02d}"
        destino = sessao_dir / slot
        _copiar_exercicio(chave, destino)
        lista = lista_por_id(chave.split("/")[0])
        ex = MAPA[chave][1]
        exercicios.append({
            "slot": slot,
            "chave": chave,
            "lista": lista["id"],
            "ex": ex["id"],
            "nome": ex["nome"],
        })

    sessao = {
        "id": sessao_dir.name,
        "exame": nome,
        "titulo": d["titulo"],
        "inicio": iso(inicio),
        "duracao": d["duracao"],
        "limite": iso(inicio + timedelta(minutes=d["duracao"])),
        "meta": d["meta"],
        "status": "aberta",
        "exercicios": exercicios,
    }
    salvar_json(sessao_dir / "sessao.json", sessao)

    linhas = [
        f"# {d['titulo']}",
        "",
        f"**Início:** {sessao['inicio']}  ",
        f"**Duração:** {d['duracao']} minutos  ",
        f"**Meta local:** {d['meta']}%  ",
        f"**Sessão:** `{sessao_dir.name}`",
        "",
        "> Simulado de treino. Não use IA, soluções prontas ou outro agente.",
        "> O cronômetro é honesto: quem para de treinar no tempo real chega",
        "> mais preparado na piscina.",
        "",
        "## Exercícios",
        "",
    ]
    for item in exercicios:
        linhas.append(f"- **{item['slot']}** — {item['chave']} — {item['nome']}")
    linhas += [
        "",
        "## Comandos",
        "",
        "```bash",
        "exame status",
        "exame entregar",
        "```",
        "",
        "Cada pasta tem o `ENUNCIADO.md` e os arquivos fornecidos. Edite apenas",
        "os arquivos pedidos pelo subject. Ao entregar, o corretor roda",
        "norminette, funções proibidas, compilação e os testes.",
        "",
    ]
    (sessao_dir / "LEIA-ME.md").write_text("\n".join(linhas), encoding="utf-8",
                                           newline="\n")

    print(f"Sessão criada: {sessao_dir}")
    print(f"Exame: {d['titulo']}  |  duração: {d['duracao']} min  |  meta: {d['meta']}%")
    print("\nExercícios:")
    for item in exercicios:
        print(f"  {item['slot']}  {item['chave']:<12} {item['nome']}")
    print("\nAbra a pasta e comece. Use `exame status` para ver o tempo.")
    return 0


def cmd_status(args):
    p = achar_sessao(args.sessao, apenas_aberta=not args.sessao)
    if p is None:
        print("Nenhuma sessão encontrada. Comece com `exame iniciar exam00`.")
        return 1
    s = ler_json(p / "sessao.json", {}) or {}
    mins, fim = restante(s)
    print(f"Sessão: {p.name}")
    print(f"Exame:  {s.get('titulo', s.get('exame'))}")
    print(f"Status: {s.get('status')}")
    print(f"Limite: {fim.strftime('%d/%m/%Y %H:%M:%S')}  (restante: {fmt_tempo(mins)})")
    if s.get("status") == "aberta" and mins < 0:
        print("ATENÇÃO: o tempo acabou. Entregue o que tiver e estude os erros.")
    print("\nExercícios:")
    for item in s.get("exercicios", []):
        pasta = p / item["slot"]
        arquivos = sorted(x.name for x in pasta.glob("*.c")) if pasta.exists() else []
        print(f"  {item['slot']}  {item['chave']:<12} {item['nome']}")
        print(f"        arquivos .c: {', '.join(arquivos) if arquivos else '(nenhum)'}")
    print("\nEntregue com: exame entregar")
    return 0


def _nota(r):
    if r.get("status") == "validado":
        return 100
    return 0


def cmd_entregar(args):
    p = achar_sessao(args.sessao, apenas_aberta=not args.sessao)
    if p is None:
        print("Nenhuma sessão encontrada.")
        return 1
    s = ler_json(p / "sessao.json", {}) or {}
    if s.get("status") != "aberta":
        print(f"Esta sessão já está {s.get('status')}. Use `exame resultado`.")
        return 1
    mins, fim = restante(s)
    s["entregue_em"] = iso(agora())
    s["minutos_usados"] = round(max(0, (agora() - datetime.fromisoformat(s["inicio"]))
                                   .total_seconds() / 60.0), 1)
    s["atrasado"] = mins < 0
    s["status"] = "entregue"

    resultados = []
    for item in s["exercicios"]:
        lista = lista_por_id(item["lista"])
        ex = MAPA[item["chave"]][1]
        pasta = p / item["slot"]
        try:
            r = corrigir(lista, ex, pasta_override=pasta)
        except Exception as e:  # noqa: BLE001 - o examinador não deve derrubar o simulado
            r = {
                "id": item["chave"], "nome": item["nome"],
                "status": "erro", "detalhe": f"{type(e).__name__}: {e}",
                "casos": "",
            }
        r["slot"] = item["slot"]
        r["chave"] = item["chave"]
        r["nota"] = _nota(r)
        resultados.append(r)

    nota = round(sum(r["nota"] for r in resultados) / len(resultados)) if resultados else 0
    s["resultados"] = resultados
    s["nota"] = nota
    s["aprovado"] = nota >= int(s.get("meta", 75))
    salvar_json(p / "sessao.json", s)

    hist = ler_json(HISTORICO, []) or []
    hist.append({
        "sessao": p.name,
        "exame": s.get("exame"),
        "data": s.get("entregue_em"),
        "nota": nota,
        "meta": s.get("meta"),
        "aprovado": s.get("aprovado"),
        "minutos_usados": s.get("minutos_usados"),
        "atrasado": s.get("atrasado"),
    })
    salvar_json(HISTORICO, hist)

    print(f"Resultado — {s.get('titulo')}")
    print(f"Sessão: {p.name}")
    print(f"Tempo usado: {s['minutos_usados']:.0f} min de {s['duracao']} min"
          + ("  (ATRASADO)" if s.get("atrasado") else ""))
    print()
    for r in resultados:
        marca = "OK " if r["nota"] == 100 else "XX "
        print(f"{marca}{r['slot']}  {r['chave']:<12} {r['nome']}")
        if r["nota"] != 100:
            det = (r.get("detalhe") or r.get("status") or "").strip().splitlines()
            for linha in det[:4]:
                print("      " + linha)
    print()
    print(f"Nota: {nota}%   Meta: {s.get('meta')}%   "
          + ("APROVADO no simulado" if s.get("aprovado") else "ABAIXO DA META"))
    print(f"Relatório: {p / 'sessao.json'}")
    print("Estude os erros e refaça os exercícios na pasta principal.")
    return 0


def _mostrar_resultado(p):
    s = ler_json(p / "sessao.json", {}) or {}
    print(f"Sessão: {p.name}")
    print(f"Exame: {s.get('titulo', s.get('exame'))}  |  Status: {s.get('status')}")
    if s.get("nota") is None:
        print("Ainda não entregue. Use `exame entregar`.")
        return 1
    print(f"Nota: {s.get('nota')}%  |  Meta: {s.get('meta')}%  |  "
          + ("aprovado" if s.get("aprovado") else "abaixo da meta"))
    for r in s.get("resultados", []):
        print(f"  {r.get('slot')}  {r.get('chave')}: {r.get('nota')}%  ({r.get('status')})")
    return 0


def cmd_resultado(args):
    p = achar_sessao(args.sessao)
    if p is None:
        print("Nenhuma sessão encontrada.")
        return 1
    return _mostrar_resultado(p)


def cmd_historico(_args):
    hist = ler_json(HISTORICO, []) or []
    if not hist:
        print("Ainda não há resultados. Faça `exame iniciar exam00`.")
        return 0
    print(f"{'Data':20} {'Exame':8} {'Nota':6} {'Meta':5} {'Tempo':8} Resultado")
    print("-" * 76)
    for h in hist:
        data = (h.get("data") or "")[:19].replace("T", " ")
        resultado = "aprovado" if h.get("aprovado") else "abaixo"
        if h.get("atrasado"):
            resultado += " (atrasado)"
        print(f"{data:20} {str(h.get('exame')):8} {str(h.get('nota')) + '%':>6} "
              f"{str(h.get('meta')) + '%':>5} {str(h.get('minutos_usados')) + ' min':>8} {resultado}")
    return 0


def cmd_abrir(args):
    p = achar_sessao(args.sessao)
    if p is None:
        print("Nenhuma sessão encontrada.")
        return 1
    try:
        os.startfile(str(p))  # type: ignore[attr-defined]
    except Exception as e:  # noqa: BLE001
        print(f"não consegui abrir o Explorer: {e}\nPasta: {p}")
    return 0


def cmd_cancelar(args):
    p = achar_sessao(args.sessao, apenas_aberta=True)
    if p is None:
        print("Nenhuma sessão aberta.")
        return 1
    s = ler_json(p / "sessao.json", {}) or {}
    s["status"] = "cancelada"
    s["cancelada_em"] = iso(agora())
    salvar_json(p / "sessao.json", s)
    print(f"Sessão cancelada: {p.name}")
    return 0


def criar_parser():
    p = argparse.ArgumentParser(
        prog="exame",
        description="Simulador de exames da Piscina 42SP (treino local).",
    )
    p.add_argument("--versao", action="version", version="exame 1.0")
    sub = p.add_subparsers(dest="comando")

    sub.add_parser("listar", help="lista os exames (padrão)")

    ini = sub.add_parser("iniciar", help="abre uma sessão cronometrada")
    ini.add_argument("exame", choices=list(EXAMES))
    ini.add_argument("--semente", type=int, default=None,
                     help="semente para sortear os mesmos exercícios")
    ini.add_argument("--forcar", action="store_true",
                     help="abre mesmo com outra sessão aberta")

    st = sub.add_parser("status", help="mostra tempo e exercícios")
    st.add_argument("sessao", nargs="?", default=None)

    en = sub.add_parser("entregar", help="corrige e encerra a sessão")
    en.add_argument("sessao", nargs="?", default=None)

    re = sub.add_parser("resultado", help="relatório de uma sessão")
    re.add_argument("sessao", nargs="?", default=None)

    sub.add_parser("historico", help="histórico de resultados")

    ab = sub.add_parser("abrir", help="abre a pasta da sessão no Explorer")
    ab.add_argument("sessao", nargs="?", default=None)

    ca = sub.add_parser("cancelar", help="cancela a sessão aberta")
    ca.add_argument("sessao", nargs="?", default=None)
    return p


def main(argv=None):
    p = criar_parser()
    args = p.parse_args(argv)
    if not args.comando:
        return cmd_listar(args)
    return {
        "listar": cmd_listar,
        "iniciar": cmd_iniciar,
        "status": cmd_status,
        "entregar": cmd_entregar,
        "resultado": cmd_resultado,
        "historico": cmd_historico,
        "abrir": cmd_abrir,
        "cancelar": cmd_cancelar,
    }[args.comando](args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\ninterrompido")
        raise SystemExit(130)
