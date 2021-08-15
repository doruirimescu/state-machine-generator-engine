#!/usr/bin/python3
from typing import Generator
from blueprint import Blueprint, blueprint
from state import State
from generator.generator import Generator


class ProceduralGenerator(Generator):
    """Generate state machine code in procedural fashion.
    """

    def generate(self, blueprint: Blueprint):
        self._generateHeaderCode(blueprint.stateLabels, blueprint.actions, blueprint.stateOutputs, blueprint.stateList)
        self._generateSourceCode(blueprint.stateLabels, blueprint.stateOutputs, blueprint.stateList)

    def _generateHeaderCode(self, labels, actions, outputs, stateList):
        add_states = ""
        for l in labels:
            add_states += "\n\t" + str(l)+","
        # Strip last comma
        add_states = add_states[:-1]

        add_actions = ""
        for a in actions:
            add_actions += "\n\t" + str(a)+","
        # Strip last comma
        add_actions = add_actions[:-1]

        add_outputs = ""
        for index, label in enumerate(labels):
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

        f = open("generated/procedural/include/header.h", "w+")
        f.write(code)
        f.close

    def _generateSourceCode(self, labels, outputs, stateList):
        add_outputs = ""
        for index, label in enumerate(labels):
            if outputs[index] != -1:
                add_outputs += "\nvoid output"+label+"()\n{\n\t" + outputs[index]+"\n}\n"

        add_onEntry = ""
        for index, label in enumerate(labels):
            if outputs[index] != -1:
                add_onEntry += "\n\t\tcase StateLabel::" + label + ":" + "\n\t\t\toutput"+label+"();\n\t\t\tbreak;\n"

        add_Transitions =""
        for index, state in enumerate(stateList):
            IFELIF = "if" if index == 0 else "else if"

            add_Transitions += "\n\t" + IFELIF + "(current_state == StateLabel::" + state.label + ")"
            add_Transitions += "\n\t{"

            for i, action in enumerate(state.successors):
                IFELIF = "if" if i == 0 else "else if"
                add_Transitions += "\n\t\t" + IFELIF + "(action == Action::" + action + ")"
                add_Transitions += "\n\t\t{"
                add_Transitions += "\n\t\t\tStateLabel next_state = StateLabel::" + labels[state.successors[action]] + ";"
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

        f= open("generated/procedural/src/source.cpp","w+")
        f.write(code)
        f.close
