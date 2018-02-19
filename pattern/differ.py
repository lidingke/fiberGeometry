from setting.parameter import SETTING
# SETTING('test')
import cv2
import numpy as np
from util.getimg import getImage
import pdb


def getFilterImg(core, origin, minRange, maxRange):
    img = np.ones(origin.shape, dtype='uint8') * 255
    core = [core, 1]
    cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(maxRange), (0, 0, 0), -1)
    cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(minRange), (255, 255, 255), -1)

    img = cv2.bitwise_or(img, origin)
    return img


def getCircleMeans(circle, origin):
    if len(circle) != 2:
        raise ValueError('circle length error')
    core, radius = circle
    x, y = core
    x, y = int(x), int(y)
    getpoint = []
    getpoint.append((x + radius, y + radius))
    getpoint.append((x - radius, y + radius))
    getpoint.append((x + radius, y - radius))
    getpoint.append((x - radius, y - radius))

    def getPoints(point, range_=3):
        points = []
        for i in range(0, range_):
            for j in range(0, range_):
                points.append((point[0] + i, point[1] + j))
        return points

    getedPoints = []
    for _ in getpoint:
        getedPoints.extend(getPoints(_))
    means = []
    for x, y in getedPoints:
        _ = origin[x, y]
        means.append(_)
        print 'indexs', x, y, _
    means.sort()
    means = means[1:-1]
    return int(sum(means) / len(means))


def getFilterColorImg(core, origin, minRange, maxRange):
    outerCircle = [core, maxRange]
    innerCircle = [core, minRange]
    corex, corey = core
    outer = getCircleMeans(outerCircle, origin)
    inner = getCircleMeans(innerCircle, origin)
    img = np.ones(origin.shape, dtype='uint8') * outer
    cv2.circle(img, corex, corey, maxRange, (0, 0, 0), -1)


def differCore():
    img = getImage("IMG\\midoc.BMP")
    print 'get shape', img.shape
    corecore = SETTING()["corepoint"]
    print getCircleMeans((corecore, 10), img)
    minRange, maxRange = SETTING()["coreRange"]
    img = getFilterImg(corecore, img, minRange, maxRange)
    print getCircleMeans((corecore, 100), img)


if __name__ == "__main__":
    differCore()
