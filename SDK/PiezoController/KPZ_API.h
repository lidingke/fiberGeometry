#ifdef KPZ_API
#define KPZ_API __declspec(dllimport)
#else
#define KPZ_API __declspec(dllexport)
#endif


#define WIN32_LEAN_AND_MEAN             // �� Windows ͷ���ų�����ʹ�õ�����
// Windows ͷ�ļ�: 
#include <windows.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>
#include <iostream>

//using namespace std;





// TODO:  �ڴ˴����ó�����Ҫ������ͷ�ļ�
#include "Thorlabs.MotionControl.KCube.Piezo.h"

KPZ_API typedef struct KPZ
{
	char Xaxis[10];
	char Yaxis[10];
	char Zaxis[10];
}KPZ;

extern "C"
{
	KPZ_API int Init_KPZ_XYZ(KPZ *info);// ��ʼ��xyz����
	KPZ_API bool Init_KPZ(char * serialNo);
	KPZ_API void Disconnect(char *serialNo);
	KPZ_API void Disconnect_XYZ(KPZ device);// �ͷ���Դ
	KPZ_API void SetVoltage(char *serialNo, double voltage);//���������ѹ
//	KPZ_API double GetVoltage(char *serialNo);//��ȡ��ǰ��ѹ
	KPZ_API bool GetVoltage(char *serialNo, double* voltage);
}
