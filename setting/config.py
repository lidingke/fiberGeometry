#coding:utf-8

import os
import logging
logger = logging.getLogger(__name__)

"""serials port number"""
MODBUS_PORT = 'com3'
LED_PORT = 'com4'

"""key directions"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logger.info('BASE_DIR:' + BASE_DIR)
CONFIGS_DIR = "setting\\configs\\"
# VIEW_LABEL = False

"""global parameter cache"""
PDF_PARAMETER = {}
DB_PARAMETER = {}

SAVED_VIEW_ITEMS = {}

""" camera configs"""
DYNAMIC_CAMERA = True

FRAME_SIZE = (1944, 2592)
FRAME_CORE = (1296, 972)
IMG_ZOOM = 2


"""unit tests configs"""
FOR_UNIT_TEST = False
RAISE_EXCEPTION = True
SAVE_TEMP_IMG = True

SIMULATOR_IMG_DIR = ('randomImg', 'IMG/G652/0912R/')

OCTAGON_FIBERS = ("10/130(oc)", "20/130(oc)","20/400(oc)")
CAPILLARY = ("capillary",)
THIN_FIBERS = ("200/220","105/125")

SPEC_ONLINE = True

LOG_LEVEL = "ERROR"

