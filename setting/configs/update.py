import pdb

from setting.config import CONFIGS_DIR
from setting import config
from util.load import WriteReadJson

import logging
logger = logging.getLogger(__name__)


def update_config_by_json(module,json_dir):
    # json_dir = CONFIGS_DIR+json_name+".json"
    # d = {"MODBUS_PORT":"com14",}
    j = WriteReadJson(json_dir)
    d = j.load()
    [module.__setattr__(k.decode('utf-8'),v) for k,v in d.items()]
    # pdb.set_trace()


def update_config_by_name(name="static"):
    json_dir = CONFIGS_DIR+name+".json"
    # logger.info(json_dir)
    update_config_by_json(config,json_dir)
    str_dict_keys = [k for k in dir(config) if k[0].isupper()]
    str_dict = {k: config.__dict__[k] for k in str_dict_keys}
    strs = ["=>{}:{}".format(k, v) for k,v in str_dict.items()]
    strs_info = json_dir+":\n    "+"\n    ".join(strs)
    return strs_info

