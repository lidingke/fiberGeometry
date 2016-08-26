def enum(**enums):
    return type('Enum', (), enums)

        
emSdkLutMode = enum(
LUTMODE_PARAM_GEN = 0 ,#//ͨ�����ڲ�����̬����LUT��
LUTMODE_PRESET = 1 ,#ʹ��Ԥ���LUT��
LUTMODE_USER_DEF  = 2) # //ʹ���û��Զ����LUT��


emSdkRunMode = enum(
RUNMODE_PLAY = 0 ,#����Ԥ��������ͼ�����ʾ�������������ڴ���ģʽ�����ȴ�����֡�ĵ�����
RUNMODE_PAUSE = 1 ,#��ͣ������ͣ�����ͼ�������ͬʱҲ����ȥ����ͼ��
RUNMODE_STOP  = 2) # //ֹͣ�������������ʼ��������ʹ���ֹͣģʽ


emSdkDisplayMode = enum(
DISPLAYMODE_SCALE = 0 ,#������ʾģʽ�����ŵ���ʾ�ؼ��ĳߴ�
DISPLAYMODE_REAL  = 1) # //1:1��ʾģʽ����ͼ��ߴ������ʾ�ؼ��ĳߴ�ʱ��ֻ��ʾ�ֲ�


emSdkRecordMode = enum(
RECORD_STOP  = 0 ,#ֹͣ
RECORD_START = 1 ,#¼����
RECORD_PAUSE  = 2) # //��ͣ


emSdkMirrorDirection = enum(
MIRROR_DIRECTION_HORIZONTAL  = 0 ,#//ˮƽ����
MIRROR_DIRECTION_VERTICAL  = 1) # //��ֱ����


emSdkRotateDirection = enum(
ROTATE_DIRECTION_0  = 0 ,# ����ת
ROTATE_DIRECTION_90 = 1 ,# ��ʱ��90��
ROTATE_DIRECTION_180 = 2 ,# ��ʱ��180��
ROTATE_DIRECTION_270 = 3) #  ��ʱ��270��


emSdkFrameSpeed = enum(
FRAME_SPEED_LOW  = 0 ,#����ģʽ
FRAME_SPEED_NORMAL = 1 ,#��ͨģʽ
FRAME_SPEED_HIGH = 2 ,#����ģʽ(��Ҫ�ϸߵĴ������,���豸���������ʱ���֡�ʵ��ȶ�����Ӱ��)
FRAME_SPEED_SUPER //超高速模式(需要较高的传输带宽 = 3) # ���豸���������ʱ���֡�ʵ��ȶ�����Ӱ��)


emSdkSnapMode = enum(
CONTINUATION  = 0 ,#//�����ɼ�ģʽ
SOFT_TRIGGER = 1 ,#�������ģʽ�����������ָ��󣬴�������ʼ�ɼ�ָ��֡����ͼ�񣬲ɼ���ɺ�ֹͣ���
EXTERNAL_TRIGGER  = 2) # //Ӳ������ģʽ�������յ��ⲿ�źţ���������ʼ�ɼ�ָ��֡����ͼ�񣬲ɼ���ɺ�ֹͣ���


emSdkLightFrequency = enum(
LIGHT_FREQUENCY_50HZ  = 0 ,#//50HZ,һ��ĵƹⶼ��50HZ
LIGHT_FREQUENCY_60HZ //60HZ = 1) # ��Ҫ��ָ��ʾ����


emSdkParameterMode = enum(
PARAM_MODE_BY_MODEL  = 0 ,#��������ͺ������ļ��м��ز���������MV-U300
PARAM_MODE_BY_NAME = 1 ,#�����豸�ǳ�(tSdkCameraDevInfo.acFriendlyName)���ļ��м��ز���������MV-U300,���ǳƿ��Զ���
PARAM_MODE_BY_SN = 2 ,#�����豸��Ψһ���кŴ��ļ��м��ز��������к��ڳ���ʱ�Ѿ�д���豸��ÿ̨���ӵ�в�ͬ�����кš�
PARAM_MODE_IN_DEVICE  = 3) # //���豸�Ĺ�̬�洢���м��ز������������е��ͺŶ�֧�ִ�����ж�д�����飬��tSdkCameraCapbility.bParamInDevice����


emSdkPropSheetMask = enum(
PROP_SHEET_INDEX_EXPOSURE  = 0 ,#
PROP_SHEET_INDEX_ISP_COLOR = 1 ,#
PROP_SHEET_INDEX_ISP_LUT = 2 ,#
PROP_SHEET_INDEX_ISP_SHAPE = 3 ,#
PROP_SHEET_INDEX_VIDEO_FORMAT = 4 ,#
PROP_SHEET_INDEX_RESOLUTION = 5 ,#
PROP_SHEET_INDEX_IO_CTRL = 6 ,#
PROP_SHEET_INDEX_TRIGGER_SET = 7 ,#
PROP_SHEET_INDEX_OVERLAY = 8 ,#
PROP_SHEET_INDEX_DEVICE_INFO = 9) # #


emSdkPropSheetMsg = enum(
SHEET_MSG_LOAD_PARAM_DEFAULT  = 0 ,#�������ָ���Ĭ�Ϻ󣬴�������Ϣ
SHEET_MSG_LOAD_PARAM_GROUP = 1 ,#����ָ�������飬��������Ϣ
SHEET_MSG_LOAD_PARAM_FROMFILE = 2 ,#��ָ���ļ����ز����󣬴�������Ϣ
SHEET_MSG_SAVE_PARAM_GROUP  = 3) # //��ǰ�����鱻����ʱ����������Ϣ


emSdkRefWinType = enum(
REF_WIN_AUTO_EXPOSURE  = 0 ,#
REF_WIN_WHITE_BALANCE = 1) # 


emSdkResolutionMode = enum(
RES_MODE_PREVIEW  = 0 ,#
RES_MODE_SNAPSHOT = 1) # 


emSdkClrTmpMode = enum(
CT_MODE_AUTO  = 0 ,#�Զ�ʶ��ɫ��
CT_MODE_PRESET = 1 ,#ʹ��ָ����Ԥ��ɫ��
CT_MODE_USER_DEF  = 2) # //�Զ���ɫ��(����;���)


emSdkLutChannel = enum(
LUT_CHANNEL_ALL  = 0 ,#//R,B,G��ͨ��ͬʱ����
LUT_CHANNEL_RED = 1 ,#��ɫͨ��
LUT_CHANNEL_GREEN = 2 ,#��ɫͨ��
LUT_CHANNEL_BLUE = 3) # ��ɫͨ��


emSdkIspProcessor = enum(
ISP_PROCESSSOR_PC  = 0 ,#//ʹ��PC�����ISPģ��
ISP_PROCESSSOR_DEVICE  = 1) # //ʹ������Դ���Ӳ��ISPģ��


emStrobeControl = enum(
STROBE_SYNC_WITH_TRIG_AUTO  = 0 ,#�ʹ����ź�ͬ������������������ع�ʱ���Զ�����STROBE�źš���ʱ����Ч���Կ�����(CameraSetStrobePolarity)��
STROBE_SYNC_WITH_TRIG_MANUAL = 1 ,#�ʹ����ź�ͬ����������STROBE��ʱָ����ʱ���(CameraSetStrobeDelayTime)���ٳ���ָ��ʱ�������(CameraSetStrobePulseWidth)����Ч���Կ�����(CameraSetStrobePolarity)��
STROBE_ALWAYS_HIGH = 2 ,#ʼ��Ϊ�ߣ�����STROBE�źŵ���������
STROBE_ALWAYS_LOW  = 3) # //ʼ��Ϊ�ͣ�����STROBE�źŵ���������


emExtTrigSignal = enum(
EXT_TRIG_LEADING_EDGE  = 0 ,#�����ش�����Ĭ��Ϊ�÷�ʽ
EXT_TRIG_TRAILING_EDGE = 1 ,#�½��ش���
EXT_TRIG_HIGH_LEVEL = 2 ,#�ߵ�ƽ����,��ƽ��Ⱦ����ع�ʱ�䣬�������ͺŵ����֧�ֵ�ƽ������ʽ��
EXT_TRIG_LOW_LEVEL = 3 ,#�͵�ƽ����
EXT_TRIG_DOUBLE_EDGE = 4) # ˫���ش���


emExtTrigShutterMode = enum(
EXT_TRIG_EXP_STANDARD  = 0 ,#��׼��ʽ��Ĭ��Ϊ�÷�ʽ��
EXT_TRIG_EXP_GRR = 1) # ȫ�ָ�λ��ʽ�����ֹ������ŵ�CMOS�ͺŵ����֧�ָ÷�ʽ������ⲿ��е���ţ����Դﵽȫ�ֿ��ŵ�Ч�����ʺ��ĸ����˶�������


emEvaluateDefinitionAlgorith = enum(
EVALUATE_DEFINITION_DEVIATION  = 0 ,# ���
EVALUATE_DEFINITION_SMD = 1 ,# �������ػҶȷ��
EVALUATE_DEFINITION_GRADIENT = 2 ,# �ݶ�ͳ��
EVALUATE_DEFINITION_SOBEL = 3 ,# Sobel
EVALUATE_DEFINITION_ROBERT = 4 ,# Robert
EVALUATE_DEFINITION_LAPLACE = 5 ,# Laplace
EVALUATE_DEFINITION_ALG_MAX = 6) # 


emCameraGPIOMode = enum(
IOMODE_TRIG_INPUT  = 0 ,#��������
IOMODE_STROBE_OUTPUT = 1 ,#��������
IOMODE_GP_INPUT = 2 ,#ͨ��������
IOMODE_GP_OUTPUT = 3 ,#ͨ�������
IOMODE_PWM_OUTPUT = 4) # PWM�����

