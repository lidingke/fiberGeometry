
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

#include "demodata.h"
#include "DataType.h"
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
protected:
	//HWND			m_hWnd;	//显示窗口句柄

	unsigned char			*m_pRawData;
	unsigned char			*m_pRgbData;
	unsigned char			*m_pSnapBuffer;
	unsigned char			*m_buffercache;

	CapInfoStruct	m_CapInfo;
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
	void CAM_Initialize(HANDLE hCamera, struct CapInfoStruct *pCapInfo, int*  pDest, int nIdx = 1);
//	void PixelCalibration();
//	void EnableCompressor(int bOn);
//	void SelectComprossor();
//	void SetTriggerMode(int bOn);
//	void SetTriggerStatus(int bOn, LPCTSTR lpPath);
//	void CAM_Initialize(HWND hWnd = NULL, int nIdx = 1);
//	LPCTSTR GetFrameRate(float &fr);
//	int IsPlaying();
//	int IsVideoStretch();
//	HANDLE GetDeviceHandle() const;
//	int IsShowCorssLine();
//	void DrawCrossLine(unsigned char * pData);
//	void EnableCrossline(int bOn);
//	void VideoAutoSize(int bChange = FALSE);
//	void SetDoAWB(int bAWB, LPVOID lpContext);
//	void SetDoAE(int bAE, LPVOID lpContext);
//	void Snap(ENUM_IMAGE_TYPE type, LPCTSTR lpszPath);
//	int Capture2AVI(int bStart, LPCTSTR lpszPath);
//	void SetVideoSize(long width, long height);
//	void SetParam(ENUM_Param type, long value, long value2 = -1);
//	CapInfoStruct * GetCapInfo();
//	void SetScrollOffset(int H = -1, int V = -1);
//	CSize GetVideoSize();
//	int StopView();
//	int StartView();
//	void Play(int bPlay);
//	CRZ_Camera(HWND hWnd, int nIdx = 1);
//	CRZ_Camera();
//	virtual ~CRZ_Camera();
//	void softTrigger();
//	void SetHDR(int bEnable);
//	RZCAMERA GetCamType() { return m_CamType; };
//	void EnableLightAvg(int bOn);
//	void ResetLightAvgTable();
//	void SetTriggerDelayTime(LONG Time);
//	void EEProm_Set(unsigned char *pData);
//	void EEProm_Get(unsigned char *pData);
//	void EEProm_Setunsigned char(int nIndex, int nCount, unsigned char *pData);
//	void EEProm_Getunsigned char(int nIndex, int nCount, unsigned char *pData);
//	void SetCustomIO(unsigned char data);
//	void SetTriggerSource(unsigned char data);
//	void SetTriggerSourceTime(LONG Time);
//	void SetAEParam(int bAE, LPVOID lpContext);
//
//	void SetHBlank(int nHBlank);
//	void SetVBlank(int nVBlank);
//	void SetZoom(int b);
//
//	void SetExpouseDelayTime(int nTime);
//
//	CString GetSerialNumber();
//	void SetNewHWDN(HWND hwnd);
//	CString GetCameraVertion();
//	void SetFastCapMode(int b);
	int GetBuffer(HANDLE hCamera, struct CapInfoStruct *pCapInfo, int*  pDest, int bFlip = false);
//	void SavePic(ENUM_IMAGE_TYPE type, LPCTSTR lpszPath);
//
//protected:
//	DECLARE_DYNCREATE(CRZ_Camera);
//	// Overrides
//	// ClassWizard generated virtual function overrides
//	//{{AFX_VIRTUAL(CRZ_Camera)
//public:
//	virtual void Serialize(CArchive& ar);
	//}}AFX_VIRTUAL
};


extern "C"
{
	RZPY_API int InitRz_Camera();
	RZPY_API int display();
	//RZPY_API PyArrayObject* rePyArrayObject();
}



#endif  //!defined(RZ_CAMERAPY_H__DE07E1D0_D0B7_4FA5_A4F3_45499366E00E__INCLUDED_)
