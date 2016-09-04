from ctypes import *
import pdb
import numpy as np
import time
import cv2
mydll = CDLL('MindPy.dll')
# pdb.set_trace()
# pyo = mydll.rePyArrayObject()
print mydll.Edisplay()
limit = 640*480*3
# ctypeArray = POINTER(c_byte)*limit
ctypeArray = c_byte * limit
arget = ctypeArray()

# pdb.set_trace()
print 'carray', arget[1:3]
begin = time.time()
md = mydll.doubleRePyArray(arget, limit)
# pdb.set_trace()

npArray = np.array(arget, dtype=np.uint8)
npArray = npArray.reshape(480,640,3)
# pdb.set_trace()
end = time.time()
print 'time: ',  end - begin
# npArray = cv2.cvtColor(npArray, cv2.COLOR_RGB2GRAY)
cv2.imshow("show",npArray[::1])
cv2.waitKey(0)

# arrlist = [x for x in arget[1:3]]
# print 'arget end ', arrlist[1:3]
# pdb.set_trace()
# print 'arget end ', arrlist
