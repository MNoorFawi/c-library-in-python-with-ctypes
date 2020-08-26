import ctypes

class Stack(ctypes.Structure):
    _fields_ = [("val", ctypes.POINTER(ctypes.c_int)),
                ("indx", ctypes.c_int), ("size", ctypes.c_int)]

def print_stack(st):
    for i in range(st.size):
        print(st.val[i], end=" ")
    print()

def wrap_function(lib, funcname, restype, argtypes):
    """Simplify wrapping ctypes functions"""
    func = lib.__getattr__(funcname)
    func.argtypes = argtypes
    func.restype = restype
    return func

lib = ctypes.CDLL("./libstack.dll.a")

def to_cpointer(pyarr):
    n = len(pyarr)
    c_type = ctypes.c_int * n
    c_arr = c_type(*pyarr)
    return c_arr

create_stack = wrap_function(lib, "create_stack", Stack, None)
is_empty = wrap_function(lib, "is_empty", ctypes.c_int, [ctypes.POINTER(Stack)])
push = wrap_function(lib, "push", None,
                     [ctypes.POINTER(Stack), ctypes.c_int])
pop = wrap_function(lib, "pop", None, [ctypes.POINTER(Stack)])
