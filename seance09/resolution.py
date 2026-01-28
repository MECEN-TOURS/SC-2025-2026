"""Description.


Résolution du chemin le plus court entre deux gares connaissant un objet ConnexionsSNCF valide.
"""

import networkx as nx
from data import Itineraire, ConnexionsSNCF


def construit_graphe(connexions: ConnexionsSNCF) -> nx.DiGraph:
    resultat = nx.DiGraph()
    for itineraire in connexions.itineraires:
        debut = itineraire.gare_depart
        instant_debut = 0
        for fin, instant_fin in itineraire.escales:
            resultat.add_edge(debut, fin, duree=instant_fin - instant_debut)
            debut = fin
            instant_debut = instant_fin

        fin = itineraire.gare_arrivee
        instant_fin = itineraire.duree
        resultat.add_edge(debut, fin, duree=instant_fin - instant_debut)

    return resultat


def resoud(
    connexions: ConnexionsSNCF, depart: str, arrivee: str
) -> list[tuple[str, int]]:
    graphe = construit_graphe(connexions=connexions)
    chemin = nx.shortest_path(G=graphe, source=depart, target=arrivee, weight="duree")
    resultat = []
    resultat.append((depart, 0))
    for gauche, droite in zip(chemin[:-1], chemin[1:]):
        resultat.append((droite, resultat[-1][1] + graphe[gauche][droite]["duree"]))
    return resultat
