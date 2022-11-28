#include <Python.h>
// #include <C:/Python27/include/Python.h>
// #include <python2.7/Python.h>
// #include <stdio.h>
// #include <conio.h>
#include <iostream>


int main()
{
	PyObject* pInt;
	std::cout << "faruk";
	
	Py_Initialize();
	// std::cout << "T1";
	// PyRun_SimpleString("print('Hello World from Embedded Python!!!')");
	// PyErr_Print()	
	// Py_Finalize();
	std::cout << Py_ABS(-5);
	Py_ABSTRACTOBJECT_H("Hello");

	// printf("\nPress any key to exit...\n");
	// if(!_getch()) _getch();
	// std::cout << "test2";

	return 0;
}