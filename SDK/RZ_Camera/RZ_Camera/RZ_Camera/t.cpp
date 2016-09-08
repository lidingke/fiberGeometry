//  m_hDevice = hCamera;
//  m_nSta = 34;
//  m_bCrossline = false;
//  m_bstretch = true;
//  m_bCompressor = false;
//  m_dwCompressor = 0;
//  m_nResCount = 0;
//  m_bTrigger = m_bTriggerMode = false;
//  m_bPlay = false;
//  m_pRawData = NULL;
//  m_pRgbData = NULL;
//  m_pSnapBuffer = NULL;
//  //  m_pSnapBuffer = ( unsigned char* ) new BYTE [ 800 * 600 * 3 * 30 +2048];
//  m_buffercache = m_pSnapBuffer;
//
//  m_nColorMode = COLOR_RGB24;
//  //m_CapInfo = *pCapInfo;
//  m_CapInfo.Buffer = pCapInfo->Buffer;
//  m_CapInfo.Width = pCapInfo->Width;
//  m_CapInfo.Height = pCapInfo->Height;
//  std::cout << "GetBuffer in width height  " << pCapInfo->Width << m_CapInfo.Height << std::endl;
//
//  m_CapInfo.Exposure = 100;
//  m_nR = m_nG = m_nB = 500;
//  m_nContrast = 16;
//  m_nFlipMode = FLIP_NATURAL;
//  m_lpszResolution = NULL;
//  m_CamColorType = RZ_COLOR;
//  m_nHBlank = m_nVBlank = 0;
//  memset(m_strFriendlyName, 0, sizeof(char) * 255);
//  m_nSharp = 0;
//
//  //m_nDevIndex = -1;
//  int    nIndex = 1;  //第1个设备
//  //                          CRZSDK_DemoApp* pApp = (CRZSDK_DemoApp *)::AfxGetApp();
//  int x = RZ_Initialize(_T("RZ_DEMO"), &nIndex, &m_CapInfo, &m_hDevice);
//  if (ResSuccess != x)//RZ_Initialize(_T("RZ_DEMO"), &nIndex, &m_CapInfo, &m_hDevice ) )
//  {
//      std::cout << "rzinit" << x << std::endl;
//      RZ_Uninitialize(m_hDevice);
//      m_hDevice = NULL;
//      return x;
//  }
//  m_nDevIndex = nIndex;
//  RZ_GetDeviceType(m_hDevice, &m_CamType);
//  //=================================================================
//  //根据型号设置支持的分辨率
//  //m_nResCount = sizeof(lpszResolution600) / sizeof(lpszResolution600[0]);
//  //m_lpszResolution = new TagResolution[m_nResCount];
//  //memcpy(m_lpszResolution, lpszResolution600, sizeof(TagResolution)*m_nResCount);
//  m_nVBlank = 0;
//  m_nVBlank = 0;
//  m_CapInfo.Gain[0] = 10;
//  m_CapInfo.Gain[1] = 100;
//  m_CapInfo.Gain[2] = 10;
//
//  //m_pRawData = (unsigned char*) new unsigned char[m_lpszResolution[0].width * m_lpszResolution[0].height + m_lpszResolution[0].width];
//  //m_pRgbData = (unsigned char*) new unsigned char[m_lpszResolution[0].width * m_lpszResolution[0].height * 3 + m_lpszResolution[0].width];
//  //m_CapInfo.Buffer = m_pRawData;
//  RZ_SetHBlank(m_hDevice, m_nHBlank);
//  RZ_SetVBlank(m_hDevice, m_nVBlank);
//  RZ_SetCapInfo(m_hDevice, &m_CapInfo);
//  RZ_GetCapInfo(m_hDevice, &m_CapInfo);
//  RZ_SetExpouseDelayTime(m_hDevice, 2000);
//
//  return 0;
