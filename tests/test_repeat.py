from __future__ import division
from pattern.octagon import ClassOctagon
from pattern.edge import ExtractEdge
import cv2
from test_edge2img import edge2img, yieldImg
from pattern.getimg import GetImage
import numpy as np
from pattern.edge import EdgeFuncs
import pdb
from setting.orderset import SETTING


if __name__ == '__main__':

    sets = SETTING({"ampFactor": "20X", "cameraID": "MindVision500"})
    resultget = []
    for img in yieldImg("IMG\\octagon\\500s\\"):
        img = ExtractEdge().run(img)
        img = cv2.medianBlur(img, 11)
        result = ClassOctagon().run(img)
        _1, _2 = result['corePoint'][0].tolist()
        radius = result['longAxisLen'] + result['shortAxisLen'] / 2
        resultget.append([_1, _2, radius])

    resultarray = np.array(resultget)
    print resultarray
    std  = np.std(resultarray, axis= 0 )
    print std * 0.088