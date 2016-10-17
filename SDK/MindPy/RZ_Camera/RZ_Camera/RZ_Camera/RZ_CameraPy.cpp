#define EXPORT_RZPY_DLL
#include "RZ_CameraPy.h"

static TagResolution lpszResolution600[] =
{
	{ ("3072 * 2048"),3072,2048 },
};

RZ_CameraPy::RZ_CameraPy()
{


	//s_nCameraCount; //
	m_nDevIndex = 1;
	//m_hDevice;
	//m_strFriendlyName[255];
	m_nContrast = false;
	m_CamType = MicroUH600C;
	m_CamColorType;
	m_nColorMode = COLOR_RAWDATA;
	m_nFlipMode = FLIP_NATURAL;
	m_nResCount = sizeof(lpszResolution600) / sizeof(lpszResolution600[0]);      //分辨率个数
	m_lpszResolution = new TagResolution[m_nResCount];   //所支持的分辨率
	memcpy(m_lpszResolution, lpszResolution600, sizeof(TagResolution)*m_nResCount);
	m_nR = 128;
	m_nG = 128;
	m_nB = 128;
	m_nVBlank = 0;
	m_nVBlank = 0;
	m_nSharp = 34;
	m_nSta = 34;
	m_CapInfo;

	m_hWnd = NULL; //显示窗口句柄
	//*m_pRawData;
	//*m_pRgbData;
	//*m_pSnapBuffer;
	//*m_buffercache;
	m_dwCompressor = 0;
	//  int             m_nContrast;
	m_bPlay;        //
	m_bCrossline = false;   //
	m_bTrigger = false;     //外触发状态,采集外触发图片
	m_bTriggerMode = false; //外触发模式,只显示外触发时的数据
	m_bstretch = true;     //视频拉伸
	m_bCompressor = false;
	m_Xoff = m_Yoff = 0;
}


RZ_CameraPy::~RZ_CameraPy()
{

	if (m_pRawData)
	{
		delete[] m_pRawData;
		m_pRawData = NULL;
	}

	if (m_pRgbData)
	{
		delete m_pRgbData;
		m_pRgbData = NULL;
	}

	if (m_pSnapBuffer)
	{
		delete m_pSnapBuffer;
		m_pSnapBuffer = NULL;
	}

	if (m_hDevice != NULL)
		RZ_Uninitialize(m_hDevice);

	if (m_lpszResolution)
		delete[]m_lpszResolution;
}



int RZ_CameraPy::CAM_Initialize(HANDLE hCamera, struct CapInfoStruct *pCapInfo)
{
	m_hDevice = hCamera;
	RZ_SetGainAll(m_hDevice, m_nG);
	m_CapInfo = *pCapInfo;
	m_CapInfo.Width = 3072;
	m_CapInfo.Height = 2048;
	m_CapInfo.Exposure = 10000;
	m_CapInfo.OffsetX = 0;
	m_CapInfo.OffsetY = 0;
	m_CapInfo.Gain[0] = 32;
	m_CapInfo.Gain[1] = 32;
	m_CapInfo.Gain[2] = 32;
	int    nIndex = 1;
	int x = RZ_Initialize(_T("RZ_DEMO"), &nIndex, &m_CapInfo, &m_hDevice);
	if (ResSuccess != x)//RZ_Initialize(_T("RZ_DEMO"), &nIndex, &m_CapInfo, &m_hDevice ) ) 
	{
		std::cout << "rzinit" << x << std::endl;
		RZ_Uninitialize(m_hDevice);
		m_hDevice = NULL;
		return x;
	}
	RZ_GetDeviceType(m_hDevice, &m_CamType);
	RZ_SetCapInfo(m_hDevice, &m_CapInfo);
	RZ_SetContrastValue(m_hDevice, m_nContrast);
	RZ_SetSaturation(m_hDevice, m_nSta);
	RZ_SetGainR(m_hDevice, m_nR);
	RZ_SetGainG(m_hDevice, m_nG);
	RZ_SetGainB(m_hDevice, m_nB);
	RZ_SetGainAll(m_hDevice, 100);
	RZ_GetDeviceColorType(m_hDevice, &m_CamColorType);
	//RZ_GetTotalDeviceNum(m_hDevice, &s_nCameraCount);
	RZ_GetFriendlyName(m_hDevice, m_strFriendlyName);
	RZ_SetGamma(m_hDevice, 16);
	RZ_SetColorAdjust(m_hDevice, COLOR_ADJUST_NO);
	std::cout << m_CapInfo.Exposure << pCapInfo ->Exposure<< std::endl;
	//RZ_SetDoAE(m_hDevice, true, 0, NULL, NULL);
	return 0;
};
//int RZ_CameraPy::CAM_Initialize(HANDLE hCamera, struct CapInfoStruct *pCapInfo)
//{
//	m_hDevice = hCamera;
//	m_nSta = 34;
//	m_bCrossline = false;
//	m_bstretch = true;
//	m_bCompressor = false;
//	m_dwCompressor = 0;
//	m_nResCount = 0;
//	m_bTrigger = m_bTriggerMode = false;
//	m_bPlay = false;
//	m_pRawData = NULL;
//	m_pRgbData = NULL;
//	m_pSnapBuffer = NULL;
//	//	m_pSnapBuffer = ( unsigned char* ) new BYTE [ 800 * 600 * 3 * 30 +2048];
//	m_buffercache = m_pSnapBuffer;
//
//	m_nColorMode = COLOR_RGB24;
//	//m_CapInfo = *pCapInfo;
//	m_CapInfo.Buffer = pCapInfo->Buffer;
//	m_CapInfo.Width = pCapInfo->Width;
//	m_CapInfo.Height = pCapInfo->Height;
//	std::cout << "GetBuffer in width height  " << pCapInfo->Width << m_CapInfo.Height << std::endl;
//
//	m_CapInfo.Exposure = 100;
//	m_nR = m_nG = m_nB = 500;
//	m_nContrast = 16;
//	m_nFlipMode = FLIP_NATURAL;
//	m_lpszResolution = NULL;
//	m_CamColorType = RZ_COLOR;
//	m_nHBlank = m_nVBlank = 0;
//	memset(m_strFriendlyName, 0, sizeof(char) * 255);
//	m_nSharp = 0;
//
//	//m_nDevIndex = -1;
//	int    nIndex = 1;	//第1个设备
//	//							CRZSDK_DemoApp* pApp = (CRZSDK_DemoApp *)::AfxGetApp();
//	int x = RZ_Initialize(_T("RZ_DEMO"), &nIndex, &m_CapInfo, &m_hDevice);
//	if (ResSuccess != x)//RZ_Initialize(_T("RZ_DEMO"), &nIndex, &m_CapInfo, &m_hDevice ) ) 
//	{
//		std::cout << "rzinit" << x << std::endl;
//		RZ_Uninitialize(m_hDevice);
//		m_hDevice = NULL;
//		return x;
//	}
//	m_nDevIndex = nIndex;
//	RZ_GetDeviceType(m_hDevice, &m_CamType);
//	//=================================================================
//	//根据型号设置支持的分辨率
//	//m_nResCount = sizeof(lpszResolution600) / sizeof(lpszResolution600[0]);
//	//m_lpszResolution = new TagResolution[m_nResCount];
//	//memcpy(m_lpszResolution, lpszResolution600, sizeof(TagResolution)*m_nResCount);
//	m_nVBlank = 0;
//	m_nVBlank = 0;
//	m_CapInfo.Gain[0] = 10;
//	m_CapInfo.Gain[1] = 100;
//	m_CapInfo.Gain[2] = 10;
//
//	//m_pRawData = (unsigned char*) new unsigned char[m_lpszResolution[0].width * m_lpszResolution[0].height + m_lpszResolution[0].width];
//	//m_pRgbData = (unsigned char*) new unsigned char[m_lpszResolution[0].width * m_lpszResolution[0].height * 3 + m_lpszResolution[0].width];
//	//m_CapInfo.Buffer = m_pRawData;
//	RZ_SetHBlank(m_hDevice, m_nHBlank);
//	RZ_SetVBlank(m_hDevice, m_nVBlank);
//	RZ_SetCapInfo(m_hDevice, &m_CapInfo);
//	RZ_GetCapInfo(m_hDevice, &m_CapInfo);
//	RZ_SetExpouseDelayTime(m_hDevice, 2000);
//
//	return 0;
//
//}

void RZ_CameraPy::Play(HANDLE hCamera, struct CapInfoStruct *pCapInfo)
{
	if (m_hDevice == NULL)     return;
	RECT    rect;
	//::GetClientRect(m_hWnd, &rect);
	//rect.right = rect.left + this->m_CapInfo.Width;
	//rect.bottom = rect.top + this->m_CapInfo.Height;
	rect.right = this->m_CapInfo.Width;
	rect.bottom = this->m_CapInfo.Height;
	//rect.right = m_CapInfo.Width;
	//rect.bottom = m_CapInfo.Height;

		//RZ_SetFrameCallBack(m_hDevice, FrameCallback, LPVOID(this));
		//RZ_StartView(m_hDevice, _T("Digital Lab"), NULL,//0x40000000L | 0x10000000L,
		//	0, 0, rect.right, rect.bottom, NULL, NULL);

		RZ_StartView(m_hDevice, _T("Digital Lab"), NULL,//0x40000000L | 0x10000000L,
			0, 0, rect.right, rect.bottom, NULL, NULL);
}



RZPY_API int InitRz_Camera(HANDLE hCamera, struct CapInfoStruct *pCapInfo)
{
	
	//m_pCamera = new RZ_CameraPy();
	int x = m_pCamera.CAM_Initialize(hCamera, pCapInfo);
	//std::cout << "RZ_CameraPy" << x << std::endl;
	std::cout << "GetBuffer width height  " << m_pCamera.m_CapInfo.Width << m_pCamera.m_CapInfo.Height << std::endl;

	//if (!m_pCamera)
	return 0;
};

RZPY_API int Display(HANDLE hCamera, struct CapInfoStruct *pCapInfo)
{
	//RZ_CameraPy m_pCamera;
	m_pCamera.Play(m_pCamera.m_hDevice, &m_pCamera.m_CapInfo);
	return 0;
};

RZPY_API int GetBuffer(HANDLE hCamera, struct CapInfoStruct *pCapInfo)
{
	float pfFrameRate;
	RZ_GetFrameRate(hCamera, &pfFrameRate);
	std::cout << "GetBuffer width height  " << m_pCamera.m_CapInfo.Width << m_pCamera.m_CapInfo.Height << std::endl;
	//std::cout << "pCapInfo " << m_pCamera.m_CapInfo.Buffer << std::endl;
	int i = RZ_GetRawFrame(m_pCamera.m_hDevice, &m_pCamera.m_CapInfo);
	pCapInfo->Buffer = m_pCamera.m_CapInfo.Buffer;
	return i;
};

RZPY_API int GetRgbBuffer(int *m_pRgbData)
{
	int i = RZ_GetRgbFrame(m_pCamera.m_hDevice, &m_pCamera.m_CapInfo, m_pRgbData, false);
	return i;
}
RZPY_API int GetRawBmp(int *m_pRgbData)
{
	//RZ_GetRgbFrameToBmp(m_pCamera.m_hDevice, &m_pCamera.m_CapInfo, m_pRgbData, "test.bmp", false);
	RZ_GetRawFrame(m_pCamera.m_hDevice, &m_pCamera.m_CapInfo);
	return 0;
};
