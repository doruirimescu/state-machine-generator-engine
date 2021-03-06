"""Generates the state machine cpp code
"""
#!/usr/bin/python3
from blueprint import blueprint
from generator.oop.oop_generator import OOPGenerator
from generator.procedural.procedural_generator import ProceduralGenerator
from enum import Enum

class Modes(Enum):
    OOP = 1
    PROCEDURAL = 2

SELECTED_MODE = Modes.OOP

if SELECTED_MODE == Modes.OOP:
    gen = OOPGenerator()
    gen.generate(blueprint)
elif SELECTED_MODE == Modes.PROCEDURAL:
    gen = ProceduralGenerator()
    gen.generate(blueprint)
