"""Description.

Module pour décrire un problème d'ordonnancement.
"""

from typing_extensions import Self
from pydantic import BaseModel, PositiveFloat, model_validator


class Tache(BaseModel):
    nom: str
    duree: PositiveFloat
    prerequis: list[str]

    @model_validator(mode="after")
    def verifie_prerequis(self) -> Self:
        """Vérifie que la tâche n'est pas son propre prérequis"""
        for prerequis in self.prerequis:
            if self.nom == prerequis:
                msg = "La tâche ne peut être son propre prérequis"
                raise ValueError(msg)
        return self


class CahierDesCharges(BaseModel):
    taches: list[Tache]

    @model_validator(mode="after")
    def verifie_noms(self) -> Self:
        """Vérifie que les tâches ont des noms distincts"""
        ...
        return self

    @model_validator(mode="after")
    def verifie_prerequis(self) -> Self:
        """Vérifie que les prérequis sont bien des tâches du cahier des charges"""
        ...
        return self
