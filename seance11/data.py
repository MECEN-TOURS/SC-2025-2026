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
        noms = set()
        for tache in self.taches:
            if tache.nom in noms:
                msg = "Les tâches doivent avoir des noms distincts"
                raise ValueError(msg)
            noms.add(tache.nom)
        return self

    @model_validator(mode="after")
    def verifie_prerequis(self) -> Self:
        """Vérifie que les prérequis sont bien des tâches du cahier des charges"""
        noms_valides = {tache.nom for tache in self.taches}
        for tache in self.taches:
            for prerequis in tache.prerequis:
                if prerequis not in noms_valides:
                    msg = "Les prérequis doivent être des tâches valides"
                    raise ValueError(msg)
        return self
