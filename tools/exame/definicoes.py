"""Definições dos exames simulados da Piscina 42SP."""

EXAMES = {
    "exam00": {
        "titulo": "Exam 00 — aquecimento",
        "descricao": "Funções e loops das primeiras listas. Ideal para o primeiro fim de semana.",
        "duracao": 120,
        "meta": 75,
        "n": 4,
        "pool": [
            "C00/ex00", "C00/ex03", "C00/ex06",
            "C01/ex00", "C01/ex05", "C01/ex07",
            "C02/ex00", "C02/ex06",
        ],
    },
    "exam01": {
        "titulo": "Exam 01 — strings e memória",
        "descricao": "Ponteiros, strings e os primeiros programas.",
        "duracao": 180,
        "meta": 75,
        "n": 4,
        "pool": [
            "C02/ex00", "C02/ex04", "C02/ex06",
            "C03/ex00", "C03/ex03",
            "C04/ex00", "C04/ex02", "C04/ex04",
        ],
    },
    "exam02": {
        "titulo": "Exam 02 — malloc e arquivos",
        "descricao": "Alocação, listas e leitura de arquivos.",
        "duracao": 240,
        "meta": 80,
        "n": 4,
        "pool": [
            "C04/ex00", "C04/ex04",
            "C05/ex00", "C05/ex03", "C05/ex06",
            "C06/ex00", "C06/ex02",
        ],
    },
    "exam03": {
        "titulo": "Exam 03 — argumentos e conversão",
        "descricao": "argc/argv, conversão de base e funções maiores.",
        "duracao": 240,
        "meta": 80,
        "n": 4,
        "pool": [
            "C06/ex00", "C06/ex02",
            "C07/ex00", "C07/ex03", "C07/ex05",
            "C08/ex00", "C08/ex03",
        ],
    },
    "final": {
        "titulo": "Simulado final — tudo junto",
        "descricao": "Quatro exercícios sorteados de todo o currículo. Use na véspera.",
        "duracao": 300,
        "meta": 90,
        "n": 4,
        "pool": [
            "C00/ex03", "C00/ex06",
            "C01/ex03", "C01/ex05",
            "C02/ex04", "C02/ex06",
            "C03/ex03",
            "C04/ex02", "C04/ex04",
            "C05/ex03", "C05/ex06",
            "C06/ex02",
            "C07/ex03", "C07/ex05",
            "C08/ex03",
        ],
    },
}
