"""Description.

Librairie pour résoudre le problème d'itinéraire SNCF.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Itineraire:
    gare_depart: str
    gare_arrivee: str
    duree: int
    escales: list[tuple[str, int]]

    def __post_init__(self):
        instant_precedent = 0
        for _, instant_courant in self.escales:
            if instant_courant < instant_precedent:
                raise ValueError("Durées d'escales invalides")
            instant_precedent = instant_courant
        if self.duree < instant_precedent:
            raise ValueError("la duree de trajet doit être positive")

    def __str__(self) -> str:
        lignes = [
            f"depart: {self.gare_depart}",
            f"arrivee: {self.gare_arrivee}",
            f"duree: {self.duree}h",
        ]
        return "\n".join(lignes)


@dataclass(frozen=True)
class ConnexionsSNCF:
    itineraires: list[Itineraire]
    date: datetime
