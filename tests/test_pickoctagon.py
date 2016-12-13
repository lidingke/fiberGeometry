from pattern.pickoctagon import PickOctagon
from pattern.getimg import GetImage
from pattern.edge import ExtractEdge
import cv2
import numpy as np
import pdb

import pytest

def test_pickOctagon():
    po = PickOctagon()
    img = GetImage().get('IMG\\IMG00001.BMP')
    img = ExtractEdge().run(img)
    img = po.pick(img)
    assert isinstance(img,np.ndarray)
    assert len(img.shape) == 2
    assert img.dtype == 'uint8'

    # contours = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # mergedpoints = np.concatenate(contours[1:])
    # ellipse = cv2.fitEllipse(mergedpoints)
    # print 'ellipse', ellipse

def test_pickForEllipese():
    img = GetImage().get('IMG\\IMG00001.BMP')
    img = ExtractEdge().run(img)
    img = PickOctagon().pick(img)
    contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    mergedpoints = np.concatenate(contours[1:])
    points = cv2.convexHull(points=mergedpoints)
    ellipse = cv2.fitEllipse(points)
    corea = ellipse[0][0]
    coreb = ellipse[0][1]
    logaxis = ellipse[1][1]
    shortaxis = ellipse[1][0]

    assert corea > 0
    assert coreb > 0
    assert logaxis > 0
    assert shortaxis > 0
    assert shortaxis/logaxis
    # print 'ellipse', ellipse, shortaxis, logaxis, shortaxis/logaxis

if __name__ == '__main__':
    po = PickOctagon()
    img = GetImage().get('IMG\\IMG00001.BMP')
    img = ExtractEdge().run(img)

    img = po.pick(img)
    cv2.imshow("pick", img[::2, ::2])
    cv2.waitKey(0)
    contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    mergedpoints = np.concatenate(contours[1:])
    # pdb.set_trace()
    points = cv2.convexHull(points=mergedpoints)
    ellipse = cv2.fitEllipse(points)
    print 'ellipse', ellipse