"""Description.

Résolution du problème d'ordonnancement encodé grâce à data.py
"""

from data import CahierDesCharges
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
