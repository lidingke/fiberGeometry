
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
//	��Ϣ����
#define	XX_MSG_FINISH_AE	WM_USER+10	//����Զ��ع�֮��,�ص������������ڷ��͵���Ϣ
#define XX_MSG_FINISH_AWB	WM_USER+11	//����Զ���ƽ��֮��,�ص������������ڷ��͵���Ϣ

#endif