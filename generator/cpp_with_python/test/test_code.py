from generator.cpp_with_python.code import Code
import unittest

class TestCode(unittest.TestCase):
    def test_code(self):
        code = Code("")
        self.assertEqual(code.code, "")
        code.code = "one_line"
        self.assertEqual(code.code, "one_line")
        code.appendNewLineWithTabs()
        code.code += "two line"
        self.assertEqual(code.code, "one_line\ntwo line")
        code.tabs += 1
        code.appendNewLineWithTabs()
        code.code += "three line"
        self.assertEqual(code.code, "one_line\ntwo line\n\tthree line")
