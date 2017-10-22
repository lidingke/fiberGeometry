#ifdef NIR_DLL_EXPORTS
#define NIR_DLL_API __declspec(dllexport)
#else
#define NIR_DLL_API __declspec(dllimport)
#endif

// 导出的函数
NIR_DLL_API bool openSpectrometers(void);								// 打开光谱仪，成功返回1，失败返回0
NIR_DLL_API void setIntegrationTime(int integrationTime);				// 设置光谱仪积分时间(例如：100ms,则设置值100000）
NIR_DLL_API void setBoxcarWidth(int n);									// 平滑光谱的像素值（降低噪声）。光谱中的每个像素都与它两边的N个像素平均
NIR_DLL_API void setScansToAverage(int n);								// 扫描平均,多个连续的光谱平均生成平均谱。 如果积分时间较长，或者平均数量较大，可能要很长时间来计算
NIR_DLL_API void setCorrectForDetectorNonlinearity(bool x);				// 非线性校正。
NIR_DLL_API void setCorrectForElectricalDark(bool x);					// 暗噪声校正。
NIR_DLL_API void setStrobe(bool x);										// 开启频闪灯。
NIR_DLL_API void closeSpectrometers(void);								// 关闭光谱仪。
NIR_DLL_API bool getSpectrum(double **wavelengths, double **spectrum, int *number);				// 获得光谱，成功返回1，失败返回0。
