# coding:utf-8
u"""二进制byte流转成16进制方式的string显示"""
def hex2str(data):
    return " ".join("{:02x}".format(ord(c)) for c in data)
