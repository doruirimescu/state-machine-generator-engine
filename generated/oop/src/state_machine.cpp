/* ----Generated code---- */
#include "state_machine.h"
using namespace std;
/*Constructor Destructor*/
StateMachine::StateMachine()
{
	state0 = new State(0,"Menu_1");
	state1 = new State(1,"Menu_2");
	state2 = new State(2,"Menu_3");
	state3 = new State(3,"Menu_1_Feature_1");
	state4 = new State(4,"Menu_1_Feature_2");
	state5 = new State(5,"Menu_1_Feature_1_Subfeature_1");
	state6 = new State(6,"Menu_3_Feature_1");
	state7 = new State(7,"Menu_2_Feature_1");
	state8 = new State(8,"Enter_game_1");
	state0->addLeft(state1);
	state0->addDown(state3);
	state0->addSelect(state8);
	state1->addLeft(state2);
	state1->addDown(state7);
	state2->addDown(state6);
	state3->addLeft(state4);
	state3->addDown(state5);
    this->ptr = state0;
}
StateMachine::~StateMachine()
{
	delete state0;
	delete state1;
	delete state2;
	delete state3;
	delete state4;
	delete state5;
	delete state6;
	delete state7;
	delete state8;
}

/* Actions */    
void StateMachine::moveLeft()
{
	ptr = ptr -> left;
	input(ptr->state);
}
void StateMachine::moveRight()
{
	ptr = ptr -> right;
	input(ptr->state);
}
void StateMachine::moveUp()
{
	ptr = ptr -> up;
	input(ptr->state);
}
void StateMachine::moveDown()
{
	ptr = ptr -> down;
	input(ptr->state);
}
void StateMachine::moveSelect()
{
	ptr = ptr -> select;
	input(ptr->state);
}
int StateMachine::getState()
{
    return ptr -> state;
}

/* Input */
void StateMachine::input( int input )
{/* As many inputs as there are blueprint.actions */
    switch( input )
    {    
	case 0:
		std::cout<<"1"<<std::endl;;
		break;
	case 1:
		std::cout<<"2"<<std::endl;;
		break;
	case 2:
		std::cout<<"3"<<std::endl;;
		break;
	case 3:
		std::cout<<"4"<<std::endl;;
		break;
	case 4:
		std::cout<<"5"<<std::endl;;
		break;
	case 5:
		std::cout<<"6"<<std::endl;;
		break;
	case 6:
		std::cout<<"7"<<std::endl;;
		break;
	case 7:
		std::cout<<"8"<<std::endl;;
		break;
	case 8:
		std::cout<<"Game1"<<std::endl;;
		break;
    default:
        print();
        break;
    }
}
void StateMachine::print()
{
    cout << "State: " << ptr -> state <<" "<<
        "Label: " << ptr->label <<endl;
}