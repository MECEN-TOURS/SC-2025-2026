#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "rich",
# ]
# ///

# -*- coding: utf-8 -*-
"""Description.

Script effectuant la répartition des sujets au élèves.
"""

import random as rd
from rich.console import Console

GROUPES = (
    ("Aaron", "Adrien", "Dorian"),
    ("Sacha", "Florian"),
    ("Hugo", "Vikrant"),
    ("Kenny", "Fatou"),
    ("Caba", "Grace"),
    ("Bastien", "William"),
    ("Kubra", "Matteo"),
    ("Mario", "Fawase"),
    ("Pierre", "Stelina"),
)

SUJETS = [f"{numero:02}" for numero in range(1, 12)]
rd.seed(2025)
rd.shuffle(SUJETS)

CS = Console()

AFFECTATION = {eleves: sujet for eleves, sujet in zip(GROUPES, SUJETS)}
CS.print(AFFECTATION)
