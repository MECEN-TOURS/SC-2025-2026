"""Description.

Librairie pour résoudre le problème d'itinéraire SNCF.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Itineraire:
    gare_depart: str
    gare_arrivee: str
    duree: int
    escales: list[tuple[str, int]]

    def __post_init__(self):
        if self.duree < 0:
            raise ValueError("la duree de trajet doit être positive")
