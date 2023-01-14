/* ----Generated code---- */
#include "header.h"

/* Function definitions */
void outputstate_2()
{
	cout << "Hello from state 2" << endl;
x += 10;
}

void outputstate_1()
{
	//Runs every time the state is active
cout << "Hello from state 1" << endl;
}

void outputstate_3()
{
	
}

void outputstart()
{
	
}

void outputend()
{
	
}

void onStateEntry(StateLabel current_state)
{
    switch (current_state)
    {
		case StateLabel::state_2:
			outputstate_2();
			break;

		case StateLabel::state_1:
			outputstate_1();
			break;

		case StateLabel::state_3:
			outputstate_3();
			break;

		case StateLabel::start:
			outputstart();
			break;

		case StateLabel::end:
			outputend();
			break;

        default:
            break;
    }
}

StateLabel performTransition(StateLabel current_state, Action action)
{
	if(current_state == StateLabel::state_2)
	{
		if(action == Action::s2_s1)
		{
			StateLabel next_state = StateLabel::state_1;
			onStateEntry(next_state);
			return next_state;
		}
		else if(action == Action::s2_s3)
		{
			StateLabel next_state = StateLabel::state_3;
			onStateEntry(next_state);
			return next_state;
		}
	}
	else if(current_state == StateLabel::state_1)
	{
		if(action == Action::exit)
		{
			StateLabel next_state = StateLabel::end;
			onStateEntry(next_state);
			return next_state;
		}
		else if(action == Action::s1_s2)
		{
			StateLabel next_state = StateLabel::state_2;
			onStateEntry(next_state);
			return next_state;
		}
	}
	else if(current_state == StateLabel::state_3)
	{
		if(action == Action::s3_s2)
		{
			StateLabel next_state = StateLabel::state_2;
			onStateEntry(next_state);
			return next_state;
		}
	}
	else if(current_state == StateLabel::start)
	{
		if(action == Action::start)
		{
			StateLabel next_state = StateLabel::state_1;
			onStateEntry(next_state);
			return next_state;
		}
	}
	else if(current_state == StateLabel::end)
	{
	}
    return current_state;
}
