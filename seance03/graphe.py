"""Descripion.

librairie de parcours de graphe abstrait.
"""

from typing import TypeVar

T = TypeVar("T")


def trouve_voisins(sommet: T, arretes: list[tuple[T, T]]) -> list[T]:
    return [arrivee for (depart, arrivee) in arretes if depart == sommet]


def sont_connectes(depart: T, arrivee: T, arretes: list[tuple[T, T]]) -> bool:
    """Teste si depart et arrivee sont relies par un chemin d'arretes."""
    sommet_courant = depart
    visites = [depart]
    a_visiter = trouve_voisins(depart, arretes)
    breakpoint()
    if sommet_courant == arrivee:
        return True
    while a_visiter:
        sommet_courant = a_visiter.pop()
        if sommet_courant == arrivee:
            return True
        visites.append(sommet_courant)
        for voisin in trouve_voisins(sommet_courant, arretes):
            if voisin not in visites:
                a_visiter.append(voisin)
    return False


## Exercice implémenter des tests pour cherche_chemin
## Implémenter cherche_chemin


def cherche_chemin(depart: T, arrivee: T, arretes: list[tuple[T, T]]) -> list[T]:
    """Cherche un chemin reliant depart et arrivee sont relies par un chemin d'arretes."""
    ...
