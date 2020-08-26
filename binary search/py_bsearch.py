import ctypes


def wrap_function(lib, funcname, restype, argtypes):
    """Simplify wrapping ctypes functions
    Thanks to this article:
    https://dbader.org/blog/python-ctypes-tutorial-part-2"""
    func = lib.__getattr__(funcname)
    func.argtypes = argtypes
    func.restype = restype
    return func

    
lib = ctypes.CDLL("./libbsearch.dll.a")

def to_cpointer(pyarr):
    n = len(pyarr)
    c_type = ctypes.c_int * n
    c_arr = c_type(*pyarr)
    return c_arr

    
def empty_arr_init(size):
    return (ctypes.c_int * size)()

                     
c_sort = wrap_function(lib, "sorted", None,
            (ctypes.POINTER(ctypes.c_int), ctypes.c_int))

            
bsearch = wrap_function(lib, "range_binary_search", None,
            [ctypes.POINTER(ctypes.c_int), ctypes.c_int, 
            ctypes.c_int, ctypes.POINTER(ctypes.c_int)])

            
def binary_search(arr, size, val, res):
    bsearch(arr, size, val, res)
    print("%s is at index %s till index %s" % (val, res[0], res[1]))
    