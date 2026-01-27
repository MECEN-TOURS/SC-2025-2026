"""Description.


Résolution du chemin le plus court entre deux gares connaissant un objet ConnexionsSNCF valide.
"""

from data import Itineraire, ConnexionsSNCF


def resoud(
    connexions: ConnexionsSNCF, depart: str, arrivee: str
) -> list[tuple[str, int]]: ...
