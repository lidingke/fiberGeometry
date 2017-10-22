import MindPy
import cv2
import numpy
import pdb

print MindPy
print dir(MindPy)
# try:
# MindPy.initCamera()
# MindPy.getCameraSerial()
# except ValueError , e:
#     print e
# # pdb.set_trace()


# try:
#     MindPy.raise_error()
# except ValueError:
#     print 'get raised error'


# MindPy.cos_func_np()
# print 'after cos'

ar =  MindPy.get_test_array()
print ar.dtype, ar.shape
print ar

# print MindPy.getIntger(30000*30000)
MindPy.init_camera()
md = MindPy.get_raw_img()
# ValueError: get raw image error: -12

print md.dtype, md.shape
# md = md.reshape(1944, 2592)
img = cv2.cvtColor(md, cv2.COLOR_BAYER_GR2BGR)
cv2.imshow("np",img[::4,::4])
cv2.waitKey()
# npArray = bayer2BGR(npArray)
