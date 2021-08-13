from dataclasses import dataclass, field
from typing import List, Optional, Dict
from enum import Enum


@dataclass()
class Code:
    """Custom type to differentiate code from other strings
    """
    code: str = ""
    tabs: int = 0
    filename: str = None

    def printToFile(self):
        pass

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

    def define(self, body, code):
        code.code += "\n"
        code.code += "\n" + self.return_type + " " + self.name + "(" + self.arguments+")"
        code.code += "\n{"
        code.code += body
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


code = Code("#include \"lal\"")
f = Function("void", "daiNarcotica", ["int lal", "string fac"], "This function os wild")
g = Function("int", "daiNarcotica", ["int lal", "string fac"], "This function os wild")
f.declare(code)
generateBrief(code, "this is nice")
oneLineComment("comm", code)

m = Method(f, AccessSpecifier.PUBLIC)
c = Class("MyClass", [Method(f, AccessSpecifier.PUBLIC), Method(g, AccessSpecifier.PRIVATE)], "Beautiful class")

c.declare(code)

# code.tabs = 1
includeGlobalHeader("New", code)
oneLineComment("lal", code)
print(code.code)
