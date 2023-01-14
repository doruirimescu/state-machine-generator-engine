#include <gtest/gtest.h>
#include "header.h"

TEST(StateMachine, ConstructStateMachineAndMove)
{
    StateLabel current_state = StateLabel::Menu_1;

    current_state = performTransition(current_state, Action::Left);
    ASSERT_EQ(current_state, StateLabel::Menu_2);

    current_state = performTransition(current_state, Action::Down);
    ASSERT_EQ(current_state, StateLabel::Menu_2_Feature_1);

    current_state = performTransition(current_state, Action::Down);
    ASSERT_EQ(current_state, StateLabel::Menu_2_Feature_1);

    current_state = performTransition(current_state, Action::Up);
    ASSERT_EQ(current_state, StateLabel::Menu_2);

    current_state = performTransition(current_state, Action::Left);
    ASSERT_EQ(current_state, StateLabel::Menu_3);

    current_state = performTransition(current_state, Action::Down);
    ASSERT_EQ(current_state, StateLabel::Menu_3_Feature_1);

    current_state = performTransition(current_state, Action::Up);
    ASSERT_EQ(current_state, StateLabel::Menu_3);

    current_state = performTransition(current_state, Action::Right);
    ASSERT_EQ(current_state, StateLabel::Menu_2);

    current_state = performTransition(current_state, Action::Right);
    ASSERT_EQ(current_state, StateLabel::Menu_1);

    current_state = performTransition(current_state, Action::Select);
    ASSERT_EQ(current_state, StateLabel::Enter_game_1);
}
