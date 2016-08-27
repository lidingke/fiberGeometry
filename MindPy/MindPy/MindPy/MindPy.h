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
#include "Python.h"
#include "ndarraytypes.h"
#include "__multiarray_api.h"

using std::string;

//#include "CameraGrabber.h"
#ifdef _WIN64
#pragma comment(lib, "..\\MVCAMSDK_X64.lib")
#else
#pragma comment(lib, "..\\MVCAMSDK.lib")
#endif
/*��������е��������SDK�ӿ���־��Ϣ*/
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
	//CStatic	        m_cPreview;//������ʾ���ͼ��Ĵ��ڿؼ�|the control used to display the images.
	CameraHandle    m_hCamera;	//������豸���|the handle of the camera we use
	tSdkFrameHead   m_sFrInfo;//���ڱ��浱ǰͼ��֡��֡ͷ��Ϣ

	int	            m_iDispFrameNum;//���ڼ�¼��ǰ�Ѿ���ʾ��ͼ��֡������
	float           m_fDispFps;//��ʾ֡��
	float           m_fCapFps;//����֡��
	tSdkFrameStatistic  m_sFrameCount;
	tSdkFrameStatistic  m_sFrameLast;
	int		        m_iTimeLast;

	BYTE*           m_pFrameBuffer;//���ڽ�ԭʼͼ������ת��ΪRGB�Ļ�����
	BOOL	        m_bPause;//�Ƿ���ͣͼ��

	UINT            m_threadID;//ͼ��ץȡ�̵߳�ID
	HANDLE          m_hDispThread;//ͼ��ץȡ�̵߳ľ��
	BOOL            m_bExit;//����֪ͨͼ��ץȡ�߳̽���
	LONG			m_SnapRequest;//��ͼ����	MindPy();
	BYTE*           passBuffer;
	MindPy();
	~MindPy();
	int display(int a);
	BOOL InitCamera();
	int OnButtonSnapshot();

};


extern "C"
{
	MINDPY_API int Edisplay(int a);
	MINDPY_API int GetImg(int language);
	MINDPY_API npy_intp* reArrayData(PyArrayObject aobj);
}









#endif // !defined(AFX_BASICDLG_H__DE07E1D0_D0B7_4FA5_A4F3_45499366E00E__INCLUDED_)
