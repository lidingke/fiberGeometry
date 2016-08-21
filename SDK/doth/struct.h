
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


//图像帧头信息
typedef struct
{
  UINT    uiMediaType;    // 图像格式,Image Format
  UINT    uBytes;         // 图像数据字节数,Total bytes
  INT     iWidth;         // 图像的宽度，调用图像处理函数后，该变量可能被动态修改，来指示处理后的图像尺寸
  INT     iHeight;        // 图像的高度，调用图像处理函数后，该变量可能被动态修改，来指示处理后的图像尺寸
  INT     iWidthZoomSw;   // 软件缩放的宽度,不需要进行软件裁剪的图像，此变量设置为0.
  INT     iHeightZoomSw;  // 软件缩放的高度,不需要进行软件裁剪的图像，此变量设置为0.
  BOOL    bIsTrigger;     // 指示是否为触发帧 is trigger
  UINT    uiTimeStamp;    // 该帧的采集时间，单位0.1毫秒
  UINT    uiExpTime;      // 当前图像的曝光值，单位为微秒us
  float   fAnalogGain;    // 当前图像的模拟增益倍数
  INT     iGamma;         // 该帧图像的伽马设定值，仅当LUT模式为动态参数生成时有效，其余模式下为-1
  INT     iContrast;      // 该帧图像的对比度设定值，仅当LUT模式为动态参数生成时有效，其余模式下为-1
  INT     iSaturation;    // 该帧图像的饱和度设定值，对于黑白相机无意义，为0
  float   fRgain;         // 该帧图像处理的红色数字增益倍数，对于黑白相机无意义，为1
  float   fGgain;         // 该帧图像处理的绿色数字增益倍数，对于黑白相机无意义，为1
  float   fBgain;         // 该帧图像处理的蓝色数字增益倍数，对于黑白相机无意义，为1
}tSdkFrameHead;

//图像帧描述
typedef struct sCameraFrame
{
  tSdkFrameHead   head;     //帧头
  BYTE *          pBuffer;  //数据区
}tSdkFrame;

// //图像捕获的回调函数定义
// typedef void (WINAPI* CAMERA_SNAP_PROC)(CameraHandle hCamera, BYTE *pFrameBuffer, tSdkFrameHead* pFrameHead,PVOID pContext);

// //SDK生成的相机配置页面的消息回调函数定义
// typedef void (WINAPI* CAMERA_PAGE_MSG_PROC)(CameraHandle hCamera,UINT MSG,UINT uParam,PVOID pContext);


//////////////////////////////////////////////////////////////////////////
// Grabber 相关

// Grabber统计信息
typedef struct
{
    int Width;  // 帧图像大小
    int Height;
    int Disp;           // 显示帧数量
    int Capture;        // 采集的有效帧的数量
    int Lost;           // 丢帧的数量
    int Error;          // 错帧的数量
    float DispFps;      // 显示帧率
    float CapFps;       // 捕获帧率
}tSdkGrabberStat;

//相机的设备信息
typedef struct
{
    char acProductSeries[32];   // 产品系列
    char acProductName[32];     // 产品名称
    char acFriendlyName[32];    // 产品昵称，用户可自定义改昵称，保存在相机内，用于区分多个相机同时使用,可以用CameraSetFriendlyName接口改变该昵称，设备重启后生效。
    char acLinkName[32];        // 内核符号连接名，内部使用
    char acDriverVersion[32];   // 驱动版本
    char acSensorType[32];      // sensor类型
    char acPortType[32];        // 接口类型
    char acSn[32];              // 产品唯一序列号
    UINT uInstance;             // 该型号相机在该电脑上的实例索引号，用于区分同型号多相机
} tSdkCameraDevInfo;

//* 定义整合的设备描述信息，这些信息可以用于动态构建UI */
typedef struct {
  tSdkTrigger   *pTriggerDesc;          // 触发模式
  INT           iTriggerDesc;           // 触发模式的个数，即pTriggerDesc数组的大小
  tSdkImageResolution   *pImageSizeDesc;// 预设分辨率选择
  INT                   iImageSizeDesc; // 预设分辨率的个数，即pImageSizeDesc数组的大小
  tSdkColorTemperatureDes *pClrTempDesc;// 预设色温模式，用于白平衡
  INT                     iClrTempDesc;
  tSdkMediaType     *pMediaTypeDesc;    // 相机输出图像格式
  INT               iMediaTypdeDesc;    // 相机输出图像格式的种类个数，即pMediaTypeDesc数组的大小。
  tSdkFrameSpeed    *pFrameSpeedDesc;   // 可调节帧速类型，对应界面上普通 高速 和超级三种速度设置
  INT               iFrameSpeedDesc;    // 可调节帧速类型的个数，即pFrameSpeedDesc数组的大小。
  tSdkPackLength    *pPackLenDesc;      // 传输包长度，一般用于网络设备
  INT               iPackLenDesc;       // 可供选择的传输分包长度的个数，即pPackLenDesc数组的大小。
  INT           iOutputIoCounts;        // 可编程输出IO的个数
  INT           iInputIoCounts;         // 可编程输入IO的个数
  tSdkPresetLut  *pPresetLutDesc;       // 相机预设的LUT表
  INT            iPresetLut;            // 相机预设的LUT表的个数，即pPresetLutDesc数组的大小
  INT           iUserDataMaxLen;        // 指示该相机中用于保存用户数据区的最大长度。为0表示无。
  BOOL          bParamInDevice;         // 指示该设备是否支持从设备中读写参数组。1为支持，0不支持。
  tSdkAeAlgorithm   *pAeAlmSwDesc;      // 软件自动曝光算法描述
  int                iAeAlmSwDesc;      // 软件自动曝光算法个数
  tSdkAeAlgorithm    *pAeAlmHdDesc;     // 硬件自动曝光算法描述，为NULL表示不支持硬件自动曝光
  int                iAeAlmHdDesc;      // 硬件自动曝光算法个数，为0表示不支持硬件自动曝光
  tSdkBayerDecodeAlgorithm   *pBayerDecAlmSwDesc; // 软件Bayer转换为RGB数据的算法描述
  int                        iBayerDecAlmSwDesc;  // 软件Bayer转换为RGB数据的算法个数
  tSdkBayerDecodeAlgorithm   *pBayerDecAlmHdDesc; // 硬件Bayer转换为RGB数据的算法描述，为NULL表示不支持
  int                        iBayerDecAlmHdDesc;  // 硬件Bayer转换为RGB数据的算法个数，为0表示不支持
  //* 图像参数的调节范围定义,用于动态构建UI*/
  tSdkExpose            sExposeDesc;      // 曝光的范围值
  tSdkResolutionRange   sResolutionRange; // 分辨率范围描述
  tRgbGainRange         sRgbGainRange;    // 图像数字增益范围描述
  tSaturationRange      sSaturationRange; // 饱和度范围描述
  tGammaRange           sGammaRange;      // 伽马范围描述
  tContrastRange        sContrastRange;   // 对比度范围描述
  tSharpnessRange       sSharpnessRange;  // 锐化范围描述
  tSdkIspCapacity       sIspCapacity;     // ISP能力描述
} tSdkCameraCapbility;
