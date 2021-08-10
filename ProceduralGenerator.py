#!/usr/bin/python3
from Blueprint import blueprint
def generateCode(labels, actions, outputs):
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
            add_outputs += "\nvoid output"+label+"()\n{\n\t" + outputs[index]+"\n}\n"

    add_onEntry= ""
    for index, label in enumerate(labels):
        if outputs[index] != -1:
            add_onEntry += "\n\t\tcase StateLabel::" + label + ":" + "\n\t\t\toutput"+label+"();\n\t\t\tbreak;\n"

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
void onStateEntry(StateLabel current_state)
{
    switch (current_state)
    {%s
        default:
            break;
    }
}
''' % ( add_states, add_actions, add_outputs, add_onEntry )

    f= open("Generated/Procedural/include.h","w+")
    f.write(code)
    f.close

generateCode(["Menu_1", "Menu_2", "Menu_3"], ["Right", "Left", "Up"], ["return;", "return;", -1])
