"""Description.

Librairie pour résoudre le problème d'itinéraire SNCF.
"""

from pydantic import BaseModel, PositiveInt, model_validator
from datetime import datetime


class Itineraire(BaseModel):
    gare_depart: str
    gare_arrivee: str
    duree: PositiveInt
    escales: list[tuple[str, PositiveInt]]

    @model_validator(mode="after")
    def verifie_ordre_etape(self) -> "Itineraire":
        instant_precedent = 0
        for _, instant_courant in self.escales:
            if instant_courant < instant_precedent:
                raise ValueError("Durées d'escales invalides")
            instant_precedent = instant_courant
        if self.duree < instant_precedent:
            raise ValueError("la duree de trajet doit être positive")
        return self

    def __str__(self) -> str:
        lignes = [
            f"depart: {self.gare_depart}",
            f"arrivee: {self.gare_arrivee}",
            f"duree: {self.duree}h",
        ]
        for gare, duree in self.escales:
            lignes.append(f"escale: ({gare}, {duree})")
        return "\n".join(lignes)


class ConnexionsSNCF(BaseModel):
    itineraires: list[Itineraire]
    date: datetime
