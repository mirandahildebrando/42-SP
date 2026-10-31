"""Pacote de dados do currículo da Piscina 42SP."""

from . import c00, c01, c02, c03, c04, c05, c06, c07, c08
from . import shell00, shell01

LISTAS = [
    c00.LISTA, c01.LISTA, c02.LISTA, c03.LISTA, c04.LISTA,
    c05.LISTA, c06.LISTA, c07.LISTA, c08.LISTA,
    shell00.LISTA, shell01.LISTA,
]

# Mapa "C00/ex00" -> (lista, exercício)
MAPA = {}
for _lista in LISTAS:
    for _ex in _lista["exercicios"]:
        MAPA[f"{_lista['id']}/{_ex['id']}"] = (_lista, _ex)


def por_id(ex_id):
    return MAPA[ex_id]


def lista_por_id(lista_id):
    for lista in LISTAS:
        if lista["id"] == lista_id:
            return lista
    return None
