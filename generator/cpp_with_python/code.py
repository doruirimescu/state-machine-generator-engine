from dataclasses import dataclass, field


@dataclass()
class Code:
    """Structure to represent, store and save to file generated code.
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

    def startCodeBlock(self):
        self.appendNewLineWithTabs()
        self.code += "{"
        self.tabs += 1

    def finishCodeBlock(self):
        self.tabs -= 1
        self.appendNewLineWithTabs()
        self.code += "}"
