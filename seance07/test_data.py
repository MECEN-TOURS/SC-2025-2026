"""Description.

Tests unitaires du module data.py
"""

import pytest
from data import Itineraire


def test_validite_itineraire():
    with pytest.raises(ValueError):
        Itineraire(
            gare_depart="Paris Gare de Lyon", gare_arrivee="Tours", duree=-1, escales=[]
        )
    with pytest.raises(ValueError):
        Itineraire(
            gare_depart="Paris Gare de Lyon",
            gare_arrivee="Tours",
            duree=1,
            escales=[("Vendome", -1)],
        )
    with pytest.raises(ValueError):
        Itineraire(
            gare_depart="Paris Gare de Lyon",
            gare_arrivee="Tours",
            duree=1,
            escales=[("Vendome", 2)],
        )
    with pytest.raises(ValueError):
        Itineraire(
            gare_depart="Paris Gare de Lyon",
            gare_arrivee="Bordeaux",
            duree=3,
            escales=[("Vendome", 2), ("Tours", 1)],
        )


def test_itineraire_to_str():
    it = Itineraire(
        gare_depart="Paris Gare de Lyon",
        gare_arrivee="Bordeaux",
        duree=3,
        escales=[("Vendome", 1), ("Tours", 2)],
    )
    assert (
        str(it)
        == """
depart: Paris Gare de Lyon 
arrivee: Bordeaux 
duree: 3h
escale: (Vendome, 1)
escale: (Tours, 2)
""".strip()
    )
