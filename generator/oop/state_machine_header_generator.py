 #!/usr/bin/python3
from blueprint import Blueprint
from generator.generator import Generator


class StateMachineHeaderGenerator(Generator):
    def generate(self, blueprint: Blueprint):
        #generate code snippets
        add_actions = ""
        for a in blueprint.actions:
            add_actions +="\n\tvoid move" + a + "();"

        add_state_pointers = ""
        for s in blueprint.state_list:
            add_state_pointers += "\tState* state" + str(s.index) + ";\n"

        code='''/* ----Generated code---- */
#pragma once
#include \"state.h\"
using namespace std;
class StateMachine
{
\tpublic:
\t/*---------------Constructor Destructor---------------*/
\tStateMachine();
\t~StateMachine();\n
\t/*---------------Methods---------------*/

\t/* Actions*/\
%s
\tint getState();\n
\t/* Input */
\tvoid input( int input );

\t /* Output */
\tvoid output();
\tvoid print();

\t/*-------------Members--------------*/
\tState * ptr;
%s
};''' % (add_actions, add_state_pointers)
        f= open("generated/oop/include/state_machine.h","w+")
        f.write(code)
        f.close
