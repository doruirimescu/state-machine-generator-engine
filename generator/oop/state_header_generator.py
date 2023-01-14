 #!/usr/bin/python3
from blueprint import Blueprint
from generator.generator import Generator


class StateHeaderGenerator(Generator):
    def __init__(self, path_to_generate) -> None:
        super().__init__(path_to_generate)
    def generate(self, blueprint: Blueprint):
        add_actions = ""
        for a in blueprint.actions:
            add_actions += "\n    void add"+str(a)+"(State* s);"

        add_states = ""
        for a in blueprint.actions:
            add_states += "\n    State* " + str(a).lower()+";"

        code = '''/* ----Generated code---- */
#pragma once
#include <iostream>
#include <string>
using namespace std;
class State
{
    public:
    /*---------------Constructor Destructor---------------*/
    State( int state, string label );
    ~State();

    /*---------------Methods---------------*/

    /* Building. Link resulting objects to actions */
    %s
    /* Debug */
    void print();

    /*-----------Members--------*/
    int state;
    string label;
    %s
};''' % (add_actions, add_states)
        state_header_path = self.path_to_generate + "oop/include/state.h"
        f = open(state_header_path, "w+")
        f.write(code)
        f.close
