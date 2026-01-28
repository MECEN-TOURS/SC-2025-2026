import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    from datetime import datetime
    from pydantic import ValidationError
    from data import ConnexionsSNCF, Itineraire
    from resolution import construit_graphe, resoud
    return (
        ConnexionsSNCF,
        Itineraire,
        ValidationError,
        construit_graphe,
        datetime,
        mo,
        pl,
        resoud,
    )


@app.cell
def _(mo):
    fichier = mo.ui.file()
    mo.md(f"fichier contenant les connexions SNCF utilisables {fichier}")
    return (fichier,)


@app.cell
def _(
    ConnexionsSNCF,
    Itineraire,
    ValidationError,
    construit_graphe,
    datetime,
    fichier,
):
    try:
        contenu_fichier = fichier.value[0].contents.decode("utf8")
    except IndexError:
        contenu_fichier = ""
    try:
        sncf = ConnexionsSNCF.model_validate_json(contenu_fichier)
    except ValidationError:
        sncf = ConnexionsSNCF(
            date=datetime.now(),
            itineraires=[
                Itineraire(gare_depart="Tours", gare_arrivee="Tours", duree=1, escales=[])
            ],
        )
    graphe = construit_graphe(sncf)
    gares = list(graphe.nodes)
    gares.sort()
    return gares, sncf


@app.cell
def _(gares, mo):
    gare_depart = mo.ui.dropdown(options=gares, value=gares[0])
    return (gare_depart,)


@app.cell
def _(gares, mo):
    gare_arrivee = mo.ui.dropdown(options=gares, value=gares[0])
    return (gare_arrivee,)


@app.cell
def _(gare_arrivee, gare_depart, mo):
    mo.md(f"""
    gare de départ: {gare_depart}

    gare d'arrivée: {gare_arrivee}
    """)
    return


@app.cell
def _(gare_arrivee, gare_depart, mo, resoud, sncf):
    bouton = mo.ui.button(
        on_click=lambda value: resoud(
            connexions=sncf,
            depart=gare_depart.value,
            arrivee=gare_arrivee.value,
        ),
        value=[],
        label="Calcule Trajet",
    )
    return (bouton,)


@app.cell
def _(bouton):
    bouton
    return


@app.cell
def _(bouton, pl):
    trajet = pl.DataFrame(
        data={
            "Gare": [gare for gare, _ in bouton.value],
            "Instant de passage": [instant for _, instant in bouton.value],
        }
    )
    return (trajet,)


@app.cell
def _(mo, trajet):
    mo.ui.table(data=trajet)
    return


if __name__ == "__main__":
    app.run()
