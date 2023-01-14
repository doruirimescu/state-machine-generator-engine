/* ----Generated code---- */
#pragma once
#include <iostream>
#include <string>
/* Enumerations */
enum class StateLabel
{
	state_2,
	state_1,
	state_3,
	start,
	end
};

enum class Action
{
	exit,
	s2_s1,
	s1_s2,
	s2_s3,
	s3_s2,
	start
};

/* Function definitions */
void outputstate_2();

void outputstate_1();

void outputstate_3();

void outputstart();

void outputend();

void onStateEntry(StateLabel current_state);

StateLabel performTransition(StateLabel current_state, Action action);

