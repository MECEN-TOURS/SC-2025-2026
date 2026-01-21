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
