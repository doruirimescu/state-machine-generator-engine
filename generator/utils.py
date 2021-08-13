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


def oneLineComment(comment_text: str, code: Code):
    code.appendNewLineWithTabs()
    code.code += "/* " + comment_text + " */"


@dataclass()
class Function:
    return_type: str
    name: str
    arguments_list: List[str]
    body: str
    comment: str = None
    arguments: str = field(init=False)

    def __post_init__(self):
        self.arguments = ", ".join([i for i in self.arguments_list])

    def declare(self, code: Code):
        code.code += "\n"
        if self.comment is not None:
            oneLineComment(self.comment, code)
        code.appendNewLineWithTabs()
        code.code += self.return_type + " " + self.name + "(" + self.arguments+");"
        code.code += "\n"

    def define(self, code: Code, className=None):
        code.code += "\n"
        if className:
            to_append = className + "::"
        else:
            to_append = ""
        code.code += "\n" + self.return_type + " " + to_append + self.name + "(" + self.arguments+")"

        code.code += "\n{"
        code.tabs = 1
        code.appendNewLineWithTabs()
        code.tabs = 0
        code.code += self.body
        code.code += "\n}"
        code.code += "\n"


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
class Method:
    method: Function
    access_specifier: AccessSpecifier = AccessSpecifier.PRIVATE

    def declare(self, code):
        return self.method.declare(code)

    def define(self, code, className=None):
        self.method.define(code, className)


@dataclass()
class Class:
    name: str
    methods: List[Method]
    comment: str = None

    def declare(self, code: Code):
        code.code += "\n"
        generateBrief(code, self.comment)
        code.code += "class " + self.name + ":"
        code.code += "\n{"
        self._declarePublicProtectedPrivate(code)
        code.code += "\n};"
        code.code += "\n"
        return code

    def _groupMethodsBasedOnAccessSpecifiers(self):
        """Groups the methods into public, protected and private methods

        Returns:
            Tuple[List[Method], List[Method], List[Method]]: tuple of lists of methods
        """
        public: List[Method] = list()
        private: List[Method] = list()
        protected: List[Method] = list()

        for method in self.methods:
            if method.access_specifier == AccessSpecifier.PUBLIC:
                public.append(method)
            elif method.access_specifier == AccessSpecifier.PRIVATE:
                private.append(method)
            elif method.access_specifier == AccessSpecifier.PROTECTED:
                protected.append(method)
        return (public, protected, private)

    def _declarePublicProtectedPrivate(self, code):
        public, protected, private = self._groupMethodsBasedOnAccessSpecifiers()
        code.tabs = 1
        if public:
            code.code += "\npublic:"
            for method in public:
                method.declare(code)
        if private:
            code.code += "\nprivate:"
            for method in private:
                method.declare(code)
        if protected:
            code.code += "\nprotected:"
            for method in protected:
                method.declare(code)
        code.tabs = 0

    def define(self, code: Code):
        for method in self.methods:
            code.appendNewLineWithTabs()
            method.define(code, self.name)


func = Function("void", "fun", ["int lal", "string fac"], "int x = 1;",
                "This function is a wild fun")
other_func = Function("int", "otherFunc", ["int lal", "string fac"],
                      "int* y = new int(2);", "This function is other")
m = Method(func, AccessSpecifier.PUBLIC)
my_class = Class("MyClass", [Method(func, AccessSpecifier.PUBLIC), Method(
    other_func, AccessSpecifier.PRIVATE)], "Beautiful class")

path = "testing.txt"
code = Code("#include \"lal\"", 0, path)
func.declare(code)
my_class.declare(code)
my_class.define(code)

# code.tabs = 1
includeGlobalHeader("New", code)
oneLineComment("lal", code)
print(code.code)

#code.saveToFile()
