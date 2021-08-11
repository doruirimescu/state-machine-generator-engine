/* ----Generated code---- */
#include "StateMachine.h"
using namespace std;
/*Constructor Destructor*/
StateMachine::StateMachine(State* ptr)
{
    this->ptr = ptr;
}
StateMachine::~StateMachine()
{
}

/* Actions */    
void StateMachine::moveLeft()
{
	ptr = ptr -> left;
}
void StateMachine::moveRight()
{
	ptr = ptr -> right;
}
void StateMachine::moveUp()
{
	ptr = ptr -> up;
}
void StateMachine::moveDown()
{
	ptr = ptr -> down;
}
void StateMachine::moveSelect()
{
	ptr = ptr -> select;
}
int StateMachine::getState()
{
    return ptr -> state;
}

/* Input */
void StateMachine::input( int input )
{/* As many inputs as there are actions */
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
/* Main */
int main()
{
    
	State state0(0,"Menu_1");
	State state1(1,"Menu_2");
	State state2(2,"Menu_3");
	State state3(3,"Menu_1_Feature_1");
	State state4(4,"Menu_1_Feature_2");
	State state5(5,"Menu_1_Feature_1_Subfeature_1");
	State state6(6,"Menu_3_Feature_1");
	State state7(7,"Menu_2_Feature_1");
	State state8(8,"Enter_game_1");
	state0.addLeft(&state1);
	state0.addDown(&state3);
	state0.addSelect(&state8);
	state1.addLeft(&state2);
	state1.addDown(&state7);
	state2.addDown(&state6);
	state3.addLeft(&state4);
	state3.addDown(&state5);
    State* ptr;
    ptr =&state0;
    
	return 0;
}