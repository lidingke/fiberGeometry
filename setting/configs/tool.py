import os
from setting.config import CONFIGS_DIR
from setting import config
from util.loadfile import WriteReadJson

import logging

logger = logging.getLogger(__name__)


def safe_argvs():
    paras = os.listdir(CONFIGS_DIR)
    return [p.split('.')[0] for p in paras if p.split('.')[-1] == 'json']


SAFE_ARGVS = safe_argvs()


def update_config_by_json(module, json_dir):
    j = WriteReadJson(json_dir)
    d = j.load()
    [setattr(module, k.decode('utf-8'), v) for k, v in d.items()]


def update_config_by_name(name="static"):
    if name not in SAFE_ARGVS:
        raise ValueError("safe argvs error {} {}:\n".format(name, SAFE_ARGVS) + " ".join(SAFE_ARGVS))
    json_dir = CONFIGS_DIR + name + ".json"
    update_config_by_json(config, json_dir)
    str_dict_keys = [k for k in dir(config) if k[0].isupper()]
    str_dict = {k: config.__dict__[k] for k in str_dict_keys}
    strs = ["=>{}:{}".format(k, v) for k, v in str_dict.items()]
    strs_info = "\n" + json_dir + ":\n    " + "\n    ".join(strs)
    return strs_info
