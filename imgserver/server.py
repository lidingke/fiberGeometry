import logging
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer
from tornado.options import options, define
import json
import cv2
from imgserver.methods import randomImg, getImage
port = 9880
define("port", default=9888, help="TCP port to listen on")
logger = logging.getLogger(__name__)


class EchoServer(TCPServer):
    @gen.coroutine
    def handle_stream(self, stream, address):
        while True:
            try:
                data = yield stream.read_until(b"\n")
                logger.info("Received bytes: %s", data)
                if not data.endswith(b"\n"):
                    data = data + b"\n"
                yield stream.write(data)
            except StreamClosedError:
                logger.warning("Lost client at host %s", address[0])
                break
            except Exception as e:
                print(e)

IMG = cv2.imread('IMG/midoc.BMP')

class ImgServer(TCPServer):
    PARA = ('randomImg', 'IMG/G652/pk/')
    IS_RUNNING = True

    @gen.coroutine
    def handle_stream(self, stream, address):
        while self.IS_RUNNING:
            try:
                data = yield stream.read_until("\n\r")
                logger.info("Received bytes: %s", data)
                # print 'data bool',
                data = data.strip()
                print 'after get', data == 'getimgonce'
                if data == 'getimgonce':
                    self._getImgOnce(stream)
                elif data[:7] == 'change:':
                    loads = json.loads(data[7:])
                    print 'get changed', loads, type(loads)
                    self.PARA = loads
                elif data =='close':
                    self._close(stream)

            except StreamClosedError:
                logger.warning("Lost client at host %s", address[0])
                break
            except Exception as e:
                raise e

    @gen.coroutine
    def _getImgOnce(self, stream):
        # self.METHOD_PARA = {'function': 'getImage', 'para': """\'IMG/midoc.bmp\'"""}
        # img = self._getImgMethod(self.METHOD_PARA['function'],self.METHOD_PARA['para'])
        print 'put in get img', self.PARA
        # img = randomImg('IMG/G652/pk/')
        img = yield self._getImgMethod(self.PARA[0],self.PARA[1])
        # img = cv2.imread('IMG/204001.BMP')
        # img = IMG
        print 'put out get img'
        img = img.tostring() + '\n\r'
        print 'write img'
        yield stream.write(img)

    @gen.coroutine
    def _getImgMethod(self, function = 'randomImg', para = 'IMG/G652/pk/'):

        print 'getImgMehtods', function, para
        if function == 'randomImg':
            return randomImg(para)
        elif function == 'getImage':
            return getImage(para)

    def _close(self, stream):
        stream.close()
        self.IS_RUNNING = False
        self.io_loop.stop()
        self.io_loop.close()


def servermain():
    # options.parse_command_line()
    print 'listening on port'
    server = ImgServer()
    server.listen(port)
    print 'listening on port'
    logger.info("Listening on TCP port %d", port)
    IOLoop.current().start()

if __name__ == "__main__":
    options.parse_command_line()
    server = ImgServer()
    server.listen(port)
    logger.info("Listening on TCP port %d", port)
    IOLoop.current().start()