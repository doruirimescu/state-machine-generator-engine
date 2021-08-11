#!/usr/bin/python3
from blueprint import Blueprint
from generator.generator import Generator
from generator.oop.state_header_generator import StateHeaderGenerator
from generator.oop.state_cpp_generator import statecpp
from generator.oop.state_machine_header_generator import machineheader
from generator.oop.state_machine_cpp_generator import machinecpp

class OOPGenerator(Generator):
    def generate(self, blueprint: Blueprint):
        stateHeaderGenerator = StateHeaderGenerator()
        stateHeaderGenerator.generate(blueprint)

        statecpp(blueprint.actions, blueprint.reverseActions)
        machineheader(blueprint.actions, blueprint.stateList)
        machinecpp(blueprint.actions, blueprint.stateList)
