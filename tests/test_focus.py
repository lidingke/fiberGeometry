import time
import random
from collections import deque
import logging
logger = logging.getLogger(__name__)
def mode(x):
    if x<0:
        return 100.0
    elif x<50:
        return 100.0-2*x
    elif x<55:
        return 0.0
    elif x<105:
        return 2*x-110.0
    else:
        return 100.0

def forward(distance, back):
    if back:
        distance = distance + 0.5
    else :
        distance = distance - 0.5
    return distance

def ttest_focus():
    RUNNING = True
    oldsharp = deque(maxlen=5)
    distance = random.randint(0,100)
    back = True
    while RUNNING:
        time.sleep(1)
        oldsharp.append(mode(distance))
        print oldsharp
        if len(oldsharp) > 2:
            if oldsharp[-2] >= oldsharp[-1]:
                distance = forward(distance, back)
            else:
                distance = forward(distance, back)
                back = not back

            print distance, oldsharp[-2], oldsharp[-1]

            if len(oldsharp) == 5:
                istrue = (oldsharp[4] >= oldsharp[2]) and (oldsharp[0] >= oldsharp[2])
                if istrue:
                    RUNNING = False

from pattern.sharper import Motor, Focuser
from imgserver.client import SharpClient
from imgserver.server import CameraMotorSever
from tornado.ioloop import IOLoop
from functools import partial
import socket

class Motortest(Motor):
    def __init__(self, port):
        super(Motortest, self).__init__()
        self.port = port

    def move(self):
        pass

    def start(self):
        IOLoop.current().run_sync(SharpClient(port=self.port).start_motor)

    def moveback(self):
        IOLoop.current().run_sync(SharpClient(port=self.port).turn_back)

    def close(self):
        IOLoop.current().run_sync(SharpClient(port=self.port).send_close)

def get_img(port):
    IOLoop.current().run_sync(SharpClient(port=port).get_sharp)

def get_img_sys(port):
    # SharpClient(port=port).get_sharp_sys()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1",port))
    sock.sendall('getsharp:\n\r')
    _ = sock.recv(4)
    _ = sock.recv(int(_))
    return _

def camer_server(port):
    print 'listening on port', port
    server = CameraMotorSever()
    server.listen(port)
    logger.info("Listening on TCP port %d", port)
    IOLoop.instance().start()

def test_motor_camera():
    # logger.setLevel('INFO')
    port = 9811
    camer_server(port)
    focus = Focuser()
    focus.motor = Motortest(port)
    # focus.getSharp = partial(get_img, port)
    # focus.run()
    focus.getSharp = partial(get_img_sys, port)
    focus.get()


