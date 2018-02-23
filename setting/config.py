# coding:utf-8

import os
import logging

logger = logging.getLogger(__name__)

"""serials port number"""
u"""电机的串口，LED的串口"""
MODBUS_PORT = 'com3'
LED_PORT = 'com4'

"""key directions"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logger.info('BASE_DIR:' + BASE_DIR)
CONFIGS_DIR = "setting\\configs\\"
# VIEW_LABEL = False

"""global parameter cache"""
u"""用来保存生成PDF的参数和存入数据库的参数，
这两个参数在多个类中共享，所以设成全局的，实际上是不好的搞法。"""
PDF_PARAMETER = {}
DB_PARAMETER = {}

SAVED_VIEW_ITEMS = {}
SQLALCHEMY_DIR = "sqlite:///setting/relation_result.db"

"""camera configs"""
u"""相机相关的配置
配置了相机使能，一帧图片分辨率，一帧图片中心，缩放比例"""
DYNAMIC_CAMERA = True

FRAME_SIZE = (1944, 2592)
FRAME_CORE = (1296, 972)
IMG_ZOOM = 2

"""unit tests configs"""
FOR_UNIT_TEST = False
RAISE_EXCEPTION = True
SAVE_TEMP_IMG = True

u"""模拟器用的相关端口和图片地址"""
# SIMULATOR_IMG_DIR = ('randomImg', 'IMG/G652/0912R/')
SIMULATOR_IMG_SERVER_COFIG = ('127.0.0.1', 9880, 'randomImg', 'IMG/G652/0912R/')

OCTAGON_FIBERS = ("10/130(oc)", "20/130(oc)", "20/400(oc)")
CAPILLARY = ("capillary",)
THIN_FIBERS = ("200/220", "105/125")

SPEC_ONLINE = True

"""logging level:DEBUG INFO WARNING ERROR CRITICAL"""
LOG_LEVEL = "ERROR"

"""if manual flag is false ,use SPECT_CONTINUE to set args automaticlly"""
u"""配置光谱仪参数模式，是手动选择光谱仪参数还是自动选择光谱仪参数。
FLAG设置为True时，需要在界面上手动设置光谱仪的时长。
FLAG设置为False时，自动根据光纤长度设置光谱仪时长。"""
MAMUAL_SPECT_ARGS_FLAG = True
SPECT_CONTINUE = (
    (0,50000),
    (20,100000),
    (30,200000),
    (40,300000))

