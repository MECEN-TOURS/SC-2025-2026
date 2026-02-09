"""Description.

Résolution du problème d'ordonnancement encodé grâce à data.py
"""

from data import CahierDesCharges, Planning, TachePlanifiee
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


def resoud_ordonnancement(cahier: CahierDesCharges, debut: float) -> Planning:
    """Résolution du problème d'ordonnancement."""
    graphe = construit_graphe(cahier=cahier)
    details = list()
    if not nx.algorithms.is_directed_acyclic_graph(graphe):
        raise ValueError("Le cahier des charges n'a pas de solution!")
    for tache in nx.algorithms.topological_sort(graphe):
        fin_prerequis = [
            tache_planifiee.fin
            for tache_planifiee in details
            if tache_planifiee.tache.nom in tache.prerequis
        ]
        debut_tache = max(fin_prerequis) if fin_prerequis else debut
        details.append(
            TachePlanifiee(
                tache=tache, debut=debut_tache, fin=debut_tache + tache.duree
            )
        )
    return Planning(cahier_des_charges=cahier, details=details)
