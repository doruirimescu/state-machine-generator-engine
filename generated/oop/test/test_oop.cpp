#include <gtest/gtest.h>
#include "state.h"
#include "state_machine.h"

TEST(StateMachine, ConstructStateMachineAndMove)
{

    StateMachine sm;
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
