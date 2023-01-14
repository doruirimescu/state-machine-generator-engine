#!/usr/bin/python3
from typing import Generator
from blueprint import Blueprint, blueprint
from state import State
from generator.generator import Generator


class ProceduralGenerator(Generator):
    """Generate state machine code in procedural fashion.
    """
    def __init__(self, path_to_generate) -> None:
        super().__init__(path_to_generate)

    def generate(self, blueprint: Blueprint):
        self._generateHeaderCode(blueprint.state_labels, blueprint.actions,
                                 blueprint.state_outputs, blueprint.state_list, blueprint.state_index_to_label)
        self._generateSourceCode(blueprint.state_labels, blueprint.state_outputs,
                                 blueprint.state_list, blueprint.state_index_to_label)

    def _generateHeaderCode(self, state_labels, actions, outputs, state_list, state_index_to_label):
        add_states = ""
        for l in state_labels:
            add_states += "\n\t" + str(l)+","
        # Strip last comma
        add_states = add_states[:-1]

        add_actions = ""
        for a in actions:
            add_actions += "\n\t" + str(a)+","
        # Strip last comma
        add_actions = add_actions[:-1]

        add_outputs = ""
        for index, label in enumerate(state_labels):
            if outputs[index] != -1:
                add_outputs += "\nvoid output"+label+"();\n"

        code = '''/* ----Generated code---- */
#pragma once
#include <iostream>
#include <string>
/* Enumerations */
enum class StateLabel
{%s
};

enum class Action
{%s
};

/* Function definitions */%s
void onStateEntry(StateLabel current_state);

StateLabel performTransition(StateLabel current_state, Action action);

''' % (add_states, add_actions, add_outputs)
        header_path = self.path_to_generate + "procedural/include/header.h"
        print("Generating header to path", header_path)
        f = open(header_path, "w+")
        f.write(code)
        f.close()

    def _generateSourceCode(self, state_labels, outputs, state_list, state_index_to_label):
        add_outputs = ""
        for index, label in enumerate(state_labels):
            if outputs[index] != -1:
                add_outputs += "\nvoid output"+label+"()\n{\n\t" + outputs[index]+"\n}\n"

        add_onEntry = ""
        for index, label in enumerate(state_labels):
            if outputs[index] != -1:
                add_onEntry += "\n\t\tcase StateLabel::" + label + ":" + "\n\t\t\toutput"+label+"();\n\t\t\tbreak;\n"

        add_Transitions =""
        for index, state in enumerate(state_list):
            IFELIF = "if" if index == 0 else "else if"

            add_Transitions += "\n\t" + IFELIF + "(current_state == StateLabel::" + state.label + ")"
            add_Transitions += "\n\t{"

            for i, action in enumerate(state.successors):
                IFELIF = "if" if i == 0 else "else if"
                add_Transitions += "\n\t\t" + IFELIF + "(action == Action::" + action + ")"
                add_Transitions += "\n\t\t{"
                add_Transitions += "\n\t\t\tStateLabel next_state = StateLabel::" + state_index_to_label[state.successors[action]] + ";"
                add_Transitions += "\n\t\t\tonStateEntry(next_state);"
                add_Transitions += "\n\t\t\treturn next_state;"
                add_Transitions += "\n\t\t}"

            add_Transitions += "\n\t}"
        code = '''/* ----Generated code---- */
#include "header.h"

/* Function definitions */%s
void onStateEntry(StateLabel current_state)
{
    switch (current_state)
    {%s
        default:
            break;
    }
}

StateLabel performTransition(StateLabel current_state, Action action)
{%s
    return current_state;
}
''' % ( add_outputs, add_onEntry, add_Transitions )
        source_path = self.path_to_generate + "procedural/src/source.cpp"
        print("Generating source to path", source_path)
        f= open(source_path,"w+")
        f.write(code)
        f.close()
