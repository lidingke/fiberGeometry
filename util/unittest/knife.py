import inspect
import pdb

from PyQt4.QtGui import QWidget
import re


class New(object):
    def __init__(self):
        self.funs = []

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __call__(self, *args, **kwargs):
        for f in self.funs:
            f()


class Knife(object):
    def __init__(self, widget_instance):
        self.root = widget_instance
        pars = self.parser_slots(widget_instance)
        self.create_slots(pars)

    def parser_slots(self, widget_instance):
        assert isinstance(widget_instance, QWidget)
        fun_with_connect = widget_instance.__init__
        assert "connect" in fun_with_connect.__code__.co_names
        codes = inspect.getsource(fun_with_connect)
        connect_lines = [x.strip() for x in codes.split("\n") if x.find('connect') > 1]
        signal_slot_par = []
        for line in connect_lines:
            signal = re.findall("(.*?)\.connect", line)[0].split('.')
            slot = re.findall(".connect\((.*?)\)", line)[0].split('.')
            signal_slot_par.append((signal, slot))
        return signal_slot_par
        # pdb.set_trace()

    def create_slots(self, pars):

        # pdb.set_trace()
        def set_attrs(instance, attrs, fun):
            if attrs:
                now_attrs = attrs[0]
                # print "attrs", instance, now_attrs, New()
                setattr(instance, now_attrs, New())
                # instance.__dict__[now_attrs] =
                return set_attrs(getattr(instance, now_attrs), attrs[1:], fun)
            else:
                instance.funs.append(fun)

        for signal, slot in pars:
            slot_fun = getattr(self.root, ".".join(slot[1:]))
            attrs_from = signal[1:]
            # attrs = (self,("a",("b")))
            set_attrs(self, attrs_from, slot_fun)
            # instance = slot_fun
        # pdb.set_trace()

        # def pars_to_dict(self,pars):
