from ctypes import *
from pystruct import *
import pdb

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
    status = sdk.CameraInit(pCameraList, c_int(-1), c_int(-1), pointer(CameraHandle))
    print 'CameraInit', status
    status = sdk.CameraDisplayInit(pCameraHandle, hWndDisplay)
    print 'CameraDisplayInit', status
    status = sdk.CameraUnInit(CameraHandle)


if __name__ == '__main__':
    initCamera()
