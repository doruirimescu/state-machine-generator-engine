from generator.cpp_with_python.switch_case import switchCase
from generator.cpp_with_python.code import *
from generator.cpp_with_python.type import *
from generator.cpp_with_python.preprocessor import *
from generator.cpp_with_python.enum_class import *
from generator.cpp_with_python.comment import *
from generator.cpp_with_python.function import *
from generator.cpp_with_python.if_else import *
from blueprint import blueprint

def generateTransitionFunction(parameter_list):
    state_label_enum, action_enum = parameter_list
    transition_function = Function("StateLabel", "performTransition", [state_label_enum, action_enum])

    first_if_code_list = list()
    for state in blueprint.stateList:
        first_if_code = Code("")
        first_if_code.tabs = 1
        first_if_condition_list = [action_enum.label + "==" +
                                   action_enum.getEnumerator(action) for action in state.successors]
        next_state_enum = EnumClass("StateLabel", "next_state", blueprint.stateLabels)

        second_if_code_list = list()
        for action in state.successors:
            second_if_condition_code = Code("")
            second_if_condition_code.tabs = first_if_code.tabs + 1
            next_state_enum.declare(second_if_condition_code)

            next_state_enum.assign(blueprint.stateLabels[state.successors[action]], second_if_condition_code)
            on_state_entry_function.call([
                next_state_enum.label], second_if_condition_code)
            second_if_condition_code.appendNewLineWithTabs()
            second_if_condition_code.code += "return next_state;"
            second_if_code_list.append(second_if_condition_code.code)

        ifElse(first_if_condition_list, second_if_code_list, first_if_code)
        first_if_code_list.append(first_if_code.code)

    condition_list = [state_label_enum.label + "==" +
                      state_label_enum.getEnumerator(enumerator) for enumerator in state_label_enum.enumerator_list]
    transition_function_body = Code("")
    ifElse(condition_list, first_if_code_list, transition_function_body)
    transition_function.body = transition_function_body.code
    return transition_function


def generateOnStateEntryFunction(state_label_enum, blueprint):
    on_state_entry_function_body = Code("")
    switchCase(state_label_enum.label, map(state_label_enum.getEnumerator, state_label_enum.enumerator_list),
            blueprint.stateOutputs, on_state_entry_function_body)
    on_state_entry_function = Function("void", "onStateEntry", [state_label_enum], on_state_entry_function_body.code)
    return on_state_entry_function


def generateOutputFunctions(blueprint):
    output_functions = list()
    for index, stateLabel in enumerate(blueprint.stateLabels):
        b = Brief("Called when state " + stateLabel + " is entered", [], None)
        output_functions.append(Function("void", "output" + stateLabel, [], blueprint.stateOutputs[index], b))
    return output_functions

state_label_enum = EnumClass("StateLabel", "current_state", blueprint.stateLabels)
action_enum = EnumClass("Action", "action", blueprint.actions)


output_functions = generateOutputFunctions(blueprint)
on_state_entry_function = generateOnStateEntryFunction(state_label_enum, blueprint)
transition_function = generateTransitionFunction([state_label_enum, action_enum])


# Declares
code = Code("", 0, "generated/procedural/src/header_v2.h")
pragmaOnce(code)
includeGlobalHeader("iostream", code)
includeGlobalHeader("string", code)
code.appendNewLineWithTabs()
oneLineComment("Enumerations", code)
state_label_enum.define(code)
action_enum.define(code)
for of in output_functions:
    of.declare(code)
on_state_entry_function.declare(code)
transition_function.declare(code)
code.saveToFile()

# Defines
code = Code("", 0, "generated/procedural/src/src_v2.cpp")
includeLocalHeader("header_v2.h", code)
for of in output_functions:
    of.define(code)
on_state_entry_function.define(code)
code.saveToFile()
transition_function.define(code)
code.saveToFile()
