"""Descripion.

librairie de parcours de graphe abstrait.
"""

from typing import TypeVar

T = TypeVar("T")


def trouve_voisins(sommet: T, arretes: list[tuple[T, T]]) -> list[T]:
    return [arrivee for (depart, arrivee) in arretes if depart == sommet]


# EXERCICE: débogguer la fonction suivante à partir des tests


def sont_connectes(depart: T, arrivee: T, arretes: list[tuple[T, T]]) -> bool:
    """Teste si depart et arrivee sont relies par un chemin d'arretes."""
    sommet_courant = depart
    visites = [depart]
    a_visiter = trouve_voisins(depart, arretes)
    while a_visiter:
        if sommet_courant == arrivee:
            return True
        sommet_courant = a_visiter.pop()
        visites.append(sommet_courant)
        for voisin in trouve_voisins(sommet_courant, arretes):
            if voisin not in visites:
                a_visiter.append(voisin)
    return False
