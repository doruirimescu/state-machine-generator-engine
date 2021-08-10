"""Contains the textual description of the state machine.
It is the blueprint used to generated the code.
"""
from dataclasses import dataclass, field
from typing import List, Tuple
from State import State

#   Label                           Left                        Right                    Up                 Down                            Select
a=( ( "Menu 1",                     "Menu 2",                   -1,                     -1,                 "Menu1 Feature 1",             "Enter game1"),
    ( "Menu 2",                     "Menu 3",                   -1,                     -1,                 "Menu2 Feature 1",             -1),
    ( "Menu 3",                     -1,                         -1,                     -1,                 "Menu3 Feature 1",             -1),
    ( "Menu1 Feature 1",            "Menu1 Feature 2",          -1,                     -1,                 "Menu1 Feature1 Subfeature 1", -1),
    ( "Menu1 Feature 2",            -1,                         -1,                     -1,                 -1,                            -1),
    ( "Menu1 Feature1 Subfeature 1",-1,                         -1,                     -1,                 -1,                            -1),
    ( "Menu3 Feature 1",            -1,                         -1,                     -1,                 -1,                            -1),
    ( "Menu2 Feature 1",            -1,                         -1,                     -1,                 -1,                            -1),
    ( "Enter game1",                -1,                         -1,                     -1,                 -1,                            -1)
   )

outputs = ("cout<<\"1\"<<endl",
           "cout<<\"2\"<<endl",
           "cout<<\"3\"<<endl",
           "cout<<\"4\"<<endl",
           "cout<<\"5\"<<endl",
           "cout<<\"6\"<<endl",
           "cout<<\"7\"<<endl",
           "cout<<\"8\"<<endl",
           "cout<<\"Game1\"<<endl")

actionList = ("Left",  "Right", "Up",   "Down", "Select")
revActionList = ("Right", "Left", "Down", "Up",   -1)


@dataclass(frozen=True)
class Blueprint:
    stateTransitionTable: Tuple[Tuple[str]]
    stateOutputs: Tuple[str]
    actions: Tuple[str]
    reverseActions: Tuple[str]
    stateList: List[State] = field(init=False)

    def extractStatesFromTransitionTable(self):
        stateLabels = list(x[0] for x in self.stateTransitionTable)
        stateList = list()

        for index, row in enumerate(self.stateTransitionTable):
            successors = dict()
            for successorIndex, successorLabel in enumerate(row[1: len(self.actions) + 1]):
                if -1 is not successorLabel:
                    successors.update({self.actions[successorIndex]: stateLabels.index(successorLabel)})
                else:
                    continue
            s = State(index, row[0], successors, self.stateOutputs[index])
            stateList.append(s)
        return stateList

    def __post_init__(self):
        object.__setattr__(self, "stateList", self.extractStatesFromTransitionTable())

blueprint = Blueprint(a, outputs, actionList, revActionList)
