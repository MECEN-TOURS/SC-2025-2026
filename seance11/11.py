import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import networkx as nx
    import matplotlib.pyplot as plt
    import polars as pl
    return mo, pl


@app.cell
def _(mo):
    mo.md(r"""
    # Séance 11

    Problèmes d'ordonnancement.
    """)
    return


@app.cell(hide_code=True)
def _(pl):
    taches = pl.DataFrame(
        data=dict(
            tache=list("ABCDEFGHI"),
            duree=[1, 2, 1, 3, 4, 5, 2, 1, 3],
            prerequis=[
                list("DE"),
                list(),
                list("AB"),
                list("EF"),
                [],
                ["I"],
                ["A"],
                ["C"],
                ["A"],
            ],
        )
    )
    taches
    return


@app.cell
def _(mo):
    mo.md(r"""
    **Objectif**: construire un planning des tâches
    1. le plus rapide possible
    2. tel qu'une tâche commence seulement après que ses prérequis soit finis
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
