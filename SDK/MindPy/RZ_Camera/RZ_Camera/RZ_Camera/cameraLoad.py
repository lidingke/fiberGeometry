from ctypes import *
from cameradefine import CapInfoStruct
import pdb
import numpy as np
import time
import cv2

rzdll = CDLL('RZ_CameraPy.dll')
print rzdll
pHeadCamera = pointer(c_void_p())
capInfo = CapInfoStruct()
# capInfo.Gain[0] = c_int(32)
# capInfo.Gain[1] = c_char(32)
# capInfo.Gain[2] = c_char(32)
# capInfo.Gain = [c_char(32),c_char(32),c_char(32)
width = 3072
height = 2048
capInfo.Width = c_ulong(width)
capInfo.Height = c_ulong(height)
# pdb.set_trace()
rawImgArrayInit = c_ubyte * (width * height )
rawImgArray = rawImgArrayInit()
capInfo.Buffer = rawImgArray
print capInfo.Buffer
pCapInfo = pointer(capInfo)
# for x in xrange(1,10):

rzdll.InitRz_Camera(pHeadCamera,pCapInfo)

# rzdll.Display(pHeadCamera,pCapInfo)
print 'pCapInfo.contents.Exposure', pCapInfo.contents.Exposure
for x in xrange(1,5):
    time.sleep(1)
    rzdll.GetBuffer(pHeadCamera,pCapInfo)
    # rzdll.GetRgbBuffer(rawImgArray)
    npArray = np.array(rawImgArray, dtype=np.uint8)
    if npArray.sum() > 0:
        print "get ab array", npArray.sum()
        break
# npArray = npArray[:-width]
time.sleep(1)
npArray = npArray.reshape(height, width )
# cv2.imshow("show",npArray[::4,::4])
# cv2.waitKey(0)
print npArray[:10,:10]
print pCapInfo.contents.Buffer
# pdb.set_trace()

rgbImgArrayInit = c_ubyte * (width * height *3)
rgbImgArray = rgbImgArrayInit()

pRgbBuff = pointer(rgbImgArray)
rzdll.GetRawBmp(rgbImgArray)

# rgbImgArrayInit = c_ubyte * (width * height *3)
# rgbImgArray = rgbImgArrayInit()

# pRgbBuff = pointer(rgbImgArray)
# rzdll.GetRgbBuffer(pRgbBuff)
# npArray = np.array(rgbImgArray, dtype=np.uint8)
# npArray = npArray.reshape(height, width, 3 )
# cv2.imshow("show",npArray[::4,::4])
# cv2.waitKey(0)
# rzdll.display()
