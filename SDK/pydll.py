from ctypes import *
# from pystruct import *
from initializer.Cstruct.structpy import tSdkFrame, tSdkFrameHead, tSdkCameraDevInfo
#coding = utf-8
import pdb
import numpy as np

CameraHandle = c_int()
hWndDisplay = c_int()
def initCamera():
    sdk = WinDLL('MVCAMSDK.dll')
    initSDKStatus = sdk.CameraSdkInit(0)
    if initSDKStatus != 0:
        print 'CameraSdkInit: ', initSDKStatus
        return
    pCameraList = pointer(tSdkCameraDevInfo())
    pnum = c_int(1)
    dev = sdk.CameraEnumerateDevice(pCameraList, pointer(pnum))
    # dev = sdk.CameraEnumerateDeviceEx()
    # pdb.set_trace()
    print 'CameraEnumerateDevice return:', dev
    pCameraHandle = pointer(CameraHandle)
    status = sdk.CameraInit(pCameraList, c_int(-1), c_int(-1), pCameraHandle)
    print 'CameraInit', status
    # status = sdk.CameraDisplayInit(pCameraHandle, hWndDisplay)
    # print 'CameraDisplayInit', status
    # status = sdk.CameraUnInit(CameraHandle)
    status = sdk.CameraPlay(CameraHandle)
    print 'CameraPlay ', status
    sdkFrameHead = tSdkFrameHead()
    pFrameInfo = pointer(sdkFrameHead)
    pWidth = pointer(c_int(sdkFrameHead.iWidth))
    pHeight = pointer(c_int(sdkFrameHead.iHeight))

    pbyBuffer = pointer(pointer(c_byte()))
    wTimes = c_uint(1000)

    # npPhoto = np.zeros([sdkFrameHead.iWidth, sdkFrameHead.iHeight], dtype=np.uint8)
    status = sdk.CameraGetImageBuffer(CameraHandle, pFrameInfo, pbyBuffer, wTimes)
    # photoHead = sdk.CameraGetImageBufferEx(CameraHandle, pWidth, pHeight, wTimes)
    # sdkFrameHead.uiMediaType =
    print 'CameraGetImageBuffer ', status
    pRgbBuffer = POINTER(c_ubyte * sdkFrameHead.iWidth * sdkFrameHead.iHeight)
    pdb.set_trace()
    status =sdk.CameraImageProcess(CameraHandle,pbyBuffer.contents, pRgbBuffer, pFrameInfo )
    # pdb
    status = sdk.CameraSaveImage(CameraHandle, '', photoHead, pFrameInfo, 1, 100)

    print 'CameraSaveImage', status

#Todo
#CameraPlay
#CameraGetImageBuffer
#
if __name__ == '__main__':
    initCamera()
