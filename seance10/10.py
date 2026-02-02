import marimo

__generated_with = "0.19.6"
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
    # Séance 10

    Exploration de `nx.algorithms.flow`.
    """)
    return


@app.cell
def _(nx):
    G = nx.DiGraph()
    return (G,)


@app.cell
def _(G):
    G.add_edge("P", "V1", capacite=10)
    G.add_edge("P", "B4", capacite=2)
    G.add_edge("V1", "B1", capacite=2)
    G.add_edge("V1", "B2", capacite=2)
    G.add_edge("V1", "B3", capacite=2)
    G.add_edge("B1", "B2", capacite=1)
    G.add_edge("B3", "B2", capacite=1)
    G.add_edge("B2", "C", capacite=3)
    G.add_edge("B4", "C", capacite=3)
    return


@app.cell
def _(G, nx, plt):
    _fig, _rep = plt.subplots()

    positions = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos=positions)
    nx.draw_networkx_edges(G, pos=positions)
    nx.draw_networkx_labels(G, pos=positions)
    nx.draw_networkx_edge_labels(
        G,
        pos=positions,
        edge_labels={
            (depart, arrivee): capacite
            for (depart, arrivee, capacite) in G.edges(data="capacite")
        },
    )
    _rep
    return


@app.cell
def _(mo):
    mo.md(r"""
    **DESCRIPTION**

    - les poids des arrêtes représente le débit maximal d'eau connectant deux locations
    - le sommet $P$ est un puit
    - le commet $C$ est un champs

    Le problème consiste à déterminer le débit effectif sur chaque arrête de façon à

    - respecter le débit maximal
    - faire que les sommets internes (hors $P$ et $C$) ait autant d'eau en entrée qu'en sortie
    - le maximum d'eau arrive au sommet $C$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Exercice

    Explorer la documentation de `nx.algorithms.flow` et résoudre le problème.
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
