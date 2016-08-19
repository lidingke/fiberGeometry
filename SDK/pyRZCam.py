from ctypes import *

rZCamAPI = CDLL.LoadLibrary("RZCamAPI.dll")

#UCHAR * | ULONG | UCHAR
#c_char_p | c_ulong | c_uchar
#buffer 需要用户分配，怎么个分配法
#HANDLE 是什么鬼

class CapInfoStruct(Structure):
    """docstring for CapInfoStruct"""
    _fields_ = [
        ("Buffer", c_char_p),
        ("Height", c_ulong),
        ("Width", c_ulong),
        ("OffsetX", c_ulong),
        ("OffsetY", c_ulong),
        ("Exposure", c_ulong),
        ("Gain", c_ulong * 3),
        ("Control", c_ulong),
        ("InternalUse", c_ulong),
        ("ColorOff", c_ulong * 3),
        ("Reserved", c_ulong * 4)]


# def RZ_Initialize(
#         pFilterName='',
#         pIndex=pointer(c_int()),
#         pCapInfo=pointer(CapInfoStruct()),
#         hCamera=pointer(c_void_p())):
#     rZCamAPI.RZ_Initialize(pFilterName, pIndex, pCapInfo, hCamera)

# def RZ_SetCapInfo(

#     ):
#     pass
#DllFunction.RZ_Initialize("RZ_DEMO", ref nIndex, ref m_CapInfo, ref m_hDevice))
#param string *int *CapInfoStruct *HANDLE
RZ_Initialize(pFilterName, pIndex, pCapInfo, hCamera)







