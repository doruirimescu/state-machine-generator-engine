from generator.cpp_with_python.code import Code
from dataclasses import dataclass


@dataclass()
class Type:
    """Represent types such as int, classes, int*, etc
    """
    name: str
    label: str

    def declare(self, code: Code):
        code.appendNewLineWithTabs()
        code.code += self.name + " " + self.label + ";"

    def assign(self, value: str, code: Code):
        code.appendNewLineWithTabs()
        code.code += self.label + " = " + value + ";"

    def asParameter(self):
        return self.name + " " + self.label
