import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from SDK.modbusabs import AbsModeBusMode
from pattern.sharper import AbsFocuser
import time

class tTestOnline():
    def test_abs_mode(self):
        logger.setLevel(logging.DEBUG)
        print 'goto direction'
        a = AbsModeBusMode('x', 'com4')
        direction = 35000

        a.goto(direction)
        readed = a.location()
        while abs(readed - direction) > 3:
            time.sleep(0.01)
            readed = a.location()
            logger.info('get readed ' + str(readed))

    def ttest_abs_sharper(self):
        a = AbsFocuser('x','com4')
        # slave.sharp_return.connect(a.get_sharp)
        a.run()
        # slave.close()