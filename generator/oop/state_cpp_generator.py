 #!/usr/bin/python3
from blueprint import Blueprint
from generator.generator import Generator

class StateCppGenerator(Generator):
    def __init__(self, path_to_generate) -> None:
          super().__init__(path_to_generate)

    def generate(self, blueprint: Blueprint):
        constructor_code = ""
        for a in blueprint.actions:
                constructor_code += "\n\tthis -> "+str(a).lower()+" = this;"
        building_code = ""
        for index, a in enumerate(blueprint.actions):
                building_code += "\nvoid State::add%s( State* s)\n{" % str(a)
                building_code +="\n\tthis -> "+str(a).lower()+" = s;"
                building_code += "\n}"

        code ='''/* ----Generated code---- */
#include \"state.h\"
using namespace std;

/*Constructor Destructor*/
State::State( int state, string label )
{
    this -> state    = state;
    this -> label    = label;\
    %s
}
State::~State()
{
}

/* Building */\
%s

/* Debugging */
void State::print()
{
    cout << this -> label <<' '<< this -> state <<endl;
}''' % (constructor_code, building_code)
        state_source_path = self.path_to_generate + "oop/src/state.cpp"
        f= open(state_source_path,"w+")
        f.write(code)
        f.close()
