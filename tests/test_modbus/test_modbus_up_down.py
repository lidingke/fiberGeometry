from SDK.modbus.modbusmerge import SendTranslater, AbsModeBusModeByAxis


def test_send_translater():
    send = SendTranslater()
    sends = send('x1', 'xstart', 35000)
    sendsstr = " ".join("{:02x}".format(ord(c)) for c in sends)
    print(sendsstr)
    assert sendsstr.upper() == "01 10 00 C8 00 02 04 00 01 88 B8 C9 EB"

    sends = send('x2', 'xstart', 'stop')
    sendsstr = " ".join("{:02x}".format(ord(c)) for c in sends)
    print(sendsstr)
    assert sendsstr.upper() == "02 10 00 C8 00 01 02 00 00 A2 E8"

    sends = send('x1', 'xstart', 'rest')
    sendsstr = " ".join("{:02x}".format(ord(c)) for c in sends)
    print(sendsstr)
    assert sendsstr.upper() == "01 10 00 E6 00 01 02 00 02 31 97"

