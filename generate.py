"""Generates the state machine cpp code
"""
#!/usr/bin/python3
from generator.oop.oop_generator import OOPGenerator
from generator.procedural.procedural_generator import ProceduralGenerator
from enum import Enum


class BlueprintSource(Enum):
    FROM_PYTHON = 1
    FROM_DRAWIO = 2


class Modes(Enum):
    OOP = 1
    PROCEDURAL = 2


# Selecting blueprint source
BLUEPRINT_SOURCE = BlueprintSource.FROM_PYTHON
state_machine_blueprint = None
if BLUEPRINT_SOURCE == BlueprintSource.FROM_PYTHON:
    from blueprint import blueprint
    state_machine_blueprint = blueprint
elif BLUEPRINT_SOURCE == BlueprintSource.FROM_DRAWIO:
    from draw_io.parse_drawio import draw_io_xml_to_blueprint
    state_machine_blueprint = draw_io_xml_to_blueprint("draw_io/example_simple.xml")

# Selecting generation mode
SELECTED_MODE = Modes.PROCEDURAL
if SELECTED_MODE == Modes.OOP:
    gen = OOPGenerator()
    gen.generate(state_machine_blueprint)
elif SELECTED_MODE == Modes.PROCEDURAL:
    gen = ProceduralGenerator()
    gen.generate(state_machine_blueprint)
