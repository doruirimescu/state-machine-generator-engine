from dataclasses import dataclass, field
from typing import List, Optional, Dict
from enum import Enum


@dataclass()
class Code:
    """Custom type to differentiate code from other strings
    """
    code: str = ""
    tabs: int = 0
    path: str = None

    def saveToFile(self):
        f = open(self.path, "w+")
        f.write(self.code)
        f.close

    def appendNewLineWithTabs(self):
        self.code += "\n"
        self.code += "\t" * self.tabs


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


def oneLineComment(comment_text: str, code: Code):
    code.appendNewLineWithTabs()
    code.code += "/* " + comment_text + " */"


@dataclass()
class Type:
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


@dataclass()
class Function:
    return_type: str
    name: str
    parameters_list: List[Type]
    body: str = ""
    comment: str = None
    parameters: str = field(init=False)

    def __post_init__(self):
        self.parameters = ", ".join([i.asParameter() for i in self.parameters_list])

    def declare(self, code: Code):
        if self.comment is not None:
            code.code += "\n"
            oneLineComment(self.comment, code)
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


def generateBrief(code, comment):
    code.code += '''
/**
 * @brief %s
 *
 */\n''' % (comment)


class AccessSpecifier(Enum):
    PUBLIC = "public",
    PRIVATE = "private",
    PROTECTED = "protected"


@dataclass()
class Member:
    member: Type
    access_specifier: AccessSpecifier = AccessSpecifier.PRIVATE

    def declare(self, code):
        self.member.declare(code)


@dataclass()
class Method:
    method: Function
    access_specifier: AccessSpecifier = AccessSpecifier.PRIVATE

    def declare(self, code):
        return self.method.declare(code)

    def define(self, code, class_name=None):
        self.method.define(code, class_name)

    def call(self, args: List, code, object_type: Type):
        self.method.call(args, code, object_type)


@dataclass()
class Class:
    name: str
    methods: List[Method]
    members: List[Member]
    comment: str = None

    def declare(self, code: Code):
        code.code += "\n"
        generateBrief(code, self.comment)
        code.code += "class " + self.name + ":"
        code.code += "\n{"

        self._declarePublicProtectedPrivateMethods(code)

        code.code += "\n};"
        code.code += "\n"
        return code

    def _groupBasedOnAccessSpecifiers(self, to_group):
        """Groups to_group into public, protected and private (methods or members)

        Returns:
            Tuple[List, List, List]: tuple of lists of methods or members
        """
        public = list()
        private = list()
        protected = list()

        for item in to_group:
            if item.access_specifier == AccessSpecifier.PUBLIC:
                public.append(item)
            elif item.access_specifier == AccessSpecifier.PRIVATE:
                private.append(item)
            elif item.access_specifier == AccessSpecifier.PROTECTED:
                protected.append(item)
        return (public, protected, private)

    def _declarePublicProtectedPrivateMethods(self, code):
        public, protected, private = self._groupBasedOnAccessSpecifiers(self.methods)
        public_members, protected_members, private_members = self._groupBasedOnAccessSpecifiers(self.members)
        print(public_members, protected_members, private_members)

        code.tabs = 1
        if public or public_members:
            code.code += "\npublic:"
            for member in public_members:
                member.declare(code)
            for method in public:
                method.declare(code)
        if private or private_members:
            code.code += "\nprivate:"
            for member in private_members:
                member.declare(code)
            for method in private:
                method.declare(code)
        if protected or protected_members:
            code.code += "\nprotected:"
            for member in protected_members:
                member.declare(code)
            for method in protected:
                method.declare(code)
        code.tabs = 0

    def define(self, code: Code):
        for method in self.methods:
            code.appendNewLineWithTabs()
            method.define(code, self.name)


def switchCase(expression, list_of_codes_for_each_case, code: Code):
    code.appendNewLineWithTabs()
    code.code += "switch(" + expression + ")"
    code.appendNewLineWithTabs()
    code.code += "{"
    code.tabs += 1

    for body in list_of_codes_for_each_case:
        code.appendNewLineWithTabs()
        code.code += "case " + body[0] + ":"
        code.tabs += 1

        for i in range(1, len(body)):
            code.appendNewLineWithTabs()
            code.code += body[i]

        code.appendNewLineWithTabs()
        code.code += "break;"
        code.tabs -= 1

    code.appendNewLineWithTabs()
    code.code += "default:"
    code.appendNewLineWithTabs()
    code.code += "\tbreak;"
    code.tabs -= 1

    code.appendNewLineWithTabs()
    code.code += "}"


func = Function("void", "fun", [Type("int", "lal"), Type("string", "fac")], "int x = 1;",
                "This function is a wild fun")
other_func = Function("int", "otherFunc", [Type("int", "lal"), Type("string", "fac")],
                      "int* y = new int(2);", "This function is other")
constructor = Method(Function("", "Myclass", [Type("int", "leb"), Type("string", "falol")], ""), AccessSpecifier.PUBLIC)

m = Method(func, AccessSpecifier.PUBLIC)
my_class = Class("MyClass", [Method(func, AccessSpecifier.PUBLIC), Method(
    other_func, AccessSpecifier.PRIVATE), constructor], [Member(Type("int* ", "myTyppa")), Member(Type("int", "myTyppB"))], "Beautiful class")

path = "testing.txt"
code = Code("", 0, path)
switchCase("expr", [["label1", "int a = 3;", "int b = 3;"]], code)

# pragmaOnce(code)
# includeGlobalHeader("iostream", code)
# includeGlobalHeader("string", code)
# usingNamespace("std", code)

# state_class_methods = [Method(Function("", "State", [Type("int", "state"), Type("string", "label")]), AccessSpecifier.PUBLIC),
#                        Method(Function("", "~State", []), AccessSpecifier.PUBLIC),
#                        Method(Function("void", "addLeft", [Type("State*", "s")]), AccessSpecifier.PUBLIC),
#                        Method(Function("void", "addRight", [Type("State*", "s")]), AccessSpecifier.PUBLIC)]
# state_class_members = []
# state = Class("State", state_class_methods, state_class_members)
# state.declare(code)
print(code.code)
