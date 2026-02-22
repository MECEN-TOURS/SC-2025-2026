# Affectation des sujets

## Groupes

1. Aaron, Adrien et Dorian
1. Sacha et Florian
1. Hugo et Vikrant
1. Kenny et Fatou
1. Caba et Grace
1. Bastien et William
1. Kubra et Matteo
1. Mario et Fawase
1. Pierre et Stelina

## Affectation

On exécutera `uv run affectation.py` pour obtenir la correspondance entre groupes et sujets.

## Consignes

Les sujets sont constitués d'un _exemple_ de problème.

1. On commencera évidemment par le résoudre manuellement ou avec interactivement dans un notebook.
2. Dans un second temps, il faudra **le généraliser** en une famille de problèmes.
   Il est bien entendu que plus la généralisation sera ambitieuse plus la potentielle note du projet sera élevée.
3. On codera ensuite une librairie permettant à des développeurs python de résoudre un problème de cette classe
4. On ajoutera finalement une interface permettant à des personnes n'utilisant pas python de résoudre de tels problèmes .

N'hésitez pas à me contacter pour des précisions.

## Concernant l'IA

- En python, de nombreux mécanismes existent pour rendre le code lisible et faciliter la maintenance.
  On pense nécessairement d'abord aux différentes docstrings et au bon nommage des objets.
  On utilisera bien sûr aussi la possibilité d'utiliser des modules, des classes et des fonctions.
  Les commentaires doivent dès lors être perçus comment un aveu d'échec:
  Je n'ai pas réussi à produire du code lisible, débrouiller vous avec des commentaires.
- Un autre défaut courant du code brut généré par IA est la propension à faire en 20000 lignes ce qui devrait l'être en 1000.
- La facilité de maintenance du code sera donc un critère **critique** lors de l'évaluation du projet.
  En effet, dans les projets réels le cout de maintenance dépasse largement celui de la production initiale.

## Projet complet

On devra avoir en particulier:

- Une gestion des dépendances pour garantir la portabilité entre machines.
  On conseille **fortement** d'utiliser `uv` pour ceci.
- Une librairie typée/testée/documentée.
  On utilisera entre autres `ty`, `mypy`, `pytest` (et `pytest-cov` pour la couverture).
  On suggère aussi fortement d'utiliser un linter tel que `ruff` pour détecter des bogues.
- On fera une démonstration via un fichier `README.md`.
  Par exemple, en utilisant l'interface pour résoudre le problème exemple.
  On pourra s'inspirer du projet [rich](https://github.com/Textualize/rich) pour le README.
- A minima une interface en ligne de commande (via `typer`)
- Mais éventuellement une interface graphique en utilisant les bibliothèques `marimo`, `streamlit`, `dash`...
- Finalement, le rendu consistera en un dépot github fonctionnel.
