from generator.cpp_with_python.code import Code
from generator.cpp_with_python.comment import *
import unittest

class TestComment(unittest.TestCase):
    def test_one_line_comment(self):
        code = Code("")
        oneLineComment("comm", code)
        self.assertEqual(code.code, "\n/* comm */")

    def test_brief(self):
        code = Code("")
        generateBrief(code, "this is brief", ["bool smth: true if some, false otherwise"], ["int returns: return good stuff"])
        self.assertEqual(code.code,'''\n/**
 * @brief this is brief
 * @param bool smth: true if some, false otherwise
 * @return int returns: return good stuff
 */''')
