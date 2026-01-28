import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from data import ConnexionsSNCF, Itineraire
    from resolution import construit_graphe, resoud
    return ConnexionsSNCF, construit_graphe, mo, resoud


@app.cell
def _(mo):
    fichier = mo.ui.file()
    fichier
    return (fichier,)


@app.cell
def _(ConnexionsSNCF, construit_graphe, fichier):
    contenu_fichier = fichier.value[0].contents.decode("utf8")
    sncf = ConnexionsSNCF.model_validate_json(contenu_fichier)
    graphe = construit_graphe(sncf)
    gares = list(graphe.nodes)                                         
    return gares, sncf


@app.cell
def _(gares, mo):
    gare_depart = mo.ui.dropdown(options=gares)
    return (gare_depart,)


@app.cell
def _(gares, mo):
    gare_arrivee = mo.ui.dropdown(options=gares)
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
        label="Calcule Trajet"
    )

    return (bouton,)


@app.cell
def _(bouton):
    bouton
    return


@app.cell
def _(bouton):
    bouton.value
    return


@app.cell
def _(mo):
    mo.md(r"""
    **EXERCICE** Reprenez la visualisation du résultat pour avoir un affichage plus lisible
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
