#ifdef NIR_DLL_EXPORTS
#define NIR_DLL_API __declspec(dllexport)
#else
#define NIR_DLL_API __declspec(dllimport)
#endif

// �����ĺ���
NIR_DLL_API bool openSpectrometers(void);								// �򿪹����ǣ��ɹ�����1��ʧ�ܷ���0
NIR_DLL_API void setIntegrationTime(int integrationTime);				// ���ù����ǻ���ʱ��(���磺100ms,������ֵ100000��
NIR_DLL_API void setBoxcarWidth(int n);									// ƽ�����׵�����ֵ�������������������е�ÿ�����ض��������ߵ�N������ƽ��
NIR_DLL_API void setScansToAverage(int n);								// ɨ��ƽ��,��������Ĺ���ƽ������ƽ���ס� �������ʱ��ϳ�������ƽ�������ϴ󣬿���Ҫ�ܳ�ʱ��������
NIR_DLL_API void setCorrectForDetectorNonlinearity(bool x);				// ������У����
NIR_DLL_API void setCorrectForElectricalDark(bool x);					// ������У����
NIR_DLL_API void setStrobe(bool x);										// ����Ƶ���ơ�
NIR_DLL_API void closeSpectrometers(void);								// �رչ����ǡ�
NIR_DLL_API bool getSpectrum(double **wavelengths, double **spectrum, int *number);				// ��ù��ף��ɹ�����1��ʧ�ܷ���0��
