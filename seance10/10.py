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

    positions = nx.planar_layout(G)

    nx.draw_networkx_nodes(G, pos=positions, ax=_rep)
    nx.draw_networkx_edges(G, pos=positions, ax=_rep)
    nx.draw_networkx_labels(G, pos=positions, ax=_rep)
    nx.draw_networkx_edge_labels(
        G,
        pos=positions,
        edge_labels={
            (depart, arrivee): capacite
            for (depart, arrivee, capacite) in G.edges(data="capacite")
        },
        ax=_rep,
    )
    _rep
    return (positions,)


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
def _(G, nx):
    valeur_max, solution = nx.algorithms.flow.maximum_flow(
        flowG=G,
        _s="P",
        _t="C",
        capacity="capacite",
    )
    solution
    return (solution,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Exercice

    Visualiser cette solution sur le graphe
    """)
    return


@app.cell
def _(G, nx, plt, positions, solution):
    _fig, _rep = plt.subplots()

    nx.draw_networkx_nodes(G, pos=positions, ax=_rep)
    nx.draw_networkx_edges(G, pos=positions, ax=_rep)
    nx.draw_networkx_labels(G, pos=positions, ax=_rep)
    nx.draw_networkx_edge_labels(
        G,
        pos=positions,
        label_pos=0.33,
        edge_labels={
            (debut, arrivee): solution[debut][arrivee] for (debut, arrivee) in G.edges
        },
        ax=_rep,
        font_color="green",
    )
    nx.draw_networkx_edge_labels(
        G,
        pos=positions,
        label_pos=0.66,
        edge_labels={
            (depart, arrivee): capacite
            for (depart, arrivee, capacite) in G.edges(data="capacite")
        },
        ax=_rep,
    )
    _rep
    return


@app.cell
def _(G, nx, plt, positions, solution):
    _fig, _rep = plt.subplots()

    nx.draw_networkx_nodes(G, pos=positions, ax=_rep)
    nx.draw_networkx_edges(G, pos=positions, ax=_rep)
    nx.draw_networkx_labels(G, pos=positions, ax=_rep)
    nx.draw_networkx_edge_labels(
        G,
        pos=positions,
        verticalalignment="bottom",
        edge_labels={
            (debut, arrivee): solution[debut][arrivee] for (debut, arrivee) in G.edges
        },
        ax=_rep,
        font_color="green",
    )
    nx.draw_networkx_edge_labels(
        G,
        pos=positions,
        verticalalignment="top",
        edge_labels={
            (depart, arrivee): capacite
            for (depart, arrivee, capacite) in G.edges(data="capacite")
        },
        ax=_rep,
    )
    _rep
    return


@app.cell
def _(G, nx, plt, positions, solution):
    _fig, _rep = plt.subplots()

    nx.draw_networkx_nodes(G, pos=positions, ax=_rep)
    nx.draw_networkx_edges(G, pos=positions, ax=_rep)
    nx.draw_networkx_labels(G, pos=positions, ax=_rep)
    nx.draw_networkx_edge_labels(
        G,
        pos=positions,
        verticalalignment="top",
        edge_labels={
            (depart, arrivee): f"{solution[depart][arrivee]} : {capacite}"
            for (depart, arrivee, capacite) in G.edges(data="capacite")
        },
        ax=_rep,
    )
    _rep
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Exercice

    On a le budget pour effectuer des travaux afin d'augmenter la capacité maximale d'UNE arrête de 5.

    Laquelle faut-il choisir?

    On réfléchira à
    - une approche proposant une exploration interactive
    - une approche calculatoire
    """)
    return


@app.cell
def _(G, nx):
    resultat = dict()
    for depart, fin in G.edges:
        ancienne_capacite = G[depart][fin]["capacite"]
        G[depart][fin]["capacite"] = ancienne_capacite + 5
        val_max = nx.algorithms.flow.maximum_flow_value(
            flowG=G,
            _s="P",
            _t="C",
            capacity="capacite",
        )
        resultat[(depart, fin)] = val_max
        G[depart][fin]["capacite"] = ancienne_capacite
    return (resultat,)


@app.cell
def _(resultat):
    resultat
    return


@app.cell
def _(mo):
    mo.md(r"""
    On constate que l'on peut soit
    - augmenter $P \to B_4$
    - augmenter $B_2 \to C$

    On note au passage, qu'une augmentation de $1$ unité de débit maximal d'une de ces connexions permet déjà d'obtenir le flot maximal.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Exercice

    Utiliser des outils de type dashboard pour explorer le même problème.
    """)
    return


@app.cell
def _(G, mo):
    selecteur_arrete = mo.ui.dropdown(options=list(G.edges))
    return (selecteur_arrete,)


@app.cell
def _(selecteur_arrete):
    selecteur_arrete
    return


@app.cell
def _(G, nx, plt, positions, selecteur_arrete, solution):
    _fig, _rep = plt.subplots()
    if selecteur_arrete.value is not None:
        _debut, _fin = selecteur_arrete.value
        backup = G[_debut][_fin]["capacite"]
        G[_debut][_fin]["capacite"] = backup + 5
        _sol, _val = nx.algorithms.flow.maximum_flow(
            flowG=G,
            _s="P",
            _t="C",
            capacity="capacite",
        )

        nx.draw_networkx_nodes(G, pos=positions, ax=_rep)
        nx.draw_networkx_edges(
            G,
            pos=positions,
            ax=_rep,
            edge_color=["red" if _arrete == (_debut, _fin) else "black" for _arrete in G.edges],
        )
        nx.draw_networkx_labels(G, pos=positions, ax=_rep)
        nx.draw_networkx_edge_labels(
            G,
            pos=positions,
            verticalalignment="top",
            edge_labels={
                (depart, arrivee): f"{solution[depart][arrivee]} : {capacite}"
                for (depart, arrivee, capacite) in G.edges(data="capacite")
            },
            ax=_rep,
        )

        G[_debut][_fin]["capacite"] = backup

    _rep
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Exercice

    Explorer les différents algorithmes de placement des sommets du graphe (i.e. `layout`)
    """)
    return


@app.cell
def _(G, nx, plt):
    def affichage(layout, **kwargs):
        _fig, _rep = plt.subplots()

        _positions = layout(G, **kwargs)
        _rep.set_title(layout.__name__)

        nx.draw_networkx_nodes(G, pos=_positions, ax=_rep)
        nx.draw_networkx_edges(G, pos=_positions, ax=_rep)
        nx.draw_networkx_labels(G, pos=_positions, ax=_rep)
        nx.draw_networkx_edge_labels(
            G,
            pos=_positions,
            edge_labels={
                (depart, arrivee): capacite
                for (depart, arrivee, capacite) in G.edges(data="capacite")
            },
            ax=_rep,
        )
        return _rep
    return (affichage,)


@app.cell
def _(affichage, nx):
    affichage(nx.spring_layout)
    return


@app.cell
def _(affichage, nx):
    affichage(nx.drawing.layout.arf_layout)
    return


@app.cell
def _(affichage, nx):
    affichage(nx.drawing.layout.kamada_kawai_layout)
    return


@app.cell
def _(affichage, nx):
    affichage(nx.drawing.layout.bfs_layout, start="P")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
