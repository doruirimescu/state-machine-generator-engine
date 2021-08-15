from typing import Type
from generator.cpp_with_python.function import Function
from generator.cpp_with_python.comment import Brief
from generator.cpp_with_python.type import Type
from generator.cpp_with_python.code import Code
import unittest


class TestFunction(unittest.TestCase):
    def test_function_declare(self):
        b = Brief("This function calculates 2D euclidean distance", [
            "int: X coordinate", "int: Y coordinate"], "calculated euclidean distance")

        f = Function("void", "calcDistance", [Type("int", "x"), Type("int", "y")], "return sqrt(x^2 + y^2);", b)

        code = Code("")
        f.declare(code)
        self.assertEqual(code.code, '''\n/**
 * @brief This function calculates 2D euclidean distance
 * @param int: X coordinate
 * @param int: Y coordinate
 * @return calculated euclidean distance
 */
void calcDistance(int x, int y);
''')

    def test_function_define(self):

        f = Function("void", "calcDistance", [Type("int", "x"), Type("int", "y")], "return sqrt(x^2 + y^2);")

        code = Code("")
        f.define(code)
        self.assertEqual(code.code, "\nvoid calcDistance(int x, int y)\n{\n\treturn sqrt(x^2 + y^2);\n}\n")
