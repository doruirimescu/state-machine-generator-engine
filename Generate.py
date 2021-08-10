"""Generates the state machine cpp code
"""
#!/usr/bin/python3
from Blueprint import blueprint
from StateHeaderGenerator import stateheader
from StateCppGenerator import statecpp
from StateMachineHeaderGenerator import machineheader
from StateMachineCppGenerator import machinecpp


stateheader(blueprint.actions)
statecpp(blueprint.actions, blueprint.reverseActions)
machineheader(blueprint.actions, blueprint.stateList)
machinecpp(blueprint.actions, blueprint.stateList)
