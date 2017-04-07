#coding:utf-8
from SDK.modbussdk import Translater

def test_modbus():
    d = Translater()
    keys = {'axis':'x',
            'start':"True",
            'forward':"False",
            'pulse':1000,
            'frequence':200}
    cmdline = d(**keys)
    cmdline = " ".join("{:02x}".format(ord(c)) for c in cmdline)
    assert cmdline.upper() == '01 10 00 C8 00 06 0C 00 01 00 00 03 E8 00 00 00 C8 00 00 F0 58'

    keys = {'axis':'x',
            'forward':"False"}
    cmdline = d(**keys)
    cmdline = " ".join("{:02x}".format(ord(c)) for c in cmdline)
    assert cmdline.upper() == '01 10 00 C9 00 01 02 00 00 B7 C9'

    keys = {'axis':'x',
            'pulse':1000}
    cmdline = d(**keys)
    cmdline = " ".join("{:02x}".format(ord(c)) for c in cmdline)
    assert cmdline.upper() == '01 10 00 CA 00 02 04 03 E8 00 00 FF F0'

    keys = {'axis':'x',
            'frequence':200}
    cmdline = d(**keys)
    cmdline = " ".join("{:02x}".format(ord(c)) for c in cmdline)
    assert cmdline.upper() == '01 10 00 CC 00 02 04 00 C8 00 00 7E 54'

    keys = {'axis': 'x',
            'start': 'True'}
    cmdline = d(**keys)
    cmdline = " ".join("{:02x}".format(ord(c)) for c in cmdline)
    assert cmdline.upper() == '01 10 00 C8 00 01 02 00 01 77 D8'