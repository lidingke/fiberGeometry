from ctypes import *
import pdb

rzdll = CDLL('RZ_CameraPy.dll')
print rzdll
rzdll.InitRz_Camera()
# pdb.set_trace()
# rzdll.display()
