from ctypes import *
import pdb
import numpy as np
mydll = CDLL('MindPy.dll')
print mydll.Edisplay()

# arget = pointer(c_byte())
# pBuff = mydll.RePyArray(arget, 10)
# arr = []
# for x in range(1,10):
#     bytenum = mydll.PointerSweep(pBuff, x)
#     arr.append(bytenum)

#     print 'arr', arr

limit = 3
ctypeArray1 = POINTER(c_int) * limit
ctypeArray2 = c_int * limit
arr1 = ctypeArray1()
arr2 = ctypeArray2(1,2,3)
print arr1[0:limit], arr2[:limit]
mydll.sweepArray(arr1, arr2, limit)
# pdb.set_trace()
print arr1[0:limit], arr2[:limit]
# print
