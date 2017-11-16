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

