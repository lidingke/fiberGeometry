## 目录结构
--/GUI#界面和界面逻辑

--/IMG#测试用图像

--/SDK#摄像头和光谱仪SDK

--/pattern#图像处理模块

--/report#报表生成模块

--/setting#配置模块

--/simulator#下位机模拟器

--/tests#单元测试

--/util#公共模块

.gitgonre

cvon.py#打包用入口文件

cvon.spec#打包用配置文件

main.py#入口文件

simulatorgui.py#模拟器入口文件



## 简介

主程序采用Python语言，该语言和其生态系统能较好的实现图像处理和数据处理算法到实际软件的落地。
图像处理部分采用OpenCV库。
衰减谱的处理采用Numpy库。
UI界面采用PyQt库。
坐标图的绘制采用Matplotlib库。
与摄像头和光谱仪等硬件连接采用Python的C语言扩展模块，该模块使得Python有调用sdk开发包中的dll的能力。
与控制电机的PLC连接采用PySerials库。




## 入口文件
由于多个产品共用一套代码，使得几个模块得动态生成，这里采取的方案是通过配置文件配置好需要动态生成的参数，在入口函数中读取并用工厂模式生成。

具体为，不同的产品对应的界面不一样，不同的产品需要加载的软件硬件模块也不同，针对生产环境和测试环境的需要加载的软件硬件模块也不一样。比如有的自动版本的产品带电机，需要加载SDK模块中的电机，并分配串口，有的手动版本产品不带电机，需要加载一个虚拟的电机类，不必分配串口，同时得在界面上把相应的电机相关的控件隐藏。又比如在测试环境中，需要将电机模块换成供测试用的模拟器，并分配指向模拟器的虚拟串口。这些环境选择参数在配置模块中配置。

在入口程序的import部分中，config模块和logging模块应优先导入。环境类型由命令行参数，即sys.argv[1]参数指定，config和logging模块应该根据该参数动态配置。在这两个模块配置完后才能导入其他模块。config模块在setting配置模块中，该模块在稍后做详细介绍。

界面的qss由loadStyleSheet函数导入。

系统采取MVC设计模式，controller和view由get_controller和get_view工厂函数生成。这两个函数在GUI模块中，这个模块稍后做详细介绍。

## GUI

界面采用MVC架构，其中，model类包含后台逻辑，view类包含前端逻辑，连接前端和后台的信号槽都在controller类里面。而这几个类都由类工厂根据不同的产品动态生成。
具体的工厂函数为get_view和get_controller。

其中，controler采用Mixin形式的多继承。这里这么做是为了分离各个具体的model。因为具体的model对应不同的硬件，应该根据参数来选择加载不同的model。

view采取顺序VeiwModel和Form的方式，其中ViewModel保存具体的View需要的定制类控件以及逻辑，Form用来渲染.ui文件生成的UI.py文件。这样就分离了UI的生成和UI的定制。因为UI.py是脚本生成的，一般不应该改动，通过一个Form类去添加功能。

界面的定制版QSS在GUI/UI/qss目录下。写qss的时候尽量用css兼容的语法，可以在pycharm中享受到css规则的代码提示。

## IMG
保存待测图片，这部分不上传到GitHub，其中的md文件夹保存markdown需要的图片，需要上传至GitHub。

## SDK
SDK模块包含这几个子模块，MindPy、pynir和modbus，分别是MindVision的摄像头，OceanOptics的光谱仪以及自研的电机和LED驱动。
前两个是供应商提供SDK开发包（C++的dll），我译成pyd文件使用。后面的电机和LED驱动是直接串口控制，下位机是modbus的协议。

后缀为Script的文件夹一般是相应的C扩展工程文件，一般包含这几个部分，一个是相应的.cpp文件和需要引用的.dll文件。一个是安装文件，名称为setup.py。还有一个单元测试文件test.Py。编译命令为
```
SET VS90COMNTOOLS=%VS140COMNTOOLS%
python setup.py build_ext --inplace
```

要注意的是引用了numpy库的话需要在cpp文件中做相应的导入。

```
PyArrayObject * out = (PyArrayObject*)
	PyArray_SimpleNewFromData(1, dims, NPY_UBYTE, outArray);

import_array();

npinclude = numpy.get_include()
```

下位机遵循的是modbus协议，用pyserial按照串口通信的基本协议写就行了。有一点要注意的是需要奇偶校验，导入第三方模块crcmod，并选择modbus的模式。
```
crcmod.predefined.mkCrcFun('modbus')
```

SDK模块处理硬件实时控制模块，还有供测试用的测试模块，根据配置文件的不同，选择加载实时硬件模块或者虚拟测试模块。一般加载json文件的命令带online，即为加载实时硬件模块，如果加载命令是offline，即为加载虚拟测试模块。

# pattern

这个模块的主文件是classify.py，该文件中的classifyObject就是端面图像识别的工程函数，根据传入的光纤类型返回相应的识别方法。
所有识别类都继承自MetaClassify，符合该父类的接口。

# report
用以生成输出报告。

# setting
setting模块负责所有的配置文件，原则上来说，配置文件变量应该是不可变的，当然，或者说，在初始化后，即在运行时不应该被随意更改。
在开发的早期，配置文件是通过一个单例模式在全局共享，这是个非常糟糕的设计。后来我改成用模块来进行全局的配置，这里的模块是python语法概念上的模块，在python中模块是天然的单例模式，需要引用模块中的变量时直接import即可。

因此，我将之前的单例配置文件中和图像处理有关的配置分离出来，分离到parameter.json中，将工程相关的配置项分离到config模块中。其他还有部分小的配置文件不一一介绍。

每个配置文件都有json和pickle版本，原因在于json文件可读性比较好，怕被用户随意更改，一般加载时先加载pickle文件，找不到pickle时加载对应的json文件。不过pickle的保密性也等同于零，并没什么卵用。

config模块在加载后会被动态更改一次，通过configs文件夹下的各个json文件来更改。该更改只应该在初始化时执行一次。动态更改用update_config_by_name函数。


# simulator
这个模块用于控制部分硬件模块，其中有控制测试图片服务器的GUI工具，也有控制LED灯的功率的GUI测试工具。




