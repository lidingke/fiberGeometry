import inspect
import re

import logging

logger = logging.getLogger(__name__)

class SubNode(object):
    def __init__(self):
        self.funs = []

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __call__(self, *args, **kwargs):
        [f() for f in self.funs]

class FailAttr(ValueError):
    """ can't get attr correct"""

class Knife(object):
    def __init__(self, widget_instance):
        pars = self.parser_slots(widget_instance)
        self.create_slots(pars, widget_instance)

    def parser_slots(self, widget_instance):
        dirs = dir(widget_instance)
        dirs = [getattr(widget_instance, d) for d in dirs]
        signal_slot_par = []
        for d in dirs:
            if hasattr(d, "__code__") and "connect" in d.__code__.co_names:
                codes = inspect.getsource(d)
                connect_lines = [x.strip() for x in codes.split("\n") if x.find('.connect') > 1]
                for line in connect_lines:
                    if line.strip()[0] == "#":
                        continue
                    signal = re.findall("(.*?)\.connect", line)[0].split('.')
                    slot = re.findall(".connect\((.*?)\)", line)[0].split('.')
                    signal_slot_par.append((signal, slot))
        return signal_slot_par

    def create_slots(self, pars, widget_instance):
        def set_attrs(instance, attrs, fun):
            if attrs:
                now_attrs = attrs[0]
                if not hasattr(instance, now_attrs):
                    setattr(instance, now_attrs, SubNode())
                return set_attrs(getattr(instance, now_attrs), attrs[1:], fun)
            else:
                instance.funs.append(fun)

        def get_attrs(instance, attrs):
            if attrs:
                try:
                    attr = getattr(instance, attrs[0])
                except Exception as e:
                    return FailAttr
                return get_attrs(attr, attrs[1:])
            else:
                return instance

        for signal, slot in pars:
            slot_fun = get_attrs(widget_instance, slot[1:])
            if slot_fun:
                attrs_from = signal[1:]
                set_attrs(self, attrs_from, slot_fun)
                logger.error("{} {}".format(attrs_from, slot_fun))
