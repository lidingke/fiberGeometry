import pdb
from time import sleep

from SDK.mdpy import GetRawImg
from SDK.modbus.ledmodes import LEDMode
from pattern.classify import classifyObject


def test_repeat_for_a_20400():
    from setting.orderset import SETTING
    SETTING().updates('20/400')
    print SETTING()
    mode = LEDMode("com4")
    classify = classifyObject("20/400")
    img_get = GetRawImg()
    current = 150
    for i in range(10):
        img = img_get.get()
        result = classify.find(img)
        # pdb.set_trace()
        print result['showResult']
        now_current = current + i * 10
        mode.set_current(c1st=now_current, c2st=500, c3st=200, savemode=True)
        sleep(10)


if __name__ == '__main__':
    test_repeat_for_a_20400()
