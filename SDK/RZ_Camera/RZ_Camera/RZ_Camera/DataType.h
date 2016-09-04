
// datatype.h

#ifndef DATATYPE_H
#define DATATYPE_H
//#define __stdcall      __stdcall
/*===========================================================*\
	AE/AWB回调函数	dw1			返回AE/AWB之后的参数, 
					dw2			返回AE/AWB之后的参数, 
					lpContext	在设置帧回调函数时传递的上下文

2011-04-12 该回调函数格式兼用作设备移除与插入消息的回调
dw1 表示设备插入或移除  0，移除;1，插入
dw2 表示设备的句柄,强制转换
\*=========================================================//*/
//typedef VOID (__stdcall *DL_AUTOCALLBACK )(unsigned long dw1, unsigned long dw2, LPVOID lpContext );

/*===========================================================*\
	帧回调函数	lpParam指向帧数据的指针, 
				lpPoint 保留, 
				lpContext在设置帧回调函数时传递的上下文
\*=========================================================//*/
//typedef VOID (__stdcall *DL_FRAMECALLBACK)( LPVOID lpParam1, LPVOID lpPoint, LPVOID lpContext );


/*-------------------------------------------------------------
	返回值定义
  *===========================================================*/
#define		ResSuccess					0x0000		// 返回成功
#define		ResNullHandleErr			0x0001		// 无效句柄
#define		ResNullPointerErr			0x0002		// 指针为空
#define		ResFileOpenErr				0x0003		// 文件创建/打开失败
#define		ResNoDeviceErr				0x0004		// 没有可用设备
#define		ResInvalidParameterErr		0x0005		// 内存分配不足
#define		ResOutOfMemoryErr			0x0006		// 没有开启预览
#define		ResNoPreviewRunningErr		0x0007		// 预览没有开启
#define		ResOSVersionErr				0x0008
#define		ResUsbNotAvailableErr		0x0009
#define		ResNotSupportedErr			0x000a
#define		ResNoSerialString			0x000b
#define		ResVerificationErr			0x000c
#define		ResTimeoutErr	            0x000d		
#define		ResScaleModeErr				0x000f
#define		ResUnknownErr				0x00ff

#define		ResDisplayWndExist			0x0011		// 应该关闭预览窗口
#define		ResAllocated				0x0012		// 内存已经分配
#define		ResAllocateFail				0x0013		// 内存分配失败
#define		ResReadError				0x0014      // USB读取失败
#define		ResWriteError				0x0015		// USB命令发出失败
#define		ResUsbOpen					0x0016      // USB端口已经打开
#define     ResCreateStreamErr			0x0017		// 创建avi流失败
#define     ResSetStreamFormatErr		0x0018		// 设置AVI流格式失败


typedef struct _tagDLVIDEORECT
{
	int     Left;		// 相对于父窗口的水平偏移
	int     Top;		// 相对于父窗口的垂直偏移
	int     Width;		// 视频窗口宽度
	int     Height;		// 视频窗口高度
}DLVIDEORECT, *PDLVIDEORECT;

/*-------------------------------------------------------------
	摄像头相关参数结构
  *===========================================================*/
struct CapInfoStruct 
{
	unsigned char	*Buffer;		// 用户分配，用于返回8bit原始数据
	unsigned long	Height;			// 采集高度
	unsigned long	Width;			// 采集宽度
	unsigned long	OffsetX;		// 水平偏移,	CCD相机禁用
	unsigned long	OffsetY;		// 垂直偏移,	CCD相机禁用
	unsigned long	Exposure;		// 曝光值 1-500MS
	unsigned char	Gain[3];		// Gain[0]整体增益 1-63. Gain[1],Gain[2]保留
	unsigned char	Control;		// 控制位
	unsigned char	InternalUse;	// 用户不要对此字节进行操作
	unsigned char	ColorOff[3];	// 用户从外面不要改变此数组的值
	unsigned char	Reserved[4];	// 保留位
};
//CapInfoStruct m_tCamerParam;
/*-----------------------------------------------------------
	Control 控制位说明
	BIT7       BIT6      BIT5     BIT4     BIT3     BIT2     BIT1     BIT0
	用户IO	触发源使能								HDR    	 触发	  裁剪/缩放
	0低电平   0										 0		 0			0裁剪
	1高电平	  1										 1开启	 1 触发采集	1缩放	
  ===========================================================*/


/*-------------------------------------------------------------
	颜色模式
  *===========================================================*/
enum	COLOR_MODE {
					COLOR_RGB24,
					COLOR_RGB24_CLEAR,
					COLOR_BW24,
					COLOR_GRAY,
					COLOR_RAWDATA,
					COLOR_Microscope	//颜色校正模式(显微镜模式)
				};


/*-------------------------------------------------------------
	翻转模式 目前仅对RGB24,BW24有效
  *===========================================================*/
enum	FLIP_MODE {	
					FLIP_NATURAL,		// 正常显示
					FLIP_LEFTRIGHT,	    // 左右翻转
					FLIP_UPDOWN,			// 上下翻转
					FLIP_ROTATE180,		// 旋转180
					FLIP_ROTATE90,
					FLIP_ROTATE270
				};

enum	RZIMAGETYPR {  
						BMP,		// 保存图像格式设置 
					    JPEG,	    // 
					};

enum	RZCAMERA{	RZUNKOWN,		//相机类型
					RZ130,			
					RZ300,
					RZ130CF,
					RZ200CF,
					RZ300CF,
					RZ500CF,
					RZ900CF,
					RZ500P,			//
					RZ130C_1_3,
					RZ36M,
					RZ300C_FPGA,
					RZ130C_FPGA,
					RZ130M_FPGA,
					RZ80C_SP16,
					RZ130SC_YUV,
					RZ120C_FPGA,
					RZ300_LED,
					RZTEST,
					RZF1400CF,
					RZF1000CF,
					RZ50C,
					RZCCD140C,
					RZUL200MFG,
					MicroUH1200C,
					RZTRIGGER,
					MicroUH600C,
					SuperUH500,
					MicroUH300C,
					SuperUH130,
					SuperUH200,
					SuperUH50,
					SuperUH30
				};

enum	RZ_COLOR_TYPE{
					RZ_COLOR,
					RZ_GRAY
				};


enum COLOR_ADJUST_TYPE {					
					COLOR_ADJUST_NO,	//
					COLOR_ADJUST_COLD,	//冷色优先
					COLOR_ADJUST_WARM	//暖色优先
				};

//自动曝光亮度效果设置
enum	RZ_AE_LEVEL
{
		RZ_AE_LEVEL_HIGH,	//更亮
		RZ_AE_LEVEL_NORMAL,	//正常
		RZ_AE_LEVEL_LOW		//更暗
};

#endif