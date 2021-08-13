#!/usr/bin/python3
from blueprint import Blueprint
from generator.generator import Generator
from generator.oop.state_header_generator import StateHeaderGenerator
from generator.oop.state_cpp_generator import StateCppGenerator
from generator.oop.state_machine_header_generator import StateMachineHeaderGenerator
from generator.oop.state_machine_cpp_generator import StateMachineCppGenerator


class OOPGenerator(Generator):
    def generate(self, blueprint: Blueprint):
        stateHeaderGenerator = StateHeaderGenerator()
        stateHeaderGenerator.generate(blueprint)

        stateCppGenerator = StateCppGenerator()
        stateCppGenerator.generate(blueprint)

        machineheaderGenerator = StateMachineHeaderGenerator()
        machineheaderGenerator.generate(blueprint)

        machinecppGenerator = StateMachineCppGenerator()
        machinecppGenerator.generate(blueprint)
