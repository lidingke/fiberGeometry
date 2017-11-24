import cv2

from pattern.fuzzy import fuzzy_circle
from pattern.sharp import is_sharp_laplacian, is_sharp_canny
from util.getimg import random_img, random_img_by_file, get_img_by_dir, list_img_by_file


def show_img(strs, img):
    cv2.imshow(strs, img[::4, ::4])
    cv2.waitKey()


def test_fuzzy():
    for i,img in enumerate(list_img_by_file("IMG\\sharp\\oc1")):
        redimg = img[::, ::, 0]
        redlines = fuzzy_circle(redimg)
        sharpla = is_sharp_laplacian(redimg)
        sharpcanny = is_sharp_canny(redimg)

        print "{},{:2f},{},{:2f}".format(i,sharpla,sharpcanny,1000*sharpla/sharpcanny)

