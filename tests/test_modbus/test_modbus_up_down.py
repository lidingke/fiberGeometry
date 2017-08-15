from SDK.modbus.modbusmerge import SendTranslater, AbsModeBusModeByAxis, ReadTranslater
from util.hexs import hex2str



def test_send_translater():
    send = SendTranslater()

    sends = send('PLAT1', 'xstart', 35000)
    sendsstr = " ".join("{:02x}".format(ord(c)) for c in sends)
    print(sendsstr)
    assert sendsstr.upper() == "01 10 00 C8 00 02 04 00 01 88 B8 C9 EB"

    sends = send('PLAT2', 'xstart', 'stop')
    sendsstr = " ".join("{:02x}".format(ord(c)) for c in sends)
    print(sendsstr)
    assert sendsstr.upper() == "02 10 00 C8 00 01 02 00 00 A2 E8"

    sends = send('PLAT1', 'xstart', 'rest')
    sendsstr = " ".join("{:02x}".format(ord(c)) for c in sends)
    print(sendsstr)
    assert sendsstr.upper() == "01 10 00 E6 00 01 02 00 02 31 97"

    read = ReadTranslater()
    readstr = hex2str(read('up1'))
    assert readstr.upper() == "01 03 00 F0 00 01 84 39"