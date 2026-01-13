"""Description.


Librairie fournissant des objets pour résoudre le problème de traversée de rivière.
"""

from enum import Enum
from dataclasses import dataclass


class Rive(Enum):
    GAUCHE = "gauche"
    DROITE = "droite"


@dataclass
class Etat:
    berger: Rive
    loup: Rive
    mouton: Rive
    choux: Rive

    def __str__(self) -> str:
        gauche = list()
        droite = list()
        if self.berger == Rive.GAUCHE:
            gauche.append("B")
        else:
            droite.append("B")
        if self.loup == Rive.GAUCHE:
            gauche.append("L")
        else:
            droite.append("L")
        if self.mouton == Rive.GAUCHE:
            gauche.append("M")
        else:
            droite.append("M")
        if self.choux == Rive.GAUCHE:
            gauche.append("C")
        else:
            droite.append("C")
        return "".join(gauche) + "|" + "".join(droite)

    @staticmethod
    def etat_from_str(chaine: str) -> "Etat":
        if sorted(chaine) != list("BCLM|"):
            raise ValueError("chaine invalide")
        indice_barre = chaine.find("|")
        if chaine.find("B") < indice_barre:
            berger = Rive.GAUCHE
        else:
            berger = Rive.DROITE
        if chaine.find("L") < indice_barre:
            loup = Rive.GAUCHE
        else:
            loup = Rive.DROITE
        if chaine.find("M") < indice_barre:
            mouton = Rive.GAUCHE
        else:
            mouton = Rive.DROITE
        if chaine.find("C") < indice_barre:
            choux = Rive.GAUCHE
        else:
            choux = Rive.DROITE
        return Etat(berger=berger, loup=loup, mouton=mouton, choux=choux)


DEPART = Etat(
    berger=Rive.GAUCHE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, choux=Rive.GAUCHE
)


ARRIVEE = Etat(
    berger=Rive.DROITE, loup=Rive.DROITE, mouton=Rive.DROITE, choux=Rive.DROITE
)


def est_valide(etat: Etat) -> bool:
    if etat.loup == etat.mouton and etat.berger != etat.loup:
        return False
    if etat.mouton == etat.choux and etat.berger != etat.mouton:
        return False
    return True


def genere_sommets() -> list[Etat]:
    etats = []
    for berger in Rive:
        for loup in Rive:
            for mouton in Rive:
                for choux in Rive:
                    etats.append(
                        Etat(
                            berger=berger,
                            loup=loup,
                            mouton=mouton,
                            choux=choux,
                        )
                    )
    return [etat for etat in etats if est_valide(etat)]


def sont_connectes(depart: Etat, arrivee: Etat) -> bool:
    if depart.berger == arrivee.berger:
        return False
    nombre_changements = 0
    if depart.loup != arrivee.loup:
        if depart.loup != depart.berger:
            return False
        else:
            nombre_changements = nombre_changements + 1
    if depart.mouton != arrivee.mouton:
        if depart.mouton != depart.berger:
            return False
        else:
            nombre_changements = nombre_changements + 1
    if depart.choux != arrivee.choux:
        if depart.choux != depart.berger:
            return False
        else:
            nombre_changements = nombre_changements + 1
    return nombre_changements < 2


def genere_arretes() -> list[tuple[Etat, Etat]]:
    resultat = []
    for depart in genere_sommets():
        for arrivee in genere_sommets():
            if sont_connectes(depart=depart, arrivee=arrivee):
                resultat.append((depart, arrivee))
    return resultat
