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
import threading

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

# def get_img(port):
#     IOLoop.current().run_sync(SharpClient(port=port).get_sharp)

    def get_img_sys(self):
        time.sleep(0.05)
        _ = IOLoop.current().run_sync(SharpClient(port=self.port).get_sharp)
        return abs(float(_.strip()))

def camer_server(port):
    print 'listening on port', port
    server = CameraMotorSever()
    server.listen(port)
    logger.info("Listening on TCP port %d", port)
    # IOLoop.instance().start()

def ttest_motor_camera_once():
    port = 9811
    _ = threading.Thread(target=camer_server, args=(port,))
    _.start()
    focus = Focuser()
    focus.motor = Motortest(port)
    focus.getSharp = Motortest(port).get_img_sys
    focus.motor.start()
    sharp = focus.getSharp()
    assert 100.0 == sharp


def test_motor_camera():
    port = 9812
    _ = threading.Thread(target=camer_server, args=(port,))
    _.start()
    focus = Focuser()
    focus.motor = Motortest(port)
    focus.getSharp = Motortest(port).get_img_sys
    # assert '100' == focus.get()
    focus.run()