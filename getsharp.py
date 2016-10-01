from SDK.piezo import Piezo
from SDK.mindpy import GetRawImg, IsInitCamera
from method.sharp import IsSharpRuntime
import time
if __name__ == '__main__':
    pie = Piezo()
    getimg = GetRawImg()
    isinitCamera = IsInitCamera()
    issharp = IsSharpRuntime()
    # if isinitCamera.isInit():
    imglist = []
    sharplist = []
    for x in range(1,10):
        # imglist.append()
        img = getimg.get()
        imglist.append(img)
        pie.setV(x * 10)
        voltage = pie.getV()
        sharplist.append((voltage, issharp.isSharp(img)))
        # sharplist.append((voltage, issharp.isSharpCanny(img)))
        time.sleep(0.5)
    for sharp in sharplist:
        print 'sharp:',sharp
    # else:
    #     print 'no camera'

