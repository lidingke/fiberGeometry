from ctypes import *
import pdb
import numpy as np
import time
import cv2
mydll = CDLL('MindPy.dll')

# limit = 640*480*3
# get img dll - GetOneImg  0.0199999809265
# transform to nparray and reshape 0.00300002098083
limit = 1920*1080*3 #0.042s get img
# get img dll - GetOneImg  0.0420000553131
# transform to nparray and reshape 0.0169999599457
limit = 2592*2048*3
# get img dll - GetOneImg  0.0889999866486
# transform to nparray and reshape 0.0299999713898
ctypeArray = c_byte * limit
arget = ctypeArray()
hand = mydll.InitCameraPlay()

begin = time.time()
md = mydll.GetOneImg(arget, limit, hand)
gettime = time.time()
print 'get img dll - GetOneImg ', gettime - begin
npArray = np.array(arget, dtype=np.uint8)
# npArray = npArray.reshape(480,640,3)
npArray = npArray.reshape(2048, 2592, 3)
end = time.time()
print 'transform to nparray and reshape',  end - gettime
cv2.imshow("show",npArray[::4,::4])
cv2.waitKey(0)
