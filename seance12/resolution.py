"""Description.

Résolution du problème d'ordonnancement encodé grâce à data.py
"""

from data import CahierDesCharges, Planning
import networkx as nx


def construit_graphe(cahier: CahierDesCharges) -> nx.DiGraph:
    resultat = nx.DiGraph()
    for tache in cahier.taches:
        for prerequis in tache.prerequis:
            resultat.add_edge(
                prerequis,
                tache.nom,
                duree=cahier[prerequis].duree,
            )
    return resultat


def a_une_solution(cahier: CahierDesCharges) -> bool:
    """Détecte la présence de cycles."""
    graphe = construit_graphe(cahier=cahier)
    return nx.algorithms.is_directed_acyclic_graph(graphe)


def resoud(cahier: CahierDesCharges) -> Planning:
    """Résolution du problème d'ordonnancement."""
    ...
