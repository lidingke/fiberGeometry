from __future__ import print_function
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.tcpclient import TCPClient
from tornado.options import options, define
import numpy as np
import json
import cv2
import time
from threading import Thread
from functools import partial
define("host", default="localhost", help="TCP server host")
define("portc", default=9888, help="TCP port to connect to")
define("message", default="getimgonce", help="Message to send")
port = 9880

@gen.coroutine
def send_message():
    stream = yield TCPClient().connect("localhost", port)
    yield stream.write(("getimgonce" + "\n\r").encode())
    print("Sent to server:", "getimgonce")
    data = yield stream.read_until("\n\r")
    rawdata = np.fromstring(data.strip(), dtype=np.uint8)
    # rawdata =
    print("Response from server:", len(rawdata))
    # rawdata.shape = (1944, 2592, 3)
    # cv2.imshow('img', rawdata[::4,::4])
    # cv2.waitKey()

@gen.coroutine
def get_change():
    stream = yield TCPClient().connect("localhost", port)
    para = ('getImage', 'IMG/midoc.BMP')
    cmd = 'change:' + json.dumps(para) + '\n\r'
    yield stream.write((cmd).encode())
    print("Sent to server:", cmd)
    # data = yield stream.read_until("\n\r")
    # rawdata = np.fromstring(data, dtype=np.uint8)
    # print("Response from server:", len(rawdata))

@gen.coroutine
def close_server():
    stream = yield TCPClient().connect("localhost", port)
    yield stream.write(("close" + "\n\r").encode())


def clientmain():
#     options.parse_command_line()
    IOLoop.current().run_sync(send_message)
    IOLoop.current().run_sync(get_change)
    IOLoop.current().run_sync(send_message)
    # IOLoop.current().run_sync(close_server)

if __name__ == "__main__":
    options.parse_command_line()
    IOLoop.current().run_sync(send_message)

    IOLoop.current().run_sync(get_change)
    # change = Thread(target=clientmain)
    # change.start()
    # change.join()
    # time.sleep(1)
    IOLoop.current().run_sync(send_message)
