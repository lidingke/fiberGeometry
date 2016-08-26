from ctypes import *
class tSdkCameraDevInfo(Structure):
    _fields_ = [("uVendorID", c_uint),
    ("uProductID", c_uint),
    ("acVendorName", c_char*32),
    ("acProductSeries", c_char*32),
    ("acProductName", c_char*32),
    ("acFriendlyName", c_char*64),
    ("acDevFileName", c_char*32),
    ("acFirmwareVersion", c_char*32),
    ("acSensorType", c_char*32),
    ("acPortType", c_char*32)]

# class tSdkCameraCapbility(Structure):
#     _fields_ = [('pTriggerDesc', pointer(tSdkTrigger)),
#     ('iTriggerDesc', c_int),
#     ('')
#     ]




class tSdkTrigger(Structure):
    _fields_ = [('iIndex', c_int),
    ('acDescription', c_char * 32)]

class tSdkImageResolution(Structure):
    _fields_ = [('iIndex', c_int),
    ('acDescription', c_char * 32),
    ('uBinSumMode', c_uint),
    ('uBinAverageMode', c_uint)]
