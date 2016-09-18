#define EXPORT_MINDPY_DLL
#include "MindPy.h"



MindPy::MindPy()
{
}


MindPy::~MindPy()
{
}

//int MindPy::display(int a)
//{
//	std::cout << "hello dll"<< a << std::endl;
//	return 0;
//}


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
		std::cout<<"Snapshot failed,is camera in pause mode? "<< status <<std::endl;
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
		pRgbBuffer = (BYTE *)CameraAlignMalloc(FrameInfo.iWidth*FrameInfo.iHeight * 3, 8);
		passBuffer = pRgbBuffer;
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

		//CameraAlignFree(pRgbBuffer);

	}
	return FrameInfo.iWidth*FrameInfo.iHeight * 3;
}


BYTE * MindPy::OnButtonSnapshotWithNoSaveFree(CameraHandle m_hCamera) //ץ��һ��ͼƬ
{

	tSdkFrameHead FrameInfo;
	BYTE *pRawBuffer;
	BYTE *pRgbBuffer;
	//string sFileName;
	//char* cFileName;
	//tSdkImageResolution sImageSize;
	CameraSdkStatus status;
	string msg;
	DWORD dwStart;
	DWORD dwEnd;
	DWORD dwTimes;
	int language = 0;
	//memset(&sImageSize, 0, sizeof(tSdkImageResolution));
	//sImageSize.iIndex = 0xff;
	//sImageSize.iWidth = 0;
	//sImageSize.iHeight = 0;
	//CameraSetResolutionForSnap����ץ��ʱ�ķֱ��ʣ����Ժ�Ԥ��ʱ��ͬ��Ҳ���Բ�ͬ��
	//sImageSize.iIndex = 0xff; sImageSize.iWidth �� sImageSize.iHeight ��0����ʾץ��ʱ�ֱ��ʺ�Ԥ��ʱ��ͬ��
	//�����ϣ��ץ��ʱΪ�����ķֱ��ʣ���ο����ǵ�Snapshot���̡����߲���SDK�ֲ����й�CameraSetResolutionForSnap�ӿڵ���ϸ˵��
	//CameraSetResolutionForSnap(m_hCamera, &sImageSize);
	//passBuffer = pRawBuffer;
	//	CameraSnapToBufferץ��һ֡ͼ�����ݵ��������У��û�������SDK�ڲ�����,�ɹ����ú���Ҫ
	dwStart = GetTickCount();
	status = CameraGetImageBuffer(m_hCamera, &FrameInfo, &pRawBuffer, 1000); // Your program.
	dwEnd = GetTickCount();
	dwTimes = dwEnd - dwStart;
	std::cout << "get img buffer time:" << dwTimes << std::endl;
	if (status  != CAMERA_STATUS_SUCCESS)
	{
		std::cout << "Snapshot failed,is camera in pause mode?" << status <<std::endl;
		return FALSE;
	}
	else
	{
		std::cout << "Function: SUCCESS!" << "CameraSnapToBuffer" << std::endl;

		bufferSize = FrameInfo.iWidth*FrameInfo.iHeight * 3;
		pRgbBuffer = (BYTE *)CameraAlignMalloc(bufferSize, 8);
		passBuffer = pRgbBuffer;
		//Process the raw data,and get the return image in RGB format
		dwStart = GetTickCount();
		status = CameraImageProcess(m_hCamera, pRawBuffer, pRgbBuffer, &FrameInfo);
		dwEnd = GetTickCount();
		dwTimes = dwEnd - dwStart;
		std::cout << "CameraImageProcess time: " << dwTimes << std::endl;
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
		
	}
	return pRgbBuffer;
	//return FrameInfo.iWidth*FrameInfo.iHeight * 3 * 8;
}

BYTE * MindPy::GetRawImg(CameraHandle m_hCamera) //ץ��һ��ͼƬ
{

	tSdkFrameHead FrameInfo;
	BYTE *pRawBuffer;
	CameraSdkStatus status;
	string msg;
	int language = 0;
	//	CameraSnapToBufferץ��һ֡ͼ�����ݵ��������У��û�������SDK�ڲ�����,�ɹ����ú���Ҫ
	if ((status = CameraGetImageBuffer(m_hCamera, &FrameInfo, &pRawBuffer, 1000)) != CAMERA_STATUS_SUCCESS)
	{
		std::cout << "Snapshot failed,is camera in pause mode?" << status << std::endl;
		return FALSE;
	}
	else
	{
		std::cout << "Function: SUCCESS!" << "CameraGetImageBuffer" << std::endl;

		//Release the buffer which get from CameraSnapToBuffer or CameraGetImageBuffer
		//CameraReleaseImageBuffer(m_hCamera, pRawBuffer);

	}
	return pRawBuffer;
	//return FrameInfo.iWidth*FrameInfo.iHeight * 3 * 8;
}
int MindPy::ReleaseRawImg(CameraHandle m_hCamera, BYTE *pbyBuffer)
{
	int status;
	//	CameraSnapToBufferץ��һ֡ͼ�����ݵ��������У��û�������SDK�ڲ�����,�ɹ����ú���Ҫ
	if ((status = CameraReleaseImageBuffer(m_hCamera, pbyBuffer)) != CAMERA_STATUS_SUCCESS)
	{
		std::cout << "release failed,error code " << status << std::endl;
		return FALSE;
	}
	else
	{
		std::cout << "Function: SUCCESS!" << "releaseBuffer" << std::endl;

		//Release the buffer which get from CameraSnapToBuffer or CameraGetImageBuffer
		//CameraReleaseImageBuffer(m_hCamera, pRawBuffer);

	}
	return status;
};



//MINDPY_API int Edisplay(int a)
//{
//	MindPy mpy;
//	mpy.display(a);
//	return 0;
//}
//
//MINDPY_API int RePyArray(BYTE *barray[], int limit)
//{
//	//int total = 0;
//	//for (int i = 0; i < limit; i++)
//	//	total = total + barray[i];
//	//	std::cout << 't ' << total << std::endl;
//
//	//return total;
//	MindPy mindpy;
//	int status;
//	int language = 0;
//	BYTE * arrayGet;
//	int limitGet;
//	status = CameraSdkInit(language);
//	if (CAMERA_STATUS_SUCCESS != status)
//	{
//		std::cout << "CameraSdkInit error " << status << std::endl;
//		return 0;
//	}
//	else
//	{
//		std::cout << "CameraSdkInit " << status << std::endl;
//	}
//	status = mindpy.InitCamera();
//	if (!status)
//	{
//		std::cout << "InitCamera error" << status << std::endl;
//		return 0;
//	}
//	else
//	{
//		std::cout << "InitCamera " << status << std::endl;
//	}
//
//	limitGet = mindpy.OnButtonSnapshot();
//	if (!limitGet)
//	{
//		std::cout << "OnButtonSnapshot error" << limitGet << std::endl;
//		return 0;
//	}
//	else
//	{
//		std::cout << "OnButtonSnapshot " << limitGet << std::endl;
//	}
//	arrayGet = mindpy.passBuffer;
//	limitGet = limitGet ;
//	if (limitGet == limit)
//	{
//		for (int i = 0; i < limit; i++)
//			barray[i] = &arrayGet[i];
//		//barray = arrayGet;
//		
//	}
//	else
//	{
//		return FALSE;
//	}
//	return TRUE;
//	//barray[1] = 5;
//
//};

//
//MINDPY_API int doubleRePyArray(BYTE barray[], int limit)
//{
//	//int total = 0;
//	//for (int i = 0; i < limit; i++)
//	//	total = total + barray[i];
//	//	std::cout << 't ' << total << std::endl;
//
//	//return total;
//	MindPy mindpy;
//	int status;
//	int language = 0;
//	BYTE * arrayGet;
//	int limitGet;
//	status = CameraSdkInit(language);
//	if (CAMERA_STATUS_SUCCESS != status)
//	{
//		std::cout << "CameraSdkInit error " << status << std::endl;
//		return 0;
//	}
//	else
//	{
//		std::cout << "CameraSdkInit " << status << std::endl;
//	}
//	status = mindpy.InitCamera();
//	if (!status)
//	{
//		std::cout << "InitCamera error" << status << std::endl;
//		return 0;
//	}
//	else
//	{
//		std::cout << "InitCamera " << status << std::endl;
//	}
//
//	limitGet = mindpy.OnButtonSnapshot();
//	if (!limitGet)
//	{
//		std::cout << "OnButtonSnapshot error" << limitGet << std::endl;
//		return 0;
//	}
//	else
//	{
//		std::cout << "OnButtonSnapshot " << limitGet << std::endl;
//	}
//	arrayGet = mindpy.passBuffer;
//	memcpy(barray, arrayGet, limitGet);
//
//	return TRUE;
//	////barray[1] = 5;
//
//};

//MINDPY_API BYTE PointerSweep(BYTE *head, int index)
//{
//	return head[index];
//};

//MINDPY_API int sweepArray(int *ar1, int *ar2, int length)
//{
//	for (int i = 0; i < length; i++)
//	{
//		ar1[i] = ar2[i];
//	}
//	return 1;
//};

MINDPY_API int GetImg()
{
	MindPy mindpy;
	int status;
	int language = 0;
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




MINDPY_API CameraHandle InitCameraPlay()
{
	MindPy mindpy;
	int status;
	int language = 0;
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
	return mindpy.m_hCamera;
};


MINDPY_API int GetOneImg(BYTE barray[], int limit, CameraHandle m_hCamera)
{
	MindPy mindpy;
	BYTE * arrayGet;
	int limitGet;
	arrayGet = mindpy.OnButtonSnapshotWithNoSaveFree(m_hCamera);
	//arrayGet = mindpy.passBuffer;
	limitGet = mindpy.bufferSize;
	//barray = arrayGet;
	memcpy(barray, arrayGet, limitGet);//2ms 1920*1080*3
	//CameraAlignFree(arrayGet);
	return TRUE;

};

MINDPY_API int GetRawImg(BYTE barray[], int limit, CameraHandle m_hCamera) 
{
	MindPy mindpy;
	BYTE * arrayGet;
	int limitGet;
	arrayGet = mindpy.GetRawImg(m_hCamera);
	//arrayGet = mindpy.passBuffer;
	//limitGet = mindpy.bufferSize;
	//barray = arrayGet;
	memcpy(barray, arrayGet, limit);//2ms 1920*1080*3
	mindpy.ReleaseRawImg(m_hCamera, arrayGet);
	//CameraAlignFree(arrayGet);
	return TRUE;

};
