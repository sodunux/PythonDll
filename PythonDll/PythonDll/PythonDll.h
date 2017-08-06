#define PythonDllAPI extern "C" __declspec(dllexport)

PythonDllAPI int func1();
PythonDllAPI int func2();
PythonDllAPI int func3();
