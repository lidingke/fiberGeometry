#define EXPORT_MINDPY_DLL
#include "MindPy.h"



MindPy::MindPy()
{
}


MindPy::~MindPy()
{
}

int MindPy::display(int a)
{
	std::cout << "hello dll"<< a << std::endl;
	return 0;
}


BOOL MindPy::InitCamera()
{
	int iCameraNums;
	CameraSdkStatus status;
	//CRect rect;
	tSdkCameraCapbility sCameraInfo;

	//ö���豸������豸�б�
	//Enumerate camera
	iCameraNums = CameraEnumerateDeviceEx();

	if (iCameraNums <= 0)
	{
		std::cout<<"No camera was found!"<<std::endl;
		return FALSE;
	}
	else
	{
		std::cout << "iCameraNums " << iCameraNums << std::endl;
	}
	//��ʾ���У�����ֻ����������һ���������ˣ�ֻ��ʼ����һ�������(-1,-1)��ʾ�����ϴ��˳�ǰ����Ĳ���������ǵ�һ��ʹ�ø�����������Ĭ�ϲ���.
	//In this demo ,we just init the first camera.
	if ((status = CameraInitEx(0, -1, -1, &m_hCamera)) != CAMERA_STATUS_SUCCESS)
	{
		std::cout<<"Failed to init the camera! Error code is"<<status<<std::endl;
		return FALSE;
	}
	else
	{
		std::cout << "CameraInitEx " << status << std::endl;
	}
	//Tell the camera begin to sendding image
	status = CameraPlay(m_hCamera);
	if (status != CAMERA_STATUS_SUCCESS)
	{
		std::cout << "Failed to start the CameraPlay! Error code is" << status << std::endl;
		return FALSE;
	}
	else
	{
		std::cout << "CameraPlay " << status << std::endl;
	}
	return TRUE;
}

int MindPy::OnButtonSnapshot() //ץ��һ��ͼƬ
{

	tSdkFrameHead FrameInfo;
	BYTE *pRawBuffer;
	BYTE *pRgbBuffer;
	string sFileName;
	char* cFileName;
	tSdkImageResolution sImageSize;
	CameraSdkStatus status;
	string msg;
	memset(&sImageSize, 0, sizeof(tSdkImageResolution));
	sImageSize.iIndex = 0xff;
	//CameraSetResolutionForSnap����ץ��ʱ�ķֱ��ʣ����Ժ�Ԥ��ʱ��ͬ��Ҳ���Բ�ͬ��
	//sImageSize.iIndex = 0xff; sImageSize.iWidth �� sImageSize.iHeight ��0����ʾץ��ʱ�ֱ��ʺ�Ԥ��ʱ��ͬ��
	//�����ϣ��ץ��ʱΪ�����ķֱ��ʣ���ο����ǵ�Snapshot���̡����߲���SDK�ֲ����й�CameraSetResolutionForSnap�ӿڵ���ϸ˵��
	CameraSetResolutionForSnap(m_hCamera, &sImageSize);
	//passBuffer = pRawBuffer;
	//	CameraSnapToBufferץ��һ֡ͼ�����ݵ��������У��û�������SDK�ڲ�����,�ɹ����ú���Ҫ
	if ((status = CameraSnapToBuffer(m_hCamera, &FrameInfo, &pRawBuffer, 1000)) != CAMERA_STATUS_SUCCESS)
	{
		std::cout<<"Snapshot failed,is camera in pause mode?"<<std::endl;
		return FALSE;
	}
	else
	{
		std::cout << "Function: SUCCESS!"<<"CameraSnapToBuffer"<< std::endl;


		////�ɹ�ץ�ĺ󣬱��浽�ļ�
		//CString msg;
		//char sCurpath[128];
		//CString strTime = CTime::GetCurrentTime().Format(_T("%Y%m%d%H%M%S"));
		//GetCurrentDirectory(128, sCurpath);
		//sFileName.Format("%s\\Snapshot%s", sCurpath, strTime);//��ʼ�������ļ����ļ���

															  //����һ��buffer����������õ�ԭʼ����ת��ΪRGB���ݣ���ͬʱ���ͼ����Ч��
		pRgbBuffer = (BYTE *)CameraAlignMalloc(FrameInfo.iWidth*FrameInfo.iHeight * 3, 16);
		//pRgbBuffer = passBuffer;
		//Process the raw data,and get the return image in RGB format
		status = CameraImageProcess(m_hCamera, pRawBuffer, pRgbBuffer, &FrameInfo);
		if (CAMERA_STATUS_SUCCESS != status)
		{
			std::cout << "CameraImageProcess error " << status << std::endl;
			return 0;
		}
		else
		{
			std::cout << "CameraImageProcess " << status << std::endl;
		}
		//Release the buffer which get from CameraSnapToBuffer or CameraGetImageBuffer
		CameraReleaseImageBuffer(m_hCamera, pRawBuffer);
		//CameraSaveImage ����ͼ�����������ʾ��α���BMPͼ�������Ҫ�����������ʽ�ģ������JPG,PNG,RAW�ȣ�
		//��ο����ǵ�Snapshot���̡����߲���SDK�ֲ����й�CameraSaveImage�ӿڵ���ϸ˵��
		sFileName = ".\\test";
		const int len = sFileName.length();
		cFileName = new char[len + 1];
		strcpy(cFileName, sFileName.c_str());

		if ((status = CameraSaveImage(m_hCamera, cFileName, pRgbBuffer, &FrameInfo, FILE_BMP, 100)) != CAMERA_STATUS_SUCCESS)
		{
			std::cout << "CameraSaveImage error " << status << std::endl;
			return 0;
		}
		else
		{
			std::cout << "CameraSaveImage " << status << std::endl;
		}

		CameraAlignFree(pRgbBuffer);

	}
}

MINDPY_API int Edisplay(int a)
{
	MindPy mpy;
	mpy.display(a);
	return 0;
}

MINDPY_API npy_intp* reArrayData(PyArrayObject aobj)
{

	npy_intp* ind;
	PyArray_GetPtr(&aobj, ind);
	//passBuffer = ind;
	return ind;

};


MINDPY_API int GetImg(int language)
{
	MindPy mindpy;
	int status;
	status = CameraSdkInit(language);
	if (CAMERA_STATUS_SUCCESS != status)
	{
		std::cout << "CameraSdkInit error " << status << std::endl;
		return 0;
	}
	else
	{
		std::cout << "CameraSdkInit " << status << std::endl;
	}
	status = mindpy.InitCamera();
	if (!status)
	{
		std::cout << "InitCamera error" << status << std::endl;
		return 0;
	}
	else
	{
		std::cout << "InitCamera " << status << std::endl;
	}
	
	status = mindpy.OnButtonSnapshot();
	if (!status)
	{
		std::cout << "OnButtonSnapshot error" << status << std::endl;
		return 0;
	}
	else
	{
		std::cout << "OnButtonSnapshot " << status << std::endl;
	}
	return TRUE;
}