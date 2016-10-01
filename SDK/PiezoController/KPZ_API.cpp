// KPZ_API.cpp : ���� DLL Ӧ�ó���ĵ���������
//

#include "KPZ_API.h"


const double N = 218.446;

int Init_KPZ_XYZ(KPZ *info)
{
	int status;
	status = TLI_BuildDeviceList();
	if (status == 0)					// �������ӵ��豸�б�
	{
		std::cout << "TLI_BuildDeviceList " << status << std::endl;
		status = TLI_GetDeviceListSize();
		std::cout << "GET device list size " << status << std::endl;
		if (status != 3)			// ����豸�б�Ĵ�С
		{

			return NULL;							// �豸�б�����3��˵�����豸δ��װ�ã����ش���
		}
		//KPZ *info = (KPZ *)malloc(sizeof(KPZ));
		char serialNos[30];
		char device[3][10];
		int i = 0;
		TLI_GetDeviceListByTypeExt(serialNos, 30, 29);// ��ȡ�豸���к�
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
			if (PCC_Open(device[i]) == 0)		    // ���δ�3���豸����ͨ��
			{
				PCC_StartPolling(device[i], 200);   // ������������λ�ú�״̬���ڲ���ѯѭ�� 200ms��ѯ����
				Sleep(20);
				// ����λ�ÿ���ģʽ 1��������2���ջ���3������ƽ����4���ջ�ƽ��
				PCC_SetPositionControlMode(device[i], PZ_ControlModeTypes::PZ_OpenLoop);
				Sleep(20);
				PCC_Enable(device[i]);				// ʹ���������������
				Sleep(20);
			}
			else
			{
				std::cout << "device error" << std::endl;
				return NULL;						// ���豸ʧ�ܣ����ش���
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
		return NULL;								// �����豸�б�ʧ�ܣ����ش���
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
	//TLI_GetDeviceListByTypeExt(serialNo, 30, 29);// ��ȡ�豸���к�
	//std::cout << "serial nos " << serialNo << std::endl;
	TLI_DeviceInfo deviceInfo;
	TLI_GetDeviceInfo(serialNo, &deviceInfo);

	if (PCC_Open(serialNo) == 0)		    // ���δ�3���豸����ͨ��
	{
		PCC_StartPolling(serialNo, 200);   // ������������λ�ú�״̬���ڲ���ѯѭ�� 200ms��ѯ����
		Sleep(20);
		// ����λ�ÿ���ģʽ 1��������2���ջ���3������ƽ����4���ջ�ƽ��
		PCC_SetPositionControlMode(serialNo, PZ_ControlModeTypes::PZ_OpenLoop);
		Sleep(20);
		PCC_Enable(serialNo);				// ʹ���������������
		Sleep(20);
		std::cout << "open serial " << serialNo << std::endl;
	}
	else
	{
		std::cout << "device error" << std::endl;
		return false;						// ���豸ʧ�ܣ����ش���
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
	PCC_SetOutputVoltage(serialNo, v);				// ���������ѹ
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
