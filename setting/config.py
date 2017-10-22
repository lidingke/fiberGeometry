#coding:utf-8

import os
import logging
logger = logging.getLogger(__name__)
MODBUS_PORT = 'com3'
LED_PORT = 'com4'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logger.info('BASE_DIR:' + BASE_DIR)

VIEW_LABEL = False

PDF_PARAMETER = {}
DB_PARAMETER = {}

SAVED_VIEW_ITEMS = {}

DYNAMIC_CAMERA = True

FRAME_SIZE = (1944, 2592)
FRAME_CORE = (1296, 972)

CONFIGS_DIR = "setting\\configs\\"

FOR_UNIT_TEST = False

SAVE_TEMP_IMG = True

OCTAGON_FIBERS = ("10/130(oc)", "20/130(oc)")
CAPILLARY = ("capillary",)
THIN_FIBERS = ("200/220","105/125")

RAISE_EXCEPTION = True

SPEC_ONLINE = True

LOG_LEVEL = "ERROR"

IMG_ZOOM = 2