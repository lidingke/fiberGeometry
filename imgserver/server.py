import logging
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer
from tornado.options import options, define
import socket
import json
import sys
import os
import cv2
import numpy as np
from imgserver.methods import randomImg, getImage
# port = 9880
# define("port", default=9888, help="TCP port to listen on")
logger = logging.getLogger(__name__)


# class EchoServer(TCPServer):
#     @gen.coroutine
#     def handle_stream(self, stream, address):
#         while True:
#             try:
#                 data = yield stream.read_until(b"\n\r")
#                 logger.info("Received bytes: %s", data)
#                 if not data.endswith(b"\n"):
#                     data = data + b"\n"
#                 yield stream.write(data)
#             except StreamClosedError:
#                 logger.warning("Lost client at host %s", address[0])
#                 break
#             except Exception as e:
#                 print(e)

class SharpSever(object):
    """docstring for SharpSever"""
    def __init__(self):
        super(SharpSever, self).__init__()
        self.dirs = "IMG/sharp/oc1/"
        self.imgs = self.getAll()

    def getAll(self):
        dirlists = os.listdir(self.dirs)
        imgs = [[i, k, cv2.imread(k)] for i,k in enumerate(dirlists)]
        self.max_border = imgs[-1][0]
        self.min_border = imgs[0][0]
        return imgs

    def img_distance(self, distance):
        if not isinstance(distance, int):
            raise ValueError("input img_distance not int")
        if distance > self.max_border:
            return 'out'
        if distance < self.min_border:
            return 'min'
        print 'img name', self.imgs[distance][1]
        return self.imgs[distance][2]




        


class ImgServer(TCPServer):
    PARA = ('randomImg', 'IMG/G652/pk/')
    IS_RUNNING = True
    sharpSever = SharpSever()

    @gen.coroutine
    def handle_stream(self, stream, address):
        while self.IS_RUNNING:
            try:
                data = yield stream.read_until("\n\r")
                logger.info("Received bytes: %s", data)
                data = data.strip()
                if data == 'getimgonce':
                    self._getImgOnce(stream)
                elif data[:7] == 'change:':
                    loads = json.loads(data[7:])
                    print data
                    self.PARA = loads
                elif data[:9] == 'distance:':
                    distance = int(data[9:])
                    print 'get distance', distance
                elif data =='close':
                    self._close()


            except StreamClosedError:
                logger.info("Lost client at host %s", address[0])
                break
            except Exception as e:
                raise e

    @gen.coroutine
    def _getImgOnce(self, stream):
        img = yield self._getImgMethod(self.PARA[0],self.PARA[1])
        img = img.tobytes() + b'\n\r\n\r'
        yield stream.write(img)

    @gen.coroutine
    def _getImgMethod(self, function = 'randomImg', para = 'IMG/G652/pk/'):
        # print 'getImgMehtods', function, para
        if function == 'randomImg':
            return randomImg(para)
        elif function == 'getImage':
            return getImage(para)

    @gen.coroutine
    def _getDistanceImg(self, stream, distance):
        img = self.sharpSever.img_distance(distance)
        if isinstance(img, np.ndarray):
            img = img.tobytes()+ b'\n\r\n\r'
            yield stream.write(img)
        elif isinstance(img, str):
            cmd = 'error:' + distance + b'\n\r\n\r'
            yield stream.write(cmd)
        else:
            raise ValueError('img not array')


    def _close(self, ):
        # stream.close()
        self.IS_RUNNING = False
        # self.io_loop.stop()
        # self.io_loop.close()


def SeverMain(port):
    # options.parse_command_line()
    print 'listening on port', port
    server = ImgServer()
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.bind(("localhost", port))
    # sock.listen(port)
    # sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # server.add_socket(sock)
    server.listen(port)

    logger.info("Listening on TCP port %d", port)

    # IOLoop.instance().start()

if __name__ == "__main__":
    options.parse_command_line()
    server = ImgServer()
    server.listen(port)
    logger.info("Listening on TCP port %d", port)
    IOLoop.current().start()