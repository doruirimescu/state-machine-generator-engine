from generator.cpp_with_python.code import Code


def includeLocalHeader(header_name: str, code: Code):
    code.appendNewLineWithTabs()
    code.code += "#include \"" + header_name + "\""
    return code


def includeGlobalHeader(header_name: str, code: Code):
    code.appendNewLineWithTabs()
    code.code += "#include <" + header_name + ">"
    return code


def pragmaOnce(code: Code):
    code.appendNewLineWithTabs()
    code.code += "#pragma once"

def usingNamespace(namespace, code: Code):
    code.appendNewLineWithTabs()
    code.code += "using namespace " + namespace + ";"
