

#include "ArrayTypes.h" 
#include "Wrapper.h"
// �����ĺ���
bool openSpectrometers(void);								// �򿪹����ǣ��ɹ�����1��ʧ�ܷ���0
void setIntegrationTime(int integrationTime);				// ���ù����ǻ���ʱ��(���磺100ms,������ֵ100000��
void setBoxcarWidth(int n);									// ƽ�����׵�����ֵ�������������������е�ÿ�����ض��������ߵ�N������ƽ��
void setScansToAverage(int n);								// ɨ��ƽ��,��������Ĺ���ƽ������ƽ���ס� �������ʱ��ϳ�������ƽ�������ϴ󣬿���Ҫ�ܳ�ʱ��������
void setCorrectForDetectorNonlinearity(bool x);				// ������У����
void setCorrectForElectricalDark(bool x);					// ������У����
void setStrobe(bool x);										// ����Ƶ���ơ�
void closeSpectrometers(void);								// �رչ����ǡ�
bool getSpectrum(double **wavelengths, double **spectrum, int *number);				// ��ù��ף��ɹ�����1��ʧ�ܷ���0��
