"""Description.

Tests unitaires de resolution.py
"""

from data import CahierDesCharges, Tache
from resolution import construit_graphe, est_soluble
import networkx as nx


def test_construction_simple():
    cahier = CahierDesCharges(
        taches=[
            Tache(nom="A", duree=1.0, prerequis=[]),
            Tache(nom="B", duree=2.0, prerequis=["A"]),
        ]
    )
    resultat = construit_graphe(cahier=cahier)
    attendu = nx.DiGraph()
    attendu.add_edge("A", "B", duree=1.0)
    assert nx.utils.graphs_equal(resultat, attendu)


def test_soluble():
    cahier = CahierDesCharges(
        taches=[
            Tache(nom="A", duree=1.0, prerequis=[]),
            Tache(nom="B", duree=2.0, prerequis=["A"]),
        ]
    )
    assert est_soluble(cahier=cahier)


def test_non_soluble():
    cahier = CahierDesCharges(
        taches=[
            Tache(nom="A", duree=1.0, prerequis=["B"]),
            Tache(nom="B", duree=1.0, prerequis=["C"]),
            Tache(nom="C", duree=1.0, prerequis=["A"]),
        ]
    )
    assert not est_soluble(cahier=cahier)
