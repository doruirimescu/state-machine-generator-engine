/* ----Generated code---- */
#pragma once
#include <iostream>
#include <string>
/* Enumerations */
enum class StateLabel
{
	Menu_1,
	Menu_2,
	Menu_3
};

enum class Action
{
	Right,
	Left,
	Up
};

/* Function definitions */
void outputMenu_1()
{
	return;
}

void outputMenu_2()
{
	return;
}

void onStateEntry(StateLabel current_state)
{
    switch (current_state)
    {
		case StateLabel::Menu_1:
			outputMenu_1();
			break;

		case StateLabel::Menu_2:
			outputMenu_2();
			break;

        default:
            break;
    }
}
