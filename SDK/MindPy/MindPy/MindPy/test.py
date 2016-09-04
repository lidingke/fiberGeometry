from ctypes import *
import pdb
import numpy as np
mydll = CDLL('MindPy.dll')
mydll.Edisplay()
mydll.GetImg(0)

npPhoto = np.zeros([2592, 2048, 3], dtype=np.uint8)
pdb.set_trace()
ad = mydll.reArrayData(npPhoto)
print 'ad ', ad
print mydll
