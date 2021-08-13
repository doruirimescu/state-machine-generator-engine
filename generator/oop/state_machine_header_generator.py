 #!/usr/bin/python3
from blueprint import Blueprint
from generator.generator import Generator


class StateMachineHeaderGenerator(Generator):
    def generate(self, blueprint: Blueprint):
        #generate code snippets
        add_actions = ""
        for a in blueprint.actions:
            add_actions +="\n\tvoid move" + a + "();"

        code='''/* ----Generated code---- */
#pragma once
#include \"state.h\"
using namespace std;
class StateMachine
{
\tpublic:
\t/*---------------Constructor Destructor---------------*/
\tStateMachine( State * ptr );
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
};''' % add_actions
        f= open("generated/oop/state_machine.h","w+")
        f.write(code)
        f.close
