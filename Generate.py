"""Generates the state machine cpp code
"""
#!/usr/bin/python3
from Blueprint import blueprint
from StateHeaderGenerator import stateheader
from StateCppGenerator import statecpp
from StateMachineHeaderGenerator import machineheader
from StateMachineCppGenerator import machinecpp
from enum import Enum

class Modes(Enum):
    OOP = 1
    PROCEDURAL = 2

SELECTED_MODE = Modes.OOP

if SELECTED_MODE == Modes.OOP:
    stateheader(blueprint.actions)
    statecpp(blueprint.actions, blueprint.reverseActions)
    machineheader(blueprint.actions, blueprint.stateList)
    machinecpp(blueprint.actions, blueprint.stateList)
elif SELECTED_MODE == Modes.PROCEDURAL:
    #TODO
    pass
