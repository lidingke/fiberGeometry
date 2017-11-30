from setting import config
from setting.config import SIMULATOR_IMG_SERVER_COFIG

from .mdpy import GetRawImg

from threading import Thread
from simulator.server import SeverMain
from simulator.client import Client
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
import numpy as np
import time
import logging
logger = logging.getLogger(__name__)

class DynamicGetRawImgTest(GetRawImg):
    """docstring for getRawImg"""
    def __init__(self, host = False, port = False):
        # super(GetRawImgTest, self).__init__()
        # self.host, self.port = host, port
        shost, sport, method, path = config.SIMULATOR_IMG_SERVER_COFIG
        print "load", config.SIMULATOR_IMG_SERVER_COFIG
        if not host:
            host = shost
        if not port:
            port = sport
        args = (host, port,method,path,)
        # print args,type(args)
        Thread(target=SeverMain, args=args).start()

    def get(self):
        try:
            result = IOLoop.current().run_sync(Client().get_img_once)
        except StreamClosedError:
            logger.warning("Lost host at client %s")
            return
        except ValueError as e:
            print e
            return
        if len(result) == 15116544:
            img = np.frombuffer(result, dtype = 'uint8')
            img.shape = (1944, 2592, 3)
            return img

    def release_camera(self):
        IOLoop.current().run_sync(Client().close_server)

