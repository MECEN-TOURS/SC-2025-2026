"""Description.

Tests unitaires du module resolution
"""

import networkx as nx
import pytest
from data import ConnexionsSNCF, Itineraire
from resolution import resoud, construit_graphe
from datetime import datetime


@pytest.fixture
def connexions_simple():
    return ConnexionsSNCF(
        itineraires=[
            Itineraire(
                gare_depart="Paris Montparnasse",
                gare_arrivee="Tours",
                duree=1,
                escales=[],
            )
        ],
        date=datetime.now(),
    )


@pytest.fixture
def connexions_moins_simple():
    return ConnexionsSNCF(
        itineraires=[
            Itineraire(
                gare_depart="Paris Montparnasse",
                gare_arrivee="Bordeaux",
                duree=3,
                escales=[("Vendome", 1), ("Tours", 2)],
            ),
            Itineraire(
                gare_depart="Tours",
                gare_arrivee="Orleans",
                duree=2,
                escales=[("Blois", 1)],
            ),
        ],
        date=datetime.now(),
    )


def test_resolution_simple(connexions_simple):
    resultat = resoud(
        connexions=connexions_simple, depart="Paris Montparnasse", arrivee="Tours"
    )
    assert resultat == [("Paris Montparnasse", 0), ("Tours", 1)]


def test_resolution(connexions_moins_simple):
    resultat = resoud(
        connexions=connexions_moins_simple, depart="Paris Montparnasse", arrivee="Blois"
    )
    assert resultat == [
        ("Paris Montparnasse", 0),
        ("Vendome", 1),
        ("Tours", 2),
        ("Blois", 3),
    ]


def test_construction_simple(connexions_simple):
    calcule = construit_graphe(connexions=connexions_simple)
    attendu = nx.DiGraph()
    attendu.add_edge("Paris Montparnasse", "Tours", duree=1)
    assert nx.utils.graphs_equal(calcule, attendu)


def test_construction(connexions_moins_simple):
    calcule = construit_graphe(connexions=connexions_moins_simple)
    attendu = nx.DiGraph()
    attendu.add_edge("Paris Montparnasse", "Vendome", duree=1)
    attendu.add_edge("Vendome", "Tours", duree=1)
    attendu.add_edge("Tours", "Bordeaux", duree=1)
    attendu.add_edge("Tours", "Blois", duree=1)
    attendu.add_edge("Blois", "Orleans", duree=1)
    assert nx.utils.graphs_equal(calcule, attendu)
