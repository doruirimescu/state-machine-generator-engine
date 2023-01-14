 #!/usr/bin/python3
from blueprint import Blueprint
from generator.generator import Generator


class StateMachineHeaderGenerator(Generator):
    def __init__(self, path_to_generate) -> None:
        super().__init__(path_to_generate)

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
        state_machine_header_path = self.path_to_generate + "oop/include/state_machine.h"
        f= open(state_machine_header_path,"w+")
        f.write(code)
        f.close
