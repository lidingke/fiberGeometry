from ctypes import *
import pdb
class XYZstruct(Structure):
    """docstring for XYZstruct"""
    _fields_ = [("axisX",c_char * 10),
    ("axisY",c_char * 10),
    ("axisZ",c_char * 10)
    ]

KPZdll = CDLL("KPZ_API.dll")

print KPZdll

# serials = c_char * 10
# serials = serials()
serial = "29500464"
KPZdll.Init_KPZ(serial)
KPZdll.SetVoltage(serial,c_double(110))
getV = c_double()
pgetV = pointer(getV)
KPZdll.GetVoltage(serial, pgetV)
print getV
# xyz = XYZstruct()
# pxyz = pointer(xyz)
# KPZdll.Init_KPZ_XYZ(pxyz)

# xNo = pxyz.contents.axisX
# # pxNo = pointer
# getxV = KPZdll.GetVoltage(xNo)
# KPZdll.SetVoltage(xNo,c_double(120))
# print getxV
# pdb.set_trace()

# print 'pxyz', pxyz
