"""Description.


Tests pour le module graphe.py
"""

import pytest

from graphe import trouve_voisins, bfs, dfs, plus_court_chemin


def test_voisinages():
    """vérifie quelques valeurs."""
    assert trouve_voisins(
        sommet=1, arretes=[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (1, 7), (7, 6)]
    ) == [2, 7]
    assert trouve_voisins(
        sommet=4, arretes=[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (1, 7), (7, 6)]
    ) == [5]
    assert (
        trouve_voisins(
            sommet=6, arretes=[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (1, 7), (7, 6)]
        )
        == []
    )


def test_court():
    assert plus_court_chemin(
        depart=1,
        arrivee=6,
        arretes=[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (1, 7), (7, 6)],
    ) == [1, 7, 6]
