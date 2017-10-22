import random

from SDK.modbus.autolight import  RightCurrent


def get_robot(x):
    if x < 56:
        y = -5e-6 * x ** 5 + 0.0012 * x ** 4 - 0.1022 * x ** 3 + 3.2753 * x ** 2 - 33.818 * x + 547.2
    elif x < 0:
        y = random.randint(480, 520)
    else:
        y = random.randint(-1, 1)
    # y = -5E-06x5 + 0.0012x4 - 0.1022x3 + 3.2753x2 - 33.818x + 547.2

    return y

def x_b(x):
    return x ** 2


def ttest_lists():
    for i in range(-50, 100):
        print i, x_b(i)


# def ttest_list_print():
#     pid = RightCurrentByPID(90)
#     func = x_b
#     # func = int
#     current = 0
#     for i in range(100):
#         light = func(current)
#         increase = pid(light)
#         current = current + increase
#         print "No.{},current:{:2.0f},increase:{:2.0f},light:{:2.0f}".format(
#             i, current, increase, light)
#         print "errors:{:2.0f},{:2.0f},{:2.0f}".format(*list(pid.errors))


def ttest_right_current():
    pid = RightCurrent(10)
    func = x_b
    # func = int
    current = 0
    for i in range(100):
        light = func(current)
        current = pid(light)
        if current:
            print "No.{},current:{:2.0f},light:{:2.0f}".format(i, current, light)
        else:
            print 'stop'
            break
