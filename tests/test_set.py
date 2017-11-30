from setting.config import CONFIGS_DIR
from setting.configs.tool import update_config_by_json, update_config_by_name
from setting.parameter import SETTING, singleton, ClassifyParameter
from setting import config
from util.zombie import ZombieSingleton

SETTING().update_by_key('G652')

def test_other_set():
    s = SETTING('G652')
    print s.store
    assert 'G652' == s.get('fiberType')
    s = SETTING('octagon')
    print s.store
    print 'singleton2', id(s)
    assert 'octagon' != s.get('fiberType')

def test_get_new_value():
    s = SETTING("printline")
    s["newkey"] = True
    assert s.get("newkey")


def test_zombiesigleton():
    a , b, c  = ZombieSingleton('a'), ZombieSingleton('b'), ZombieSingleton('a'),
    assert id(a) != id(b)
    assert id(a) == id(c)
# def test_updateSets_args():
#     s = SETTING("Default")
#     s.update_by_key()
#     assert "set" not in s.keys()
#     assert "testsetdict" not in s.keys()
#     s.update_by_key("set", {"testsetdict": "dict"})
#     assert s.get("testset") == ".json"
#     assert s.get("testsetdict") == "dict"
#
# def test_updateSets_kwargs():
#     s = SETTING("Default")
#     assert 'testkwargs' not in s.keys()
#     s.update_by_key(testkwargs='get')
#     assert s.get('testkwargs') == 'get'

def test_updateSets_Exception():
    s = SETTING("Default")
    try:
        s.update_by_key(1)
    except Exception, e:
        assert isinstance(e, ValueError)


# def test_updatekeys():
#     s = SETTING()
#     s.update_by_key('20/400')
#     assert s.get('fiberType') == "20/400"
#     s.update_by_key('20/130(oc)')
#     assert s.get('fiberType') == "20/130(oc)"
#     s.update_by_key('G652')
#     assert s.get('fiberType') == "G652"

def test_update_config_by_json():
    json_dir = CONFIGS_DIR+"static"+".json"
    # assert config.FOR_UNIT_TEST == False

    update_config_by_json(config,json_dir)
    config_flag =  config.FOR_UNIT_TEST
    config_flag_not = not config_flag
    config.FOR_UNIT_TEST = config_flag_not
    assert config_flag != config_flag_not
    update_config_by_json(config,json_dir)
    assert config.FOR_UNIT_TEST == config_flag



def test_update_config_by_name():
    config.FOR_UNIT_TEST = False
    assert config.FOR_UNIT_TEST == False
    update_config_by_name()
    assert config.FOR_UNIT_TEST == True


def test_classify_parameter():
    fiberType = "G652"
    sets = ClassifyParameter()
    sets.update_by_key(fiberType)
    assert fiberType == "G652"
    index = sets['ampPixSize']
    fiberType = "capillary"
    sets.update_by_key(fiberType)
    assert fiberType == "capillary"
    assert index != sets['ampPixSize']


if __name__ == '__main__':
    # from setting.orderset import SETTING
    # s = SETTING({})
    # print s
    # del SETTING
    # import SETTING
    # from setting.orderset import SETTING
    test_update_config_by_name()