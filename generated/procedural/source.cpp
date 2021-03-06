/* ----Generated code---- */
#include "header.h"

/* Function definitions */
void outputMenu_1()
{
	std::cout<<"1"<<std::endl;
}

void outputMenu_2()
{
	std::cout<<"2"<<std::endl;
}

void outputMenu_3()
{
	std::cout<<"3"<<std::endl;
}

void outputMenu_1_Feature_1()
{
	std::cout<<"4"<<std::endl;
}

void outputMenu_1_Feature_2()
{
	std::cout<<"5"<<std::endl;
}

void outputMenu_1_Feature_1_Subfeature_1()
{
	std::cout<<"6"<<std::endl;
}

void outputMenu_3_Feature_1()
{
	std::cout<<"7"<<std::endl;
}

void outputMenu_2_Feature_1()
{
	std::cout<<"8"<<std::endl;
}

void outputEnter_game_1()
{
	std::cout<<"Game1"<<std::endl;
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

		case StateLabel::Menu_3:
			outputMenu_3();
			break;

		case StateLabel::Menu_1_Feature_1:
			outputMenu_1_Feature_1();
			break;

		case StateLabel::Menu_1_Feature_2:
			outputMenu_1_Feature_2();
			break;

		case StateLabel::Menu_1_Feature_1_Subfeature_1:
			outputMenu_1_Feature_1_Subfeature_1();
			break;

		case StateLabel::Menu_3_Feature_1:
			outputMenu_3_Feature_1();
			break;

		case StateLabel::Menu_2_Feature_1:
			outputMenu_2_Feature_1();
			break;

		case StateLabel::Enter_game_1:
			outputEnter_game_1();
			break;

        default:
            break;
    }
}

StateLabel performTransition(StateLabel current_state, Action action)
{
	if(current_state == StateLabel::Menu_1)
	{
		if(action == Action::Left)
		{
			StateLabel next_state = StateLabel::Menu_2;
			onStateEntry(next_state);
			return next_state;
		}
		else if(action == Action::Down)
		{
			StateLabel next_state = StateLabel::Menu_1_Feature_1;
			onStateEntry(next_state);
			return next_state;
		}
		else if(action == Action::Select)
		{
			StateLabel next_state = StateLabel::Enter_game_1;
			onStateEntry(next_state);
			return next_state;
		}
	}
	else if(current_state == StateLabel::Menu_2)
	{
		if(action == Action::Left)
		{
			StateLabel next_state = StateLabel::Menu_3;
			onStateEntry(next_state);
			return next_state;
		}
		else if(action == Action::Down)
		{
			StateLabel next_state = StateLabel::Menu_2_Feature_1;
			onStateEntry(next_state);
			return next_state;
		}
	}
	else if(current_state == StateLabel::Menu_3)
	{
		if(action == Action::Down)
		{
			StateLabel next_state = StateLabel::Menu_3_Feature_1;
			onStateEntry(next_state);
			return next_state;
		}
	}
	else if(current_state == StateLabel::Menu_1_Feature_1)
	{
		if(action == Action::Left)
		{
			StateLabel next_state = StateLabel::Menu_1_Feature_2;
			onStateEntry(next_state);
			return next_state;
		}
		else if(action == Action::Down)
		{
			StateLabel next_state = StateLabel::Menu_1_Feature_1_Subfeature_1;
			onStateEntry(next_state);
			return next_state;
		}
	}
	else if(current_state == StateLabel::Menu_1_Feature_2)
	{
	}
	else if(current_state == StateLabel::Menu_1_Feature_1_Subfeature_1)
	{
	}
	else if(current_state == StateLabel::Menu_3_Feature_1)
	{
	}
	else if(current_state == StateLabel::Menu_2_Feature_1)
	{
	}
	else if(current_state == StateLabel::Enter_game_1)
	{
	}
    return current_state;
}
