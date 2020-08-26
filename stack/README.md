# Implementing C Stack Structure in Python
Importing C libraries into Python using ctypes library to implement stack data structure

Compile the library into a shared one using the **Makefile**:
```bash
$ make builddll

gcc -fPIC -c stack.c -o stack.o
gcc -shared stack.o -o ./libstack.dll.a
```
Now let's define the **C Struct** into a python class:
```python
import ctypes

class Stack(ctypes.Structure):
    _fields_ = [("val", ctypes.POINTER(ctypes.c_int)),
                ("indx", ctypes.c_int), ("size", ctypes.c_int)]
```
Now, Let's get everything ready with the wrapper function and importing the functions from the library
```python
## print the stack
def print_stack(st):
    for i in range(st.size):
        print(st.val[i], end=" ")
    print()

## wrapper function
def wrap_function(lib, funcname, restype, argtypes):
    """Simplify wrapping ctypes functions"""
    func = lib.__getattr__(funcname)
    func.argtypes = argtypes
    func.restype = restype
    return func

## reading the library
lib = ctypes.CDLL("./libstack.dll.a")

## convert python list into c array
def to_cpointer(pyarr):
    n = len(pyarr)
    c_type = ctypes.c_int * n
    c_arr = c_type(*pyarr)
    return c_arr

## import the functions from the library
create_stack = wrap_function(lib, "create_stack", Stack, None)

is_empty = wrap_function(lib, "is_empty", ctypes.c_int, [ctypes.POINTER(Stack)])

push = wrap_function(lib, "push", None,
                     [ctypes.POINTER(Stack), ctypes.c_int])

pop = wrap_function(lib, "pop", None, [ctypes.POINTER(Stack)])
```
Let's test everything
```python
# initiate an empty stack
st = create_stack()
n = 10 # size
st.val = (ctypes.c_int * n)() # convert into c array
```
```python
is_empty(st)
# 1

push(st, 13)
push(st, 11)
push(st, 19)
push(st, 91)

is_empty(st)
# 0

st.indx
# 3
st.size
# 4

print_stack(st)
# 13 11 19 91

pop(st)
pop(st)

st.indx
# 1
st.size
# 2

print_stack(st)
# 13 11

pop(st)
pop(st)

is_empty(st)
# 1
```