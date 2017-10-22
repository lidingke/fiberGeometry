#pragma once
#if !defined(AFX_BASICDLG_H__DE07E1D0_D0B7_4FA5_A4F3_45499366E00E__INCLUDED_)
#define AFX_BASICDLG_H__DE07E1D0_D0B7_4FA5_A4F3_45499366E00E__INCLUDED_


//#include "SdkCallTrace.h"
#include <iostream>
#include <string>
#include "windows.h"

//#include "minwindef.h"
#include "Include\\CameraApi.h"	
#include "Python.h"

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
//#include "ndarraytypes.h"
//#include "__multiarray_api.h"
#include <numpy/arrayobject.h>

using std::string;

//#include "CameraGrabber.h"
#ifdef _WIN64
#pragma comment(lib, "Lib\\MVCAMSDK_X64.lib")
#else
#pragma comment(lib, "Lib\\MVCAMSDK.lib")
#endif



class MindPy
{
public:
	//CStatic	        m_cPreview;//������ʾ���ͼ��Ĵ��ڿؼ�|the control used to display the images.
	CameraHandle    m_hCamera;	//������豸���|the handle of the camera we use
	tSdkFrameHead   m_sFrInfo;//���ڱ��浱ǰͼ��֡��֡ͷ��Ϣ
	tSdkCameraDevInfo*   pCameraInfo;

	BYTE*           pRawBuffer;//ԭʼͼ��Ļ�������

	CameraSdkStatus status;
	string          funName;
	unsigned int     u_imageResolution = 0;

	MindPy();
	~MindPy();
	//int display(int a);
	CameraSdkStatus InitCamera();
	CameraSdkStatus GetRawImg();
	CameraSdkStatus ReleaseRawImg();
	CameraSdkStatus UninitCamera();
	//CameraSdkStatus AdaptInitCamera();

private:
	inline BOOL IsCameraStatusSuccess(int status, string* funName);

};


static MindPy* pMindpy;


static PyObject* InitCameraPlay(PyObject* self, PyObject* args);
static PyObject* GetRawImg(PyObject* self, PyObject* args);
static PyObject* UninitCamera(PyObject* self, PyObject* args);
static PyObject* GetCameraSerial(PyObject* self, PyObject* args);








#endif // !defined(AFX_BASICDLG_H__DE07E1D0_D0B7_4FA5_A4F3_45499366E00E__INCLUDED_)
