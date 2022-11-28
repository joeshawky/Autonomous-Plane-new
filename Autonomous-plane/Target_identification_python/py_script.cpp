
#include <boost/python.hpp>
namespace py = boost::python;

int main()
{
    Py_Initialize(); //Must be called first

    try
    {
        //In Python "print('Hello World!')Execute
        py::object global = py::import("__main__").attr("__dict__");
        py::exec("print('Hello World!')", global);
    }
    catch (const py::error_already_set &)
    {
        //If an error occurs while executing Python code, the error content is displayed.
        PyErr_Print();
    }

    return 0;
}