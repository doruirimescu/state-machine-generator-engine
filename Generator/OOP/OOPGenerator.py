#!/usr/bin/python3
from Blueprint import Blueprint
from Generator.Generator import Generator
from Generator.OOP.StateHeaderGenerator import StateHeaderGenerator
from Generator.OOP.StateCppGenerator import statecpp
from Generator.OOP.StateMachineHeaderGenerator import machineheader
from Generator.OOP.StateMachineCppGenerator import machinecpp

class OOPGenerator(Generator):
    def generate(self, blueprint: Blueprint):
        stateHeaderGenerator = StateHeaderGenerator()
        stateHeaderGenerator.generate(blueprint)

        statecpp(blueprint.actions, blueprint.reverseActions)
        machineheader(blueprint.actions, blueprint.stateList)
        machinecpp(blueprint.actions, blueprint.stateList)
