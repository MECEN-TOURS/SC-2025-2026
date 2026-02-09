"""Description.

Tests unitaires de resolution.py
"""

from data import CahierDesCharges, Tache, TachePlanifiee, Planning
from resolution import construit_graphe, a_une_solution, resoud_ordonnancement
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
    assert a_une_solution(cahier=cahier)


def test_non_soluble():
    cahier = CahierDesCharges(
        taches=[
            Tache(nom="A", duree=1.0, prerequis=["B"]),
            Tache(nom="B", duree=1.0, prerequis=["C"]),
            Tache(nom="C", duree=1.0, prerequis=["A"]),
        ]
    )
    assert not a_une_solution(cahier=cahier)


def test_resolution_simple():
    a = Tache(nom="A", duree=1.0, prerequis=[])
    b = Tache(nom="B", duree=2.0, prerequis=["A"])
    cahier = CahierDesCharges(taches=[a, b])
    planning = resoud_ordonnancement(cahier=cahier, debut=1.0)
    assert planning["A"].debut == 1.0
    assert planning["A"].fin == 2.0
    assert planning["B"].debut == 2.0
    assert planning["B"].fin == 4.0
