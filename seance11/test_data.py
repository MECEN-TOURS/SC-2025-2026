"""Description.

Module de tests unitaires pour data.py
"""

from data import Tache, CahierDesCharges
from pydantic import ValidationError
import pytest


def test_duree_tache():
    with pytest.raises(ValidationError):
        Tache(nom="A", duree=-1.0, prerequis=[])


def test_tache_prerequis_circulaire():
    with pytest.raises(ValidationError):
        Tache(nom="A", duree=1.0, prerequis=["A", "B"])


def test_noms_cahier_des_charges():
    with pytest.raises(ValidationError):
        CahierDesCharges(
            taches=[
                Tache(nom="A", duree=1.0, prerequis=[]),
                Tache(nom="A", duree=2.0, prerequis=[]),
            ]
        )


def test_prerequis_cahier_des_charges():
    with pytest.raises(ValidationError):
        CahierDesCharges(
            taches=[
                Tache(nom="A", duree=1.0, prerequis=["B"]),
            ]
        )
