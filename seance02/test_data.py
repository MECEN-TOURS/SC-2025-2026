from data import (
    Etat,
    Rive,
    DEPART,
    ARRIVEE,
    est_valide,
    sont_connectes,
    genere_arretes,
    genere_sommets,
)


def test_etat_to_str():
    entree = Etat(
        berger=Rive.GAUCHE, loup=Rive.DROITE, mouton=Rive.GAUCHE, choux=Rive.DROITE
    )
    assert str(entree) == "BM|LC"


def test_Etat_from_str():
    attendu = Etat(
        berger=Rive.GAUCHE, loup=Rive.DROITE, mouton=Rive.GAUCHE, choux=Rive.DROITE
    )
    entree = "BM|LC"
    assert attendu == Etat.from_str(entree)


def test_est_valide():
    assert est_valide(Etat.from_str("|BLMC"))
    assert est_valide(Etat.from_str("BLMC|"))
    assert not est_valide(Etat.from_str("LM|BC"))


def test_sont_connectes(): ...
