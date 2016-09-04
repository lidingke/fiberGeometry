def enum(**enums):
    return type('Enum', (), enums)

        
emSdkLutMode = enum(
LUTMODE_PARAM_GEN = 0 ,#//Í¨¹ýµ÷½Ú²ÎÊý¶¯Ì¬Éú³ÉLUT±í
LUTMODE_PRESET = 1 ,#Ê¹ÓÃÔ¤ÉèµÄLUT±í
LUTMODE_USER_DEF  = 2) # //Ê¹ÓÃÓÃ»§×Ô¶¨ÒåµÄLUT±í


emSdkRunMode = enum(
RUNMODE_PLAY = 0 ,#Õý³£Ô¤ÀÀ£¬²¶»ñµ½Í¼Ïñ¾ÍÏÔÊ¾¡££¨Èç¹ûÏà»ú´¦ÓÚ´¥·¢Ä£Ê½£¬Ôò»áµÈ´ý´¥·¢Ö¡µÄµ½À´£©
RUNMODE_PAUSE = 1 ,#ÔÝÍ££¬»áÔÝÍ£Ïà»úµÄÍ¼ÏñÊä³ö£¬Í¬Ê±Ò²²»»áÈ¥²¶»ñÍ¼Ïñ
RUNMODE_STOP  = 2) # //Í£Ö¹Ïà»ú¹¤×÷¡£·´³õÊ¼»¯ºó£¬Ïà»ú¾Í´¦ÓÚÍ£Ö¹Ä£Ê½


emSdkDisplayMode = enum(
DISPLAYMODE_SCALE = 0 ,#Ëõ·ÅÏÔÊ¾Ä£Ê½£¬Ëõ·Åµ½ÏÔÊ¾¿Ø¼þµÄ³ß´ç
DISPLAYMODE_REAL  = 1) # //1:1ÏÔÊ¾Ä£Ê½£¬µ±Í¼Ïñ³ß´ç´óÓÚÏÔÊ¾¿Ø¼þµÄ³ß´çÊ±£¬Ö»ÏÔÊ¾¾Ö²¿


emSdkRecordMode = enum(
RECORD_STOP  = 0 ,#Í£Ö¹
RECORD_START = 1 ,#Â¼ÏñÖÐ
RECORD_PAUSE  = 2) # //ÔÝÍ£


emSdkMirrorDirection = enum(
MIRROR_DIRECTION_HORIZONTAL  = 0 ,#//Ë®Æ½¾µÏñ
MIRROR_DIRECTION_VERTICAL  = 1) # //´¹Ö±¾µÏñ


emSdkRotateDirection = enum(
ROTATE_DIRECTION_0  = 0 ,# ²»Ðý×ª
ROTATE_DIRECTION_90 = 1 ,# ÄæÊ±Õë90¶È
ROTATE_DIRECTION_180 = 2 ,# ÄæÊ±Õë180¶È
ROTATE_DIRECTION_270 = 3) #  ÄæÊ±Õë270¶È


emSdkFrameSpeed = enum(
FRAME_SPEED_LOW  = 0 ,#µÍËÙÄ£Ê½
FRAME_SPEED_NORMAL = 1 ,#ÆÕÍ¨Ä£Ê½
FRAME_SPEED_HIGH = 2 ,#¸ßËÙÄ£Ê½(ÐèÒª½Ï¸ßµÄ´«Êä´ø¿í,¶àÉè±¸¹²Ïí´«Êä´ø¿íÊ±»á¶ÔÖ¡ÂÊµÄÎÈ¶¨ÐÔÓÐÓ°Ïì)
FRAME_SPEED_SUPER //è¶…é«˜é€Ÿæ¨¡å¼(éœ€è¦è¾ƒé«˜çš„ä¼ è¾“å¸¦å®½ = 3) # ¶àÉè±¸¹²Ïí´«Êä´ø¿íÊ±»á¶ÔÖ¡ÂÊµÄÎÈ¶¨ÐÔÓÐÓ°Ïì)


emSdkSnapMode = enum(
CONTINUATION  = 0 ,#//Á¬Ðø²É¼¯Ä£Ê½
SOFT_TRIGGER = 1 ,#Èí¼þ´¥·¢Ä£Ê½£¬ÓÉÈí¼þ·¢ËÍÖ¸Áîºó£¬´«¸ÐÆ÷¿ªÊ¼²É¼¯Ö¸¶¨Ö¡ÊýµÄÍ¼Ïñ£¬²É¼¯Íê³Éºó£¬Í£Ö¹Êä³ö
EXTERNAL_TRIGGER  = 2) # //Ó²¼þ´¥·¢Ä£Ê½£¬µ±½ÓÊÕµ½Íâ²¿ÐÅºÅ£¬´«¸ÐÆ÷¿ªÊ¼²É¼¯Ö¸¶¨Ö¡ÊýµÄÍ¼Ïñ£¬²É¼¯Íê³Éºó£¬Í£Ö¹Êä³ö


emSdkLightFrequency = enum(
LIGHT_FREQUENCY_50HZ  = 0 ,#//50HZ,Ò»°ãµÄµÆ¹â¶¼ÊÇ50HZ
LIGHT_FREQUENCY_60HZ //60HZ = 1) # Ö÷ÒªÊÇÖ¸ÏÔÊ¾Æ÷µÄ


emSdkParameterMode = enum(
PARAM_MODE_BY_MODEL  = 0 ,#¸ù¾ÝÏà»úÐÍºÅÃû´ÓÎÄ¼þÖÐ¼ÓÔØ²ÎÊý£¬ÀýÈçMV-U300
PARAM_MODE_BY_NAME = 1 ,#¸ù¾ÝÉè±¸êÇ³Æ(tSdkCameraDevInfo.acFriendlyName)´ÓÎÄ¼þÖÐ¼ÓÔØ²ÎÊý£¬ÀýÈçMV-U300,¸ÃêÇ³Æ¿É×Ô¶¨Òå
PARAM_MODE_BY_SN = 2 ,#¸ù¾ÝÉè±¸µÄÎ¨Ò»ÐòÁÐºÅ´ÓÎÄ¼þÖÐ¼ÓÔØ²ÎÊý£¬ÐòÁÐºÅÔÚ³ö³§Ê±ÒÑ¾­Ð´ÈëÉè±¸£¬Ã¿Ì¨Ïà»úÓµÓÐ²»Í¬µÄÐòÁÐºÅ¡£
PARAM_MODE_IN_DEVICE  = 3) # //´ÓÉè±¸µÄ¹ÌÌ¬´æ´¢Æ÷ÖÐ¼ÓÔØ²ÎÊý¡£²»ÊÇËùÓÐµÄÐÍºÅ¶¼Ö§³Ö´ÓÏà»úÖÐ¶ÁÐ´²ÎÊý×é£¬ÓÉtSdkCameraCapbility.bParamInDevice¾ö¶¨


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
SHEET_MSG_LOAD_PARAM_DEFAULT  = 0 ,#²ÎÊý±»»Ö¸´³ÉÄ¬ÈÏºó£¬´¥·¢¸ÃÏûÏ¢
SHEET_MSG_LOAD_PARAM_GROUP = 1 ,#¼ÓÔØÖ¸¶¨²ÎÊý×é£¬´¥·¢¸ÃÏûÏ¢
SHEET_MSG_LOAD_PARAM_FROMFILE = 2 ,#´ÓÖ¸¶¨ÎÄ¼þ¼ÓÔØ²ÎÊýºó£¬´¥·¢¸ÃÏûÏ¢
SHEET_MSG_SAVE_PARAM_GROUP  = 3) # //µ±Ç°²ÎÊý×é±»±£´æÊ±£¬´¥·¢¸ÃÏûÏ¢


emSdkRefWinType = enum(
REF_WIN_AUTO_EXPOSURE  = 0 ,#
REF_WIN_WHITE_BALANCE = 1) # 


emSdkResolutionMode = enum(
RES_MODE_PREVIEW  = 0 ,#
RES_MODE_SNAPSHOT = 1) # 


emSdkClrTmpMode = enum(
CT_MODE_AUTO  = 0 ,#×Ô¶¯Ê¶±ðÉ«ÎÂ
CT_MODE_PRESET = 1 ,#Ê¹ÓÃÖ¸¶¨µÄÔ¤ÉèÉ«ÎÂ
CT_MODE_USER_DEF  = 2) # //×Ô¶¨ÒåÉ«ÎÂ(ÔöÒæºÍ¾ØÕó)


emSdkLutChannel = enum(
LUT_CHANNEL_ALL  = 0 ,#//R,B,GÈýÍ¨µÀÍ¬Ê±µ÷½Ú
LUT_CHANNEL_RED = 1 ,#ºìÉ«Í¨µÀ
LUT_CHANNEL_GREEN = 2 ,#ÂÌÉ«Í¨µÀ
LUT_CHANNEL_BLUE = 3) # À¶É«Í¨µÀ


emSdkIspProcessor = enum(
ISP_PROCESSSOR_PC  = 0 ,#//Ê¹ÓÃPCµÄÈí¼þISPÄ£¿é
ISP_PROCESSSOR_DEVICE  = 1) # //Ê¹ÓÃÏà»ú×Ô´øµÄÓ²¼þISPÄ£¿é


emStrobeControl = enum(
STROBE_SYNC_WITH_TRIG_AUTO  = 0 ,#ºÍ´¥·¢ÐÅºÅÍ¬²½£¬´¥·¢ºó£¬Ïà»ú½øÐÐÆØ¹âÊ±£¬×Ô¶¯Éú³ÉSTROBEÐÅºÅ¡£´ËÊ±£¬ÓÐÐ§¼«ÐÔ¿ÉÉèÖÃ(CameraSetStrobePolarity)¡£
STROBE_SYNC_WITH_TRIG_MANUAL = 1 ,#ºÍ´¥·¢ÐÅºÅÍ¬²½£¬´¥·¢ºó£¬STROBEÑÓÊ±Ö¸¶¨µÄÊ±¼äºó(CameraSetStrobeDelayTime)£¬ÔÙ³ÖÐøÖ¸¶¨Ê±¼äµÄÂö³å(CameraSetStrobePulseWidth)£¬ÓÐÐ§¼«ÐÔ¿ÉÉèÖÃ(CameraSetStrobePolarity)¡£
STROBE_ALWAYS_HIGH = 2 ,#Ê¼ÖÕÎª¸ß£¬ºöÂÔSTROBEÐÅºÅµÄÆäËûÉèÖÃ
STROBE_ALWAYS_LOW  = 3) # //Ê¼ÖÕÎªµÍ£¬ºöÂÔSTROBEÐÅºÅµÄÆäËûÉèÖÃ


emExtTrigSignal = enum(
EXT_TRIG_LEADING_EDGE  = 0 ,#ÉÏÉýÑØ´¥·¢£¬Ä¬ÈÏÎª¸Ã·½Ê½
EXT_TRIG_TRAILING_EDGE = 1 ,#ÏÂ½µÑØ´¥·¢
EXT_TRIG_HIGH_LEVEL = 2 ,#¸ßµçÆ½´¥·¢,µçÆ½¿í¶È¾ö¶¨ÆØ¹âÊ±¼ä£¬½ö²¿·ÖÐÍºÅµÄÏà»úÖ§³ÖµçÆ½´¥·¢·½Ê½¡£
EXT_TRIG_LOW_LEVEL = 3 ,#µÍµçÆ½´¥·¢
EXT_TRIG_DOUBLE_EDGE = 4) # Ë«±ßÑØ´¥·¢


emExtTrigShutterMode = enum(
EXT_TRIG_EXP_STANDARD  = 0 ,#±ê×¼·½Ê½£¬Ä¬ÈÏÎª¸Ã·½Ê½¡£
EXT_TRIG_EXP_GRR = 1) # È«¾Ö¸´Î»·½Ê½£¬²¿·Ö¹ö¶¯¿ìÃÅµÄCMOSÐÍºÅµÄÏà»úÖ§³Ö¸Ã·½Ê½£¬ÅäºÏÍâ²¿»úÐµ¿ìÃÅ£¬¿ÉÒÔ´ïµ½È«¾Ö¿ìÃÅµÄÐ§¹û£¬ÊÊºÏÅÄ¸ßËÙÔË¶¯µÄÎïÌå


emEvaluateDefinitionAlgorith = enum(
EVALUATE_DEFINITION_DEVIATION  = 0 ,# ·½²î·¨
EVALUATE_DEFINITION_SMD = 1 ,# ÏàÁÚÏñËØ»Ò¶È·½²î·¨
EVALUATE_DEFINITION_GRADIENT = 2 ,# ÌÝ¶ÈÍ³¼Æ
EVALUATE_DEFINITION_SOBEL = 3 ,# Sobel
EVALUATE_DEFINITION_ROBERT = 4 ,# Robert
EVALUATE_DEFINITION_LAPLACE = 5 ,# Laplace
EVALUATE_DEFINITION_ALG_MAX = 6) # 


emCameraGPIOMode = enum(
IOMODE_TRIG_INPUT  = 0 ,#´¥·¢ÊäÈë
IOMODE_STROBE_OUTPUT = 1 ,#ÉÁ¹âµÆÊä³ö
IOMODE_GP_INPUT = 2 ,#Í¨ÓÃÐÍÊäÈë
IOMODE_GP_OUTPUT = 3 ,#Í¨ÓÃÐÍÊä³ö
IOMODE_PWM_OUTPUT = 4) # PWMÐÍÊä³ö

