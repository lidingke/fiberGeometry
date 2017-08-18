#coding:utf-8
import pdb
import random
from time import sleep

import cv2
import logging
logger = logging.getLogger(__name__)
from pattern.classify import classifyObject
import matplotlib;matplotlib.use("Qt4Agg")
import matplotlib.pyplot as plt
from SDK.mdpy import GetRawImg
from SDK.modbus.ledmodes import LEDMode


def test_create_background_light_by_current():
    img_mode = GetRawImg()
    mode = LEDMode("com4")
    classify = classifyObject("20400")
    lights = []
    currents = []
    clads = []
    ranges = (150,230)
    for i in range(30):

        current = random.randint(*ranges)
        mode.set_current(c1st=current, c2st=500, c3st=200, savemode=True)  # 当前红光光强800
        sleep(30)
        img = img_mode.get()
        result = classify.find(img)
        clad = result["showResult"][2]
        # print result["showResult"]
        light = (img[::, ::, 0]).sum() / (255 * 1544 * 3)
        cv2.imwrite('tests\\data\\1.bmp',img)
        lights.append(light)
        currents.append(current)
        clads.append(clad)
        logger.error('{},{},{:0.2f}'.format(current,light,clad))

        for x,y,z in zip(currents,lights,clads):
            print '{},{},{:0.2f}'.format(x,y,z)

    # plt.plot(currents, lights)
    # plt.axes()
    # #
    # # # plt.plot(self.dict.keys(),self.dict.values())
    # plt.title("light")
    # plt.show()

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    test_create_background_light_by_current()