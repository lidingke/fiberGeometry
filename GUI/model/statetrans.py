from time import sleep

from SDK.modbusabs import AbsModeBusMode, AbsModeBusModeByAxis
from util.observer import MySignal
from collections import namedtuple


def state_number():
    while True:
        for i in xrange(0, 5):
            yield i


def ex1():
    print 'state1'


def ex2():
    print 'state2'


def ex3():
    print 'state3'


class StateTransform(object):
    def __init__(self):
        self.state_number = state_number()
        self.state_operate = StateApi.STATE_OPERATE

    def next_state(self):
        operater = self.state_operate[next(self.state_number)]
        for fun in operater:
            fun()

    def previous_state(self):
        pass


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
