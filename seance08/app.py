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
    fichier = mo.ui.file()
    fichier
    return


@app.cell
def _(mo):
    bouton = mo.ui.button(
        on_click=lambda _: print("cliqué"), 
    label="Cliquez moi"
    )
    bouton
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
