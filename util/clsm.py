import pdb


# class Base(object):
#     """ The base class that all of the object model classes inherit from. """
#
#     def __init__(self, cls, fields):
#         """ Every object has a class. """
#         self.cls = cls
#         self._fields = fields
#
#     def read_attr(self, fieldname):
#         """ read field 'fieldname' out of the object """
#         return self._read_dict(fieldname)
#
#     def write_attr(self, fieldname, value):
#         """ write field 'fieldname' into the object """
#         self._write_dict(fieldname, value)
#
#     def isinstance(self, cls):
#         """ return True if the object is an instance of class cls """
#         return self.cls.issubclass(cls)
#
#     def callmethod(self, methname, *args):
#         """ call method 'methname' with arguments 'args' on object """
#         meth = self.cls._read_from_class(methname)
#         return meth(self, *args)
#
#     def _read_dict(self, fieldname):
#         """ read an field 'fieldname' out of the object's dict """
#         return self._fields.get(fieldname, MISSING)
#
#     def _write_dict(self, fieldname, value):
#         """ write a field 'fieldname' into the object's dict """
#         self._fields[fieldname] = value
#
# MISSING = object()

class Base(object):
    def __init__(self):
        print "enter Base"
        print "leave Base"


class A(Base):
    def __init__(self):
        print "enter A"
        super(A, self).__init__()
        print "leave A"


class B(Base):
    def __init__(self):
        print "enter B"
        super(B, self).__init__()
        print "leave B"


class C(A, B):

    def __new__(cls, *args, **kwargs):
        mro = list(cls.__mro__)
        mro.sort()
        cls.__mro__ = tuple(mro)
        return cls

    def __init__(self):
        print "enter C"
        super(C, self).__init__()
        print "leave C"


# c = C()
