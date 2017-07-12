from time import sleep

from GUI.model.stateconf import CONTEXT, state_number
from SDK.modbus.directions import MOTOR_STATE
from SDK.modbusabs import AbsModeBusMode
from util.observer import MySignal
from collections import namedtuple
from collections import OrderedDict


class StateTransform(object):
    def __init__(self):
        self.state_number = state_number()
        self.state_operate = StateApi.STATE_OPERATE
        self._platform_state = None


    def next_state(self):
        sequence = next(self.state_number)
        self.update(CONTEXT[sequence])
        print(sequence,self)
        operater = self.state_operate[sequence]
        for fun in operater:
            fun(self)

    @property
    def platform_state(self):
        return self._platform_state

    @platform_state.setter
    def platform_state(self,value):
        assert value in MOTOR_STATE.keys()
        self._platform_state = value

def platform_state_transform(self,*args,**kwargs):
    self.update(**kwargs)

class StateApi(object):
    emit_state = MySignal()
    STATE_OPERATE = ((ex1,),
                     (ex2,),
                     (ex3,),
                     (ex1, ex2),
                     (ex2, ex3)
                     )
    move = AbsModeBusModeByAxis('com4')
    move_state = (((2000, 'x'), (3000, 'y'), (4000, 'z')),
                  ((2000, 'x'), (3000, 'y'), (4000, 'z')),
                  ((2000, 'x'), (3000, 'y'), (4000, 'z')),
                  ((2000, 'x'), (3000, 'y'), (4000, 'z')),
                  ((2000, 'x'), (3000, 'y'), (4000, 'z')))

    def state(self):
        self.emit_state.emit()

    def get_move(self, number):
        move_state = self.move_state[number]
        for para in move_state:
            self.move.goto(*para)


if __name__ == '__main__':
    S_begin = StateApi()
    S_get = StateTransform()
    S_begin.emit_state.connect(S_get.next_state)
    for i in xrange(5):
        S_begin.state()
        sleep(1)
