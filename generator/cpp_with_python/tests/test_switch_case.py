from generator.cpp_with_python.code import Code
from generator.cpp_with_python.switch_case import switchCase
import unittest


class TestSwitchCase(unittest.TestCase):
    def test_switch_case(self):
        code = Code("")
        switchCase("my_expression", ["label1", "label2"], ["int a = 23;", "int b = 203;"], code)

        self.assertEqual(code.code, 'switch(my_expression)\n{\n\tcase label1:\n\t\tint a = 23;\n\t\tbreak;\n\tcase label2:\n\t\tint b = 203;\n\t\tbreak;\n\tdefault:\n\t\tbreak;\n}')
