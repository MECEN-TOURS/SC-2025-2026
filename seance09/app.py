import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from data import ConnexionsSNCF, Itineraire
    from resolution import construit_graphe, resoud
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Exercice

    Utiliser les éléments d'ui ci-dessous et les fonctions de la bibliothèque pour créer une application permettant de trouver l'itinéraire le plus court entre deux gares.
    """)
    return


@app.cell
def _(mo):
    fichier = mo.ui.file()
    fichier
    return


@app.cell
def _(mo):
    menu1 = mo.ui.dropdown(options=["a", "b", "c"], value="a")
    menu1
    return (menu1,)


@app.cell
def _(menu1):
    print(menu1.value)
    return


@app.cell
def _(mo):
    bouton = mo.ui.button(on_click=lambda _: print("cliqué"), label="Cliquez moi")
    bouton
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
