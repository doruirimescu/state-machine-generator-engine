from generator.cpp_with_python.switch_case import switchCase
from generator.cpp_with_python.code import *
from generator.cpp_with_python.type import *
from generator.cpp_with_python.preprocessor import *
from generator.cpp_with_python.enum_class import *
from generator.cpp_with_python.comment import *
from generator.cpp_with_python.function import *
from blueprint import blueprint

state_label_enum = EnumClass("StateLabel", "current_state", blueprint.stateLabels)
action_enum = EnumClass("Action", "action", blueprint.actions)


functions = list()
for index, stateLabel in enumerate(blueprint.stateLabels):
    b = Brief("Called when state " + stateLabel + " is entered", [], None)
    functions.append(Function("void", "output" + stateLabel, [], blueprint.stateOutputs[index], b))

on_state_entry_function_body = Code("")
on_state_entry_function_body.tabs = 1
switchCase(state_label_enum.label, map(state_label_enum.getEnumerator, state_label_enum.enumerator_list),
           blueprint.stateOutputs, on_state_entry_function_body)
on_state_entry_function = Function("void", "onStateEntry", [state_label_enum], on_state_entry_function_body.code)
transition_function = Function("StateLabel", "performTransition", [state_label_enum, action_enum])


## Declares
code = Code("", 0, "generated/procedural/src/header_v2.h")
pragmaOnce(code)
includeGlobalHeader("iostream", code)
includeGlobalHeader("string", code)

code.appendNewLineWithTabs()
oneLineComment("Enumerations", code)
state_label_enum.declare(code)
action_enum.declare(code)

for function in functions:
    function.declare(code)
on_state_entry_function.declare(code)
transition_function.declare(code)
code.saveToFile()

## Defines
code = Code("", 0, "generated/procedural/src/src_v2.cpp")
includeLocalHeader("header_v2.h", code)
for function in functions:
    function.define(code)
on_state_entry_function.define(code)
code.saveToFile()
