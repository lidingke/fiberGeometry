#coding:utf-8
from setting.config import DYNAMIC_CAMERA
import matplotlib;matplotlib.use("Qt4Agg")
import matplotlib.pyplot as plt
import socket
import json
print 'get camera status', DYNAMIC_CAMERA
if DYNAMIC_CAMERA:
    from SDK.mdpy import GetRawImg
else:
    from SDK.mdpytest import DynamicGetRawImgTest as GetRawImg
    # 当摄像头关闭时，图像从文件夹读取
    # GetRawImg = DynamicGetRawImgTest
import serial
from PyQt4.QtCore import pyqtSignal, QObject
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
import numpy as np

# from SDK.mdpy import GetRawImg
from threading import Thread

from SDK.modbus.ledmodes import LEDMode
from SDK.simulator.server import SeverMain
from SDK.simulator.client import Client
import time
import logging

logger = logging.getLogger(__name__)

#通过tcp/ip协议传输指令修改预读取的图像
class Model(Thread,QObject):
    emitinfodao_dir = pyqtSignal(object)# 新建信号槽，为接受slave中的信息

    def __init__(self):
        QObject.__init__(self)
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.sock.connect(("127.0.0.1", 9883))
            print "connect",9880
        except Exception:
            print("no init connect")
        self.slave = Slave()  # 初始化Slave
        self.slave.start()  # 启动串口通信
        self.slave.emitinfo_dir.connect(self.info)

        # self.img_mode = GetRawImg()
        self.input_list = []
        self.output_list=[]
        # self.dict={}

    def okContact(self,fileName):#接受信号槽的参数
        js=('randomImg',str(fileName))#qstring转化为string
        cmd = 'change:' + json.dumps(js) + '\n\r'
        self.sock.sendall(cmd.encode('utf-8'))#Send a data string to the socket.

    def info(self,mystr):#接受slave中的信息并传到myview中
        self.emitinfodao_dir.emit(mystr)

    def led_test(self,port,redlight,greenlight):
        logging.basicConfig(level=logging.INFO)
        mode = LEDMode(port)  # 光端口
        mode.set_current(c1st=redlight, c2st=500, c3st=greenlight, savemode=True)

    def getIMGlight(self,redlight):
        pass
        # try:
        #     self.img = self.img_mode.get()
        #     self.red = (self.img[::, ::, 0]).sum()/(255*1544*3)
        #     # self.dict[redlight]=self.red
        #     print self.red
        #     self.input_list.append(redlight)
        #     self.output_list.append(self.red)
        #     # print self.list
        #     # print self.output_list
        # except Exception as e:
        #     print "don't get img"
        #     raise e

    def plotlight(self):
        # print self.list
        # plt.plot(self.dict)

        # d=sorted(self.dict.items())
        # print d
        # print self.dict
        plt.plot(self.input_list,self.output_list)

        # plt.plot(self.dict.keys(),self.dict.values())
        plt.title("light")
        plt.show()


    def reset(self):
        self.input_list=[]
        self.output_list=[]


    def close(self):
        # self.sock.close()
        self.slave.close()

    def close(self):
        print 'close slave'
        self.slave.close()





#接受串口com14发送的消息并显示到窗口上
class Slave(Thread,QObject):
    emitinfo_dir = pyqtSignal(object)  # 新建信号槽
    def __init__(self):
        super(Slave, self).__init__()
        QObject.__init__(self)
        # 串口为com13，波特率为19200，超时0.05，校验位,接受串口14发送的信息
        # timeout:超时时间到，执行下一条语句，如果不设置timeout，读不到数据，程序将死在这个地方。
        self.ser = serial.Serial('com13', 19200, timeout=0.05, parity= 'E')
        self.RUNNING = True

        print(self.ser.parity)#打印当前的奇偶校验设置

    def run(self):
        while self.RUNNING:
            try:
                readed = self.ser.read(100)
                #从串口读取100大小字节。
            except Exception as e:
                return e

            if readed:
                _str = 'get write '+ " ".join("{:02x}".format(ord(c)) for c in readed)  # 将字符串转化为十六进制
                self.mystr= str(_str)
                #print self.mystr
                self.emitinfo_dir.emit(self.mystr)#将该字符串放到信号槽中
                # Model.emitinfo_dir.emit(self.mystr)
        self.ser.close()  # 关闭串口函数

    # 当关闭窗口后，会触发这个函数，导致循环条件为false，停止接受串口信息
    def close(self):
        print('get slave close')
        self.RUNNING = False


#测试台窗口显示静态图片
class DynamicGetRawImgTest(GetRawImg):
    """docstring for getRawImg"""
    def __init__(self, host = '127.0.0.1', port = 9880):
        # super(GetRawImgTest, self).__init__()
        self.host, self.port = host, port
        Thread(target=SeverMain, args=(self.port,)).start()#线程-图像读取
    def get(self):
        # time.sleep(0.01)
        try:
            result = IOLoop.current().run_sync(Client().get_img_once)
        except StreamClosedError:
            logger.warning("Lost host at client %s")
            return
        except ValueError as e:
            print e
            return
        if len(result) == 15116544:
            img = np.frombuffer(result, dtype = 'uint8')
            img.shape = img.shape = (1944, 2592, 3)
            return img

    def un_init_camera(self):
        pass











