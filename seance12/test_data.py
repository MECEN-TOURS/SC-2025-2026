"""Description.

Module de tests unitaires pour data.py
"""

from data import Tache, CahierDesCharges, TachePlanifiee, Planning
from pydantic import ValidationError
import pytest


def test_duree_tache():
    with pytest.raises(ValidationError):
        Tache(nom="A", duree=-1.0, prerequis=[])


def test_tache_prerequis_circulaire():
    with pytest.raises(ValidationError):
        Tache(nom="A", duree=1.0, prerequis=["A", "B"])


def test_compatibilite_duree():
    a = Tache(nom="A", duree=1.0, prerequis=[])
    with pytest.raises(ValidationError):
        TachePlanifiee(tache=a, debut=0.0, fin=2.0)


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


def test_cahier_des_charges_getitem():
    tache = Tache(nom="A", duree=1.0, prerequis=[])
    cahier = CahierDesCharges(taches=[tache])
    assert cahier["A"] == tache


def test_cahier_des_charges_getitem_invalide():
    tache = Tache(nom="A", duree=1.0, prerequis=[])
    cahier = CahierDesCharges(taches=[tache])
    with pytest.raises(KeyError):
        cahier["B"]


def test_planning_getitem():
    """Vérifie que les contraintes tache prerequis sont vérifiées."""
    a = Tache(nom="A", duree=1.0, prerequis=[])
    b = Tache(nom="B", duree=2.0, prerequis=["A"])
    cahier = CahierDesCharges(taches=[a, b])
    ap = TachePlanifiee(tache=a, debut=0.0, fin=1.0)
    bp = TachePlanifiee(tache=b, debut=1.0, fin=3.0)
    planning = Planning(cahier_des_charges=cahier, details=[ap, bp])
    assert planning["A"] == ap
    assert planning["B"] == bp
    with pytest.raises(KeyError):
        planning["C"]


def test_planning_complet():
    """Vérifie que toutes les tâches sont bien planifiées."""
    a = Tache(nom="A", duree=1.0, prerequis=[])
    b = Tache(nom="B", duree=2.0, prerequis=["A"])
    cahier = CahierDesCharges(taches=[a, b])
    ap = TachePlanifiee(tache=a, debut=0.0, fin=1.0)
    with pytest.raises(ValidationError):
        Planning(
            cahier_des_charges=cahier,
            details=[ap],
        )


def test_planning_contrainte():
    """Vérifie que les contraintes tache prerequis sont vérifiées."""
    a = Tache(nom="A", duree=1.0, prerequis=[])
    b = Tache(nom="B", duree=2.0, prerequis=["A"])
    cahier = CahierDesCharges(taches=[a, b])
    ap = TachePlanifiee(tache=a, debut=0.0, fin=1.0)
    bp = TachePlanifiee(tache=b, debut=0.5, fin=2.5)
    with pytest.raises(ValidationError):
        Planning(
            cahier_des_charges=cahier,
            details=[ap, bp],
        )
