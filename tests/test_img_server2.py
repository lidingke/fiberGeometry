from imgserver.client import send_message, clientmain
from imgserver.server import ImgServer, servermain
from threading import Thread
import multiprocessing
from tornado.ioloop import IOLoop

def test_imgserver():
    # Thread(target = servermain).start()
    multiprocessing.Process(target=servermain).start()
    clientmain()
    # IOLoop.current().stop()
    # IOLoop.current().close()