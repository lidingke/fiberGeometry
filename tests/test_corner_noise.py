from util.getimg import randomImg, getImage
from pattern.sharp import corner_noise, take_white_light_in_core, black_points


def test_corner_noise():
    """unit test case for corner_noise"""
    img = randomImg("IMG\\20400\\396\\")
    assert corner_noise(img,300) > 0

def test_black_points():
    """unit test case for black_points"""
    img = randomImg("IMG\\20400\\396\\")
    assert black_points(img) >10
    img = randomImg("IMG\\200210\\nomid\\")
    assert black_points(img)<10


def test_take_white_light_in_core():
    """unit test case for take_white_light_in_core"""
    img = getImage("IMG\\20400\\size1.bmp")
    print take_white_light_in_core(img,800)



if __name__ == '__main__':
    print "noise"
    test_take_white_light_in_core()