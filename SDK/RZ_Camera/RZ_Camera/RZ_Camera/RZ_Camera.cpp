// RZ_Camera.cpp: implementation of the CRZ_Camera class.
//
//////////////////////////////////////////////////////////////////////

#include "stdafx.h"
#include "RZ_Camera.h"


#ifdef _DEBUG
#undef THIS_FILE
static char THIS_FILE[]=__FILE__;
#define new DEBUG_NEW
#endif

static TagResolution lpszResolution900[] = 
{
	{_T("3488 * 2560"),3488,2560},
	{_T("1744 * 1280"),1744,1280},
	{_T("872 * 640"),872,640},
};

static TagResolution lpszResolution500P_New[] = 
{
	{_T("2592 * 1944"),2592,1944},
 	{_T("2560 * 1944"),2560,1944},
	{_T("2048 * 1536"),2048,1536},
 	{_T("1280 * 972"),1280,972},
	{_T("640 * 480"),640,480},
};

static TagResolution lpszResolution500P[] = 
{
	{_T("2560 * 1944"),2560,1944},
	{_T("1280 * 972"),1280,972},
	{_T("640 * 486"),640,486},
};
static TagResolution lpszResolution500[] = 
{
	{_T("2592 * 1944"),2592,1944},
	{_T("2560 * 800"),2560,800},
	{_T("2048 * 1536"),2048,1536},
	{_T("1600 * 1200"),1600,1200},
	{_T("1280 * 1024"),1280,1024},
	{_T("1280 * 400"),1280,400},
	{_T("1024 * 768"),1024,768},
	{_T("800 * 600"),800,600},
	{_T("640 * 480"),640,480},
};
static TagResolution lpszResolution500Super[] = 
{
	{_T("2592 * 2048"),2592,2048},
	{_T("2592 * 1944"),2560,1944},
	{_T("2048 * 1536"),2048,1536},
	{_T("1600 * 1200"),1600,1200},
	{_T("1280 * 1024"),1280,1024},
	{_T("1280 * 400"),1280,400},
	{_T("1024 * 768"),1024,768},
	{_T("800 * 600"),800,600},
	{_T("640 * 480"),640,480},
};

static TagResolution lpszResolution300[] = 
{
	{_T("2048 * 1536"),2048,1536},
	{_T("1600 * 1200"),1600,1200},
	{_T("1280 * 1024"),1280,1024},
	{_T("1024 * 768"),1024,768},
	{_T("800 * 600"),800,600},
	{_T("640 * 480"),640,480},
};

static TagResolution lpszResolution200[] = 
{
	{_T("1600 * 1200"),1600,1200},
	{_T("1280 * 1024"),1280,1024},
	{_T("1024 * 768"),1024,768},
	{_T("800 * 600"),800,600},
	{_T("640 * 480"),640,480},
};
static TagResolution lpszResolution200Super[] = 
{
	{_T("1920 * 1200"),1920,1200},
	{_T("1600 * 1200"),1600,1200},
	{_T("1280 * 1024"),1280,1024},
	{_T("1024 * 768"),1024,768},
	{_T("800 * 600"),800,600},
	{_T("640 * 480"),640,480},
};
static TagResolution lpszResolutionDft[] = 
{
	{_T("1280 * 1024"),1280,1024},
	{_T("1024 * 768"),1024,768},
	{_T("800 * 600"),800,600},
	{_T("640 * 480"),640,480},
};
static TagResolution lpszResolution50[] = 
{
	
	{_T("800 * 600"),800,600},
	{_T("640 * 480"),640,480},
};
static TagResolution lpszResolution30[] = 
{
	{_T("640 * 480"),640,480},
};
static TagResolution lpszResolution120[] = 
{
	{_T("1280 * 960"),1280,960},
	{_T("1280 * 720"),1280,720},
	{_T("1024 * 768"),1024,768},
	{_T("800 * 600"),800,600},
	{_T("640 * 480"),640,480},
};
static TagResolution lpszResolution1400[] = 
{
	{_T("4608 * 3288"),4608,3288},
	{_T("3488 * 2560"),3488,2560},
	{_T("2592 * 1944"),2592,1944},
	{_T("2048 * 1536"),2048,1536},
	{_T("1600 * 1200"),1600,1200},
	{_T("1280 * 1024"),1280,1024},
	{_T("1024 * 768"),1024,768},
//	{_T("800 * 600"),800,600},
// 	{_T("640 * 480"),640,480},
};
static TagResolution lpszResolution1000[] = 
{
	{_T("3840 * 2748"),3840,2748},
	{_T("3488 * 2560"),3488,2560},
	{_T("2592 * 1944"),2592,1944},
	{_T("2048 * 1536"),2048,1536},
	{_T("1600 * 1200"),1600,1200},
	{_T("1280 * 1024"),1280,1024},
	{_T("1024 * 768"),1024,768},
	{_T("800 * 600"),800,600},
	{_T("640 * 480"),640,480},
};
static TagResolution lpszResolution1200[] = 
{
	{_T("4000 * 3000"),4000,3000},
	{_T("2000 * 1500"),2000,1500},
};
static TagResolution lpszResolution600[] =
{
	{_T("3072 * 2048"),3072,2048},
};
static TagResolution lpszResolution36M[] = 
{
	{_T("752 * 480"),752,480},
};
static TagResolution lpszResolution140[] = 
{
	{_T("1360 * 1024"),1360,1024}
};
//////////////////////////////////////////////////////////////////////
// Construction/Destruction
//////////////////////////////////////////////////////////////////////

VOID CALLBACK FrameCallback( LPVOID pData, LPVOID lpReserve, LPVOID lpContext )
{
	//帧回调函数,请尽快返回.
	TRACE(_T("--- frame callback --- \n"));
	CRZ_Camera * pCamera = (CRZ_Camera *)lpContext;
	pCamera->DrawCrossLine(PBYTE(pData));
};

VOID CALLBACK AECallBack(DWORD dw1, DWORD dw2, LPVOID lpContext)
{
	//(::AfxGetMainWnd())->PostMessage(XX_MSG_FINISH_AE,dw1,dw2);
	((CWnd *)lpContext)->SendMessage(XX_MSG_FINISH_AE,dw1,dw2);
};

VOID CALLBACK AWBCallBack(DWORD dw1, DWORD dw2, LPVOID lpContext)
{
	//(::AfxGetMainWnd())->PostMessage(XX_MSG_FINISH_AWB,dw1,dw2);
	((CWnd *)lpContext)->SendMessage(XX_MSG_FINISH_AWB,dw1,dw2);
};

//===========================================================================
/////////////////////////////////////////////////////////////////////////////
// CRZ_Camera 实现
int	CRZ_Camera::s_nCameraCount = 0;

IMPLEMENT_DYNCREATE(CRZ_Camera, CObject)

CRZ_Camera::CRZ_Camera(HWND hWnd, int nIdx)
{
	CAM_Initialize(hWnd, nIdx);
}

CRZ_Camera::CRZ_Camera()
{
	CAM_Initialize();
}

CRZ_Camera::~CRZ_Camera()
{
	if(m_bPlay)
	    Play( FALSE );
	if( m_pRawData )
	{
		delete [] m_pRawData;
		m_pRawData = NULL;
	}

	if( m_pRgbData )
	{
		delete m_pRgbData;
		m_pRgbData = NULL;
	}

	if( m_pSnapBuffer )
	{
		delete m_pSnapBuffer;
		m_pSnapBuffer = NULL;
	}

	if( m_hDevice != NULL )    
		RZ_Uninitialize( m_hDevice );	

	if(m_lpszResolution)
		delete []m_lpszResolution;
}

void CRZ_Camera::Play(BOOL bPlay)
{
	if( m_hDevice == NULL )     return;
	m_bPlay = bPlay;

	RECT    rect;
	::GetClientRect(m_hWnd, &rect);
	rect.right = rect.left + this->m_CapInfo.Width;
	rect.bottom = rect.top + this->m_CapInfo.Height;

	if( m_bPlay )
	{
		RZ_SetFrameCallBack(m_hDevice,FrameCallback,LPVOID(this));		
		RZ_StartView( m_hDevice, _T("Digital Lab"), WS_CHILD | WS_VISIBLE, 
			0, 0, rect.right, rect.bottom, m_hWnd, NULL );
	}
	else
	{
		RZ_StopView( m_hDevice );
	}
}

BOOL CRZ_Camera::StartView()
{
	if( m_hDevice == NULL )    return FALSE;
	if(m_bPlay)                return FALSE;
	Play( TRUE );
	VideoAutoSize();
	return TRUE;
}

BOOL CRZ_Camera::StopView()
{
	if( m_hDevice == NULL )    return FALSE;
	if(!m_bPlay)               return FALSE; 
	// TODO: Add your control notification handler code here
	Play( FALSE );
	return TRUE;
}

CSize CRZ_Camera::GetVideoSize()
{
	return CSize(m_CapInfo.Width,m_CapInfo.Height);
}

void CRZ_Camera::SetScrollOffset(int H, int V)
{
	if(H!=-1)
		m_Xoff=H;
	if(V!=-1)
		m_Yoff=V;

	if(!m_bPlay)	return;
	RZ_SetScrollOffset(m_hDevice, m_Xoff, m_Yoff);
}

CapInfoStruct * CRZ_Camera::GetCapInfo()
{
	return &m_CapInfo;
}

void CRZ_Camera::SetParam(ENUM_Param type, long value, long value2)
{
	switch(type)
	{
	case idResolution:
		m_CapInfo.Width = value;
		m_CapInfo.Height= value2;
		break;
	case idContrast:
		m_nContrast = value;
		RZ_SetContrastValue(m_hDevice,value);
		return;
	case idExposure:
		m_CapInfo.Exposure=value;
		break;
	case idGain_All:
	
		if (m_CamType == RZ130SC_YUV)
		{
			m_nSharp = (int)value;
			RZ_SetSharpness(m_hDevice, (int)value);
			return;
		} 
		else if (m_CamType==RZF1400CF)
		{
			m_CapInfo.Gain[0]=(BYTE)value&0x7F;
			m_CapInfo.Gain[1]=(BYTE)(value>>7);
		}
		else if ((m_CamType == MicroUH1200C) || (m_CamType == MicroUH600C))
		{
			m_nG = value;
			RZ_SetGainAll(m_hDevice,m_nG);
			return;
		}
		else
		{
			m_CapInfo.Gain[0]=(BYTE)value;
			
		}
		break;
	case idGain_R:
		if (m_CamType == RZ130SC_YUV)
		{
			m_CapInfo.Gain[0]=(BYTE)value;
			break;
		} 
		else
		{
			RZ_SetGainR(m_hDevice, value);
			return;
		}
	case idGain_G:
		if (m_CamType == RZ130SC_YUV)
		{
			m_CapInfo.Gain[1]=(BYTE)value;
			break;
		} 
		else
		{
			RZ_SetGainG(m_hDevice, value);
			return;
		}
	case idGain_B:
		if (m_CamType == RZ130SC_YUV)
		{
			m_CapInfo.Gain[2]=(BYTE)value;
			break;
		} 
		else
		{
			RZ_SetGainB(m_hDevice, value);
			return;
		}
	case idOffsetX:
		m_CapInfo.OffsetX=value;
		break;
	case idOffsetY:
		m_CapInfo.OffsetY=value;
		break;
	case idControl:
		m_CapInfo.Control=(BYTE)value;
		break;
	case idFlipMode:
		m_nFlipMode = FLIP_MODE(value);
		RZ_SetParamFlip(m_hDevice, FLIP_MODE(value));
		VideoAutoSize();
		return;
	case idColorMode:
		m_nColorMode = COLOR_MODE(value);
		RZ_SetParamColor(m_hDevice, COLOR_MODE(value));
		return;
	case idSharp:
		m_nSharp = (int)value;
		RZ_SetSharpness(m_hDevice, (int)value);
		return;
	case idSta:
		m_nSta = (int)value;
		RZ_SetSaturation(m_hDevice,m_nSta);
		return;
	default:
		return;
	}
	RZ_SetCapInfo(m_hDevice,&m_CapInfo);
	RZ_GetCapInfo(m_hDevice,&m_CapInfo);
}

void CRZ_Camera::SetVideoSize(long width, long height)
{
	RZ_SetVideoSize(m_hDevice,width,height);
}

BOOL CRZ_Camera::Capture2AVI(BOOL bStart, LPCTSTR lpszPath)
{
	RZ_CaptureToAvi(m_hDevice,bStart,lpszPath);
	return TRUE;
}

void CRZ_Camera::Snap(ENUM_IMAGE_TYPE type, LPCTSTR lpszPath)
{
	CString strPath = lpszPath;

	switch(type)
	{
	case IMG_TYPE_BMP:
		strPath += _T(".bmp");
		RZ_GetRgbFrameToBmp(m_hDevice, &m_CapInfo, m_pRgbData, strPath, TRUE);
		break;
	case IMG_TYPE_JPG:
		strPath += _T(".jpg");
		RZ_GetRgbFrameToJpeg(m_hDevice, &m_CapInfo, NULL, strPath, 100);
		break;
	default:
		break;
	};

}

void CRZ_Camera::SetDoAE(BOOL bAE, LPVOID lpContext)
{
	RZ_SetDoAE( m_hDevice, bAE, 0, 
			 AECallBack, lpContext );
}

void CRZ_Camera::SetDoAWB(BOOL bAWB, LPVOID lpContext)
{
	RZ_SetDoAWB( m_hDevice, bAWB, 0, 
			 AWBCallBack, lpContext );
}

void CRZ_Camera::VideoAutoSize(BOOL bChange)
{
	RECT rect;
	::GetClientRect(m_hWnd,&rect);	

	if(bChange)	//切换拉伸模式
		m_bstretch = !m_bstretch;

	if(m_bstretch)	
	{
		int w,h;
		w = rect.right - rect.left;	h = rect.bottom - rect.top;
		
		int nW,nH,nX,nY;
		nW = m_CapInfo.Width;nH = m_CapInfo.Height;
		if (m_nFlipMode == FLIP_ROTATE90 ||m_nFlipMode==FLIP_ROTATE270)
		{
			nW = m_CapInfo.Height;
			nH = m_CapInfo.Width;
		}
		float ff = min(float(w)/nW,float(h)/nH);
		if (ff < 1.0f)
		{
			nW = nW * ff;
			nH = nH * ff;
		}
		nW = nW + nW%4;	nH = nH + nH%4;

		nX = w-nW > 0 ? (w-nW)/2 : 0;
		nY = h-nH > 0 ? (h-nH)/2 : 0;
		
		RZ_SetScrollOffset(m_hDevice, -nX, -nY);
		RZ_SetVideoSize(m_hDevice,nW,nH);
	}
	else
	{
		long lw=(long)m_CapInfo.Width; long lh=(long)m_CapInfo.Height;
		rect.left = (rect.right-rect.left-lw > 0) ? 
			(int)((rect.right-rect.left-lw)/2) : rect.left ; 
		rect.top = (rect.bottom-rect.top-lh > 0) ? 
			(int)((rect.bottom-rect.top-lh)/2) : rect.top ;
	
		RZ_SetScrollOffset(m_hDevice, -rect.left, -rect.top);
		m_Xoff = -rect.left;	m_Yoff = -rect.top;
		RZ_SetVideoSize(m_hDevice,lw,lh);
		
	}
}

void CRZ_Camera::EnableCrossline(BOOL bOn)
{
	m_bCrossline=bOn;
}

void CRZ_Camera::DrawCrossLine(BYTE *pData)
{
	if(!m_bCrossline)
		return;

	int actual_w,actual_h;
	if (m_nFlipMode==FLIP_ROTATE90||m_nFlipMode==FLIP_ROTATE270)
	{
		actual_w=m_CapInfo.Height;
		actual_h=m_CapInfo.Width;
	}
	else
	{
		actual_w=m_CapInfo.Width;
		actual_h=m_CapInfo.Height;
	}
	
	int nBytesOfPixel;
	if(m_nColorMode==COLOR_RGB24 || m_nColorMode==COLOR_BW24 || m_nColorMode==COLOR_RGB24_CLEAR ||m_nColorMode ==COLOR_Microscope)
		nBytesOfPixel = 3;
	else
		nBytesOfPixel = 1;
	
	
	BYTE *pLine = pData + 	actual_w * nBytesOfPixel * (actual_h / 2);
	
	if(m_nColorMode==COLOR_RGB24 || m_nColorMode==COLOR_BW24 || m_nColorMode==COLOR_RGB24_CLEAR||m_nColorMode ==COLOR_Microscope)
	{
		for( int i=0; i<actual_w; i++ )
		{
			*( pLine + nBytesOfPixel * i ) = 0;
			*( pLine + nBytesOfPixel * i + 1 ) = 0;
			*( pLine + nBytesOfPixel * i + 2 ) = 255;
		}
		for( int j = 0; j<actual_h; j++)
		{
			BYTE *pLine = pData + actual_w * nBytesOfPixel * j; 
			*( pLine + ( actual_w/2 ) * nBytesOfPixel ) = 0;
			*( pLine + ( actual_w/2 ) * nBytesOfPixel + 1 ) = 0;
			*( pLine + ( actual_w/2 ) * nBytesOfPixel + 2 ) = 255;
		}
	}
	else
	{
		for( int i=0; i<actual_w; i++ )
		{
			*( pLine + nBytesOfPixel * i + 0 ) = 255;
		}
		for( int j = 0; j<actual_h; j++)
		{
			BYTE *pLine = pData + actual_w * nBytesOfPixel * j; 
			*( pLine + ( actual_w/2 ) * nBytesOfPixel + 0 ) = 255;
		}	
	}
}

BOOL CRZ_Camera::IsShowCorssLine()
{
	return m_bCrossline;
}

HANDLE CRZ_Camera::GetDeviceHandle() const
{
	return m_hDevice;
}

BOOL CRZ_Camera::IsVideoStretch()
{
	return m_bstretch;
}

BOOL CRZ_Camera::IsPlaying()
{
	return m_bPlay;
}

LPCTSTR CRZ_Camera::GetFrameRate(float &fr)
{
	CString strRet=_T("");
	if(RZ_GetFrameRate(m_hDevice, &fr)==0)
		strRet.Format(_T("%.2f"),fr);

	return (LPCTSTR)strRet;
}

void CRZ_Camera::Serialize(CArchive& ar)
{
/*	UCHAR	*Buffer;		// 用户分配，用于返回8bit原始数据
	ULONG	Height;			// 采集高度
	ULONG	Width;			// 采集宽度
	ULONG	OffsetX;		// 水平偏移,	CCD相机禁用
	ULONG	OffsetY;		// 垂直偏移,	CCD相机禁用
	ULONG	Exposure;		// 曝光值 1-500MS
	UCHAR	Gain[3];		// R G B 增益 1-63
	UCHAR	Control;		// 控制位
	UCHAR	InternalUse;	// 用户不要对此字节进行操作
	UCHAR	ColorOff[3];	// 用户从外面不要改变此数组的值
	UCHAR	Reserved[4];	// 保留位//*/
	if (ar.IsStoring())
	{
		// TODO: add storing code here
		ar<<m_CapInfo.Exposure<<m_CapInfo.Gain[0]<<m_CapInfo.Gain[1]<<m_CapInfo.Gain[2]
			<<m_CapInfo.OffsetX<<m_CapInfo.OffsetY<<m_CapInfo.OffsetY<<m_nContrast;
	}
	else
	{
		// TODO: add loading code here
		ar>>m_CapInfo.Exposure>>m_CapInfo.Gain[0]>>m_CapInfo.Gain[1]>>m_CapInfo.Gain[2]
			>>m_CapInfo.OffsetX>>m_CapInfo.OffsetY>>m_CapInfo.OffsetY>>m_nContrast;
	}
}

void CRZ_Camera::CAM_Initialize(HWND hWnd, int nIdx)
{
	m_nSta = 34;
	m_bCrossline = FALSE;
	m_bstretch = TRUE;
	m_bCompressor = FALSE;
	m_dwCompressor = 0;
	m_nResCount =0;
	m_bTrigger = m_bTriggerMode = FALSE;

	m_hWnd = hWnd;

	m_bPlay=FALSE;

	m_pRawData = NULL;
	m_pRgbData = NULL;
//	m_pRawData = ( BYTE* ) new BYTE [ 2048 * 1536 + 2048 ];
//	m_pRgbData = ( BYTE* ) new BYTE [ 2048 * 1536 * 3 +512];

	m_pSnapBuffer = NULL;
//	m_pSnapBuffer = ( BYTE* ) new BYTE [ 800 * 600 * 3 * 30 +2048];
	m_buffercache = m_pSnapBuffer;

	m_nColorMode = COLOR_RGB24;
	memset( &m_CapInfo, 0, sizeof( CapInfoStruct ) );
	m_CapInfo.Buffer = m_pRawData;
	m_CapInfo.Width		= 752;
	m_CapInfo.Height	= 480;
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
	memset(m_strFriendlyName, 0 , sizeof(TCHAR)*255);
	m_nSharp = 0;
	///////////////////////////////////////////////////////////////

	m_nDevIndex = -1;
	int    nIndex = nIdx;	//第1个设备
//	CRZSDK_DemoApp* pApp = (CRZSDK_DemoApp *)::AfxGetApp();
	DWORD x = RZ_Initialize(_T("RZ_DEMO"), &nIndex, &m_CapInfo, &m_hDevice );
	if( ResSuccess != x)//RZ_Initialize(_T("RZ_DEMO"), &nIndex, &m_CapInfo, &m_hDevice ) ) 
	{
		RZ_Uninitialize( m_hDevice );	
		m_hDevice = NULL;
		::MessageBox( NULL, _T("Initial Error"), _T("Demo"), 0 );
		return;
	}
	m_nDevIndex = nIndex;
	RZ_GetDeviceType(m_hDevice,&m_CamType);
	if (m_CamType!=RZ130SC_YUV)
	{
		RZ_SetExpouseUnit(m_hDevice,1);
		m_CapInfo.Exposure = 10000;
	}
	if (m_CamType==RZCCD140C)
	{
		m_CapInfo.OffsetX = 100;
	}
	if ((m_CamType == MicroUH1200C) || (m_CamType == MicroUH600C))
	{
		if(m_CamType == MicroUH1200C)
		{
			m_CapInfo.Width = 4000;
			m_CapInfo.Height = 3000;
		}
		else
		{
			m_CapInfo.Width = 3072;
			m_CapInfo.Height = 2048;
		}	
		RZ_SetCapInfo( m_hDevice, &m_CapInfo );	
		m_nColorMode = COLOR_RGB24_CLEAR;
		RZ_SetParamColor(m_hDevice, COLOR_RGB24_CLEAR );	
		m_nContrast = 37;
		RZ_SetContrastValue(m_hDevice,m_nContrast);
		RZ_SetSaturation(m_hDevice,m_nSta);
		m_nR = 260;
		m_nB = 264;
		m_nG = 1;
		RZ_SetGainR(m_hDevice, m_nR);
		//RZ_SetGainG(m_hDevice, m_nG);
		RZ_SetGainB(m_hDevice, m_nB);
		RZ_SetGainAll(m_hDevice,m_nG);
	}
	else
	{
		RZ_SetCapInfo( m_hDevice, &m_CapInfo );	
		RZ_SetParamColor(m_hDevice, COLOR_RGB24 );	
		
		RZ_SetContrastValue(m_hDevice,m_nContrast);
		
		RZ_SetGainR(m_hDevice, m_nR);
		RZ_SetGainG(m_hDevice, m_nG);
		RZ_SetGainB(m_hDevice, m_nB);
		
	}
	RZ_SetParamFlip(m_hDevice, FLIP_NATURAL );	
	RZ_GetDeviceColorType(m_hDevice,&m_CamColorType);
	
	m_Xoff = m_Yoff = 0;
	
	RZ_GetTotalDeviceNum(m_hDevice, &s_nCameraCount);
	RZ_GetFriendlyName(m_hDevice, m_strFriendlyName);
	RZ_SetGamma(m_hDevice,16);
	RZ_SetColorAdjust(m_hDevice,COLOR_ADJUST_NO);
	
	//=================================================================
	//根据型号设置支持的分辨率
	switch(m_CamType)
	{
	case RZ500P:
		{
			m_nResCount = sizeof(lpszResolution500P_New)/sizeof(lpszResolution500P_New[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution500P_New,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 25;
			m_nHBlank = 0;
		}
		break;
	case SuperUH500:
		{
			m_nResCount = sizeof(lpszResolution500Super)/sizeof(lpszResolution500Super[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution500Super,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 25;
			m_nHBlank = 0;
			m_CapInfo.Gain[0] = 8;
		}
		break;
	case SuperUH200:
		{
			m_nResCount = sizeof(lpszResolution200Super)/sizeof(lpszResolution200Super[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution200Super,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 25;
			m_nHBlank = 0;
			m_CapInfo.Gain[0] = 8;
		}
		break;
	case SuperUH130:
		{
			m_nResCount = sizeof(lpszResolutionDft)/sizeof(lpszResolutionDft[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolutionDft,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 25;
			m_nHBlank = 0;
			m_CapInfo.Gain[0] = 8;
		}
		break;
	case SuperUH50:
		{
			m_nResCount = sizeof(lpszResolution50)/sizeof(lpszResolution50[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution50,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 25;
			m_nHBlank = 0;
			m_CapInfo.Gain[0] = 8;
		}
		break;
	case SuperUH30:
		{
			m_nResCount = sizeof(lpszResolution30)/sizeof(lpszResolution30[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution30,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 25;
			m_nHBlank = 0;
			m_CapInfo.Gain[0] = 8;
		}
		break;
	case RZ900CF:
		{
			m_nResCount = sizeof(lpszResolution900)/sizeof(lpszResolution900[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution900,sizeof(TagResolution)*m_nResCount);
			Sleep(50);
		}
		break;
	case RZ200CF:
		{
			m_nResCount = sizeof(lpszResolution200)/sizeof(lpszResolution200[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution200,sizeof(TagResolution)*m_nResCount);
		}
		break;
	case RZ500CF:
		{
			m_nResCount = sizeof(lpszResolution500)/sizeof(lpszResolution500[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution500,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 25;
			m_nHBlank = 0;
		}
		break;
	case RZ300:
	case RZ300CF:
	case RZ300_LED:
		{
			m_nResCount = sizeof(lpszResolution300)/sizeof(lpszResolution300[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution300,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 25;
			m_nHBlank = 142;
		}
		break;
	case RZ300C_FPGA:
		{
			m_nResCount = sizeof(lpszResolution300)/sizeof(lpszResolution300[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution300,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 25;
			m_nHBlank = 142;
		}
		break;
	case RZ36M:
		{
			m_nResCount = sizeof(lpszResolution36M)/sizeof(lpszResolution36M[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution36M,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 45;
			m_nHBlank = 94;
		}
		break;
	case RZ130CF:
		{
			m_nResCount = sizeof(lpszResolutionDft)/sizeof(lpszResolutionDft[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolutionDft,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 25;
			m_nHBlank = 25;
		}
		break;
	case RZ120C_FPGA:
		{
			m_nResCount = sizeof(lpszResolution120)/sizeof(lpszResolution120[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution120,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 0;
			m_nHBlank = 0;
			m_CapInfo.Gain[0] = 60;
		}
		break;
	case RZCCD140C:
		{
			m_nResCount = sizeof(lpszResolution140)/sizeof(lpszResolution140[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution140,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 0;
			m_nHBlank = 0;
			m_CapInfo.Gain[0] = 32;
		}
		break;
	case RZF1400CF:
		{
			m_nResCount = sizeof(lpszResolution1400)/sizeof(lpszResolution1400[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution1400,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 0;
			m_nHBlank = 0;
			m_CapInfo.Gain[0] = 13;
			m_CapInfo.Gain[1] = 0;
		}
		break;
	case RZF1000CF:
		{
			m_nResCount = sizeof(lpszResolution1000)/sizeof(lpszResolution1000[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution1000,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 0;
			m_nHBlank = 0;
			m_CapInfo.Gain[0] = 96;
			m_CapInfo.Gain[1] = 0;
		}
		break;
	case RZ130C_FPGA:
	case RZ130M_FPGA:
		{
			m_nResCount = sizeof(lpszResolutionDft)/sizeof(lpszResolutionDft[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolutionDft,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 25;
			m_nHBlank = 9;
		}
		break;
	case MicroUH1200C:
		{
			m_nResCount = sizeof(lpszResolution1200)/sizeof(lpszResolution1200[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution1200,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 0;
			m_nHBlank = 0;
			m_CapInfo.Gain[0] = 0;
			m_CapInfo.Gain[1] = 0;
		}
		break;
	case MicroUH600C:
		{
			m_nResCount = sizeof(lpszResolution600)/sizeof(lpszResolution600[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolution600,sizeof(TagResolution)*m_nResCount);
			m_nVBlank = 0;
			m_nVBlank = 0;
			m_CapInfo.Gain[0] = 0;
			m_CapInfo.Gain[1] = 0;
		}
		break;
	case RZ130:
	case RZ130SC_YUV:
	default:
		{
			m_nResCount = sizeof(lpszResolutionDft)/sizeof(lpszResolutionDft[0]);
			m_lpszResolution = new TagResolution[m_nResCount];
			memcpy(m_lpszResolution,lpszResolutionDft,sizeof(TagResolution)*m_nResCount);		
		}
		break;
	}
	m_CapInfo.Width = m_lpszResolution[0].width;
	m_CapInfo.Height= m_lpszResolution[0].height;

	m_pRawData = ( BYTE* ) new BYTE [ m_lpszResolution[0].width * m_lpszResolution[0].height + m_lpszResolution[0].width ];
	m_pRgbData = ( BYTE* ) new BYTE [ m_lpszResolution[0].width * m_lpszResolution[0].height * 3 +m_lpszResolution[0].width];
	m_CapInfo.Buffer = m_pRawData;
	RZ_SetHBlank( m_hDevice,m_nHBlank);
	RZ_SetVBlank(m_hDevice,m_nVBlank);
	RZ_SetCapInfo(m_hDevice,&m_CapInfo);
	RZ_GetCapInfo(m_hDevice,&m_CapInfo);
	if (((int)m_CapInfo.Width!=m_lpszResolution[0].width) && m_CamType==RZ500P)
	{
		if(m_lpszResolution)
			delete []m_lpszResolution;
		m_lpszResolution = NULL;
		m_nResCount = sizeof(lpszResolution500P)/sizeof(lpszResolution500P[0]);
		m_lpszResolution = new TagResolution[m_nResCount];
		memcpy(m_lpszResolution,lpszResolution500P,sizeof(TagResolution)*m_nResCount);
	}
	if (m_CamType == RZ130SC_YUV)
	{
		RZ_SetSharpness(m_hDevice,m_nSharp);
	}
}

void CRZ_Camera::SetTriggerStatus(BOOL bOn, LPCTSTR lpPath)
{
	if(RZ_GetTrigger( m_hDevice, bOn, BMP, lpPath, 100)==0)
		m_bTrigger = bOn;
}

void CRZ_Camera::SetTriggerMode(BOOL bOn)
{
	RZ_SetTriggerMode(m_hDevice, bOn);
	m_bTriggerMode = bOn;
}

void CRZ_Camera::SelectComprossor()
{
	DWORD dwCode = 0;
	if(RZ_SelectAviCompressor(m_hDevice, &dwCode)==0)
	{
		m_dwCompressor = dwCode;
	}

	EnableCompressor(m_bCompressor);
}

void CRZ_Camera::EnableCompressor(BOOL bOn)
{
	if(bOn)
	{
		RZ_SetAviCompressor(m_hDevice, m_dwCompressor);
	}
	else
	{
		RZ_SetAviCompressor(m_hDevice, 0);	
	}
	m_bCompressor = bOn;
}

void CRZ_Camera::PixelCalibration()
{
	RZ_PixelCalibration(m_hDevice);
}

void CRZ_Camera::softTrigger()
{
	RZ_SoftTrigger(m_hDevice);
}

void CRZ_Camera::SetHDR(BOOL bHDR)
{
	RZ_SetHDR(m_hDevice,bHDR);
}

void CRZ_Camera::EnableLightAvg(BOOL bOn)
{
	RZ_EnableLightAvg(m_hDevice,bOn);
}

void CRZ_Camera::ResetLightAvgTable()
{
	RZ_ResetLightAvgTable(m_hDevice);
}

void CRZ_Camera::SetTriggerDelayTime(LONG Time)
{
	if (m_CamType == RZ36M)
	{
		RZ_SetTriggerCheckSignalTime(m_hDevice,(USHORT)Time);
	}
	else
		RZ_SetTriggerDelayTime(m_hDevice,Time);
}

void CRZ_Camera::EEProm_Set(BYTE *pData)
{
	RZ_EEProm_Set(m_hDevice,pData);
}

void CRZ_Camera::EEProm_Get(BYTE *pData)
{
	RZ_EEProm_Get(m_hDevice,pData);
}

void CRZ_Camera::EEProm_SetByte(int nIndex, int nCount, BYTE *pData)
{
	RZ_EEProm_SetByte(m_hDevice,nIndex,nCount,pData);
}

void CRZ_Camera::EEProm_GetByte(int nIndex, int nCount, BYTE *pData)
{
	RZ_EEProm_GetByte(m_hDevice,nIndex,nCount,pData);
}

void CRZ_Camera::SetCustomIO(BYTE data)
{
	RZ_SetCustomIO(m_hDevice,data);
}

void CRZ_Camera::SetTriggerSource(BYTE data)
{
	RZ_SetTriggerSource(m_hDevice,data);
}

void CRZ_Camera::SetTriggerSourceTime(LONG Time)
{
	RZ_SetTriggerSourceTime(m_hDevice,Time);
}

void CRZ_Camera::SetAEParam(BOOL bAE,LPVOID lpContext)
{
	if ((m_CamType==MicroUH1200C) || (m_CamType==MicroUH600C))
	{
		RZ_SetDoAE( m_hDevice, bAE, 0, 
			AECallBack, this );
	} 
	else
	{
		RZ_SetDoAE( m_hDevice, TRUE, 0, 
			AECallBack, this );
	}
	
//	RZ_AEParam(m_hDevice,bAE,RZ_AE_LEVEL_NORMAL,AECallBack,lpContext);
}

void CRZ_Camera::SetHBlank(int nHBlank)
{
	RZ_SetHBlank(m_hDevice,nHBlank);
}

void CRZ_Camera::SetVBlank(int nVBlank)
{
	RZ_SetVBlank(m_hDevice,nVBlank);
}

void CRZ_Camera::SetZoom(BOOL b)
{
	if(b)
	{
		m_CapInfo.Control |=0x01;
	}
	else
	{
		m_CapInfo.Control &=0xFE;	
	}
	RZ_SetCapInfo( m_hDevice, &m_CapInfo );	
}

void CRZ_Camera::SetExpouseDelayTime(int nTime)
{
	RZ_SetExpouseDelayTime(m_hDevice,nTime);
}

CString CRZ_Camera::GetSerialNumber()
{
	BYTE pData[17];
	memset(&pData,0,sizeof(BYTE)*17);
	RZ_GetSerialNumber(m_hDevice,pData);
	CString str;
	str = pData;
	return str; 
}
CString CRZ_Camera::GetCameraVertion()
{
		BYTE pData[16];
		CString str;
		memset(&pData,0,sizeof(BYTE)*16);
		RZ_GetDeviceVertion(m_hDevice,pData);
		str = pData;
	return str; 
}

void CRZ_Camera::SetNewHWDN(HWND hwnd)
{
	m_hWnd = hwnd;
}

void CRZ_Camera::SetFastCapMode(BOOL b)
{
		RZ_CapFastMode(m_hDevice,b);
		if(b)
		RZ_GetRgbFrame(m_hDevice,&m_CapInfo,m_pRgbData,FALSE);
}
int CRZ_Camera::GetBuffer()
{
	int i =RZ_GetRgbFrame(m_hDevice,&m_CapInfo,m_pRgbData,FALSE);

	
	return i;
}

void CRZ_Camera::SavePic(ENUM_IMAGE_TYPE type, LPCTSTR lpszPath)
{
	CString strPath = lpszPath;
	int color = m_nColorMode>2 ? 8:24;
	switch(type)
	{
	case IMG_TYPE_BMP:
		strPath += _T(".bmp");
		break;
	case IMG_TYPE_JPG:
		strPath += _T(".jpg");
		break;
	default:
		break;
	};
	RZ_FrameToImage(strPath, m_pRgbData, m_CapInfo.Width,m_CapInfo.Height,color,(RZIMAGETYPR)type);
}