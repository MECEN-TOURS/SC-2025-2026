from data import (
    Etat,
    Rive,
    DEPART,
    ARRIVEE,
    est_valide,
    sont_connectes,
    genere_arretes,
    genere_sommets,
    visualise_chemin,
)
import pytest


def test_constantes():
    assert DEPART == Etat.from_str("BLMC|")
    assert ARRIVEE == Etat.from_str("|BLMC")


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


def test_Etat_from_str_bogue():
    """vérifie que la méthode from_str plante pour des entrées non valides."""
    with pytest.raises(ValueError):
        Etat.from_str("blabla")
    with pytest.raises(ValueError):
        Etat.from_str("BL | MC")


def test_est_valide():
    assert est_valide(Etat.from_str("|BLMC"))
    assert est_valide(Etat.from_str("BLMC|"))
    assert not est_valide(Etat.from_str("LM|BC"))


def test_sont_connectes():
    assert sont_connectes(depart=Etat.from_str("BLMC|"), arrivee=Etat.from_str("LC|BM"))
    assert not sont_connectes(
        depart=Etat.from_str("BLMC|"), arrivee=Etat.from_str("BLMC|")
    )
    assert not sont_connectes(
        depart=Etat.from_str("BLMC|"), arrivee=Etat.from_str("C|BLM")
    )
    assert not sont_connectes(
        depart=Etat.from_str("BL|MC"), arrivee=Etat.from_str("LMC|B")
    )


def test_genere_sommets():
    """Vérifie qu'on a 10 sommets 2 à 2 distincts."""
    sommets = genere_sommets()
    assert len(sommets) == 10
    for i, sommet in enumerate(sommets):
        for j, autre in enumerate(sommets):
            assert sommet != autre or i == j


def test_genere_arretes():
    """Présence ou pas de quelques arretes."""
    arretes = genere_arretes()
    assert (Etat.from_str("BLMC|"), Etat.from_str("LC|BM")) in arretes
    assert (Etat.from_str("BLMC|"), Etat.from_str("C|BLM")) not in arretes


def test_genere_arretes_symetrique():
    """Vérifie que le graphe est symétrique."""
    arretes = genere_arretes()
    for depart, arrivee in arretes:
        assert (arrivee, depart) in arretes


def test_visualisation():
    """Quelques valeurs de chemins."""
    assert visualise_chemin(chemin=[]) == ""
    entree = [Etat.from_str("BLMC|")]
    assert visualise_chemin(chemin=entree) == "BLMC|"
    entree = [
        Etat.from_str("BLMC|"),
        Etat.from_str("LC|BM"),
        Etat.from_str("BLC|M"),
    ]
    assert (
        visualise_chemin(chemin=entree)
        == """
BLMC|
  BM ->
LC|BM
  B <-
BLC|M
        """.strip()
    )
