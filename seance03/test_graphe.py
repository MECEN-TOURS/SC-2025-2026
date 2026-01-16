"""Description.

Test de la librairie graphe.
"""

from graphe import _sont_connectes, _trouve_voisins, cherche_chemin


def test_trouve_voisins_bateau():
    arretes = [(1, 2)]
    assert _trouve_voisins(sommet=1, arretes=arretes) == [2]
    assert _trouve_voisins(sommet=2, arretes=arretes) == []


def test_trouve_voisins():
    arretes = [(1, 2), (2, 3), (3, 4), (4, 5), (4, 2), (2, 6), (6, 7)]
    assert _trouve_voisins(sommet=2, arretes=arretes) == [3, 6]
    assert _trouve_voisins(sommet=4, arretes=arretes) == [5, 2]


def test_parcours_bateau():
    arretes = [(1, 2)]
    assert _sont_connectes(depart=1, arrivee=2, arretes=arretes)
    assert not _sont_connectes(depart=2, arrivee=1, arretes=arretes)


def test_parcours():
    arretes = [(1, 2), (2, 3), (3, 4), (4, 5), (4, 2), (2, 6), (6, 7)]
    assert _sont_connectes(depart=1, arrivee=7, arretes=arretes)
    assert not _sont_connectes(depart=2, arrivee=1, arretes=arretes)


def test_chemin_bateau():
    arretes = [(1, 2)]
    assert cherche_chemin(depart=1, arrivee=2, arretes=arretes) == [1, 2]
    assert cherche_chemin(depart=2, arrivee=1, arretes=arretes) == []


def test_chemin():
    arretes = [(1, 2), (2, 3), (3, 4), (4, 5), (4, 2), (2, 6), (6, 7)]
    assert cherche_chemin(depart=1, arrivee=7, arretes=arretes) == [1, 2, 6, 7]
    assert cherche_chemin(depart=2, arrivee=1, arretes=arretes) == []
