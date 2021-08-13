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
            add_actions += "\n\tinput(ptr->state);"
            add_actions += "\n}"

        add_states = ""
        for s in blueprint.stateList:
            add_states += "\n\tcase {}:".format(str(s.index))
            add_states += "\n\t\t{};".format(s.output)
            add_states += "\n\t\tbreak;"

        add_constructor = ""
        for s in blueprint.stateList:
            add_constructor += '\n\tstate{name} = new State({state},\"{label}\");'.format(name=str(s.index),
                label=s.label, state=str(s.index))
        add_destructor = ""
        for s in blueprint.stateList:
            add_destructor += '\n\tdelete state{name};'.format(name=str(s.index))

        for s in blueprint.stateList:
            transitions =""
            for action in s.successors:
                transitions+= "\n\tstate{}->add{}(state{});".format( str(s.index),
                                                action, s.successors[ action ] )
            add_constructor += transitions

        # generate the code
        code = '''/* ----Generated code---- */
#include "state_machine.h"
using namespace std;
/*Constructor Destructor*/
StateMachine::StateMachine()
{%s
    this->ptr = state%s;
}
StateMachine::~StateMachine()
{%s
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
}''' % (add_constructor, str(blueprint.stateList[0].index), add_destructor, add_actions, add_states)
        f = open("generated/oop/src/state_machine.cpp", "w+")
        f.write(code)
        f.close
