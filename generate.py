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
path_to_generate = "generated/"
BLUEPRINT_SOURCE = BlueprintSource.FROM_DRAWIO
state_machine_blueprint = None
if BLUEPRINT_SOURCE == BlueprintSource.FROM_PYTHON:
    from blueprint import blueprint
    state_machine_blueprint = blueprint
    path_to_generate += "from_python/"
elif BLUEPRINT_SOURCE == BlueprintSource.FROM_DRAWIO:
    path_to_generate += "from_drawio/"
    from draw_io.parse_drawio import draw_io_xml_to_blueprint
    state_machine_blueprint = draw_io_xml_to_blueprint("draw_io/example_simple.xml")

print("State machine blueprint is ", state_machine_blueprint)

# Selecting generation mode
SELECTED_MODE = Modes.PROCEDURAL
if SELECTED_MODE == Modes.OOP:
    gen = OOPGenerator(path_to_generate)
    gen.generate(state_machine_blueprint)
    print("OOP generation ended")
elif SELECTED_MODE == Modes.PROCEDURAL:
    gen = ProceduralGenerator(path_to_generate)
    gen.generate(state_machine_blueprint)
    print("Procedural generation ended")
