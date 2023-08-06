import ctypes

def get_object_address(object):
    return id(object)

def get_object_by_address(address):
    return ctypes.cast(address, ctypes.py_object).value