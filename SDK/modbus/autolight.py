# coding:utf-8
import threading
import time

from SDK.modbus.ledmodes import LEDMode
from pattern.sharp import corner_noise, take_white_light_in_core, black_points, black_points_not
from setting.config import MODBUS_PORT, LED_PORT
from setting.parameter import SETTING
from util.load import WriteReadJson, WriteReadJsonNoB
from util.observer import PyTypeSignal
import logging

logger = logging.getLogger(__name__ + ":" + str(LED_PORT))


class RightCurrent(object):
    def __init__(self, current, ranges=(0, 10), call="red"):
        self.ranges = ranges
        self.current = current
        if call == "red":
            self.call = self.red
        else:
            self.call = self.green

    def green(self, light):

        min_, max_ = self.ranges
        if light > max_ * 100:
            self.current -= 100
        elif light > max_ * 10:
            self.current -= 10
        elif light > max_:
            self.current -= 1
            if self.current == 0:
                self.current = 0
        elif light < min_:
            if light == 0:
                step = 10
            else:
                step = 1
            self.current += step
        else:
            return self.current
        return self.current

    def red(self, light):
        step = light // 100 + 1
        min_, max_ = self.ranges
        if light > max_:
            self.current += step
        elif light < min_:
            if light == 0:
                step = 10
            else:
                step = 1
            self.current -= step
        else:
            return self.current
        return self.current

    def __call__(self, x):
        result = self.call(x)
        if result < 0:
            result = 0
        if result > 2000:
            result = 2000

        return result


# class RightCurrentP(object):
#     def __init__(self, current, ranges=(0, 10), call="red"):
#         self.ranges = ranges
#         self.target = sum(ranges) // 2
#         self.current = current
#         # if call == "red":
#         #     self.call = 1
#         # else:
#         #     self.call = -1
#
#     def __call__(self, light):
#         min_, max_ = self.ranges
#         if light > max_:
#             step = (light - self.target) // 100 + 1
#             if step > 100:
#                 step = 100
#             self.current = self.current - step
#
#         elif light < min_:
#             if light == 0:
#                 step = 100
#             else:
#                 step = 1
#             self.current = self.current + step
#
#         else:
#             if self.current == 0:
#                 self.current = 0
#             if self.current >2000:
#                 self.current = 2000
#             return self.current
#         if self.current == 0:
#             self.current = 0
#         if self.current > 2000:
#             self.current = 2000
#         return self.current
#         print "current",self.current,type(self.current)
#
#     # def green(self, light):
#     #
#     #     min_, max_ = self.ranges
#     #     if light > max_:
#     #         step = (light - self.target) // 100 + 1
#     #         if step > 100:
#     #             step = 100
#     #         self.current -= step
#     #         if self.current == 0:
#     #             self.current = 0
#     #     elif light < min_:
#     #         if light == 0:
#     #             step = 100
#     #         else:
#     #             step = 1
#     #         self.current += step
#     #     else:
#     #         return self.current
#     #     return self.current
#     #
#     # def red(self, light):
#     #     # return self.call(x)
#     #     min_, max_ = self.ranges
#     #     if light < min_:
#     #         if light == 0:
#     #             step = 100
#     #         else:
#     #             step = 1
#     #         self.current -= step
#     #         if self.current <= 0:
#     #             self.current = 0
#     #     elif light > max_:
#     #         step = (light - self.target) // 100 + 1
#     #         if step > 100:
#     #             step = 100
#     #         self.current += step
#     #     else:
#     #         return self.current


class LightController(object):
    def __init__(self):

        self.SET = SETTING()
        self.mode = LEDMode(LED_PORT)
        self.emit_light_ready = PyTypeSignal()
        self.emit_dynamic_light = PyTypeSignal()
        self.IS_RUNNING = True
        self.fiber_type = self.SET["fiberType"]

        self.saved_light_current_handle = WriteReadJson("setting\\led_light.json")
        # try:
        self.saved_light_currents = self.saved_light_current_handle.load()
        # except ValueError:
        #     self.saved_light_currents= {}
        self.light_current = self._get_light_current()

        self.light_range = self.SET["light_range"]

    def _get_light_current(self):
        # self.fiber_type = self.SET["fiberType"]
        if self.fiber_type in self.saved_light_currents.keys():
            logger.info("get_light_current:{} {}".format(self.fiber_type, self.saved_light_currents[self.fiber_type]))
            return self.saved_light_currents[self.fiber_type]
        else:
            return self.SET["light_current"]

    def _save_light_current(self, lights):
        self.saved_light_currents.update({self.fiber_type.encode('utf-8'): lights})
        self.saved_light_current_handle.save(self.saved_light_currents)

    # def start(self):
    #     logger.error("start light controller")
    #     threading.Thread(target=self.run_coroutine).start()


    def start_coroutine(self):
        logger.warning("start light controller")
        handle = self.run_coroutine()
        next(handle)
        return handle

    def run_coroutine(self):
        self.light_current = self._get_light_current()
        self.light_range = self.SET["light_range"]
        red = self.light_current["red"]
        green = self.light_current["green"]
        red_ranges_min, red_ranges_max = self.light_range["red"]
        green_ranges_min, green_ranges_max = self.light_range["green"]
        self.mode.set_current(c1st=red, c2st=0, c3st=green, savemode=True)
        self.red_right_current = RightCurrent(
            red, (red_ranges_min, red_ranges_max), "red")
        self.green_right_current = RightCurrent(
            green, (green_ranges_min, green_ranges_max), "green")
        for i in range(100):
            img = yield
            red, green, noise, white = self._get_right_current(img)
            self.mode.set_current(c1st=red, c2st=0, c3st=green, savemode=True)
            self.light_current["red"] = int(red)
            self.light_current["green"] = int(green)
            # self.emit_dynamic_light.emit()
            if red_ranges_min < noise < red_ranges_max \
                    and green_ranges_min < white < green_ranges_max:
                break
                # if not self.IS_RUNNING:
                #     break
        self.emit_light_ready.emit()
        self._save_light_current(self.light_current)

    def _get_right_current(self, img):

        # img = get_img()
        noise = black_points(img, 300)
        # red = self.light_current["red"]
        red = self.red_right_current(noise)
        # red = 50
        white = take_white_light_in_core(img, 800)

        green = self.green_right_current(white)
        cmd = "red:{}#{} green:{}#{}".format(noise, red, white, green)
        logger.error(cmd)

        self.emit_dynamic_light.emit(cmd)
        return red, green, noise, white

    def close(self):
        self.IS_RUNNING = False

    def update_fibertype(self, fiber_type):
        self.SET.update_by_key(fiber_type)
        self.SET['fiberType'] = fiber_type
        current = self.SET["light_current"]
        logger.error('set to {}'.format(current))
        self.fiber_type = fiber_type
        self.mode.set_current(
            c1st=current['red'], c2st=0, c3st=current['green'], savemode=True)


# class Pid(object):
#     def __init__(self, target):
#         """pid_output: current, pid_input:light"""
#         self.integral = 0
#         self.target = target
#         # self.now = 0
#         self.kp, self.ki, self.kd = 0.02, 0.1, 0.2
#         self.last_err = 0
#         self.next_err = 0
#         self.ranges = (0, 50)
#         self.call = self.increase
#
#     def __call__(self, x):
#         return self.call(x)
#
#     # def __call__(self, ):
#
#     def real(self, vol):
#         raise NotImplementedError
#
#     def basic(self, now):
#         err = self.target - now
#         if abs(err) < 1:
#             return now
#         self.integral += err
#         vol = self.kp * err + self.ki * self.integral + self.kd * (err - self.last_err)
#         self.last_err = err
#         # now = self.real(vol)
#         return vol
#
#     def _ranges(self):
#         err = self.target - self.now
#         if self.now > 500 or self.now < 0:
#             if_integral = 0
#             self.integral = 0
#         if abs(err) > 500:
#             if_integral = 0
#         else:
#             if_integral = 1
#             self.integral += err
#         vol = self.kp * err + if_integral * self.ki * self.integral \
#               + self.kd * (err - self.last_err)
#         # print "target:",vol,",",self.now
#
#         self.last_err = err
#         self.now = self.real(vol)
#         return self.now
#
#     def increase(self, now):
#         err = self.target - now
#         if abs(err) < 1:
#             return now
#         # self.integral += err
#         vol = self.kp * (err - self.next_err) + self.ki * err + self.kd * (err - 2 * self.next_err + self.last_err)
#         self.last_err = self.next_err
#         self.next_err = err
#         now += vol
#         return now


from collections import deque


# class RightCurrentByPID():
#     def __init__(self, target_light):
#         """pid_output: current, pid_input:light"""
#         self.integral = 0
#         self.target = target_light
#         # self.now = 0
#         self.kp, self.ki, self.kd = 0.01, 0.01, 0.02
#
#         self.errors = deque(maxlen=3)
#         [self.errors.append(i) for i in [0] * 3]
#         self.call = self.increase
#
#     def __call__(self, x):
#         return self.call(x)
#
#     def increase(self, now_light):
#         error = self.target - now_light
#         # if abs(error) > 100:
#         #     IF_INTERGR = 0
#         # else:
#         #     IF_INTERGR = 1
#         self.errors.append(error)
#
#         ek2, ek1, ek = list(self.errors)
#         perror = ek - ek1
#         ierror = ek
#         derror = ek - ek1 * 2 + ek2
#         # light0,light1,light2,light3 = lights
#         # error0 = light1-light0
#         # error1 = light2-light1
#         # error2 = light3-light2
#
#         increase = self.kp * perror + self.ki * ierror + self.kd * derror
#         # self.ek2 = self.ek1
#         # self.ek1 = self.ek
#         return int(increase)
#
#     def basic(self, now_light):
#         pass
