from setting.set import SETTING
import pdb
import numpy as np
import cv2
from pattern.getimg import GetImage
from pattern.edge import ExtractEdge
from pattern.classify import G652Classify
from pattern.draw import DecorateImg
from pattern.sharp import IsSharp

class Draw(object):

    def __init__(self):
        SETTING({})
        img = GetImage().get("IMG\\GIOF1\\sig")
        # pdb.set_trace()
        # self.assertIsInstance(img, np.ndarray)
        self.img = img

    def _caculate(self, img):
        # img = self.img
        origin = img
        img = ExtractEdge().run(img)
        classify = G652Classify()
        ellipses = classify.find(img)
        result = classify.getResult()
        origin = cv2.cvtColor(origin, cv2.COLOR_GRAY2RGB)
        # origin = np.ones_like(origin)*255
        # origin = np.zeros_like(origin)
        # cv2.ellipse(origin, ellipses['clad'], (131,210,253), 5, lineType=2)#(162,183,0)(green, blue, red)
        # cv2.ellipse(origin, ellipses['core'], (0,102,255), 5, lineType=2)#255,102,0#FF6600
        # corex,corey = ellipses['core'][0]
        # core = (int(corex), int(corey))
        # coreR = str(result[2])
        # print ('core to show', coreR)
        # cv2.putText(origin, coreR, core,
        #             cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,255), thickness=3)
        print 'ellipse', ellipses
        origin = DecorateImg(origin, ellipses, result)
        print 'result', result
        return origin
        # pdb.set_trace()


    def show(self):
        img = self.img
        img = self._caculate(img)
        cv2.imshow('img', img[::4,::4,::])
        cv2.waitKey(0)


if __name__ == "__main__":
    d = Draw()
    d.show()