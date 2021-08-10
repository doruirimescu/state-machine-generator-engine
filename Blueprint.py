"""Contains the textual description of the state machine.
It is the blueprint used to generated the code.
"""
from dataclasses import dataclass, field
from typing import List, Tuple
from State import State

""" State transition table. First column represents the starting state.
The rest of the columns represent the state labels where you end up when performing
the specified action from the starting state. -1 means that you remain in the starting state i.e. action not applicable.
"""
#   Label                               Left                        Right                    Up                 Down                                Select
a=( ( "Menu_1",                         "Menu_2",                   -1,                     -1,                 "Menu_1_Feature_1",                 "Enter_game_1"),
    ( "Menu_2",                         "Menu_3",                   -1,                     -1,                 "Menu_2_Feature_1",                 -1),
    ( "Menu_3",                         -1,                         -1,                     -1,                 "Menu_3_Feature_1",                 -1),
    ( "Menu_1_Feature_1",               "Menu_1_Feature_2",         -1,                     -1,                 "Menu_1_Feature_1_Subfeature_1",    -1),
    ( "Menu_1_Feature_2",               -1,                         -1,                     -1,                 -1,                                 -1),
    ( "Menu_1_Feature_1_Subfeature_1",  -1,                         -1,                     -1,                 -1,                                 -1),
    ( "Menu_3_Feature_1",               -1,                         -1,                     -1,                 -1,                                 -1),
    ( "Menu_2_Feature_1",               -1,                         -1,                     -1,                 -1,                                 -1),
    ( "Enter_game_1",                   -1,                         -1,                     -1,                 -1,                                 -1)
   )

"""List of cpp code strings to be executed when each state is entered.
"""
outputs = ("cout<<\"1\"<<endl",
           "cout<<\"2\"<<endl",
           "cout<<\"3\"<<endl",
           "cout<<\"4\"<<endl",
           "cout<<\"5\"<<endl",
           "cout<<\"6\"<<endl",
           "cout<<\"7\"<<endl",
           "cout<<\"8\"<<endl",
           "cout<<\"Game1\"<<endl")
"""List of all possible actions
"""
actionList = ("Left",  "Right", "Up",   "Down", "Select")

"""List of reverse actions corresponding to actionList.
Eg. If for each state A (from all state labels), whenever you take Left from state A
and you end up in state B (from all state labels), you can specify
Right in revActionList so that when you take Right in state B.
"""
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
