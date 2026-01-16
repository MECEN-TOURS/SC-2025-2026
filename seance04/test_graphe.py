"""Description.


Tests pour le module graphe.py
"""

from graphe import cherche_chemin_court


def test_chemin_court_simple():
    """Valeur elementaire."""
    assert cherche_chemin_court(
        depart=1,
        arrivee=6,
        arretes=[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (1, 7), (7, 6)],
    ) == [1, 7, 6]
