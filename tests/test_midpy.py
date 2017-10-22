from setting.parameter import SETTING
SETTING("")
import SDK.MindPy as mdp
from SDK.mdpy import GetRawImg
import time
import numpy as np

def test_MindPy_pyd():
    print dir(mdp)
    assert hasattr(mdp, "getCameraSerial")
    assert hasattr(mdp, "getRawImg")
    assert hasattr(mdp, "initCamera")
    assert hasattr(mdp, "uninitCamera")


def test_init_release_camera():
    try:
        get = GetRawImg()
    except ValueError as e:
        assert str(e)[-2:] == '16'
    else:
        get.release_camera()
    # time.sleep(0.3)
    try:
        get = GetRawImg()
    except ValueError as e:
        assert str(e)[-2:] == '16'
    else:
        get.release_camera()

def test_camera_get():
    try:
        get = GetRawImg()
    except ValueError as e:
        print e
        assert str(e)[-2:] == '16'
    else:
        getnp = get.get()
        assert isinstance(getnp, np.ndarray)
        assert getnp.shape == (1944, 2592,3)
        number = get.get_camera_serial()
        assert isinstance(number, str)
        assert len(number) == 12


# def test_init



if __name__ == "__main__":
    test_camera_get()