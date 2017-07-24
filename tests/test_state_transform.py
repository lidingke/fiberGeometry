from GUI.controller import StateMixin
from GUI.model.stateconf import state_number


def test_state_number():
    sn = state_number()
    sns =  [next(sn)+1 for i in range(6)]
    assert sns == [1,2,3,4,5,1]