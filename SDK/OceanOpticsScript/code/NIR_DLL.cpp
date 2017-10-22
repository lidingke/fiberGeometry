// NIR_DLL.cpp : 定义 DLL 应用程序的导出函数。
//

//#include "stdafx.h"
#include "NIR_DLL.h"

#pragma comment(lib,"common32.lib")								// 引用库
#pragma comment(lib,"OmniDriver32.lib")


Wrapper* pWrapper = NULL;


void GetInstance(void)
{
	if (pWrapper == NULL)										// 判断是否第一次调用
	{
		pWrapper = new Wrapper( );
	}
}


NIR_DLL_API bool openSpectrometers(void)						// 查找连接的所有光谱仪
{
	int	numberOfSpectrometers;									// 连接的光谱仪数量
	GetInstance( );

	numberOfSpectrometers = pWrapper->openAllSpectrometers( );	// 查找连接的所有光谱仪

	if (numberOfSpectrometers <= 0)								// 没有发现光谱仪
	{
		return 0;
	}
	else
	{
		return 1;
	}
}


NIR_DLL_API void setIntegrationTime(int integrationTime)
{
	GetInstance( );
	/*---------------------------------------------------------------------------------------------------------------
	*光谱仪积分时间。第一个参数为光谱仪索引号，第二个参数表示光谱仪积分时间ms
	*---------------------------------------------------------------------------------------------------------------*/
	pWrapper->setIntegrationTime(0, integrationTime);			// 设置光谱仪积分时间。
}


NIR_DLL_API void setBoxcarWidth(int n)
{
	GetInstance( );
	/*---------------------------------------------------------------------------------------------------------------
	*平滑光谱的像素值（降低噪声）。光谱中的每个像素都与它两边的N个像素平均
	*第一个参数为光谱仪索引号，第二个参数表示 像素与它每边N个像素平均
	*---------------------------------------------------------------------------------------------------------------*/
	pWrapper->setBoxcarWidth(0, n);								// 像素平滑
}



NIR_DLL_API void setScansToAverage(int n)
{
	GetInstance( );
	/*---------------------------------------------------------------------------------------------------------------
	*平均法。光谱降低噪的另一种方法。多个连续的光谱平均生成平均谱。  如果积分时间较长，或者平均数量较大，可能要很长时间来计算
	*第一个参数为光谱仪索引号。第二个参数表示 多少个像素平均，设置为1则不执行。
	*例如设置为5，则pixel[0]的值为pixel[0]~pixel[4]的和再除以5
	*---------------------------------------------------------------------------------------------------------------*/
	pWrapper->setScansToAverage(0, n);							// 扫描平均
}



NIR_DLL_API void setCorrectForDetectorNonlinearity(bool x)
{
	GetInstance( );
	/*---------------------------------------------------------------------------------------------------------------
	*非线性校正。将CCD阵列的所有像素平均化，实现非线性校正。第一个参数为光谱仪索引号，第二个参数使能
	*---------------------------------------------------------------------------------------------------------------*/
	pWrapper->setCorrectForDetectorNonlinearity(0, x);			// 非线性校正
}


NIR_DLL_API void setCorrectForElectricalDark(bool x)
{
	GetInstance( );
	/*---------------------------------------------------------------------------------------------------------------
	*暗噪声校正。第一个参数为光谱仪索引号，第二个参数使能
	*---------------------------------------------------------------------------------------------------------------*/
	pWrapper->setCorrectForElectricalDark(0, x);				// 暗噪声校正
}



NIR_DLL_API void setStrobe(bool x)
{
	GetInstance( );
	/*---------------------------------------------------------------------------------------------------------------
	*以下两个函数必须成组使用。
	*开启频闪灯。在每次光谱采集时自动使能，然后自动关闭。可以延长频闪灯的寿命。第一个参数为光谱仪索引号，第二个参数使能
	*---------------------------------------------------------------------------------------------------------------*/
	pWrapper->setStrobeEnable(0, x);							// 设置频闪使能
	pWrapper->setAutoToggleStrobeLampEnable(0, x);				// 频闪灯自动触发使能
}



NIR_DLL_API void closeSpectrometers(void)
{
	GetInstance( );
	pWrapper->closeAllSpectrometers();							// 关闭所有连接的光谱仪
}



NIR_DLL_API bool getSpectrum(double **wavelengths, double **spectrum, int *number)
{
	DoubleArray wavelengthArray;								// 波长
	DoubleArray spectrumArray;									// 光谱 

	GetInstance( );
	spectrumArray = pWrapper->getSpectrum(0);					// 获取光谱
	if (pWrapper->getWrapperExtensions().isSpectrumValid(0) == false)
	{
		return 0;												// 获取光谱出错
	}
	else
	{
		wavelengthArray = pWrapper->getWavelengths(0);			// 获取波长
		*number = spectrumArray.getLength();					// 光谱的像素数

		*wavelengths = wavelengthArray.getDoubleValues();		// 指向波长值数组的指针
		*spectrum = spectrumArray.getDoubleValues();			// 指向光谱值数组的指针
		return 1;
	}
}



