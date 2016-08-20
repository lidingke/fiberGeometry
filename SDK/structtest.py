
class tSdkResolutionRange(Structure):
    _fields_ = [
    ("iHeightMax", c_int), #图像最大高度
    ("iHeightMin", c_int), #图像最小高度
    ("iWidthMax", c_int), #图像最大宽度
    ("iWidthMin", c_int), #图像最小宽度
    ("uSkipModeMask", c_uint), #SKIP模式掩码，为0，表示不支持SKIP 。bit0为1,表示支持SKIP 2x2 ;bit1为1，表示支持SKIP 3x3....
    ("uBinSumModeMask", c_uint), #BIN(求和)模式掩码，为0，表示不支持BIN 。bit0为1,表示支持BIN 2x2 ;bit1为1，表示支持BIN 3x3....
    ("uBinAverageModeMask", c_uint), #BIN(求均值)模式掩码，为0，表示不支持BIN 。bit0为1,表示支持BIN 2x2 ;bit1为1，表示支持BIN 3x3....
    ("uResampleMask", c_uint)] 硬件重采样的掩码
    

class tSdkImageResolution(Structure):
    _fields_ = [
    ("iIndex", c_int), # 索引号，[0,N]表示预设的分辨率(N 为预设分辨率的最大个数，一般不超过20),OXFF 表示自定义分辨率(ROI)
    ("acDescriptio", char * 32), # 该分辨率的描述信息。仅预设分辨率时该信息有效。自定义分辨率可忽略该信息
    ("uBinSumMode", c_uint), # BIN(求和)的模式,范围不能超过tSdkResolutionRange中uBinSumModeMask
    ("uBinAverageMode", c_uint), # BIN(求均值)的模式,范围不能超过tSdkResolutionRange中uBinAverageModeMask
    ("uSkipMode", c_uint), # 是否SKIP的尺寸，为0表示禁止SKIP模式，范围不能超过tSdkResolutionRange中uSkipModeMask
    ("uResampleMask", c_uint), # 硬件重采样的掩码
    ("iHOffsetFOV", c_int), # 采集视场相对于Sensor最大视场左上角的垂直偏移
    ("iVOffsetFOV", c_int), # 采集视场相对于Sensor最大视场左上角的水平偏移
    ("iWidthFOV", c_int), # 采集视场的宽度
    ("iHeightFOV", c_int), # 采集视场的高度
    ("iWidth", c_int), # 相机最终输出的图像的宽度
    ("iHeight", c_int), # 相机最终输出的图像的高度
    ("iWidthZoomHd", c_int), # 硬件缩放的宽度,不需要进行此操作的分辨率，此变量设置为0.
    ("iHeightZoomHd", c_int), # 硬件缩放的高度,不需要进行此操作的分辨率，此变量设置为0.
    ("iWidthZoomSw", c_int), # 软件缩放的宽度,不需要进行此操作的分辨率，此变量设置为0.
    ("iHeightZoomSw", c_int)]  软件缩放的高度,不需要进行此操作的分辨率，此变量设置为0.
    

class tSdkColorTemperatureDes(Structure):
    _fields_ = [
    ("iIndex", c_int), # 模式索引号
    ("acDescriptio", char * 32)]  描述信息
    

class tSdkFrameSpeed(Structure):
    _fields_ = [
    ("iIndex", c_int), # 帧率索引号，一般0对应于低速模式，1对应于普通模式，2对应于高速模式
    ("acDescriptio", char * 32)]  描述信息
    

class tSdkExpose(Structure):
    _fields_ = [
    ("uiTargetMin", c_uint), #自动曝光亮度目标最小值
    ("uiTargetMax", c_uint), #自动曝光亮度目标最大值
    ("uiAnalogGainMin", c_uint), #模拟增益的最小值，单位为fAnalogGainStep中定义
    ("uiAnalogGainMax", c_uint), #模拟增益的最大值，单位为fAnalogGainStep中定义
    ("fAnalogGainStep", c_float), #模拟增益每增加1，对应的增加的放大倍数。例如，uiAnalogGainMin一般为16，fAnalogGainStep一般为0.125，那么最小放大倍数就是16*0.125 = 2倍
    ("uiExposeTimeMin", c_uint), #手动模式下，曝光时间的最小值，单位:行。根据CameraGetExposureLineTime可以获得一行对应的时间(微秒),从而得到整帧的曝光时间
    ("uiExposeTimeMax", c_uint)] 手动模式下，曝光时间的最大值，单位:行
    

class tSdkTrigger(Structure):
    _fields_ = [
    ("iIndex", c_int), #模式索引号
    ("acDescriptio", char * 32)] 该模式的描述信息
    

class tSdkPackLength(Structure):
    _fields_ = [
    ("iIndex", c_int), #分包大小索引号
    ("acDescriptio", char * 32), #对应的描述信息
    ("iPackSize", c_uint)] 
    

class tSdkPresetLut(Structure):
    _fields_ = [
    ("iIndex", c_int), #编号
    ("acDescriptio", char * 32)] 描述信息
    

class tSdkAeAlgorithm(Structure):
    _fields_ = [
    ("iIndex", c_int), #编号
    ("acDescriptio", char * 32)] 描述信息
    

class tSdkBayerDecodeAlgorithm(Structure):
    _fields_ = [
    ("iIndex", c_int), #编号
    ("acDescriptio", char * 32)] 描述信息
    

class tSdkFrameStatistic(Structure):
    _fields_ = [
    ("iTotal", c_int), #当前采集的总帧数（包括错误帧）
    ("iCapture", c_int), #当前采集的有效帧的数量
    ("iLost", c_int)] 当前丢帧的数量
    

class tSdkMediaType(Structure):
    _fields_ = [
    ("iIndex", c_int), #格式种类编号
    ("acDescriptio", char * 32), #描述信息
    ("iMediaType", c_uint)] 对应的图像格式编码，如CAMERA_MEDIA_TYPE_BAYGR8，在本文件中有定义。
    

class tGammaRange(Structure):
    _fields_ = [
    ("iMin", c_int), #最小值
    ("iMax", c_int)] 最大值
    

class tContrastRange(Structure):
    _fields_ = [
    ("iMin", c_int), #最小值
    ("iMax", c_int)] 最大值
    

class tRgbGainRange(Structure):
    _fields_ = [
    ("iRGainMin", c_int), #红色增益的最小值
    ("iRGainMax", c_int), #红色增益的最大值
    ("iGGainMin", c_int), #绿色增益的最小值
    ("iGGainMax", c_int), #绿色增益的最大值
    ("iBGainMin", c_int), #蓝色增益的最小值
    ("iBGainMax", c_int)] 蓝色增益的最大值
    

class tSaturationRange(Structure):
    _fields_ = [
    ("iMin", c_int), #最小值
    ("iMax", c_int)] 最大值
    

class tSharpnessRange(Structure):
    _fields_ = [
    ("iMin", c_int), #最小值
    ("iMax", c_int)] 最大值
    

class tSdkIspCapacity(Structure):
    _fields_ = [
    ("bMonoSensor", c_bool), #表示该型号相机是否为黑白相机,如果是黑白相机，则颜色相关的功能都无法调节
    ("bWbOnce", c_bool), #表示该型号相机是否支持手动白平衡功能
    ("bAutoWb", c_bool), #表示该型号相机是否支持自动白平衡功能
    ("bAutoExposure", c_bool), #表示该型号相机是否支持自动曝光功能
    ("bManualExposure", c_bool), #表示该型号相机是否支持手动曝光功能
    ("bAntiFlick", c_bool), #表示该型号相机是否支持抗频闪功能
    ("bDeviceIsp", c_bool), #表示该型号相机是否支持硬件ISP功能
    ("bForceUseDeviceIsp", c_bool), #//bDeviceIsp和bForceUseDeviceIsp同时为TRUE时，表示强制只用硬件ISP，不可取消。
    ("bZoomHD", c_bool)] 相机硬件是否支持图像缩放输出(只能是缩小)。
    
