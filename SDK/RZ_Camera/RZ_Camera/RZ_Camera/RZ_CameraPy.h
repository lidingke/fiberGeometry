
#if !defined(RZ_CAMERAPY_H__DE07E1D0_D0B7_4FA5_A4F3_45499366E00E__INCLUDED_)
#define RZ_CAMERAPY_H__DE07E1D0_D0B7_4FA5_A4F3_45499366E00E__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifdef EXPORT_RZPY_DLL  
#define RZPY_API __declspec(dllexport)  
#else  
#define RZPY_API __declspec(dllimport)  
#endif  




//
#include "RZCamAPI.H"

#include <iostream>
#include <string>

using std::string;

class RZ_CameraPy
{
public:
	static int		s_nCameraCount;	//
	int				m_nDevIndex;
	HANDLE			m_hDevice;
	char			m_strFriendlyName[255];
	int				m_nContrast;
	RZCAMERA		m_CamType;
	RZ_COLOR_TYPE	m_CamColorType;
	COLOR_MODE		m_nColorMode;
	FLIP_MODE		m_nFlipMode;
public:
	int				m_nResCount;		//分辨率个数
	TagResolution *	m_lpszResolution;	//所支持的分辨率
	int				m_nR, m_nG, m_nB;
	int				m_nHBlank, m_nVBlank;
	int				m_nSharp;
	int				m_nSta;
	CapInfoStruct	m_CapInfo;
protected:
	HWND			m_hWnd;	//显示窗口句柄

	unsigned char			*m_pRawData;
	unsigned char			*m_pRgbData;
	unsigned char			*m_pSnapBuffer;
	unsigned char			*m_buffercache;

	unsigned long			m_dwCompressor;

	//	int				m_nContrast;

	int			m_bPlay;		//
	int			m_bCrossline;	//
	int			m_bTrigger;		//外触发状态,采集外触发图片
	int			m_bTriggerMode;	//外触发模式,只显示外触发时的数据
	int			m_bstretch;		//视频拉伸
	int			m_bCompressor;


	int	m_Xoff, m_Yoff;


public:
	RZ_CameraPy();
	~RZ_CameraPy();
	int CAM_Initialize(HANDLE hCamera, struct CapInfoStruct *pCapInfo);
	void Play(HANDLE hCamera, struct CapInfoStruct *pCapInfo);

};

static RZ_CameraPy m_pCamera;

extern "C"
{
	RZPY_API int InitRz_Camera(HANDLE hCamera, struct CapInfoStruct *pCapInfo);
	RZPY_API int Display(HANDLE hCamera, struct CapInfoStruct *pCapInfo);
	RZPY_API int GetBuffer(HANDLE hCamera, struct CapInfoStruct *pCapInfo);
	RZPY_API int GetRgbBuffer(int *m_pRgbData);
	RZPY_API int GetRawBmp(int *m_pRgbData);

	//RZPY_API PyArrayObject* rePyArrayObject();
}



#endif  //!defined(RZ_CAMERAPY_H__DE07E1D0_D0B7_4FA5_A4F3_45499366E00E__INCLUDED_)
