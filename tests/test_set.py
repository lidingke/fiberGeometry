from setting.orderset import SETTING


def test_get_new_value():
    s = SETTING("MindVision500")
    print 'get if carmera'
    assert isinstance(s.get("ifcamera"), bool)
    s["newkey"] = True
    assert s.get("newkey")

if __name__ == '__main__':
    # from setting.orderset import SETTING
    # s = SETTING({})
    # print s
    # del SETTING
    # import SETTING
    # from setting.orderset import SETTING

    s = SETTING({'ampFactor':'20X','cameraID':'MindVision500'})

    # s = SETTING("MindVision500","20X")
    print s, s.get("ifcamera"), s.get("ampPixSize")