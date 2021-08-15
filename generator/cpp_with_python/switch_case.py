from generator.cpp_with_python.code import Code


def switchCase(expression, expression_values_list, code_to_execute_list, code: Code):
    code.appendNewLineWithTabs()
    code.code += "switch(" + expression + ")"
    code.appendNewLineWithTabs()
    code.code += "{"
    code.tabs += 1

    for index, expression_value in enumerate(expression_values_list):
        code.appendNewLineWithTabs()
        code.code += "case " + expression_value + ":"
        code.tabs += 1
        code.appendNewLineWithTabs()
        code.code += code_to_execute_list[index]
        code.appendNewLineWithTabs()
        code.code += "break;"
        code.tabs -= 1

    code.appendNewLineWithTabs()
    code.code += "default:"
    code.tabs += 1
    code.appendNewLineWithTabs()
    code.code += "break;"
    code.tabs -= 2

    code.appendNewLineWithTabs()
    code.code += "}"
