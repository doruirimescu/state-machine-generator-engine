/* ----Generated code---- */
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

/* Function definitions */
void outputMenu_1();

void outputMenu_2();

void outputMenu_3();

void outputMenu_1_Feature_1();

void outputMenu_1_Feature_2();

void outputMenu_1_Feature_1_Subfeature_1();

void outputMenu_3_Feature_1();

void outputMenu_2_Feature_1();

void outputEnter_game_1();

void onStateEntry(StateLabel current_state);

StateLabel performTransition(StateLabel current_state, Action action);

