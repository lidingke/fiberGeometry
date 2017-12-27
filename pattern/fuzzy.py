import cv2


def fuzzy_circle(img):
    #todo: fuzzy detect circle.
    img = cv2.Canny(img,15,15)
    return img