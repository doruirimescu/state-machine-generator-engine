
#pragma once
#include <iostream>
#include <string>

/* Enumerations */
enum class StateLabel
{
	Menu_1,
	Menu_2,
	Menu_3,
	Menu_1_Feature_1,
	Menu_1_Feature_2,
	Menu_1_Feature_1_Subfeature_1,
	Menu_3_Feature_1,
	Menu_2_Feature_1,
	Enter_game_1
};
enum class Action
{
	Left,
	Right,
	Up,
	Down,
	Select
};
/**
 * @brief Called when state Menu_1 is entered
 */
void outputMenu_1();

/**
 * @brief Called when state Menu_2 is entered
 */
void outputMenu_2();

/**
 * @brief Called when state Menu_3 is entered
 */
void outputMenu_3();

/**
 * @brief Called when state Menu_1_Feature_1 is entered
 */
void outputMenu_1_Feature_1();

/**
 * @brief Called when state Menu_1_Feature_2 is entered
 */
void outputMenu_1_Feature_2();

/**
 * @brief Called when state Menu_1_Feature_1_Subfeature_1 is entered
 */
void outputMenu_1_Feature_1_Subfeature_1();

/**
 * @brief Called when state Menu_3_Feature_1 is entered
 */
void outputMenu_3_Feature_1();

/**
 * @brief Called when state Menu_2_Feature_1 is entered
 */
void outputMenu_2_Feature_1();

/**
 * @brief Called when state Enter_game_1 is entered
 */
void outputEnter_game_1();

void onStateEntry(StateLabel current_state);

StateLabel performTransition(StateLabel current_state, Action action);
