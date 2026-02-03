"""Description.

Module pour décrire un problème d'ordonnancement.
"""

from pydantic import BaseModel, PositiveFloat, model_validator


class Tache(BaseModel):
    nom: str
    duree: PositiveFloat
    prerequis: list[str]


class CahierDesCharges(BaseModel):
    taches: list[Tache]

    # @model_validator
    # def verifie_noms(self):
    #     """Vérifie que les tâches ont des noms distincts"""
    #     ...
    #
    # @model_validator
    # def verifie_prerequis(self):
    #     """Vérifie que les prérequis sont bien des tâches du cahier des charges"""
    #     ...
