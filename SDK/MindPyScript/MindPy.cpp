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
	int iCameraNums = 10;
	tSdkCameraDevInfo sCameraList[10];
	//Enumerate camera
	status = CameraSdkInit(0);
	funName = "CameraSdkInit";
	
	if (!IsCameraStatusSuccess(status, &funName))
	{
		return status;
	}
	//枚丼相机，最多返回10个相机的描述信息 
	status = CameraEnumerateDevice(sCameraList, &iCameraNums);
	if (status !=
		CAMERA_STATUS_SUCCESS || iCameraNums == 0)
	{
		return CAMERA_STATUS_NO_DEVICE_FOUND;
	}
	//如果只有一个相机，iCameraNums会被CameraEnumerateDevice内部修改为1。 
	if ((status = CameraInit(&sCameraList[0], -1, -1, &m_hCamera)) !=
		CAMERA_STATUS_SUCCESS)
	{
		return status;
	}
	pCameraInfo = &sCameraList[0];
	//std::cout << "pCameraInfo " << pCameraInfo->acSn << std::endl;
	status = CameraPlay(m_hCamera);
	funName = "CameraPlay";
	IsCameraStatusSuccess(status, &funName);
	if (status != CAMERA_STATUS_SUCCESS) { return status; }
	return CAMERA_STATUS_SUCCESS;
}


CameraSdkStatus MindPy::GetRawImg() 
{

	//tSdkFrameHead FrameInfo;
	//	CameraSnapToBuffer抓拍一帧图像数据到缓冲区中，该缓冲区由SDK内部申请,成功调用后，需要释放
	if ((status = CameraGetImageBuffer(m_hCamera, &m_sFrInfo, &pRawBuffer, 1000)) != CAMERA_STATUS_SUCCESS)
	{
		std::cout << "Snapshot failed,is camera in pause mode?" << status << std::endl;
		return status;
	}
	return status;
}

CameraSdkStatus MindPy::ReleaseRawImg()
{
	//	释放缓冲区
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
	//npy_int limit = 5038848;
	//if (pMindpy->u_imageResolution != 0){
	//	limit = pMindpy->u_imageResolution;
	//}
	
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
	//printf("frame,%d,%d,%d", pMindpy->m_sFrInfo.uBytes,
	//	pMindpy->m_sFrInfo.iHeight, pMindpy->m_sFrInfo.iWidth);
	//PyArrayObject * out = (PyArrayObject*)
	//	PyArray_NewFromDescr(&PyArray_Type,
	//		PyArray_DescrFromType(PyArray_UINT8),
	//		1, &limit, NULL, NULL, NPY_F_CONTIGUOUS, NULL);
	//memcpy(out->data, pMindpy->pRawBuffer, sizeof(npy_byte) * limit);
	//dynamic get dims by frame info
	npy_intp dims[] = { pMindpy->m_sFrInfo.iHeight, pMindpy->m_sFrInfo.iWidth };
	PyArrayObject * out = (PyArrayObject*)
		PyArray_SimpleNewFromData(2, dims, NPY_UBYTE, pMindpy->pRawBuffer);

	status = pMindpy->ReleaseRawImg();
	if (status != CAMERA_STATUS_SUCCESS)
	{
		PyErr_Format(PyExc_ValueError, "release raw img buffer error: %d", status);
		Py_DECREF(out);
		return NULL;
	}
	
	return PyArray_Return(out);

};

static PyObject* GetCameraSerial(PyObject* self, PyObject* args)
{
	return Py_BuildValue("s", pMindpy->pCameraInfo->acSn);
}

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

static PyObject* GetTestArray(PyObject* self, PyObject* args)
{

	npy_byte da[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	int limit = 9;
	//npy_intp dim = 9;
	npy_byte* outArray;
	outArray = (npy_byte*)malloc(sizeof(npy_byte)*limit);
	for (int i = 0; i<limit; i++)
	{
		outArray[i] = da[i];
	}
	//PyArrayObject * out = (PyArrayObject*)PyArray_NewFromDescr(&PyArray_Type, PyArray_DescrFromType(PyArray_BYTE), 1, &dim, NULL, NULL, NPY_C_CONTIGUOUS, NULL);
	npy_intp dims[] = { 9 };
	PyArrayObject * out = (PyArrayObject*)
		PyArray_SimpleNewFromData(1, dims, NPY_UBYTE, outArray);
	//memcpy(out->data, da, sizeof(npy_byte) * 9);
	return PyArray_Return(out);

}


static PyMethodDef MindMethods[] =
{
	{ "init_camera", InitCameraPlay, METH_VARARGS, "init camera" },
	{ "get_raw_img", GetRawImg ,METH_VARARGS, "get raw image from camera"},
	{ "uninit_camera", UninitCamera, METH_VARARGS, "release camera source" },
	{ "raise_error", raiseError, METH_VARARGS, "raise a simple error" },
	{ "get_test_array", GetTestArray, METH_VARARGS, "get ndarray"},
	{"get_camera_serial", GetCameraSerial, METH_VARARGS, "get camera serial number"},
	{ NULL, NULL, 0, NULL }

};

PyMODINIT_FUNC

initMindPy(void)
{
	(void)Py_InitModule("MindPy", MindMethods);
	// a important things is to call import_array!!!
	import_array();
}

