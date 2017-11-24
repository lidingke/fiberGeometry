import cv2


def fuzzy_circle(img):
    img = cv2.Canny(img,15,15)
    return img