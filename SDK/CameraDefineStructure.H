
//相机的分辨率设定范围，用于构件UI
typedef struct
{
  INT iHeightMax;             //图像最大高度
  INT iHeightMin;             //图像最小高度
  INT iWidthMax;              //图像最大宽度
  INT iWidthMin;              //图像最小宽度
  UINT uSkipModeMask;         //SKIP模式掩码，为0，表示不支持SKIP 。bit0为1,表示支持SKIP 2x2 ;bit1为1，表示支持SKIP 3x3....
  UINT uBinSumModeMask;       //BIN(求和)模式掩码，为0，表示不支持BIN 。bit0为1,表示支持BIN 2x2 ;bit1为1，表示支持BIN 3x3....
  UINT uBinAverageModeMask;   //BIN(求均值)模式掩码，为0，表示不支持BIN 。bit0为1,表示支持BIN 2x2 ;bit1为1，表示支持BIN 3x3....
  UINT uResampleMask;         //硬件重采样的掩码
} tSdkResolutionRange;


//相机的分辨率描述
typedef struct
{
  INT     iIndex;             // 索引号，[0,N]表示预设的分辨率(N 为预设分辨率的最大个数，一般不超过20),OXFF 表示自定义分辨率(ROI)
  char    acDescription[32];  // 该分辨率的描述信息。仅预设分辨率时该信息有效。自定义分辨率可忽略该信息
  UINT    uBinSumMode;        // BIN(求和)的模式,范围不能超过tSdkResolutionRange中uBinSumModeMask
  UINT    uBinAverageMode;    // BIN(求均值)的模式,范围不能超过tSdkResolutionRange中uBinAverageModeMask
  UINT    uSkipMode;          // 是否SKIP的尺寸，为0表示禁止SKIP模式，范围不能超过tSdkResolutionRange中uSkipModeMask
  UINT    uResampleMask;      // 硬件重采样的掩码
  INT     iHOffsetFOV;        // 采集视场相对于Sensor最大视场左上角的垂直偏移
  INT     iVOffsetFOV;        // 采集视场相对于Sensor最大视场左上角的水平偏移
  INT     iWidthFOV;          // 采集视场的宽度
  INT     iHeightFOV;         // 采集视场的高度
  INT     iWidth;             // 相机最终输出的图像的宽度
  INT     iHeight;            // 相机最终输出的图像的高度
  INT     iWidthZoomHd;       // 硬件缩放的宽度,不需要进行此操作的分辨率，此变量设置为0.
  INT     iHeightZoomHd;      // 硬件缩放的高度,不需要进行此操作的分辨率，此变量设置为0.
  INT     iWidthZoomSw;       // 软件缩放的宽度,不需要进行此操作的分辨率，此变量设置为0.
  INT     iHeightZoomSw;      // 软件缩放的高度,不需要进行此操作的分辨率，此变量设置为0.
} tSdkImageResolution;

//相机白平衡色温模式描述信息
typedef struct
{
    INT  iIndex;            // 模式索引号
    char acDescription[32]; // 描述信息
} tSdkColorTemperatureDes;

//相机帧率描述信息
typedef struct
{
    INT  iIndex;             // 帧率索引号，一般0对应于低速模式，1对应于普通模式，2对应于高速模式
    char acDescription[32];  // 描述信息
} tSdkFrameSpeed;

//相机曝光功能范围定义
typedef struct
{
    UINT  uiTargetMin;      //自动曝光亮度目标最小值
    UINT  uiTargetMax;      //自动曝光亮度目标最大值
    UINT  uiAnalogGainMin;  //模拟增益的最小值，单位为fAnalogGainStep中定义
    UINT  uiAnalogGainMax;  //模拟增益的最大值，单位为fAnalogGainStep中定义
    float fAnalogGainStep;  //模拟增益每增加1，对应的增加的放大倍数。例如，uiAnalogGainMin一般为16，fAnalogGainStep一般为0.125，那么最小放大倍数就是16*0.125 = 2倍
    UINT  uiExposeTimeMin;  //手动模式下，曝光时间的最小值，单位:行。根据CameraGetExposureLineTime可以获得一行对应的时间(微秒),从而得到整帧的曝光时间
    UINT  uiExposeTimeMax;  //手动模式下，曝光时间的最大值，单位:行
} tSdkExpose;

//触发模式描述
typedef struct
{
  INT   iIndex;            //模式索引号
  char  acDescription[32]; //该模式的描述信息
} tSdkTrigger;

//传输分包大小描述(主要是针对网络相机有效)
typedef struct
{
    INT  iIndex;              //分包大小索引号
    char acDescription[32];   //对应的描述信息
    UINT iPackSize;
} tSdkPackLength;

//预设的LUT表描述
typedef struct
{
    INT  iIndex;                //编号
    char acDescription[32];     //描述信息
} tSdkPresetLut;

//AE算法描述
typedef struct
{
    INT  iIndex;                //编号
    char acDescription[32];     //描述信息
} tSdkAeAlgorithm;

//RAW转RGB算法描述
typedef struct
{
    INT  iIndex;                //编号
    char acDescription[32];     //描述信息
} tSdkBayerDecodeAlgorithm;


//帧率统计信息
typedef struct
{
  INT iTotal;           //当前采集的总帧数（包括错误帧）
    INT iCapture;       //当前采集的有效帧的数量
    INT iLost;          //当前丢帧的数量
} tSdkFrameStatistic;

//相机输出的图像数据格式
typedef struct
{
  INT     iIndex;             //格式种类编号
  char    acDescription[32];  //描述信息
  UINT    iMediaType;         //对应的图像格式编码，如CAMERA_MEDIA_TYPE_BAYGR8，在本文件中有定义。
} tSdkMediaType;

//伽马的设定范围
typedef struct
{
  INT iMin;       //最小值
  INT iMax;       //最大值
} tGammaRange;

//对比度的设定范围
typedef struct
{
    INT iMin;   //最小值
    INT iMax;   //最大值
} tContrastRange;

//RGB三通道数字增益的设定范围
typedef struct
{
    INT iRGainMin;    //红色增益的最小值
    INT iRGainMax;    //红色增益的最大值
    INT iGGainMin;    //绿色增益的最小值
    INT iGGainMax;    //绿色增益的最大值
    INT iBGainMin;    //蓝色增益的最小值
    INT iBGainMax;    //蓝色增益的最大值
} tRgbGainRange;

//饱和度设定的范围
typedef struct
{
    INT iMin;   //最小值
    INT iMax;   //最大值
} tSaturationRange;

//锐化的设定范围
typedef struct
{
  INT iMin;   //最小值
  INT iMax;   //最大值
} tSharpnessRange;

//ISP模块的使能信息
typedef struct
{
    BOOL bMonoSensor;       //表示该型号相机是否为黑白相机,如果是黑白相机，则颜色相关的功能都无法调节
    BOOL bWbOnce;           //表示该型号相机是否支持手动白平衡功能
    BOOL bAutoWb;           //表示该型号相机是否支持自动白平衡功能
    BOOL bAutoExposure;     //表示该型号相机是否支持自动曝光功能
    BOOL bManualExposure;   //表示该型号相机是否支持手动曝光功能
    BOOL bAntiFlick;        //表示该型号相机是否支持抗频闪功能
    BOOL bDeviceIsp;        //表示该型号相机是否支持硬件ISP功能
    BOOL bForceUseDeviceIsp;//bDeviceIsp和bForceUseDeviceIsp同时为TRUE时，表示强制只用硬件ISP，不可取消。
    BOOL bZoomHD;           //相机硬件是否支持图像缩放输出(只能是缩小)。
} tSdkIspCapacity;


