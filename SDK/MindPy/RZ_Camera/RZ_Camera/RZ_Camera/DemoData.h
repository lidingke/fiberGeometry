
//demodata.h

#ifndef	__DEMODATA_H__

#define	__DEMODATA_H__

typedef struct _tagResolution
{
	char * lpszDesc;
	int	width;
	int	height;
}TagResolution;


typedef enum		//
{
	idResolution,	//
	idContrast,		//
	idExposure,		//
	idGain_All,		//
	idGain_R,		//
	idGain_G,		//
	idGain_B,		//
	idOffsetX,		//
	idOffsetY,		//
	idControl,
	idImageType,	//
	idFlipMode,
	idColorMode,
	idSharp,
	idSta
}ENUM_Param;

typedef enum
{
	IMG_TYPE_BMP,
	IMG_TYPE_JPG,
	IMG_TYPE_PNG,
	IMG_TYPE_TIF
}ENUM_IMAGE_TYPE;



//======================================================
//	消息定义
#define	XX_MSG_FINISH_AE	WM_USER+10	//完成自动曝光之后,回调函数向主窗口发送的消息
#define XX_MSG_FINISH_AWB	WM_USER+11	//完成自动白平衡之后,回调函数向主窗口发送的消息

#endif