import unittest
from generator.utils import *

class TestUtils(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def testincludeLocalHeader(self):
        code = "#pragma once"
        self.assertEqual(includeLocalHeader("library", code), "#pragma once\n#include \"library\"")

    def includeGlobalHeader(self):
        code = "int main"
        self.assertEqual(includeGlobalHeader("library", code), "int main\n#include \"library\"")

    def oneLineComment(self):
        code = "#pragma once"
        self.assertEqual(oneLineComment("commet comet", code), "#pragma once\n/* commet comet */")
