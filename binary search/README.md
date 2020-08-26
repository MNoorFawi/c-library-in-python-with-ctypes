# C Binary Search Library in Python

Imporing C library into Python using **ctypes** library

First compile the C shared library using the **Makefile**
```bash
make

gcc -fPIC -shared -o libbsearch.dll.a binary_search.c
```
Now in python:

We will begin by defining a wrapper function to import C functions from the library into python functions:
```python
import ctypes

def wrap_function(lib, funcname, restype, argtypes):
    """Simplify wrapping ctypes functions
    Thanks to this article:
    https://dbader.org/blog/python-ctypes-tutorial-part-2"""
    func = lib.__getattr__(funcname)
    func.argtypes = argtypes
    func.restype = restype
    return func
```
Then we read the shared library
```python
lib = ctypes.CDLL("./libbsearch.dll.a")
```
Now, before starting anything, we define a function to convert a python list into a C array (Pointer to Int)
```python
## To convert a full array
def to_cpointer(pyarr):
    n = len(pyarr)
    c_type = ctypes.c_int * n
    c_arr = c_type(*pyarr)
    return c_arr
    
## To initiate an empty C array
def empty_arr_init(size):
    return (ctypes.c_int * size)()
```

Now we start importing the functions from the library using the wrapper function
```python
c_sort = wrap_function(lib, "sorted", None,
            (ctypes.POINTER(ctypes.c_int), ctypes.c_int))
            
bsearch = wrap_function(lib, "range_binary_search", None,
            [ctypes.POINTER(ctypes.c_int), ctypes.c_int, 
                ctypes.c_int, ctypes.POINTER(ctypes.c_int)])
```
Look how we use **ctypes.POINTER** because the functions use values passed by reference.
 
Finally a wrapper function to print the results
```python
def binary_search(arr, size, val, res):
    bsearch(arr, size, val, res)
    print("%s is at index %s till index %s" % (val, res[0], res[1]))
```
Now let's test everything:
```python
# random unsorted list
arr = [4, 5, 5, 3, 2, 3, 7, 9, 10, 0, 11, 17, 25]
n = ctypes.c_int(len(arr))

# convert python list to c array
carr = to_cpointer(arr)
# initialize an empty c array (2 because function returns range(left, right))
res = empty_arr_init(2)

# Sort the array
c_sort(carr, n)
```
Examples:
```python
binary_search(carr, n, 2, res)
# 2 is at index 1 till index 1

binary_search(carr, n, 3, res)
# 3 is at index 2 till index 3

binary_search(carr, n, 17, res)
# 17 is at index 11 till index 11

binary_search(carr, n, 30, res)
# 30 is at index -1 till index -1
## Not found
```