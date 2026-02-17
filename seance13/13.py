# /// script
# dependencies = [
#     "marimo",
#     "scipy==1.17.0",
# ]
# ///

import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Séance 13

    Retour sur la programmation linéaire
    """)
    return


@app.cell
def _():
    from scipy import optimize
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Formulation abstraite

    Il s'agit de résoudre un problème de type

    $$
    \begin{cases}
    \underset{x\in \mathbb{R}^d}{\min}\ a^\top x\\
    B x \leq b\\
    C x = c
    \end{cases}
    $$

    où $a \in \mathbb{R}^n$, $b\in \mathbb{R}^{d_i}$, $c\in \mathbb{R}^{d_e}$,
    $B\in \mathcal{M}_{d_i, n}(\mathbb{R})$ et $C\in \mathcal{M}_{d_e, n}(\mathbb{R})$.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Exercice

    On a deux entrepots avec des quantités de produit $q_1$ $q_2$ et trois clients avec des demandes $d_1$, $d_2$ et $d_3$.

    On le cout pour transporter une quantité unitaire de produit de l'entrepot $i$ au client $j$ est $C_{i,j}$.

    Comment faut-il organiser le transport?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    **Modélisation**

    - Inconnues $x_{i,j}$ quantité de produit transportée de l'entrepot $i$ vers le client $j$.
    - Le cout total de transport (qu'on veut donc  minimiser) est

    $$
    C_{1, 1} x_{1, 1} + C_{2, 1} x_{2, 1} + C_{1, 2} x_{1, 2} + C_{2, 2} x_{2, 2} +  C_{1, 3} x_{1, 3} +  C_{2, 3} x_{2, 3}
    $$
    - On ne peut transporter que des quantités positives

    $$ x_{i,j} \geq 0$$
    - On ne peut prendre plus que ce qui est présent dans chaque entrepot

    $$
    \begin{cases}
    x_{1, 1} + x_{1, 2} + x_{1, 3} \leq q_1\\
    x_{2, 1} + x_{2, 2} + x_{2, 3} \leq q_2
    \end{cases}
    $$

    - Chaque client doit être livré exactement la quantité qu'il a commandé

    $$
    \begin{cases}
    x_{1, 1} + x_{2, 1} =d_1\\
    x_{1, 2} + x_{2, 2} =d_2\\
    x_{1, 3} + x_{2, 3} =d_3
    \end{cases}
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Exercice

    Résoudre ce problème linéaire avec `linprog`.
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
