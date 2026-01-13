import marimo

__generated_with = "0.19.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Prblème de traversée de rivière
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    D'un côté d'une rivière se tiennent

    - un berger
    - un loup
    - un mouton
    - un choux

    ils doivent traverser la rivière mais

    - seul le berger sait ramer
    - la barque possède deux places seulement
    - on ne peut laisser le loup et le mouton sans la surveillance du berger
    - on ne peut laisser le mouton et le chou sans la surveillance du berger

    Comment organise-t-on les traversées?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Modélisation


    Un état du système consiste à associer à chaque personnage le côté de la rivière où il se trouve.

    Un état valide est un état qui respecte les contraintes loup/mouton, mouton/choux.

    Une arrête est un couple de deux états tel qu'on peut passer du premier au deuxième en une seule traversée de rivière.
    """)
    return


@app.cell
def _():
    from enum import Enum
    from dataclasses import dataclass
    return Enum, dataclass


@app.cell
def _(Enum):
    class Rive(Enum):
        GAUCHE = 'gauche'
        DROITE = 'droite'
    return (Rive,)


@app.cell
def _(Rive):
    Rive.GAUCHE
    return


@app.cell
def _(Rive):
    Rive.DROITE
    return


@app.cell
def _(Rive, dataclass):
    @dataclass
    class Etat:
        berger: Rive
        loup: Rive
        mouton: Rive 
        choux: Rive
    return (Etat,)


@app.cell
def _(Etat, Rive):
    DEPART = Etat(berger=Rive.GAUCHE, loup=Rive.GAUCHE, mouton=Rive.GAUCHE, choux=Rive.DROITE)
    DEPART
    return


@app.cell
def _(Etat):
    def est_valide(etat: Etat) -> bool:
        if etat.loup == etat.mouton and etat.berger != etat.loup:
            return False
        if etat.mouton == etat.choux and etat.berger != etat.mouton:
            return False
        return True
    return


@app.cell
def _(mo):
    mo.md(r"""
    **EXERCICE.**

    1. Construire la liste de tous les états.
    2. Construire la liste de tous les états valides.
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
