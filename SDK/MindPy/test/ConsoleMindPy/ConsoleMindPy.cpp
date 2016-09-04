// ConsoleMindPy.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "MindPy.h"


int main()
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
    return 0;
}

