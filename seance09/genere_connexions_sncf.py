"""Description.

Script pour générer une sérialisation json d'un objet ConnexionsSNCF.
"""

from data import ConnexionsSNCF, Itineraire
from datetime import datetime
from pathlib import Path


def main():
    csncf = ConnexionsSNCF(
        date=datetime.now(),
        itineraires=[
            Itineraire(
                gare_depart="Paris",
                gare_arrivee="Bordeaux",
                duree=3,
                escales=[("Vendome", 1), ("Tours", 2)],
            ),
            Itineraire(
                gare_depart="Nantes",
                gare_arrivee="Lyon",
                duree=4,
                escales=[("Angers", 1), ("Tours", 2), ("Blois", 3), ("Orleans", 4)],
            ),
            Itineraire(
                gare_depart="Orleans",
                gare_arrivee="Paris",
                duree=1,
                escales=[],
            ),
        ],
    )
    chemin = Path(".").resolve() / "backup_sncf.json"
    chemin.write_text(csncf.model_dump_json())


if __name__ == "__main__":
    main()
