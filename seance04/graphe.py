"""Description.


Recherche de chemin le plus court
"""

from typing import Iterable
from collections import deque


def trouve_voisins(sommet: int, arretes: list[tuple[int, int]]) -> list[int]:
    """Trouve tous les voisins de sommet dans le graphe encodé par arretes."""
    return [arrivee for (depart, arrivee) in arretes if depart == sommet]


def dfs(depart: int, arretes: list[tuple[int, int]]) -> Iterable[int]:
    visite = set()
    a_visiter = deque([depart])
    while a_visiter:
        sommet_courant = a_visiter.pop()
        visite.add(sommet_courant)
        yield sommet_courant
        for voisin in trouve_voisins(sommet=sommet_courant, arretes=arretes):
            if voisin not in visite:
                a_visiter.append(voisin)


def bfs(depart: int, arretes: list[tuple[int, int]]) -> Iterable[int]:
    visite = set()
    a_visiter = deque([depart])
    while a_visiter:
        sommet_courant = a_visiter.popleft()
        visite.add(sommet_courant)
        yield sommet_courant
        for voisin in trouve_voisins(sommet=sommet_courant, arretes=arretes):
            if voisin not in visite:
                a_visiter.append(voisin)


def plus_court_chemin(
    depart: int, arrivee: int, arretes: list[tuple[int, int]]
) -> list[int]:
    """Cherche le chemin de depart a arrivee avec le moins d'arretes"""
    ...
