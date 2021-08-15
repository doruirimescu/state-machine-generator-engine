from generator.cpp_with_python.code import Code


def generateBrief(code: Code, brief: str, params, returned):
    """Generates a doxygen-style brief comment

    Args:
        code (Code): code object
        brief (str): Brief description
        params (List[str]): list of params and their description
        returned (List[str]): list of returned type
    """
    brief_code = "\n/**\n * @brief " + brief

    param_code = ""
    for param in params:
        param_code += "\n * @param " + param

    returned_code = ""
    for r in returned:
        returned_code += "\n * @return " + r
    code.code += brief_code + param_code + returned_code
    code.code += "\n */"


def oneLineComment(comment_text: str, code: Code):
    code.appendNewLineWithTabs()
    code.code += "/* " + comment_text + " */"
