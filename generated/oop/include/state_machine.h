/* ----Generated code---- */
#pragma once
#include "state.h"
using namespace std;
class StateMachine
{
	public:
	/*---------------Constructor Destructor---------------*/
	StateMachine();
	~StateMachine();

	/*---------------Methods---------------*/

	/* Actions*/
	void moveLeft();
	void moveRight();
	void moveUp();
	void moveDown();
	void moveSelect();
	int getState();

	/* Input */
	void input( int input );

	 /* Output */
	void output();
	void print();

	/*-------------Members--------------*/
	State * ptr;
	State* state0;
	State* state1;
	State* state2;
	State* state3;
	State* state4;
	State* state5;
	State* state6;
	State* state7;
	State* state8;

};