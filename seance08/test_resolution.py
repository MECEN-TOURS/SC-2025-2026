"""Description.

Tests unitaires du module resolution
"""

from data import ConnexionsSNCF, Itineraire
from resolution import resoud
from datetime import datetime


# Exercice: coder des tests élémentaires de la fonction resoud
def test_resolution_simple():
    connexions = ConnexionsSNCF(
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
    resultat = resoud(
        connexions=connexions, depart="Paris Montparnasse", arrivee="Tours"
    )
    assert resultat == [("Paris Montparnasse", 0), ("Tours", 1)]


def test_resolution():
    connexions = ConnexionsSNCF(
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
    resultat = resoud(
        connexions=connexions, depart="Paris Montparnasse", arrivee="Blois"
    )
    assert resultat == [("Paris Montparnasse", 0), ("Tours", 2), ("Blois", 3)]
