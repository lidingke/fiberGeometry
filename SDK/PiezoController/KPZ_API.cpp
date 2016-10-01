// KPZ_API.cpp : 定义 DLL 应用程序的导出函数。
//

#include "KPZ_API.h"


const double N = 218.446;

int Init_KPZ_XYZ(KPZ *info)
{
	int status;
	status = TLI_BuildDeviceList();
	if (status == 0)					// 建立连接的设备列表
	{
		std::cout << "TLI_BuildDeviceList " << status << std::endl;
		status = TLI_GetDeviceListSize();
		std::cout << "GET device list size " << status << std::endl;
		if (status != 3)			// 获得设备列表的大小
		{

			return NULL;							// 设备列表不等于3，说明有设备未安装好，返回错误
		}
		//KPZ *info = (KPZ *)malloc(sizeof(KPZ));
		char serialNos[30];
		char device[3][10];
		int i = 0;
		TLI_GetDeviceListByTypeExt(serialNos, 30, 29);// 获取设备序列号
		std::cout << "serial nos" << serialNos << std::endl;
		char *p = strtok(serialNos, ",");
		while (p != NULL)
		{
			TLI_DeviceInfo deviceInfo;
			TLI_GetDeviceInfo(p, &deviceInfo);
			char serialNo[9];
			strncpy_s(serialNo, deviceInfo.serialNo, 8);
			serialNo[8] = '\0';
			strcpy_s(device[i], serialNo);
			i++;
			p = strtok(NULL, ",");
		}
		for (int i = 0; i < 3; i++)
		{
			std::cout << device[i] << " device id" << std::endl;
			if (PCC_Open(device[i]) == 0)		    // 依次打开3个设备进行通信
			{
				PCC_StartPolling(device[i], 200);   // 启动持续请求位置和状态的内部轮询循环 200ms轮询速率
				Sleep(20);
				// 设置位置控制模式 1：开环，2：闭环，3：开环平滑，4：闭环平滑
				PCC_SetPositionControlMode(device[i], PZ_ControlModeTypes::PZ_OpenLoop);
				Sleep(20);
				PCC_Enable(device[i]);				// 使能软件控制驱动器
				Sleep(20);
			}
			else
			{
				std::cout << "device error" << std::endl;
				return NULL;						// 打开设备失败，返回错误
			}
		}
		strcpy_s(info->Xaxis, device[0]);
		strcpy_s(info->Yaxis, device[1]);
		strcpy_s(info->Zaxis, device[2]);
		std::cout << info->Xaxis << std::endl;
		return 1;
	}
	else
	{
		return NULL;								// 建立设备列表失败，返回错误
	}
}


bool Init_KPZ(char * serialNo)
{
		//char serialNo[10];
		//char device[3][10];
		//int i = 0;
	//int status;
	//status = TLI_BuildDeviceList();
	//std::cout << "TLI_BuildDeviceList " << status << std::endl;
	//TLI_GetDeviceListByTypeExt(serialNo, 30, 29);// 获取设备序列号
	//std::cout << "serial nos " << serialNo << std::endl;
	TLI_DeviceInfo deviceInfo;
	TLI_GetDeviceInfo(serialNo, &deviceInfo);

	if (PCC_Open(serialNo) == 0)		    // 依次打开3个设备进行通信
	{
		PCC_StartPolling(serialNo, 200);   // 启动持续请求位置和状态的内部轮询循环 200ms轮询速率
		Sleep(20);
		// 设置位置控制模式 1：开环，2：闭环，3：开环平滑，4：闭环平滑
		PCC_SetPositionControlMode(serialNo, PZ_ControlModeTypes::PZ_OpenLoop);
		Sleep(20);
		PCC_Enable(serialNo);				// 使能软件控制驱动器
		Sleep(20);
		std::cout << "open serial " << serialNo << std::endl;
	}
	else
	{
		std::cout << "device error" << std::endl;
		return false;						// 打开设备失败，返回错误
	}
	return true;
};


void Disconnect(char *serialNo)
{
	PCC_StopPolling(serialNo);
	PCC_Close(serialNo);
};

void Disconnect_XYZ(KPZ device)
{
	PCC_StopPolling(device.Xaxis);
	PCC_StopPolling(device.Yaxis);
	PCC_StopPolling(device.Zaxis);
	PCC_Close(device.Xaxis);
	PCC_Close(device.Yaxis);
	PCC_Close(device.Zaxis);
}

void SetVoltage(char *serialNo, double voltage)//0v 150
{
	//std::cout << serialNo << voltage << std::endl;
	short v = (short)(voltage * N);
	PCC_SetOutputVoltage(serialNo, v);				// 设置输出电压
}

//double GetVoltage(char *serialNo)
//{
//	//std::cout << serialNo << std::endl;
//	double voltage = PCC_GetOutputVoltage(serialNo) / N;
//	return voltage;
//}

bool GetVoltage(char *serialNo, double* voltage)
{
	//std::cout << serialNo << std::endl;
	*voltage = PCC_GetOutputVoltage(serialNo) / N;
	std::cout << "get voltage " << *voltage << std::endl;
	return true;
}
