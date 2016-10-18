#define EXPORT_MINDPY_DLL
#include "MindPy.h"


MindPy::MindPy()
{
}


MindPy::~MindPy()
{
}



inline BOOL MindPy::IsCameraStatusSuccess(int status, string* funName)
{
	if (status != CAMERA_STATUS_SUCCESS)
	{
		std::cout << "Failed to run"<< funName << "Error code is" << status << std::endl;
		
		return FALSE;
	}
	else
	{
		return TRUE;
	}
}

CameraSdkStatus MindPy::InitCamera()
{
	int iCameraNums;

	//tSdkCameraCapbility sCameraInfo;
	//枚举设备，获得设备列表
	//Enumerate camera
	status = CameraSdkInit(0);
	funName = "CameraSdkInit";
	
	if (!IsCameraStatusSuccess(status, &funName))
	{
		return status;
	}
	iCameraNums = CameraEnumerateDeviceEx();

	if (iCameraNums <= 0)
	{
		
		//PyErr_SetString(PyExc_TypeError, "camera error");
		
		std::cout<<"No camera was found! "<< iCameraNums <<std::endl;
		//Py_XDECREF(NULL);
		return CAMERA_STATUS_NO_DEVICE_FOUND;
	}
	//else
	//{
	//	std::cout << "iCameraNums " << iCameraNums << std::endl;
	//}
	//In this demo ,we just init the first camera.
	status = CameraInitEx(0, -1, -1, &m_hCamera);
	funName = "CameraInitEx";
	IsCameraStatusSuccess(status, &funName);
	if (status != CAMERA_STATUS_SUCCESS){return status;}

	//Tell the camera begin to sendding image
	status = CameraPlay(m_hCamera);
	funName = "CameraPlay";
	IsCameraStatusSuccess(status, &funName);
	if (status != CAMERA_STATUS_SUCCESS) { return status; }
	return CAMERA_STATUS_SUCCESS;
}



CameraSdkStatus MindPy::GetRawImg() 
{

	tSdkFrameHead FrameInfo;
	//	CameraSnapToBuffer抓拍一帧图像数据到缓冲区中，该缓冲区由SDK内部申请,成功调用后，需要
	if ((status = CameraGetImageBuffer(m_hCamera, &FrameInfo, &pRawBuffer, 1000)) != CAMERA_STATUS_SUCCESS)
	{
		std::cout << "Snapshot failed,is camera in pause mode?" << status << std::endl;
		return status;
	}
	return status;
}

CameraSdkStatus MindPy::ReleaseRawImg()
{
	//	CameraSnapToBuffer抓拍一帧图像数据到缓冲区中，该缓冲区由SDK内部申请,成功调用后，需要
	if ((status = CameraReleaseImageBuffer(m_hCamera, pRawBuffer)) != CAMERA_STATUS_SUCCESS)
	{
		std::cout << "release failed, error code " << status << std::endl;
		return status;
	}
	CameraAlignFree(this->pRawBuffer);
	return status;
}

CameraSdkStatus MindPy::UninitCamera()
{
	return CameraUnInit(m_hCamera);
}


static PyObject* InitCameraPlay(PyObject* self, PyObject* args)
{
	pMindpy = new MindPy;
	CameraSdkStatus status = pMindpy->InitCamera();
	if (status != 0)
	{
		PyErr_Format(PyExc_ValueError, "Camera init error: %d", status);
		return NULL;
	}
	return Py_BuildValue("l", pMindpy->m_hCamera);
}

static PyObject* GetRawImg(PyObject* self, PyObject* args)
{

	CameraSdkStatus status;
	// 1944*2052 dpi
	npy_int limit = 5038848;

	//if (!PyArg_ParseTuple(args, "I", &limit))
	//{
	//	PyErr_SetString(PyExc_ValueError, "lentgh value get wrong");
	//	return NULL;
	//}
	status = pMindpy->GetRawImg();
	if (status != CAMERA_STATUS_SUCCESS)
	{
		PyErr_Format(PyExc_ValueError, "get raw image error: %d", status);
		return NULL;
	}
	PyArrayObject * out = (PyArrayObject*)
		PyArray_NewFromDescr(&PyArray_Type,
			PyArray_DescrFromType(PyArray_UINT8),
			1, &limit, NULL, NULL, NPY_F_CONTIGUOUS, NULL);
	memcpy(out->data, pMindpy->pRawBuffer, sizeof(npy_byte) * limit);
	//return PyArray_Return(out);

	status = pMindpy->ReleaseRawImg();
	if (status != CAMERA_STATUS_SUCCESS)
	{
		PyErr_Format(PyExc_ValueError, "release raw img buffer error: %d", status);
		Py_DECREF(out);
		return NULL;
	}
	
	return PyArray_Return(out);

};

static PyObject* UninitCamera(PyObject* self, PyObject* args)
{
	CameraSdkStatus status;
	status = pMindpy->UninitCamera();
	if (status != CAMERA_STATUS_SUCCESS)
	{
		PyErr_Format(PyExc_ValueError, "uninit camera error: %d", status);
		return NULL;
	}
	delete pMindpy;
	return Py_BuildValue("i", 1);
}


static PyObject* raiseError(PyObject* self, PyObject* args)
{
	PyErr_SetString(PyExc_ValueError, "Ooops");
	return NULL;
}




static PyObject* GetInter(PyObject* self, PyObject* args)
{

	npy_int limit;

	if (!PyArg_ParseTuple(args, "i", &limit))
	{
		PyErr_SetString(PyExc_ValueError, "lentgh value get worry type");
		return NULL;
	}
	return Py_BuildValue("i", limit);

}





static PyObject* GetNdarray(PyObject* self, PyObject* args)
{

	npy_byte da[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	npy_intp dim = 9;

	PyArrayObject * out = (PyArrayObject*)PyArray_NewFromDescr(&PyArray_Type, PyArray_DescrFromType(PyArray_BYTE), 1, &dim, NULL, NULL, NPY_C_CONTIGUOUS, NULL);

	memcpy(out->data, da, sizeof(npy_byte) * 9);
	return PyArray_Return(out);

}


static PyMethodDef MindMethods[] =
{
	{ "initCamera", InitCameraPlay, METH_VARARGS, "init camera" },
	{ "getRawImg", GetRawImg ,METH_VARARGS, "get raw image from camera"},
	{ "uninitCamera", UninitCamera, METH_VARARGS, "release camera source" },
	{ "raise_error", raiseError, METH_VARARGS, "raise a simple error" },
	{ "getNdarray", GetNdarray, METH_VARARGS, "get ndarray"},
	{"getIntger", GetInter, METH_VARARGS, "get int"},
	{ NULL, NULL, 0, NULL }

};

PyMODINIT_FUNC

initMindPy(void)
{
	(void)Py_InitModule("MindPy", MindMethods);
	// a important things is to call import_array!!!
	import_array();
}

