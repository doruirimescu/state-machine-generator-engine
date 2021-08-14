from generator.cpp_with_python.code import Code
from generator.cpp_with_python.preprocessor import *
import unittest

class TestPreprocessor(unittest.TestCase):
    def test_local_header(self):
        code = Code("")
        includeLocalHeader("header", code)
        self.assertEqual(code.code, "\n#include \"header\"")

    def test_global_header(self):
        code = Code("")
        includeGlobalHeader("header", code)
        self.assertEqual(code.code, "\n#include <header>")

    def test_pragma_once(self):
        code = Code("")
        pragmaOnce(code)
        self.assertEqual(code.code, "\n#pragma once")

    def test_using_namespace(self):
        code = Code("")
        usingNamespace("std", code)
        self.assertEqual(code.code, "\nusing namespace std;")
