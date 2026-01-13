"""Descripion.

librairie de parcours de graphe abstrait.
"""

from typing import TypeVar

T = TypeVar("T")


def trouve_voisins(sommet: T, arretes: list[tuple[T, T]]) -> list[T]:
    return [arrivee for (depart, arrivee) in arretes if depart == sommet]


def sont_connectes(depart: T, arrivee: T, arretes: list[tuple[T, T]]) -> bool:
    """Teste si depart et arrivee sont relies par un chemin d'arretes."""
    ...
