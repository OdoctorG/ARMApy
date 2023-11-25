import ctypes
libname = "ARMA.dll"
c_lib = ctypes.CDLL(libname)


def ARparameters(p,x):
    c_lib._ARparameters.restype = ctypes.POINTER(ctypes.c_double * p)
    c_lib._ARparameters.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
    ret = c_lib._ARparameters(ctypes.c_int(len(x)),ctypes.c_int(p),(ctypes.c_double * len(x))(*x))
    return ret[0][:]

def toARMAparameters(param):
    c_lib._toARMAparameters.restype = ctypes.POINTER(ctypes.c_double * int(len(param)*0.5+1))
    v1 = (ctypes.c_double * len(param))(*param)
    ret = c_lib._toARMAparameters(v1, len(param))
    return ret[0][:]

def ARMAparameters(p,x):
    c_lib._ARMAparameters.restype = ctypes.POINTER(ctypes.c_double * (p+1))
    ret = c_lib._ARMAparameters(ctypes.c_int(p),ctypes.c_int(len(x)),(ctypes.c_double * len(x))(*x))
    return ret[0][:]

def ARforecast(x,param):
    c_lib._ARforecast.restype = ctypes.c_double
    v1 = (ctypes.c_double * len(x))(*x)
    v2 = (ctypes.c_double * len(param))(*param)
    ret = c_lib._ARforecast(v1,len(x),v2,len(param))
    return ret

def ARMAforecast(x,param):
    c_lib._ARMAforecast.restype = ctypes.c_double
    v1 = (ctypes.c_double * len(x))(*x)
    v2 = (ctypes.c_double * len(param))(*param)
    ret = c_lib._ARMAforecast(v1,len(x),v2,len(param))
    return ret


