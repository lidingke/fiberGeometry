from pattern.getimg import randomImg, getImage
from pattern.sharp import corner_noise, take_white_light_in_core


def test_corner_noise():
    img = randomImg("IMG\\20400\\396\\")
    assert corner_noise(img,300) > 0

def test_take_white_light_in_core():
    img = getImage("IMG\\20400\\size1.bmp")
    print take_white_light_in_core(img,800)



if __name__ == '__main__':
    print "noise"
    test_take_white_light_in_core()