from logging import BASIC_FORMAT
from generator.cpp_with_python.code import Code
from generator.cpp_with_python.type import Type
from generator.cpp_with_python.comment import *
from dataclasses import dataclass, field
from typing import List


@dataclass()
class Function:
    return_type: str
    name: str
    parameters_list: List[Type]
    body: str = ""
    brief: Brief = None
    parameters: str = field(init=False)

    def __post_init__(self):
        self.parameters = ", ".join([i.asParameter() for i in self.parameters_list])

    def declare(self, code: Code):
        if self.brief is not None:
            self.brief.generate(code)
        code.appendNewLineWithTabs()
        code.code += self.return_type + " " + self.name + "(" + self.parameters+");"

    def define(self, code: Code, class_name=None):
        code.code += "\n"
        if class_name:
            to_append = class_name + "::"
        else:
            to_append = ""

        if self.return_type is not "":
            self.return_type += " "

        code.code += "\n" + self.return_type + to_append + self.name + "(" + self.parameters+")"
        code.code += "\n{"
        code.tabs = 1
        code.appendNewLineWithTabs()
        code.tabs = 0
        code.code += self.body
        code.code += "\n}"
        code.code += "\n"

    def call(self, args: List, code: Code, object_type: Type = None):
        if len(args) != len(self.parameters_list):
            raise ValueError("Wrong number of arguments")
        code.appendNewLineWithTabs()

        if object_type is not None:
            object = object_type.label + "."
        code.code += object + self.name + "(" + ", ".join(args) + ");"


b = Brief("This function calculates 2D euclidean distance", [
          "int: X coordinate", "int: Y coordinate"], "calculated euclidean distance")
f = Function("void", "calcDistance", [Type("int", "x"), Type("int", "y")], "return sqrt(x^2 + y^2);", b)

code = Code("")
f.declare(code)
f.define(code)
print(code.code)
