from ctypes import *
class CapInfoStruct(Structure):
    _fields_ = [("Buffer", POINTER(c_uchar)),
    ("Height", c_ulong),
    ("Width", c_ulong),
    ("OffsetX", c_ulong),
    ("OffsetY", c_ulong),
    ("Exposure", c_ulong),
    ("Gain", c_char * 3),
    ("Control", c_char),
    ("InternalUse", c_char),
    ("ColorOff", c_char * 3),
    ("Reserved", c_char * 4)]
