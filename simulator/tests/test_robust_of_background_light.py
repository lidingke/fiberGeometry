#coding:utf-8
import pdb
import random
from time import sleep

import cv2
import logging

from pattern.sharp import corner_noise, take_white_light_in_core

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

def test_background_light_noise_by_current():
    mode = LEDMode("com4")
    img_mode = GetRawImg()

    for current in range(30,60,2):
        mode.set_current(c1st=current, c2st=500, c3st=200, savemode=True)
        sleep(10)
        img = img_mode.get()
        noise = corner_noise(img,300)
        logger.error('{}:{:0.2f}'.format(current,noise))


def test_white_light_in_core_by_current():
    mode = LEDMode("com4")
    img_mode = GetRawImg()
    lights = []
    for current in range(150,300,10):
        mode.set_current(c1st=50, c2st=500, c3st=current, savemode=True)
        sleep(3)
        img = img_mode.get()
        light1 = take_white_light_in_core(img,300,0)
        light2 = take_white_light_in_core(img,300,1)
        light3 = take_white_light_in_core(img,300,2)
        # logger.error('{}:{:0.2f}:{:0.2f}:{:0.2f}'.format(current,light1,light2,light3))
        print '{},{:0.2f},{:0.2f},{:0.2f}'.format(current,light1,light2,light3)
        lights.append((light1,light2,light3))

    # plt.plot(currents, lights)
    # plt.axes()
    # #
    # # # plt.plot(self.dict.keys(),self.dict.values())
    # plt.title("light")
    # plt.show()

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    # test_background_light_noise_by_current()
    # test_white_light_in_core_by_current()
    mode = LEDMode("com4")
    mode.set_current(c1st=36, c2st=500, c3st=200, savemode=True)