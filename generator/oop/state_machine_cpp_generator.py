#!/usr/bin/python3
from blueprint import Blueprint
from generator.generator import Generator


class StateMachineCppGenerator:
    def generate(self, blueprint: Blueprint):
        # generate code snippets
        add_actions = ""
        for a in blueprint.actions:
            add_actions += "\nvoid StateMachine::move{}()".format(a)
            add_actions += "\n{"
            add_actions += "\n\tptr = ptr -> {};".format(a.lower())
            add_actions += "\n}"

        add_states = ""
        for s in blueprint.stateList:
            add_states += "\n\tcase {}:".format(str(s.index))
            add_states += "\n\t\t{};".format(s.output)
            add_states += "\n\t\tbreak;"

        add_main = ""
        for s in blueprint.stateList:
            add_main += '\n\t{Class} state{name}({state},\"{label}\");'.format(
                Class="State", name=str(s.index),
                label=s.label, state=str(s.index))

        for s in blueprint.stateList:
            transitions =""
            for action in s.successors:
                transitions+= "\n\tstate{}.add{}(&state{});".format( str(s.index),
                                                action, s.successors[ action ] )
            add_main += transitions

        # generate the code
        code = '''/* ----Generated code---- */
#include "state_machine.h"
using namespace std;
/*Constructor Destructor*/
StateMachine::StateMachine(State* ptr)
{
    this->ptr = ptr;
}
StateMachine::~StateMachine()
{
}

/* Actions */\
    %s
int StateMachine::getState()
{
    return ptr -> state;
}

/* Input */
void StateMachine::input( int input )
{/* As many inputs as there are blueprint.actions */
    switch( input )
    {\
    %s
    default:
        print();
        break;
    }
}
void StateMachine::print()
{
    cout << "State: " << ptr -> state <<" "<<
        "Label: " << ptr->label <<endl;
}
/* Main */
int main()
{
    %s
    State* ptr;
    ptr =&state%s;
    ''' % (add_actions, add_states, add_main, str(blueprint.stateList[0].index))
        code += "\n\treturn 0;\n}"
        f = open("generated/oop/src/state_machine.cpp", "w+")
        f.write(code)
        f.close
