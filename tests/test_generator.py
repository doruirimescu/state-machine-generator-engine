from generator.generator import Generator
import unittest
from blueprint import blueprint
from generator.procedural.procedural_generator import ProceduralGenerator
from generator.oop.oop_generator import OOPGenerator


class TestProceduralGenerator(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        proceduralGenerator = ProceduralGenerator()
        proceduralGenerator.generate(blueprint)

        oopGenerator = OOPGenerator()
        oopGenerator.generate(blueprint)

    def compareFiles(self, filepath_1, filepath_2):
        f = open(filepath_1, "r+")
        data_1 = f.read()
        f.close()

        f = open(filepath_2, "r+")
        data_2 = f.read()
        f.close()

        self.assertEqual(data_1, data_2)

    def test_ProceduralGeneratorHeader(self):
        test_path = "tests/test_files/procedural/header.h"
        generated_path = "generated/procedural/header.h"
        self.compareFiles(test_path, generated_path)

    def test_ProceduralGeneratorSource(self):
        test_path = "tests/test_files/procedural/source.cpp"
        generated_path = "generated/procedural/source.cpp"
        self.compareFiles(test_path, generated_path)

    def test_OopGeneratorStateHeader(self):
        test_path = "tests/test_files/oop/include/state.h"
        generated_path = "generated/oop/include/state.h"
        self.compareFiles(test_path, generated_path)

    def test_OopGeneratorStateSource(self):
        test_path = "tests/test_files/oop/src/state.cpp"
        generated_path = "generated/oop/src/state.cpp"
        self.compareFiles(test_path, generated_path)

    def test_OopGeneratorStateMachineHeader(self):
        test_path = "tests/test_files/oop/include/state_machine.h"
        generated_path = "generated/oop/include/state_machine.h"
        self.compareFiles(test_path, generated_path)

    def test_OopGeneratorStateMachineSource(self):
        test_path = "tests/test_files/oop/src/state_machine.cpp"
        generated_path = "generated/oop/src/state_machine.cpp"
        self.compareFiles(test_path, generated_path)
