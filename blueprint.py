"""Contains the textual description of the state machine.
It is the blueprint used to generated the code.
"""
from dataclasses import dataclass, field
from typing import List, Tuple, Optional
from state import State

""" State transition table. First column represents the starting state.
The rest of the columns represent the state labels where you end up when performing
the specified action from the starting state. -1 means that you remain in the starting state i.e. action not applicable.
"""
#   Label                               Left                        Right                    Up                 Down                                Select
a=( ( "Menu_1",                         "Menu_2",                   -1,                     -1,                 "Menu_1_Feature_1",                 "Enter_game_1"),
    ( "Menu_2",                         "Menu_3",                   "Menu_1",               -1,                 "Menu_2_Feature_1",                 -1),
    ( "Menu_3",                         -1,                         "Menu_2",               -1,                 "Menu_3_Feature_1",                 -1),
    ( "Menu_1_Feature_1",               "Menu_1_Feature_2",         -1,                     "Menu_1",           "Menu_1_Feature_1_Subfeature_1",    -1),
    ( "Menu_1_Feature_2",               -1,                         "Menu_1_Feature_1",     -1,                 -1,                                 -1),
    ( "Menu_1_Feature_1_Subfeature_1",  -1,                         -1,                     -1,                 -1,                                 -1),
    ( "Menu_3_Feature_1",               -1,                         -1,                     "Menu_3",           -1,                                 -1),
    ( "Menu_2_Feature_1",               -1,                         -1,                     "Menu_2",           -1,                                 -1),
    ( "Enter_game_1",                   -1,                         -1,                     -1,                 -1,                                 -1)
   )

"""List of cpp code strings to be executed when each state is entered.
"""
outputs = ("std::cout<<\"1\"<<std::endl;",
           "std::cout<<\"2\"<<std::endl;",
           "std::cout<<\"3\"<<std::endl;",
           "std::cout<<\"4\"<<std::endl;",
           "std::cout<<\"5\"<<std::endl;",
           "std::cout<<\"6\"<<std::endl;",
           "std::cout<<\"7\"<<std::endl;",
           "std::cout<<\"8\"<<std::endl;",
           "std::cout<<\"Game1\"<<std::endl;")
"""List of all possible actions
"""
actionList = ("Left",  "Right", "Up",   "Down", "Select")


def extractStatesFromTransitionTable(state_transition_table, actions, state_outputs):
    state_labels = list(x[0] for x in state_transition_table)
    state_list = list()

    for index, row in enumerate(state_transition_table):
        successors = dict()
        for successorIndex, successorLabel in enumerate(row[1: len(actions) + 1]):
            if -1 is not successorLabel:
                successors.update({actions[successorIndex]: state_labels.index(successorLabel)})
            else:
                continue
        s = State(index, row[0], successors, state_outputs[index])
        state_list.append(s)
    return (state_list, state_labels)

@dataclass(frozen=False)
class Blueprint:
    state_labels: List[str]
    state_list: List[State]
    state_outputs: Tuple[str]
    actions: Tuple[str]
    state_index_to_label: Optional[dict] = None

    def __str__(self):
        # Initialize an empty string to store the contents of the Blueprint class
        contents = "---------BLUEPRINT--------\n"

        # Add the state outputs to the contents string
        # contents += "State outputs:\n"
        # for row in self.state_outputs:
        #     contents += f"{row}\n"
        # contents += "\n"

        # Add the actions to the contents string
        contents += f"Actions:\n{self.actions}\n\n"

        # Add the state_labels to the contents string
        contents += f"state_labels:\n{self.state_labels}\n\n"

        # Add the state_list to the contents string
        contents+="List of States:\n"
        for state in self.state_list:
            contents+=f"  Label: {state.label}\n"
            contents+=f"  Index: {state.index}\n"
            contents+=f"  Successors:\n"
            for action, next_state in state.successors.items():
                ns = [state for state in self.state_list if state.index == next_state][0]
                contents+=f"    {action}: {ns.label}\n"
            contents+=f"  Output: {state.output}\n"
            contents+=f"  One_entry: {state.on_entry}\n"
            contents+=f"  One_exit: {state.on_exit}\n"
            contents+="\n"
        return contents

def initialize_blueprint(state_transition_table, state_outputs, action_list):
    state_list, state_labels = extractStatesFromTransitionTable(state_transition_table, action_list, state_outputs)
    return Blueprint(state_labels, state_list, outputs, actionList)

blueprint = initialize_blueprint(a, outputs, actionList)

blueprint.state_index_to_label = dict()
for i, label in enumerate(blueprint.state_labels):
    blueprint.state_index_to_label[i] = label

# print(blueprint)
#print(blueprint.state_list)
