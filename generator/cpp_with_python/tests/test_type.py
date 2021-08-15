from typing import Type
from generator.cpp_with_python.code import Code
from generator.cpp_with_python.type import Type
import unittest

class TestType(unittest.TestCase):
    def test_type(self):
        code = Code("")
        my_int = Type("int", "a")
        my_int.declare(code)
        self.assertEqual(code.code, "\nint a;")
