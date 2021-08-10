"""Generates the state machine cpp code
"""
#!/usr/bin/python3
from Blueprint import blueprint
from StateHeaderGenerator import stateheader
from StateCppGenerator import statecpp
from StateMachineHeaderGenerator import machineheader
from StateMachineCppGenerator import machinecpp
className = "State"

class State:
    def __init__( self, index, label, successors, output ):
        self.index = index
        self.label = label
        self.output = output
        self.successors = successors

    def __repr__(self):
        return "Label: {} Index: {} Successors: ".format( self.label,
                                            str(self.index), self.successors )

    def addNode(self):
        return '\n\t{Class} state{name}({state},\"{label}\");'.format(
                    Class = className, name = str(self.index),
                    label=self.label, state=str(self.index) )

    def addTransition(self):
        ret =""
        for action in self.successors:
            ret+= "\n\tstate{}.add{}(&state{});".format( str(self.index),
                                            action, self.successors[ action ] )
        return ret

fc = list( x[0] for x in blueprint.stateTransitionTable )
stateList = list()

for i, row in enumerate(blueprint.stateTransitionTable):
    successors = dict()
    for j, field in enumerate( row[ 1 : len(blueprint.actions) + 1 ] ):
        if -1 is not field:
            successors.update( { blueprint.actions[j] : fc.index(field) } )
        else:
            continue
    s = State( i, row[ 0 ], successors, blueprint.stateOutputs[ i ] )
    stateList.append( s )

stateheader(blueprint.actions)
statecpp(blueprint.actions, blueprint.reverseActions)
machineheader(blueprint.actions, stateList)
machinecpp(blueprint.actions, stateList)
