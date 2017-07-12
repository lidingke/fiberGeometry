HEAD_DIR = {
    'xstart':     "\x00\xc8",
    'xdir':       "\x00\xc9",

    'ystart':     "\x00\xd2",
    'ydir':       "\x00\xd3",

    'zstart':     "\x00\xdc",
    'zdir':       "\x00\xdd",
    'rest':       "\x00\xe6",
    'up1':        "\x00\xf0",
    'up2':        "\x00\xf1",
    'up3':        "\x00\xf2"
}

MOTOR_GROUP = (
    ('x1','y1','z1','up1','up2','up3'),
    ('x2','y2','z2')
)
STATION_DIR = {
    "UP_DOWN":"\x00",
    "PLAT1": "\x01",
    "PLAT2": "\x02"
}

START_STOP = ('\x00\x01','\x00\x00')
UP_DOWN = ('\x00\x01','\x00\x02')

MOTOR_STATE = {
    "UP_DOWN":('up1','up2','up3'),
    "PLAT1":('x1','y1','z1'),
    "PLAT2":('x2','y2','z2')
}