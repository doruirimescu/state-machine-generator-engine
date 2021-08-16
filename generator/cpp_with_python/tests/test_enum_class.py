from generator.cpp_with_python.code import Code
from generator.cpp_with_python.enum_class import EnumClass
import unittest


class TestEnumClass(unittest.TestCase):
    def test_enum_class_define(self):
        code = Code("")
        ec = EnumClass("StateLabel", "current_state", ["ACTION_UP", "ACTION_DOWN"])
        ec.define(code)
        self.assertEqual(code.code, '\nenum class StateLabel\n{\n\tACTION_UP,\n\tACTION_DOWN\n};')

    def test_enum_class_declare(self):
        code = Code("")
        ec = EnumClass("StateLabel", "current_state", ["ACTION_UP", "ACTION_DOWN"])
        ec.declare(code)
        self.assertEqual(code.code, '\nStateLabel current_state;')


    def test_enum_class_assign(self):
        code = Code("")
        ec = EnumClass("StateLabel", "current_state", ["ACTION_UP", "ACTION_DOWN"])

        with self.assertRaises(ValueError) as cm:
            ec.assign("ACTION_UPasd", code)
        ec.assign("ACTION_UP", code)
        self.assertEqual(code.code, '\ncurrent_state = StateLabel::ACTION_UP;')
