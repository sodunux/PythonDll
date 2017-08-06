from ctypes import *
dll=CDLL("PythonDll.dll")
print dll.func1()
print dll.func2()
print dll.func3()
print dir(dll)