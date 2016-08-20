
//相机的分辨率描述
typedef struct
{
  INT     iIndex;             // 索引号，[0,N]表示预设的分辨率(N 为预设分辨率的最大个数，一般不超过20),OXFF 表示自定义分辨率(ROI)
  char    acDescription[32];  // 该分辨率的描述信息。仅预设分辨率时该信息有效。自定义分辨率可忽略该信息
  UINT    uBinSumMode;        // BIN(求和)的模式,范围不能超过tSdkResolutionRange中uBinSumModeMask
  UINT    uBinAverageMode;    // BIN(求均值)的模式,范围不能超过tSdkResolutionRange中uBinAverageModeMask
  UINT    uSkipMode;          // 是否SKIP的尺寸，为0表示禁止SKIP模式，范围不能超过tSdkResolutionRange中uSkipModeMask
  UINT    * uResampleMask;      // 硬件重采样的掩码
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


