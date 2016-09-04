#define EXPORT_RZPY_DLL
#include "RZ_CameraPy.h"



RZ_CameraPy::RZ_CameraPy()
{
	CAM_Initialize();
}


RZ_CameraPy::~RZ_CameraPy()
{
}

static TagResolution lpszResolution600[] =
{
	{ ("3072 * 2048"),3072,2048 },
};

void RZ_CameraPy::CAM_Initialize(HANDLE hCamera, struct CapInfoStruct *pCapInfo, int*  pDest, int nIdx)
{
	m_nSta = 34;
	m_bCrossline = false;
	m_bstretch = true;
	m_bCompressor = false;
	m_dwCompressor = 0;
	m_nResCount = 0;
	m_bTrigger = m_bTriggerMode = false;

	//m_hWnd = hWnd;

	m_bPlay = false;

	m_pRawData = NULL;
	m_pRgbData = NULL;
	m_pRawData = (unsigned char* ) new unsigned char[3072 * 2048 * 3 + 2048 ];
	//	m_pRgbData = ( unsigned char* ) new BYTE [ 2048 * 1536 * 3 +512];

	m_pSnapBuffer = NULL;
	//	m_pSnapBuffer = ( unsigned char* ) new BYTE [ 800 * 600 * 3 * 30 +2048];
	m_buffercache = m_pSnapBuffer;

	m_nColorMode = COLOR_RGB24;
	memset(&m_CapInfo, 0, sizeof(CapInfoStruct));
	m_CapInfo.Buffer = m_pRawData;
	m_CapInfo.Width = 752;
	m_CapInfo.Height = 480;
	m_CapInfo.Exposure = 100;
	//	memset( m_CapInfo.Gain, 30, 3 );
	m_CapInfo.Gain[0] = 32;
	m_CapInfo.Gain[1] = 32;
	m_CapInfo.Gain[2] = 32;

	m_nR = m_nG = m_nB = 500;
	m_nContrast = 16;
	m_nFlipMode = FLIP_NATURAL;
	m_lpszResolution = NULL;
	m_CamColorType = RZ_COLOR;
	m_nHBlank = m_nVBlank = 0;
	memset(m_strFriendlyName, 0, sizeof(char) * 255);
	m_nSharp = 0;
	///////////////////////////////////////////////////////////////

	//m_nDevIndex = -1;
	int    nIndex = nIdx;	//第1个设备
	//							CRZSDK_DemoApp* pApp = (CRZSDK_DemoApp *)::AfxGetApp();
	unsigned long x = RZ_Initialize(L"RZ_DEMO", &nIndex, &m_CapInfo, &m_hDevice);
	if (ResSuccess != x)//RZ_Initialize(_T("RZ_DEMO"), &nIndex, &m_CapInfo, &m_hDevice ) ) 
	{
		RZ_Uninitialize(m_hDevice);
		m_hDevice = NULL;
		return;
	}
	m_nDevIndex = nIndex;
	RZ_GetDeviceType(m_hDevice, &m_CamType);
	if (m_CamType != RZ130SC_YUV)
	{
		RZ_SetExpouseUnit(m_hDevice, 1);
		m_CapInfo.Exposure = 10000;
	}
	if (m_CamType == RZCCD140C)
	{
		m_CapInfo.OffsetX = 100;
	}
	if ((m_CamType == MicroUH1200C) || (m_CamType == MicroUH600C))
	{
		if (m_CamType == MicroUH1200C)
		{
			m_CapInfo.Width = 4000;
			m_CapInfo.Height = 3000;
		}
		else
		{
			m_CapInfo.Width = 3072;
			m_CapInfo.Height = 2048;
		}
		RZ_SetCapInfo(m_hDevice, &m_CapInfo);
		m_nColorMode = COLOR_RGB24_CLEAR;
		RZ_SetParamColor(m_hDevice, COLOR_RGB24_CLEAR);
		m_nContrast = 37;
		RZ_SetContrastValue(m_hDevice, m_nContrast);
		RZ_SetSaturation(m_hDevice, m_nSta);
		m_nR = 260;
		m_nB = 264;
		m_nG = 1;
		RZ_SetGainR(m_hDevice, m_nR);
		RZ_SetGainG(m_hDevice, m_nG);
		RZ_SetGainB(m_hDevice, m_nB);
		RZ_SetGainAll(m_hDevice, m_nG);
	}
	else
	{
		RZ_SetCapInfo(m_hDevice, &m_CapInfo);
		RZ_SetParamColor(m_hDevice, COLOR_RGB24);

		RZ_SetContrastValue(m_hDevice, m_nContrast);

		RZ_SetGainR(m_hDevice, m_nR);
		RZ_SetGainG(m_hDevice, m_nG);
		RZ_SetGainB(m_hDevice, m_nB);

	}
	RZ_SetParamFlip(m_hDevice, FLIP_NATURAL);
	RZ_GetDeviceColorType(m_hDevice, &m_CamColorType);

	m_Xoff = m_Yoff = 0;

	//RZ_GetTotalDeviceNum(m_hDevice, &s_nCameraCount);
	RZ_GetFriendlyName(m_hDevice, m_strFriendlyName);
	RZ_SetGamma(m_hDevice, 16);
	RZ_SetColorAdjust(m_hDevice, COLOR_ADJUST_NO);

	//=================================================================
	//根据型号设置支持的分辨率
	m_nResCount = sizeof(lpszResolution600) / sizeof(lpszResolution600[0]);
	m_lpszResolution = new TagResolution[m_nResCount];
	memcpy(m_lpszResolution, lpszResolution600, sizeof(TagResolution)*m_nResCount);
	m_nVBlank = 0;
	m_nVBlank = 0;
	m_CapInfo.Gain[0] = 0;
	m_CapInfo.Gain[1] = 0;

	m_CapInfo.Width = m_lpszResolution[0].width;
	m_CapInfo.Height = m_lpszResolution[0].height;

	m_pRawData = (unsigned char*) new unsigned char[m_lpszResolution[0].width * m_lpszResolution[0].height + m_lpszResolution[0].width];
	m_pRgbData = (unsigned char*) new unsigned char[m_lpszResolution[0].width * m_lpszResolution[0].height * 3 + m_lpszResolution[0].width];
	m_CapInfo.Buffer = m_pRawData;
	RZ_SetHBlank(m_hDevice, m_nHBlank);
	RZ_SetVBlank(m_hDevice, m_nVBlank);
	RZ_SetCapInfo(m_hDevice, &m_CapInfo);
	RZ_GetCapInfo(m_hDevice, &m_CapInfo);
	if (((int)m_CapInfo.Width != m_lpszResolution[0].width) && m_CamType == RZ500P)
	{
		if (m_lpszResolution)
			delete[]m_lpszResolution;
		m_lpszResolution = NULL;
		m_nResCount = sizeof(lpszResolution600) / sizeof(lpszResolution600[0]);
		m_lpszResolution = new TagResolution[m_nResCount];
		memcpy(m_lpszResolution, lpszResolution600, sizeof(TagResolution)*m_nResCount);
	}
	if (m_CamType == RZ130SC_YUV)
	{
		RZ_SetSharpness(m_hDevice, m_nSharp);
	}
}


int RZ_CameraPy::GetBuffer()
{
	int i = RZ_GetRgbFrame(m_hDevice, &m_CapInfo, m_pRgbData, false);


	return i;
}


RZPY_API int InitRz_Camera() 
{
	RZ_CameraPy *m_pCamera;


	m_pCamera = new RZ_CameraPy();
	std::cout << m_pCamera << std::endl;
	//if (!m_pCamera)
	return 0;
};

RZPY_API int display()
{
	std::cout << "hello" << std::endl;
	return 0;
};