import cv2

from util.getimg import random_img, random_img_by_file


def show_img(strs,img):
    cv2.imshow(strs,img[::4,::4])
    cv2.waitKey()

def test_fuzzy():
    img = random_img_by_file("IMG\\emptytuple\\sharp")
    show_img("1",img)