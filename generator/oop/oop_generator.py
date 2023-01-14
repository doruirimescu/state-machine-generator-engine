#!/usr/bin/python3
from blueprint import Blueprint
from generator.generator import Generator
from generator.oop.state_header_generator import StateHeaderGenerator
from generator.oop.state_cpp_generator import StateCppGenerator
from generator.oop.state_machine_header_generator import StateMachineHeaderGenerator
from generator.oop.state_machine_cpp_generator import StateMachineCppGenerator


class OOPGenerator(Generator):
    def __init__(self, path_to_generate) -> None:
        super().__init__(path_to_generate)

    def generate(self, blueprint: Blueprint):
        stateHeaderGenerator = StateHeaderGenerator(self.path_to_generate)
        stateHeaderGenerator.generate(blueprint)

        stateCppGenerator = StateCppGenerator(self.path_to_generate)
        stateCppGenerator.generate(blueprint)

        machineheaderGenerator = StateMachineHeaderGenerator(self.path_to_generate)
        machineheaderGenerator.generate(blueprint)

        machinecppGenerator = StateMachineCppGenerator(self.path_to_generate)
        machinecppGenerator.generate(blueprint)
