"""Description.


Librairie fournissant des objets pour résoudre le problème de traversée de rivière.
"""

from enum import Enum
from dataclasses import dataclass


class Rive(Enum):
    """Objet modélisant un côté de la rivière."""

    GAUCHE = "gauche"
    DROITE = "droite"


@dataclass
class Etat:
    """Objet modélisant l'état du système. Chaque personnage étant d'un côté de la rivière.

    Pas de vérification de validité à ce stade.
    """

    berger: Rive
    loup: Rive
    mouton: Rive
    choux: Rive

    def __str__(self) -> str:
        """Encode un état avec une chaine de caractéres."""
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
    def from_str(chaine: str) -> "Etat":
        """Convertit une chaine de caractères en état.

        Une chaine valide contient B L M C | exactement une fois.
        La position de BLMC par rapport à | encode la vide du personnage correspondant.
        """
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


# DEPART représente l'état ou tout le monde est à gauche
DEPART = Etat(
    berger=Rive.GAUCHE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, choux=Rive.GAUCHE
)


# ARRIVEE représente l'état ou tout le monde est à droite
ARRIVEE = Etat(
    berger=Rive.DROITE, loup=Rive.DROITE, mouton=Rive.DROITE, choux=Rive.DROITE
)


def est_valide(etat: Etat) -> bool:
    """Teste si l'état respecte les contraintes sur les personnages."""
    if etat.loup == etat.mouton and etat.berger != etat.loup:
        return False
    if etat.mouton == etat.choux and etat.berger != etat.mouton:
        return False
    return True


def genere_sommets() -> list[Etat]:
    """Renvoie la liste des etats valides."""
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
    """Teste si on peut passer de depart à arrivee en une seule traversée de rivière."""
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
    """Génère toutes les arrêtes du graphe."""
    resultat = []
    for depart in genere_sommets():
        for arrivee in genere_sommets():
            if sont_connectes(depart=depart, arrivee=arrivee):
                resultat.append((depart, arrivee))
    return resultat


# Exercice implémenter la fonction
def visualise_chemin(chemin: list[Etat]) -> str:
    """Permet un meilleur affichage du résultat."""
    ...
