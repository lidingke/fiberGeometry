from time import sleep

import cv2

from SDK.mdpy import GetRawImg
from SDK.modbus.ledmodes import LEDMode


def test_create_background_light_by_current():
    img_mode = GetRawImg()
    mode = LEDMode("com4")
    lights = []
    currents = []
    for i in range(100,350,50):
        sleep(20)

        redlight = i
        mode.set_current(c1st=redlight, c2st=500, c3st=200, savemode=True)  # 当前红光光强800
        img = img_mode.get()
        red = (img[::, ::, 0]).sum() / (255 * 1544 * 3)
        cv2.imwrite(img,str(i)+'.png')
        lights.append(red)
        currents.append(redlight)
        print redlight,red

    plt.plot(currents, lights)

    # plt.plot(self.dict.keys(),self.dict.values())
    plt.title("light")
    plt.show()