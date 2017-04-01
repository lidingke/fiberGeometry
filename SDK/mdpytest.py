from .mdpy import GetRawImg
from threading import Thread
from imgserver.server import SeverMain
from imgserver.client import Client
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
        # time.sleep(0.01)
        try:
            result = IOLoop.current().run_sync(Client().get_img_once)
        except StreamClosedError:
            logger.warning("Lost host at client %s")
            return
        except ValueError as e:
            print e
            # IOLoop.current().run_sync(Client().close_server)
            # Thread(target=SeverMain, args=(self.port,)).start()
            # logger.info("select number full")
            return
        if len(result) == 15116544:
            img = np.frombuffer(result, dtype = 'uint8')
            img.shape = img.shape = (1944, 2592, 3)
            return img

    def unInitCamera(self):
        pass

