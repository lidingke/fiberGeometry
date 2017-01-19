import cv2
import numpy as np
import pdb
from pattern.edge import ExtractEdge
from util.toolkit import cv2CircleIndex



def test_thres():
    img = np.fromfile("tests\\data\\midcoreafterdif.bin",dtype='uint8')
    img.shape = [1944,2592]
    size, img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    # pdb.set_trace()
    # img = ExtractEdge().run(img)
    img = cv2.bitwise_not(img)
    contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    assert len(contours) < 4
    # pdb.set_trace()


if __name__ == "__main__":
    test_thres()