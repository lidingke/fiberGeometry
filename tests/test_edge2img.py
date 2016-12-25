from pattern.edge import ExtractEdge
from pattern.getimg import GetImage
import cv2
import numpy as np
import os
from pattern.edge import EdgeFuncs

def edge2img(dirs):
    dirlist = os.listdir(dirs)
    dirlist = [dirs + x for x in dirlist]
    imgs = []
    for dir_ in dirlist:
        img = GetImage().get(dir_)
        imgs.append(img)
    imgAllor = np.zeros(imgs[0].shape, dtype=imgs[0].dtype)
    for img in imgs:
        img = ExtractEdge().run(img)
        imgAllor = cv2.bitwise_or(imgAllor, img)
    img = imgAllor
    img = EdgeFuncs().open(img, 10)
    img = cv2.medianBlur(img, 3)
    return img


def yieldImg(dirs):
    dirlist = os.listdir(dirs)
    dirlist = [dirs + x for x in dirlist]
    for dir_ in dirlist:
        img = GetImage().get(dir_)
        yield  img

if __name__ == "__main__":
    img = edge2img("IMG\\octagon\\500s\\")
    cv2.imshow("bitwise_not", img[::4, ::4])
    cv2.waitKey(0)