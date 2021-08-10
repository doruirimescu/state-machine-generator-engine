className = "State"
from typing import List, Tuple, Dict
class State:
    def __init__( self, index: int, label: str, successors: Dict[str, int], output: Tuple[str] ):
        self.index = index
        self.label = label
        self.output = output
        self.successors = successors

    def __repr__(self):
        return "Label: {} Index: {} Successors: ".format( self.label,
                                            str(self.index), self.successors )

    def addNode(self):
        return '\n\t{Class} state{name}({state},\"{label}\");'.format(
                    Class = className, name = str(self.index),
                    label=self.label, state=str(self.index) )

    def addTransition(self):
        ret =""
        for action in self.successors:
            ret+= "\n\tstate{}.add{}(&state{});".format( str(self.index),
                                            action, self.successors[ action ] )
        return ret
