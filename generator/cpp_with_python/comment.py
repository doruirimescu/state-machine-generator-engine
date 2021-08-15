from generator.cpp_with_python.code import Code
from dataclasses import dataclass
from typing import List


@dataclass()
class Brief:
    brief: str
    params_and_description_list: List[str]
    returned_description: str

    def generate(self, code: Code):
        brief_code = "\n/**\n * @brief " + self.brief

        param_code = ""
        for param in self.params_and_description_list:
            param_code += "\n * @param " + param

        returned_code = "\n * @return " + self.returned_description

        code.code += brief_code + param_code + returned_code
        code.code += "\n */"


def oneLineComment(comment_text: str, code: Code):
    code.appendNewLineWithTabs()
    code.code += "/* " + comment_text + " */"
