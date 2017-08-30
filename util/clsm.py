# class Meta(type):
#
#     def __new__(meta,name,bases,class_dict):
#         print("meta",meta,name,bases,class_dict)
#         class_dict['stuff'] = 2
#         return type.__new__(meta,name,bases,class_dict)
#
# class My(object,metaclass = Meta):
#     stuff = 1
#
#     def __new__(cls, *args, **kwargs):
#         print('\nnew',cls, *args, **kwargs)
#         cls.__dict__['stuff']=3
#         return super(My, cls).__new__(cls, *args, **kwargs)
#
#     def foo(self):
#         pass
#
# # My