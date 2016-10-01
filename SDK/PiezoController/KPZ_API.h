#ifdef KPZ_API
#define KPZ_API __declspec(dllimport)
#else
#define KPZ_API __declspec(dllexport)
#endif


#define WIN32_LEAN_AND_MEAN             // 从 Windows 头中排除极少使用的资料
// Windows 头文件: 
#include <windows.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>
#include <iostream>

//using namespace std;





// TODO:  在此处引用程序需要的其他头文件
#include "Thorlabs.MotionControl.KCube.Piezo.h"

KPZ_API typedef struct KPZ
{
	char Xaxis[10];
	char Yaxis[10];
	char Zaxis[10];
}KPZ;

extern "C"
{
	KPZ_API int Init_KPZ_XYZ(KPZ *info);// 初始化xyz函数
	KPZ_API bool Init_KPZ(char * serialNo);
	KPZ_API void Disconnect(char *serialNo);
	KPZ_API void Disconnect_XYZ(KPZ device);// 释放资源
	KPZ_API void SetVoltage(char *serialNo, double voltage);//设置输出电压
//	KPZ_API double GetVoltage(char *serialNo);//读取当前电压
	KPZ_API bool GetVoltage(char *serialNo, double* voltage);
}
