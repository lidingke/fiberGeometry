#coding:utf-8
from setting.parameter import SETTING
SETTING("")
import SDK.MindPy as mdp
from SDK.mdpy import GetRawImg
import time
import numpy as np

def test_MindPy_pyd():
    u"""测试接口的合法性"""
    print dir(mdp)
    assert hasattr(mdp, "get_camera_serial")
    assert hasattr(mdp, "get_raw_img")
    assert hasattr(mdp, "init_camera")
    assert hasattr(mdp, "uninit_camera")


def test_init_release_camera():
    u"""测试相机模块的释放"""
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
    u"""测试相机模块的读取"""
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