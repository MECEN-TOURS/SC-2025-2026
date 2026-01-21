# /// script
# dependencies = [
#     "marimo",
#     "matplotlib==3.10.8",
#     "pydot==4.0.1",
# ]
# ///

import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import networkx as nx
    import matplotlib.pyplot as plt
    return mo, nx, plt


@app.cell
def _(mo):
    mo.md(r"""
    # Graphes pondérés
    """)
    return


@app.cell
def _(nx):
    G = nx.DiGraph()
    print(G)
    return (G,)


@app.cell
def _(G):
    G.add_edge("A", "C", poids=3)
    G.add_edge("C", "B", poids=6)
    G.add_edge("A", "E", poids=1)
    G.add_edge("E", "F", poids=1)
    G.add_edge("F", "G", poids=1)
    G.add_edge("G", "D", poids=1)
    G.add_edge("D", "B", poids=1)
    print(G)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Exercice

    Afficher le graphe G avec les poids des arrêtes indiqués et le nom des sommets aussi.
    """)
    return


@app.cell
def _(G, nx, plt):
    _, _rep = plt.subplots()
    nx.draw_networkx(G, ax=_rep)
    _rep
    return


@app.cell
def _(G, nx):
    positions = nx.spring_layout(G)
    return (positions,)


@app.cell
def _(G, nx, plt, positions):
    _, _rep = plt.subplots()
    nx.draw_networkx_nodes(G, pos=positions, ax=_rep)
    nx.draw_networkx_edges(G, pos=positions, ax=_rep)
    nx.draw_networkx_labels(G, pos=positions, ax=_rep)
    nx.draw_networkx_edge_labels(
        G, pos=positions, edge_labels={arr: arr[2] for arr in G.edges(data="poids")}, ax=_rep
    )
    _rep
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Exercice
    Déterminer le chemin le plus court de A à B dans le graphe

    - en fonction du nombre d'arrêtes
    - en fonction du poids total des arrêtes du chemin
    """)
    return


@app.cell
def _(G, nx):
    nx.shortest_path(G, "A")
    return


@app.cell
def _(G, nx):
    nx.shortest_path(G, "A")["B"]
    return


@app.cell
def _(G, nx):
    nx.shortest_path(G, source="A", target="B")
    return


@app.cell
def _(G, nx):
    nx.shortest_path(G, source="A", target="B", weight="poids")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Sérialisation et Désérialisation

    i.e. aller retour entre la mémoire vive du programme et le disque dur du pc.

    On trouvera aussi les mots clefs `read/write` et `input/output`.

    On consultera

    1. [cette page](https://networkx.org/documentation/stable/reference/readwrite/dot.html) pour utiliser le format `dot`
    2. [cette page](https://networkx.org/documentation/stable/reference/readwrite/json_graph.html) pour utiliser le format `json`.

    ## Exercice

    Sauvegarder le graphe dans les deux formats ci-dessus.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    **ATTENTION** pour utiliser `nx.nx_pydot` il faut installer la librairie supplémentaire `pydot`.
    """)
    return


@app.cell
def _(G, nx):
    objet_dot = nx.nx_pydot.to_pydot(G)
    print(objet_dot)
    return (objet_dot,)


@app.cell
def _(objet_dot):
    str(objet_dot)
    return


@app.cell
def _():
    # module de la librairie standard de python, pour interagir avec le système de fichiers
    from pathlib import Path
    return (Path,)


@app.cell
def _(Path, objet_dot):
    chemin = Path(".") / "sauvegarde.dot"
    chemin.write_text(str(objet_dot))
    return (chemin,)


@app.cell
def _(chemin):
    contenu_fichier = chemin.read_text()
    print(contenu_fichier)
    return


@app.cell
def _(chemin, nx):
    G2 = nx.nx_pydot.read_dot(chemin)
    return (G2,)


@app.cell
def _(G2, nx, plt, positions):
    _, _rep = plt.subplots()
    nx.draw_networkx_nodes(G2, pos=positions, ax=_rep)
    nx.draw_networkx_edges(G2, pos=positions, ax=_rep)
    nx.draw_networkx_labels(G2, pos=positions, ax=_rep)
    nx.draw_networkx_edge_labels(
        G2, pos=positions, edge_labels={arr: arr[2] for arr in G2.edges(data="poids")}, ax=_rep
    )
    _rep
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
