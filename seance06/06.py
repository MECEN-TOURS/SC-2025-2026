# /// script
# dependencies = [
#     "marimo",
#     "matplotlib==3.10.8",
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
        G, 
        pos=positions,
        edge_labels={arr: arr[2] for arr in G.edges(data="poids")}, 
        ax=_rep
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
def _():
    return


if __name__ == "__main__":
    app.run()
