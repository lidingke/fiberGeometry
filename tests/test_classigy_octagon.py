from setting.orderset import SETTING
SETTING('MindVision500', 'test', 'octagon','centerImg')

import cv2
import numpy as np
import pdb

from pattern.classify import OctagonClassify




if __name__ == '__main__':
    img = np.fromfile("tests\\data\\dynamicimg.bin", "uint8")
    img.shape = SETTING().get("imgsize",(1944,2592))
    oca = OctagonClassify().find(img)
    plot = oca['coreResult']['plot']
    print 'shape', plot.shape
    print oca['coreResult']['longAxisLen'], oca['coreResult']['shortAxisLen'], oca["coreResult"]["corePoint"]
    print oca['cladResult']['longAxisLen'], oca['cladResult']['shortAxisLen'], oca["cladResult"]["corePoint"]
    cv2.imshow('core', plot[::4,::4])
    cv2.waitKey()
    cv2.imshow('clad', oca['cladResult']['plot'][::4,::4])
    cv2.waitKey()
    # pdb.set_trace()