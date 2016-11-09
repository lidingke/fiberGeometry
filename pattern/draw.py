import numpy as np
import cv2


def DecorateImg(origin, ellipses, result):
    if len(origin.shape)<3:
        print 'origin shape', origin.shape
        origin = cv2.cvtColor(origin, cv2.COLOR_GRAY2RGB)
    # origin = np.ones_like(origin)*255
    # origin = np.zeros_like(origin)
    print 'ellipses result', ellipses, result
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
    print ('clad', coreR, core)
    cv2.putText(origin, coreR, core,
                cv2.FONT_HERSHEY_SIMPLEX, 2, (215, 207, 39), thickness=3)
    #clad radius
    corex, corey = ellipses['clad'][0]
    radius = ellipses['clad'][1]
    radius = (radius[0]+radius[1])/4
    core = (int(corex + radius*0.7), int(corey - radius*0.7))
    coreR = "%4.2f"%result[2]
    print ('clad', coreR, core)
    cv2.putText(origin, coreR, core,
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=3)
    # corex, corey = result[0], result[1]
    return  origin
