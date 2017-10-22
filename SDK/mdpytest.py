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
    def __init__(self, host = '127.0.0.1', port = 9880):
        # super(GetRawImgTest, self).__init__()
        self.host, self.port = host, port
        Thread(target=SeverMain, args=(self.port,)).start()

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
            img.shape = img.shape = (1944, 2592, 3)
            return img

    def release_camera(self):
        pass

