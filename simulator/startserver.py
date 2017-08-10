from threading import Thread
from simulator.server import SeverMain, ImgServer
from tornado.ioloop import IOLoop
port = 9801
print 'listening on port', port
server = ImgServer()

server.listen(port,address='127.0.0.1')
IOLoop.instance().start()