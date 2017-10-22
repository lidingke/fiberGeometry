from __future__ import print_function

import threading

from gevent.server import StreamServer
import logging
logger = logging.getLogger(__name__)

# this handler will be run for each incoming connection in a dedicated greenlet
def echo(socket, address):
    print('New connection from %s:%s' % address)
    # socket.sendall(b'Welcome to the echo server! Type quit to exit.\r\n')
    # using a makefile because we want to use readline()
    rfileobj = socket.makefile(mode='rb')
    while True:
        line = rfileobj.readline()
        if not line:
            print("client disconnected")
            break
        if line.strip().lower() == b'quit':
            print("client quit")
            break
        result = eval(line.strip())
        print(result)
        echoline = str(result).encode('utf-8')+b'\r\n'
        socket.sendall(echoline)
        print("echoed %r" % echoline)
    rfileobj.close()




class MonkeyServer(threading.Thread):

    def __init__(self,instance):
        super(MonkeyServer, self).__init__()
        self.instance = instance
        self.RUNNING = True

    def parser_cmd_in(self, cmd):
        pass
        # if cmd == 'test':
        #     self.instance._view._disableCVButton(False)
        #     logger.error("test")


    def readline(self, socket, address):
        logger.info('New connection from %s:%s' % address)
        rfileobj = socket.makefile(mode='rb')
        while self.RUNNING:
            line = rfileobj.readline().strip()
            if not line:
                logger.debug("client disconnected")
                break
            if line.strip().lower() == b'quit':
                logger.debug("client quit")
                break
            self.parser_cmd_in(line)
            logger.info("get cmdline %r" % line)
        rfileobj.close()

    def run(self):
        self.server = StreamServer(('0.0.0.0', 16000), self.readline)
        logger.error('Starting monkey server on port 16000')
        self.server.serve_forever()


    def close(self):
        self.RUNNING = False
        self.server.close()
