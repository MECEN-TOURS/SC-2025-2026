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


def cherche_chemin(depart: T, arrivee: T, arretes: list[tuple[T, T]]) -> list[T]:
    """Cherche un chemin reliant depart et arrivee sont relies par un chemin d'arretes."""

    def auxiliaire(depart: T, arrivee: T, visites=list[T]) -> list[T]:
        visites.append(depart)
        if depart == arrivee:
            return [depart]
        for voisin in trouve_voisins(depart, arretes):
            if voisin not in visites:
                candidat = auxiliaire(depart=voisin, arrivee=arrivee, visites=visites)
                if candidat:
                    return [depart] + candidat
        return []

    visites: list[T] = list()
    return auxiliaire(depart=depart, arrivee=arrivee, visites=visites)
