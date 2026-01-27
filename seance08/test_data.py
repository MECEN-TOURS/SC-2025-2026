"""Description.

Tests unitaires du module data.py
"""

import pytest
from data import Itineraire, ConnexionsSNCF
from datetime import datetime


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


def test_itineraire_to_str_sans_escale():
    it = Itineraire(
        gare_depart="Paris Gare de Lyon",
        gare_arrivee="Bordeaux",
        duree=3,
        escales=[],
    )
    assert (
        str(it)
        == """
depart: Paris Gare de Lyon
arrivee: Bordeaux
duree: 3h
""".strip()
    )


def test_itineraire_to_str_avec_escales():
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


def test_serialisation_itineraire():
    it = Itineraire(
        gare_depart="Paris Gare de Lyon",
        gare_arrivee="Bordeaux",
        duree=3,
        escales=[("Vendome", 1), ("Tours", 2)],
    )
    assert (
        it.model_dump_json(indent=2)
        == """
{
  "gare_depart": "Paris Gare de Lyon",
  "gare_arrivee": "Bordeaux",
  "duree": 3,
  "escales": [
    [
      "Vendome",
      1
    ],
    [
      "Tours",
      2
    ]
  ]
}
    """.strip()
    )


def test_deserialisation_itineraire():
    it = Itineraire(
        gare_depart="Paris Gare de Lyon",
        gare_arrivee="Bordeaux",
        duree=3,
        escales=[("Vendome", 1), ("Tours", 2)],
    )
    json = """
{
  "gare_depart": "Paris Gare de Lyon",
  "gare_arrivee": "Bordeaux",
  "duree": 3,
  "escales": [
    [
      "Vendome",
      1
    ],
    [
      "Tours",
      2
    ]
  ]
}
    """.strip()
    assert it == Itineraire.model_validate_json(json_data=json)


def test_instanciation_connexion_SNCF():
    cs = ConnexionsSNCF(
        itineraires=[],
        date=datetime.now(),
    )
    assert isinstance(cs, ConnexionsSNCF)
