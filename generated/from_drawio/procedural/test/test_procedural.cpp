#include <gtest/gtest.h>
#include "header.h"

TEST(StateMachine, ConstructStateMachineAndMove)
{
    StateLabel current_state = StateLabel::state_1;

    current_state = performTransition(current_state, Action::s1_s2);
    ASSERT_EQ(current_state, StateLabel::state_2);

    current_state = performTransition(current_state, Action::s2_s1);
    ASSERT_EQ(current_state, StateLabel::state_1);

    current_state = StateLabel::start;
    performTransition(current_state, Action::start);
    ASSERT_EQ(current_state, StateLabel::state_1);

}
