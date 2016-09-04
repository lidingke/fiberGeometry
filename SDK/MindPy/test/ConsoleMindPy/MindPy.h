#pragma once
#if !defined(AFX_BASICDLG_H__DE07E1D0_D0B7_4FA5_A4F3_45499366E00E__INCLUDED_)
#define AFX_BASICDLG_H__DE07E1D0_D0B7_4FA5_A4F3_45499366E00E__INCLUDED_

#ifdef EXPORT_MINDPY_DLL  
#define MINDPY_API __declspec(dllexport)  
#else  
#define MINDPY_API __declspec(dllimport)  
#endif  


#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

//#include "SdkCallTrace.h"
#include <iostream>
#include <string>
#include "windows.h"

//#include "minwindef.h"
#include "CameraApi.h"	
//#include "Python.h"
//#include "ndarraytypes.h"
//#include "__multiarray_api.h"

using std::string;

//#include "CameraGrabber.h"
#ifdef _WIN64
#pragma comment(lib, "..\\MVCAMSDK_X64.lib")
#else
#pragma comment(lib, "..\\MVCAMSDK.lib")
#endif
/*输出例程中调用相机的SDK接口日志信息*/
#define SDK_TRACE(_FUNC_,TXT) \
{\
	CameraSdkStatus status;\
	string msg;\
	string FuncName;\
	FuncName = #_FUNC_;\
	FuncName = FuncName.Left(FuncName.FindOneOf("("));\
\
	status = _FUNC_;\
	if (status != CAMERA_STATUS_SUCCESS)\
	{\
	msg = "Function:"+FuncName+" return error";\
	std::cout<<msg<<std::endl;\
	msg = "Error code:"+status+".refer to CameraStatus.h for more information";\
	std::cout<<msg<<std::endl;\
	}\
	else\
	{\
	msg = "Function:"+FuncName+" return error";\
	std::cout<<msg<<std::endl;\
	msg = "Error code:"+status+".refer to CameraStatus.h for more information";\
	std::cout<<msg<<std::endl;\
	}\
	msg = "";\
	std::cout<<msg<<std::endl;\
}





class MindPy
{
public:
	//CStatic	        m_cPreview;//用于显示相机图像的窗口控件|the control used to display the images.
	CameraHandle    m_hCamera;	//相机的设备句柄|the handle of the camera we use
	tSdkFrameHead   m_sFrInfo;//用于保存当前图像帧的帧头信息

	int	            m_iDispFrameNum;//用于记录当前已经显示的图像帧的数量
	float           m_fDispFps;//显示帧率
	float           m_fCapFps;//捕获帧率
	tSdkFrameStatistic  m_sFrameCount;
	tSdkFrameStatistic  m_sFrameLast;
	int		        m_iTimeLast;

	BYTE*           m_pFrameBuffer;//用于将原始图像数据转换为RGB的缓冲区
	BOOL	        m_bPause;//是否暂停图像

	UINT            m_threadID;//图像抓取线程的ID
	HANDLE          m_hDispThread;//图像抓取线程的句柄
	BOOL            m_bExit;//用来通知图像抓取线程结束
	LONG			m_SnapRequest;//截图请求	
	BYTE*           passBuffer;
	int             bufferSize;
	MindPy();
	~MindPy();
	int display(int a);
	BOOL InitCamera();
	int OnButtonSnapshot();
	BYTE * OnButtonSnapshotWithNoSaveFree(CameraHandle m_hCamera);
	BYTE * GetRawImg(CameraHandle m_hCamera);

};


extern "C"
{
	MINDPY_API int Edisplay(int a);
	MINDPY_API int GetImg();

	MINDPY_API int RePyArray(BYTE *barray[], int limit);
	MINDPY_API int doubleRePyArray(BYTE barray[], int limit);

	MINDPY_API BYTE PointerSweep(BYTE *head, int index);
	MINDPY_API int sweepArray(int *ar1, int *ar2, int length);

	MINDPY_API CameraHandle InitCameraPlay();
	MINDPY_API int GetRawImg(BYTE barray[], int limit, CameraHandle m_hCamera);
	MINDPY_API int GetOneImg(BYTE barray[], int limit, CameraHandle m_hCamera);
	//MINDPY_API PyArrayObject* getPyArrayObject(PyArrayObject* aobj);
	//MINDPY_API npy_intp* reArrayData(PyArrayObject* aobj);
	//MINDPY_API PyArrayObject* rePyArrayObject();
}





#endif // !defined(AFX_BASICDLG_H__DE07E1D0_D0B7_4FA5_A4F3_45499366E00E__INCLUDED_)
