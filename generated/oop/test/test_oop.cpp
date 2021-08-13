#include <gtest/gtest.h>
#include "state.h"
#include "state_machine.h"

TEST(StateMachine, ConstructStateMachineAndMove)
{
    State state0(0,"Menu_1");
	State state1(1,"Menu_2");
	State state2(2,"Menu_3");
	State state3(3,"Menu_1_Feature_1");
	State state4(4,"Menu_1_Feature_2");
	State state5(5,"Menu_1_Feature_1_Subfeature_1");
	State state6(6,"Menu_3_Feature_1");
	State state7(7,"Menu_2_Feature_1");
	State state8(8,"Enter_game_1");
	state0.addLeft(&state1);
	state0.addDown(&state3);
	state0.addSelect(&state8);
	state1.addLeft(&state2);
	state1.addDown(&state7);
	state2.addDown(&state6);
	state3.addLeft(&state4);
	state3.addDown(&state5);
    State* ptr;
    ptr =&state0;

    StateMachine sm(ptr);
    ASSERT_EQ(sm.getState(), 0);
    sm.moveLeft();
    ASSERT_EQ(sm.getState(), 1);
    sm.moveDown();
    ASSERT_EQ(sm.getState(), 7);
    sm.moveDown();
    ASSERT_EQ(sm.getState(), 7);
    sm.moveUp();
    ASSERT_EQ(sm.getState(), 1);
    sm.moveRight();
    ASSERT_EQ(sm.getState(), 0);
}
