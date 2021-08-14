from generator.cpp_with_python.code import Code
from generator.cpp_with_python.comment import *
import unittest

class TestComment(unittest.TestCase):
    def test_one_line_comment(self):
        code = Code("")
        oneLineComment("comm", code)
        self.assertEqual(code.code, "\n/* comm */")
