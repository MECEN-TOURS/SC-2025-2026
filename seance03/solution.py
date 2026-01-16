"""Description.

Script résolvant le problème de traversée de rivière à l'aide des bibliothèques graphe.py data.py
"""

from graphe import cherche_chemin
from data import DEPART, ARRIVEE, genere_arretes, visualise_chemin


def main():
    """Fonction principale."""
    arretes = genere_arretes()
    print(
        visualise_chemin(
            cherche_chemin(depart=DEPART, arrivee=ARRIVEE, arretes=arretes)
        )
    )


if __name__ == "__main__":
    main()
