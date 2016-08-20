
class tSdkResolutionRange(Structure):
    _fields_ = [
    ("iHeightMax", c_int), #ͼ�����߶�
    ("iHeightMin", c_int), #ͼ����С�߶�
    ("iWidthMax", c_int), #ͼ�������
    ("iWidthMin", c_int), #ͼ����С���
    ("uSkipModeMask", c_uint), #SKIPģʽ���룬Ϊ0����ʾ��֧��SKIP ��bit0Ϊ1,��ʾ֧��SKIP 2x2 ;bit1Ϊ1����ʾ֧��SKIP 3x3....
    ("uBinSumModeMask", c_uint), #BIN(���)ģʽ���룬Ϊ0����ʾ��֧��BIN ��bit0Ϊ1,��ʾ֧��BIN 2x2 ;bit1Ϊ1����ʾ֧��BIN 3x3....
    ("uBinAverageModeMask", c_uint), #BIN(���ֵ)ģʽ���룬Ϊ0����ʾ��֧��BIN ��bit0Ϊ1,��ʾ֧��BIN 2x2 ;bit1Ϊ1����ʾ֧��BIN 3x3....
    ("uResampleMask", c_uint)] Ӳ���ز���������
    

class tSdkImageResolution(Structure):
    _fields_ = [
    ("iIndex", c_int), # �����ţ�[0,N]��ʾԤ��ķֱ���(N ΪԤ��ֱ��ʵ���������һ�㲻����20),OXFF ��ʾ�Զ���ֱ���(ROI)
    ("acDescriptio", char * 32), # �÷ֱ��ʵ�������Ϣ����Ԥ��ֱ���ʱ����Ϣ��Ч���Զ���ֱ��ʿɺ��Ը���Ϣ
    ("uBinSumMode", c_uint), # BIN(���)��ģʽ,��Χ���ܳ���tSdkResolutionRange��uBinSumModeMask
    ("uBinAverageMode", c_uint), # BIN(���ֵ)��ģʽ,��Χ���ܳ���tSdkResolutionRange��uBinAverageModeMask
    ("uSkipMode", c_uint), # �Ƿ�SKIP�ĳߴ磬Ϊ0��ʾ��ֹSKIPģʽ����Χ���ܳ���tSdkResolutionRange��uSkipModeMask
    ("uResampleMask", c_uint), # Ӳ���ز���������
    ("iHOffsetFOV", c_int), # �ɼ��ӳ������Sensor����ӳ����ϽǵĴ�ֱƫ��
    ("iVOffsetFOV", c_int), # �ɼ��ӳ������Sensor����ӳ����Ͻǵ�ˮƽƫ��
    ("iWidthFOV", c_int), # �ɼ��ӳ��Ŀ��
    ("iHeightFOV", c_int), # �ɼ��ӳ��ĸ߶�
    ("iWidth", c_int), # ������������ͼ��Ŀ��
    ("iHeight", c_int), # ������������ͼ��ĸ߶�
    ("iWidthZoomHd", c_int), # Ӳ�����ŵĿ��,����Ҫ���д˲����ķֱ��ʣ��˱�������Ϊ0.
    ("iHeightZoomHd", c_int), # Ӳ�����ŵĸ߶�,����Ҫ���д˲����ķֱ��ʣ��˱�������Ϊ0.
    ("iWidthZoomSw", c_int), # ������ŵĿ��,����Ҫ���д˲����ķֱ��ʣ��˱�������Ϊ0.
    ("iHeightZoomSw", c_int)]  ������ŵĸ߶�,����Ҫ���д˲����ķֱ��ʣ��˱�������Ϊ0.
    

class tSdkColorTemperatureDes(Structure):
    _fields_ = [
    ("iIndex", c_int), # ģʽ������
    ("acDescriptio", char * 32)]  ������Ϣ
    

class tSdkFrameSpeed(Structure):
    _fields_ = [
    ("iIndex", c_int), # ֡�������ţ�һ��0��Ӧ�ڵ���ģʽ��1��Ӧ����ͨģʽ��2��Ӧ�ڸ���ģʽ
    ("acDescriptio", char * 32)]  ������Ϣ
    

class tSdkExpose(Structure):
    _fields_ = [
    ("uiTargetMin", c_uint), #�Զ��ع�����Ŀ����Сֵ
    ("uiTargetMax", c_uint), #�Զ��ع�����Ŀ�����ֵ
    ("uiAnalogGainMin", c_uint), #ģ���������Сֵ����λΪfAnalogGainStep�ж���
    ("uiAnalogGainMax", c_uint), #ģ����������ֵ����λΪfAnalogGainStep�ж���
    ("fAnalogGainStep", c_float), #ģ������ÿ����1����Ӧ�����ӵķŴ��������磬uiAnalogGainMinһ��Ϊ16��fAnalogGainStepһ��Ϊ0.125����ô��С�Ŵ�������16*0.125 = 2��
    ("uiExposeTimeMin", c_uint), #�ֶ�ģʽ�£��ع�ʱ�����Сֵ����λ:�С�����CameraGetExposureLineTime���Ի��һ�ж�Ӧ��ʱ��(΢��),�Ӷ��õ���֡���ع�ʱ��
    ("uiExposeTimeMax", c_uint)] �ֶ�ģʽ�£��ع�ʱ������ֵ����λ:��
    

class tSdkTrigger(Structure):
    _fields_ = [
    ("iIndex", c_int), #ģʽ������
    ("acDescriptio", char * 32)] ��ģʽ��������Ϣ
    

class tSdkPackLength(Structure):
    _fields_ = [
    ("iIndex", c_int), #�ְ���С������
    ("acDescriptio", char * 32), #��Ӧ��������Ϣ
    ("iPackSize", c_uint)] 
    

class tSdkPresetLut(Structure):
    _fields_ = [
    ("iIndex", c_int), #���
    ("acDescriptio", char * 32)] ������Ϣ
    

class tSdkAeAlgorithm(Structure):
    _fields_ = [
    ("iIndex", c_int), #���
    ("acDescriptio", char * 32)] ������Ϣ
    

class tSdkBayerDecodeAlgorithm(Structure):
    _fields_ = [
    ("iIndex", c_int), #���
    ("acDescriptio", char * 32)] ������Ϣ
    

class tSdkFrameStatistic(Structure):
    _fields_ = [
    ("iTotal", c_int), #��ǰ�ɼ�����֡������������֡��
    ("iCapture", c_int), #��ǰ�ɼ�����Ч֡������
    ("iLost", c_int)] ��ǰ��֡������
    

class tSdkMediaType(Structure):
    _fields_ = [
    ("iIndex", c_int), #��ʽ������
    ("acDescriptio", char * 32), #������Ϣ
    ("iMediaType", c_uint)] ��Ӧ��ͼ���ʽ���룬��CAMERA_MEDIA_TYPE_BAYGR8���ڱ��ļ����ж��塣
    

class tGammaRange(Structure):
    _fields_ = [
    ("iMin", c_int), #��Сֵ
    ("iMax", c_int)] ���ֵ
    

class tContrastRange(Structure):
    _fields_ = [
    ("iMin", c_int), #��Сֵ
    ("iMax", c_int)] ���ֵ
    

class tRgbGainRange(Structure):
    _fields_ = [
    ("iRGainMin", c_int), #��ɫ�������Сֵ
    ("iRGainMax", c_int), #��ɫ��������ֵ
    ("iGGainMin", c_int), #��ɫ�������Сֵ
    ("iGGainMax", c_int), #��ɫ��������ֵ
    ("iBGainMin", c_int), #��ɫ�������Сֵ
    ("iBGainMax", c_int)] ��ɫ��������ֵ
    

class tSaturationRange(Structure):
    _fields_ = [
    ("iMin", c_int), #��Сֵ
    ("iMax", c_int)] ���ֵ
    

class tSharpnessRange(Structure):
    _fields_ = [
    ("iMin", c_int), #��Сֵ
    ("iMax", c_int)] ���ֵ
    

class tSdkIspCapacity(Structure):
    _fields_ = [
    ("bMonoSensor", c_bool), #��ʾ���ͺ�����Ƿ�Ϊ�ڰ����,����Ǻڰ����������ɫ��صĹ��ܶ��޷�����
    ("bWbOnce", c_bool), #��ʾ���ͺ�����Ƿ�֧���ֶ���ƽ�⹦��
    ("bAutoWb", c_bool), #��ʾ���ͺ�����Ƿ�֧���Զ���ƽ�⹦��
    ("bAutoExposure", c_bool), #��ʾ���ͺ�����Ƿ�֧���Զ��ع⹦��
    ("bManualExposure", c_bool), #��ʾ���ͺ�����Ƿ�֧���ֶ��ع⹦��
    ("bAntiFlick", c_bool), #��ʾ���ͺ�����Ƿ�֧�ֿ�Ƶ������
    ("bDeviceIsp", c_bool), #��ʾ���ͺ�����Ƿ�֧��Ӳ��ISP����
    ("bForceUseDeviceIsp", c_bool), #//bDeviceIsp��bForceUseDeviceIspͬʱΪTRUEʱ����ʾǿ��ֻ��Ӳ��ISP������ȡ����
    ("bZoomHD", c_bool)] ���Ӳ���Ƿ�֧��ͼ���������(ֻ������С)��
    
