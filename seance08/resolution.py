"""Description.


Résolution du chemin le plus court entre deux gares connaissant un objet ConnexionsSNCF valide.
"""

import networkx as nx
from data import Itineraire, ConnexionsSNCF


def construit_graphe(connexions: ConnexionsSNCF) -> nx.DiGraph: ...


def resoud(
    connexions: ConnexionsSNCF, depart: str, arrivee: str
) -> list[tuple[str, int]]: ...
