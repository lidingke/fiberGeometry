from ctypes import *


KPZdll = CDLL("SDK\\PiezoController\\KPZ_API.dll")
print KPZdll

class Piezo(object):
    """docstring for Piezo"""
    def __init__(self,):
        super(Piezo, self).__init__()
        # self.arg = arg
        self.serial = "29500475"
        KPZdll.Init_KPZ(self.serial)

    def setV(self,voltage):
        KPZdll.SetVoltage(self.serial,c_double(voltage))

    def getV(self):
        getV = c_double()
        pgetV = pointer(getV)
        KPZdll.GetVoltage(self.serial, pgetV)
        return getV

    def disconnect(self,serial):
        KPZdll.Disconnect(serial)
