from generator.cpp_with_python.code import Code
from generator.cpp_with_python.comment import *
import unittest

class TestComment(unittest.TestCase):
    def test_one_line_comment(self):
        code = Code("")
        oneLineComment("comm", code)
        self.assertEqual(code.code, "\n/* comm */")

    def test_BriefClass(self):
        code = Code("")
        b = Brief("This function does smth", ["bool a: True if a, False if not a"], "int val: The calculated value")
        b.generate(code)
        self.assertEqual(code.code, '''\n/**
 * @brief This function does smth
 * @param bool a: True if a, False if not a
 * @return int val: The calculated value
 */''')
