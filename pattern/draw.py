from __future__ import  division
import numpy as np
import cv2
from setting.orderset import SETTING

def newDecorateImg(origin, ellipses, result):
    # print ellipses.keys()
    if len(origin.shape)<3:
        origin = cv2.cvtColor(origin, cv2.COLOR_GRAY2RGB)
    if not (ellipses or result):
        return origin
    x, y = ellipses['cladResult']['longPlot']
    cv2.line(origin, x, y, (25,255,0), 8)
    x, y = ellipses['cladResult']['shortPlot']
    cv2.line(origin, x, y, (25, 200, 0), 8)
    # cv2.ellipse(origin, ellipses['clad'], (131, 210, 253), 5, lineType=2)  # (162,183,0)(green, blue, red)
    cv2.ellipse(origin, ellipses['core'], (0, 102, 255), 5, lineType=2)  # 255,102,0#FF6600
    corex, corey = ellipses['core'][0]
    # radius = ellipses['core'][1]
    radius = ellipses['coreResult']['shortAxisLen']
    core = (int(corex + radius * 0.7), int(corey - radius * 0.7))
    coreR = "%4.2f" % result[1]
    cv2.putText(origin, coreR, core,
                cv2.FONT_HERSHEY_SIMPLEX, 2, (215, 207, 39), thickness=3)
    corex, corey = ellipses['clad'][0]
    radius = ellipses['cladResult']['shortAxisLen']
    core = (int(corex + radius * 0.5), int(corey - radius * 0.5))
    coreR = "%4.2f" % result[2]
    cv2.putText(origin, coreR, core,
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=3)
    return origin

def DecorateImg20400(origin, ellipses, result):
    # print ellipses.keys()
    if len(origin.shape)<3:
        origin = cv2.cvtColor(origin, cv2.COLOR_GRAY2RGB)
    cv2.ellipse(origin, ellipses['clad'], (0, 102, 255), 5, lineType=2)
    # cv2.ellipse(origin, ellipses['clad'], (131, 210, 253), 5, lineType=2)  # (162,183,0)(green, blue, red)
    cv2.ellipse(origin, ellipses['core'], (0, 102, 255), 5, lineType=2)  # 255,102,0#FF6600
    corex, corey = ellipses['core'][0]
    # radius = ellipses['core'][1]
    radius = ellipses['coreResult']['shortAxisLen']
    core = (int(corex + radius * 0.7), int(corey - radius * 0.7))
    coreR = "%4.2f" % result[1]
    cv2.putText(origin, coreR, core,
                cv2.FONT_HERSHEY_SIMPLEX, 2, (215, 207, 39), thickness=3)
    corex, corey = ellipses['clad'][0]
    radius = ellipses['cladResult']['shortAxisLen']
    core = (int(corex + radius * 0.5), int(corey - radius * 0.5))
    coreR = "%4.2f" % result[2]
    cv2.putText(origin, coreR, core,
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=3)
    return origin

def oldDecorateImg(origin, ellipses, result):
    if len(origin.shape)<3:
        print 'origin shape', origin.shape
        origin = cv2.cvtColor(origin, cv2.COLOR_GRAY2RGB)
    # origin = np.ones_like(origin)*255
    # origin = np.zeros_like(origin)
    # print 'ellipses result', ellipses, result
    if not (ellipses or result):
        return origin
    cv2.ellipse(origin, ellipses['clad'], (131, 210, 253), 5, lineType=2)  # (162,183,0)(green, blue, red)
    cv2.ellipse(origin, ellipses['core'], (0, 102, 255), 5, lineType=2)  # 255,102,0#FF6600
    #core radius
    corex, corey = ellipses['core'][0]
    radius = ellipses['core'][1]
    radius = (radius[0]+radius[1])/4
    core = (int(corex + radius*0.7), int(corey - radius*0.7))
    coreR = "%4.2f"%result[1]
    # print ('clad', coreR, core)
    cv2.putText(origin, coreR, core,
                cv2.FONT_HERSHEY_SIMPLEX, 2, (215, 207, 39), thickness=3)
    #clad radius
    corex, corey = ellipses['clad'][0]
    radius = ellipses['clad'][1]
    radius = (radius[0]+radius[1])/4
    core = (int(corex + radius*0.7), int(corey - radius*0.7))
    coreR = "%4.2f"%result[2]
    # print ('clad', coreR, core)
    cv2.putText(origin, coreR, core,
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=3)
    # corex, corey = result[0], result[1]
    return  origin

def DecorateImg(origin, ellipses, result):
    if SETTING().get("fiberType") == "20400":
        return DecorateImg20400(origin, ellipses, result)
    if isinstance(ellipses, dict):
        return newDecorateImg(origin, ellipses, result)
    else:
        return oldDecorateImg(origin, ellipses, result)


def drawCoreCircle(img):
    SET = SETTING()
    corecore = SET.get("corepoint",(1296,972))
    core = [corecore,1]
    # print "corecorex, corecorey", corecorex, corecorey
    minRange, maxRange = SET.get("coreRange")

    # cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(maxRange), (255, 255, 255), 4)
    cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(minRange), (0,0,0), 4)
    x0,y0 = corecore
    x1, y1 = x0 + minRange, y0
    x2, y2 = x0 + maxRange, y0
    cv2.line(img, (x1,y1), (x2,y2), (255,255,255), 4)
    x1, y1 = x0, y0 + minRange
    x2, y2 = x0, y0 + maxRange
    cv2.line(img, (x1,y1), (x2,y2), (255,255,255), 4)
    x1, y1 = x0 - minRange, y0
    x2, y2 = x0 - maxRange, y0
    cv2.line(img, (x1,y1), (x2,y2), (255,255,255), 4)
    x1, y1 = x0, y0 - minRange
    x2, y2 = x0, y0 - maxRange
    cv2.line(img, (x1,y1), (x2,y2), (255,255,255), 4)

    # minRange, maxRange = SET.get("cladRange")
    # cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(maxRange), (0, 0, 0), 4)
    # cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(minRange), (255, 255, 255), 4)
    return img