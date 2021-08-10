"""Contains the textual description of the state machine.
It is the blueprint used to generated the code.
"""
from dataclasses import dataclass, field
from State import State

#   Label                           Left                        Right                    Up                 Down                            Select
a = (("Menu 1",                     "Menu 2",                   -1,                     -1,                 "Menu1 Feature 1",             "Enter game1"),
     ("Menu 2",                     "Menu 3",                   -
      1,                     -1,                 "Menu2 Feature 1",             -1),
     ("Menu 3",                     -1,                         -
      1,                     -1,                 "Menu3 Feature 1",             -1),
     ("Menu1 Feature 1",            "Menu1 Feature 2",          -
      1,                     -1,                 "Menu1 Feature1 Subfeature 1", -1),
     ("Menu1 Feature 2",            -1,                         -
      1,                     -1,                 -1,                            -1),
     ("Menu1 Feature1 Subfeature 1", -1,                         -
      1,                     -1,                 -1,                            -1),
     ("Menu3 Feature 1",            -1,                         -
      1,                     -1,                 -1,                            -1),
     ("Menu2 Feature 1",            -1,                         -
      1,                     -1,                 -1,                            -1),
     ("Enter game1",                -1,                         -
      1,                     -1,                 -1,                            -1)
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
    stateTransitionTable: tuple
    stateOutputs: tuple
    actions: tuple
    reverseActions: tuple
    stateList: list = field(init=False)

    def __post_init__(self):
        fc = list(x[0] for x in self.stateTransitionTable)
        stateList = list()

        for index, row in enumerate(self.stateTransitionTable):
            successors = dict()
            for j, field in enumerate(row[1: len(self.actions) + 1]):
                if -1 is not field:
                    successors.update({self.actions[j]: fc.index(field)})
                else:
                    continue
            s = State(index, row[0], successors, self.stateOutputs[index])
            stateList.append(s)

        object.__setattr__(self, "stateList", stateList)

blueprint = Blueprint(a, outputs, actionList, revActionList)
