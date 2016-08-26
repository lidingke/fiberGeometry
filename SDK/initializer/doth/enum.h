//图像查表变换的方式
typedef enum
{
    LUTMODE_PARAM_GEN= 0,//通过调节参数动态生成LUT表
    LUTMODE_PRESET,     //使用预设的LUT表
    LUTMODE_USER_DEF    //使用用户自定义的LUT表
}emSdkLutMode;

//相机的视频流控制
typedef enum
{
    RUNMODE_PLAY= 0,    //正常预览，捕获到图像就显示。（如果相机处于触发模式，则会等待触发帧的到来）
    RUNMODE_PAUSE,     //暂停，会暂停相机的图像输出，同时也不会去捕获图像
    RUNMODE_STOP       //停止相机工作。反初始化后，相机就处于停止模式
}emSdkRunMode;

//SDK内部显示接口的显示方式
typedef enum
{
    DISPLAYMODE_SCALE= 0, //缩放显示模式，缩放到显示控件的尺寸
    DISPLAYMODE_REAL     //1:1显示模式，当图像尺寸大于显示控件的尺寸时，只显示局部
}emSdkDisplayMode;

//录像状态
typedef enum
{
  RECORD_STOP = 0,  //停止
  RECORD_START,     //录像中
  RECORD_PAUSE      //暂停
}emSdkRecordMode;

//图像的镜像操作
typedef enum
{
    MIRROR_DIRECTION_HORIZONTAL = 0,//水平镜像
    MIRROR_DIRECTION_VERTICAL       //垂直镜像
}emSdkMirrorDirection;

//图像的旋转操作
typedef enum
{
    ROTATE_DIRECTION_0 = 0,     // 不旋转
    ROTATE_DIRECTION_90,        // 逆时针90度
    ROTATE_DIRECTION_180,       // 逆时针180度
    ROTATE_DIRECTION_270,       // 逆时针270度
}emSdkRotateDirection;

//相机视频的帧率
typedef enum
{
    FRAME_SPEED_LOW = 0,  //低速模式
    FRAME_SPEED_NORMAL,   //普通模式
    FRAME_SPEED_HIGH,     //高速模式(需要较高的传输带宽,多设备共享传输带宽时会对帧率的稳定性有影响)
    FRAME_SPEED_SUPER     //超高速模式(需要较高的传输带宽,多设备共享传输带宽时会对帧率的稳定性有影响)
}emSdkFrameSpeed;

//相机中的图像传感器的工作模式
typedef enum
{
    CONTINUATION = 0,//连续采集模式
    SOFT_TRIGGER,    //软件触发模式，由软件发送指令后，传感器开始采集指定帧数的图像，采集完成后，停止输出
    EXTERNAL_TRIGGER //硬件触发模式，当接收到外部信号，传感器开始采集指定帧数的图像，采集完成后，停止输出
} emSdkSnapMode;

//自动曝光时抗频闪的频闪
typedef enum
{
    LIGHT_FREQUENCY_50HZ = 0,//50HZ,一般的灯光都是50HZ
    LIGHT_FREQUENCY_60HZ     //60HZ,主要是指显示器的
}emSdkLightFrequency;


typedef enum
{
  PARAM_MODE_BY_MODEL = 0,  //根据相机型号名从文件中加载参数，例如MV-U300
  PARAM_MODE_BY_NAME,       //根据设备昵称(tSdkCameraDevInfo.acFriendlyName)从文件中加载参数，例如MV-U300,该昵称可自定义
  PARAM_MODE_BY_SN,         //根据设备的唯一序列号从文件中加载参数，序列号在出厂时已经写入设备，每台相机拥有不同的序列号。
  PARAM_MODE_IN_DEVICE      //从设备的固态存储器中加载参数。不是所有的型号都支持从相机中读写参数组，由tSdkCameraCapbility.bParamInDevice决定
}emSdkParameterMode;


//SDK生成的相机配置页面掩码值
typedef enum
{
  PROP_SHEET_INDEX_EXPOSURE = 0,
  PROP_SHEET_INDEX_ISP_COLOR,
  PROP_SHEET_INDEX_ISP_LUT,
  PROP_SHEET_INDEX_ISP_SHAPE,
  PROP_SHEET_INDEX_VIDEO_FORMAT,
  PROP_SHEET_INDEX_RESOLUTION,
  PROP_SHEET_INDEX_IO_CTRL,
  PROP_SHEET_INDEX_TRIGGER_SET,
  PROP_SHEET_INDEX_OVERLAY,
  PROP_SHEET_INDEX_DEVICE_INFO
}emSdkPropSheetMask;

//SDK生成的相机配置页面的回调消息类型
typedef enum
{
  SHEET_MSG_LOAD_PARAM_DEFAULT = 0, //参数被恢复成默认后，触发该消息
  SHEET_MSG_LOAD_PARAM_GROUP,       //加载指定参数组，触发该消息
  SHEET_MSG_LOAD_PARAM_FROMFILE,    //从指定文件加载参数后，触发该消息
  SHEET_MSG_SAVE_PARAM_GROUP        //当前参数组被保存时，触发该消息
}emSdkPropSheetMsg;

//可视化选择参考窗口的类型
typedef enum
{
  REF_WIN_AUTO_EXPOSURE = 0,
  REF_WIN_WHITE_BALANCE,
}emSdkRefWinType;

//可视化选择参考窗口的类型
typedef enum
{
  RES_MODE_PREVIEW = 0,
  RES_MODE_SNAPSHOT,
}emSdkResolutionMode;

//白平衡时色温模式
typedef enum
{
  CT_MODE_AUTO = 0, //自动识别色温
  CT_MODE_PRESET,   //使用指定的预设色温
  CT_MODE_USER_DEF  //自定义色温(增益和矩阵)
}emSdkClrTmpMode;

//LUT的颜色通道
typedef enum
{
  LUT_CHANNEL_ALL = 0,//R,B,G三通道同时调节
  LUT_CHANNEL_RED,    //红色通道
  LUT_CHANNEL_GREEN,  //绿色通道
  LUT_CHANNEL_BLUE,   //蓝色通道
}emSdkLutChannel;

//ISP处理单元
typedef enum
{
  ISP_PROCESSSOR_PC = 0,//使用PC的软件ISP模块
  ISP_PROCESSSOR_DEVICE //使用相机自带的硬件ISP模块
}emSdkIspProcessor;

//闪光灯信号控制方式
typedef enum
{
  STROBE_SYNC_WITH_TRIG_AUTO = 0,    //和触发信号同步，触发后，相机进行曝光时，自动生成STROBE信号。此时，有效极性可设置(CameraSetStrobePolarity)。
  STROBE_SYNC_WITH_TRIG_MANUAL,      //和触发信号同步，触发后，STROBE延时指定的时间后(CameraSetStrobeDelayTime)，再持续指定时间的脉冲(CameraSetStrobePulseWidth)，有效极性可设置(CameraSetStrobePolarity)。
  STROBE_ALWAYS_HIGH,                //始终为高，忽略STROBE信号的其他设置
  STROBE_ALWAYS_LOW                  //始终为低，忽略STROBE信号的其他设置
}emStrobeControl;

//硬件外触发的信号种类
typedef enum
{
    EXT_TRIG_LEADING_EDGE = 0,      //上升沿触发，默认为该方式
    EXT_TRIG_TRAILING_EDGE,         //下降沿触发
    EXT_TRIG_HIGH_LEVEL,            //高电平触发,电平宽度决定曝光时间，仅部分型号的相机支持电平触发方式。
    EXT_TRIG_LOW_LEVEL,             //低电平触发
    EXT_TRIG_DOUBLE_EDGE,           //双边沿触发
}emExtTrigSignal;

//硬件外触发时的快门方式
typedef enum
{
  EXT_TRIG_EXP_STANDARD = 0,     //标准方式，默认为该方式。
  EXT_TRIG_EXP_GRR,              //全局复位方式，部分滚动快门的CMOS型号的相机支持该方式，配合外部机械快门，可以达到全局快门的效果，适合拍高速运动的物体
}emExtTrigShutterMode;

// 清晰度评估算法
typedef enum
{
    EVALUATE_DEFINITION_DEVIATION = 0,  // 方差法
    EVALUATE_DEFINITION_SMD,            // 相邻像素灰度方差法
    EVALUATE_DEFINITION_GRADIENT,       // 梯度统计
    EVALUATE_DEFINITION_SOBEL,          // Sobel
    EVALUATE_DEFINITION_ROBERT,         // Robert
    EVALUATE_DEFINITION_LAPLACE,        // Laplace
    EVALUATE_DEFINITION_ALG_MAX,
}emEvaluateDefinitionAlgorith;


// GPIO模式
typedef enum
{
    IOMODE_TRIG_INPUT = 0,      //触发输入
    IOMODE_STROBE_OUTPUT,       //闪光灯输出
    IOMODE_GP_INPUT,            //通用型输入
    IOMODE_GP_OUTPUT,           //通用型输出
    IOMODE_PWM_OUTPUT,          //PWM型输出
}emCameraGPIOMode;

