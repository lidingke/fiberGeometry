from setting.orderset import SETTING, singleton
import unittest



class TestDom1(unittest.TestCase):
    def setUp(self):
        self.s = SETTING("printline")

    def test_get_in(self):
        s = self.s
        assert s.keys()
        # assert not s.keys()
        assert "ampPixSize" in s.keys()
        assert 'overdom' not in s.keys()
        s['overdom'] = True

class TestDom2(unittest.TestCase):
    def setUp(self):
        self.s = SETTING("octagon", "printline")

    def test_get_out(self):
        s = self.s
        # print singleton.instance
        print 'dom2', s.get("fiberType")
        assert s.get("fiberType") == "octagon"
        assert 'overdom' in s.keys()
        assert s.get('overdom')



def test_get_new_value():
    s = SETTING("printline")
    s["newkey"] = True
    assert s.get("newkey")

def test_updateSets_args():
    s = SETTING("Default")
    s.updates()
    assert "set" not in s.keys()
    assert "testsetdict" not in s.keys()
    s.updates("set", {"testsetdict": "dict"})
    assert s.get("testset") == ".json"
    assert s.get("testsetdict") == "dict"

def test_updateSets_kwargs():
    s = SETTING("Default")
    assert 'testkwargs' not in s.keys()
    s.updates(testkwargs='get')
    assert s.get('testkwargs') == 'get'

def test_updateSets_Exception():
    s = SETTING("Default")
    try:
        s.updates(1)
    except Exception, e:
        assert isinstance(e, ValueError)



if __name__ == '__main__':
    # from setting.orderset import SETTING
    # s = SETTING({})
    # print s
    # del SETTING
    # import SETTING
    # from setting.orderset import SETTING
    pass