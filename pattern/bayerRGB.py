# from setting.set import SETTING
import pdb
import numpy as np
import cv2
from pattern.getimg import GetImage
from pattern.edge import ExtractEdge
from pattern.sharp import IsSharp
from SDK.mdpy import GetRawImg

method = [cv2.COLOR_BAYER_BG2BGR,
          cv2.COLOR_BAYER_BG2RGB,
          cv2.COLOR_BAYER_GB2BGR,
          cv2.COLOR_BAYER_GR2RGB,
          cv2.COLOR_BAYER_GB2RGB,
          cv2.COLOR_BAYER_GR2BGR,
          ]

def get():
    shape = (1944, 2592)
    getnp = np.fromfile("tests\\data\\imgblue.bin", dtype="uint8")
    getnp.shape = shape
    for m in method[2:-2]:
        img = getnp.copy()
        img = cv2.cvtColor(img, m)
        cv2.imshow(str(m), img[::8, ::8])
        cv2.waitKey(0)


def getNp():
    grt = GetRawImg()
    img = grt.get()
    grt.unInitCamera()
    pdb.set_trace()
    img.tofile("tests\\data\\imggreen.bin")
    img = cv2.cvtColor(img, cv2.COLOR_BAYER_GR2RGB)
    cv2.imshow('img', img[::8, ::8])
    cv2.waitKey(0)



if __name__ == "__main__":
    getNp()
    # get()
