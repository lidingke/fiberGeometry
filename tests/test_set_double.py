from setting.orderset import SETTING


def test_multi_set():
    s = SETTING('octagon','test','printline')
    assert 'ifcamera' in s.keys()
    print 'get camera', s.get('ifcamera')
    assert not s.get('ifcamera')
    assert s.get('fiberType') == "octagon"
    print s
    SETTING('octagon',  'printline')


if __name__ == "__main__":
    test_multi_set()