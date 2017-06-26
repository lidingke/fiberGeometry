from util.observer import MySignal
from collections import namedtuple

def state_number():
    while True:
        for i in xrange(0,5):
            yield i

STATE_OPERATE = ((),(),

)

class StateTransform(object):

    def __init__(self):
        self.state_number = state_number()
        self.state_operate = STATE_OPERATE

    def next_state(self):
        operater = self.state_operate[self.state_number]
        for fun in operater:
            fun()

    def previous_state(self):
        pass



class State(object):

    state0 = ()
    state1 = ()
    state2 = ()
    state3 = ()
    state4 = ()