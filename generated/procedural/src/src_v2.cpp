
#include "header_v2.h"
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
	switch(current_state)
		{
			case StateLabel::Menu_1:
				std::cout<<"1"<<std::endl;
				break;
			case StateLabel::Menu_2:
				std::cout<<"2"<<std::endl;
				break;
			case StateLabel::Menu_3:
				std::cout<<"3"<<std::endl;
				break;
			case StateLabel::Menu_1_Feature_1:
				std::cout<<"4"<<std::endl;
				break;
			case StateLabel::Menu_1_Feature_2:
				std::cout<<"5"<<std::endl;
				break;
			case StateLabel::Menu_1_Feature_1_Subfeature_1:
				std::cout<<"6"<<std::endl;
				break;
			case StateLabel::Menu_3_Feature_1:
				std::cout<<"7"<<std::endl;
				break;
			case StateLabel::Menu_2_Feature_1:
				std::cout<<"8"<<std::endl;
				break;
			case StateLabel::Enter_game_1:
				std::cout<<"Game1"<<std::endl;
				break;
			default:
				break;
		}
}
