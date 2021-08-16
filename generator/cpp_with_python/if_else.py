from generator.cpp_with_python.code import Code
from typing import List


def ifElse(conditions_list: List, code_to_execute_for_each_condition_list: List, code : Code):
    """Create if else if code

    Args:
        conditions_list (List): List of conditions. Make an empty condition for the last else.
        code_to_execute_for_each_condition_list (List): list of code to execute for each condition
        code (Code): code where if else if is stored
    """
    if len(conditions_list) != len(code_to_execute_for_each_condition_list):
        raise(ValueError("Conditions and code to execute for each condition do not match in size"))
    for index, condition in enumerate(conditions_list):
        code.appendNewLineWithTabs()
        if index == 0:
            code.code += "if"
        elif condition == "":
            code.code += "else"
        else:
            code.code += "else if"
        code.code += "(" + condition + ")"
        code.startCodeBlock()
        code.appendNewLineWithTabs()
        code.code += code_to_execute_for_each_condition_list[index]
        code.tabs -= 1
    code.finishCodeBlock()

code = Code("")
ifElse(["a==b", "b == c"], ["return 0;", "return 1;"], code)
print(code.code)
