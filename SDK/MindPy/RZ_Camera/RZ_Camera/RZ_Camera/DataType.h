
// datatype.h

#ifndef DATATYPE_H
#define DATATYPE_H
//#define __stdcall      __stdcall
/*===========================================================*\
	AE/AWB�ص�����	dw1			����AE/AWB֮��Ĳ���, 
					dw2			����AE/AWB֮��Ĳ���, 
					lpContext	������֡�ص�����ʱ���ݵ�������

2011-04-12 �ûص�������ʽ�������豸�Ƴ��������Ϣ�Ļص�
dw1 ��ʾ�豸������Ƴ�  0���Ƴ�;1������
dw2 ��ʾ�豸�ľ��,ǿ��ת��
\*=========================================================//*/
//typedef VOID (__stdcall *DL_AUTOCALLBACK )(unsigned long dw1, unsigned long dw2, LPVOID lpContext );

/*===========================================================*\
	֡�ص�����	lpParamָ��֡���ݵ�ָ��, 
				lpPoint ����, 
				lpContext������֡�ص�����ʱ���ݵ�������
\*=========================================================//*/
//typedef VOID (__stdcall *DL_FRAMECALLBACK)( LPVOID lpParam1, LPVOID lpPoint, LPVOID lpContext );


/*-------------------------------------------------------------
	����ֵ����
  *===========================================================*/
#define		ResSuccess					0x0000		// ���سɹ�
#define		ResNullHandleErr			0x0001		// ��Ч���
#define		ResNullPointerErr			0x0002		// ָ��Ϊ��
#define		ResFileOpenErr				0x0003		// �ļ�����/��ʧ��
#define		ResNoDeviceErr				0x0004		// û�п����豸
#define		ResInvalidParameterErr		0x0005		// �ڴ���䲻��
#define		ResOutOfMemoryErr			0x0006		// û�п���Ԥ��
#define		ResNoPreviewRunningErr		0x0007		// Ԥ��û�п���
#define		ResOSVersionErr				0x0008
#define		ResUsbNotAvailableErr		0x0009
#define		ResNotSupportedErr			0x000a
#define		ResNoSerialString			0x000b
#define		ResVerificationErr			0x000c
#define		ResTimeoutErr	            0x000d		
#define		ResScaleModeErr				0x000f
#define		ResUnknownErr				0x00ff

#define		ResDisplayWndExist			0x0011		// Ӧ�ùر�Ԥ������
#define		ResAllocated				0x0012		// �ڴ��Ѿ�����
#define		ResAllocateFail				0x0013		// �ڴ����ʧ��
#define		ResReadError				0x0014      // USB��ȡʧ��
#define		ResWriteError				0x0015		// USB�����ʧ��
#define		ResUsbOpen					0x0016      // USB�˿��Ѿ���
#define     ResCreateStreamErr			0x0017		// ����avi��ʧ��
#define     ResSetStreamFormatErr		0x0018		// ����AVI����ʽʧ��


typedef struct _tagDLVIDEORECT
{
	int     Left;		// ����ڸ����ڵ�ˮƽƫ��
	int     Top;		// ����ڸ����ڵĴ�ֱƫ��
	int     Width;		// ��Ƶ���ڿ��
	int     Height;		// ��Ƶ���ڸ߶�
}DLVIDEORECT, *PDLVIDEORECT;

/*-------------------------------------------------------------
	����ͷ��ز����ṹ
  *===========================================================*/
struct CapInfoStruct 
{
	unsigned char	*Buffer;		// �û����䣬���ڷ���8bitԭʼ����
	unsigned long	Height;			// �ɼ��߶�
	unsigned long	Width;			// �ɼ����
	unsigned long	OffsetX;		// ˮƽƫ��,	CCD�������
	unsigned long	OffsetY;		// ��ֱƫ��,	CCD�������
	unsigned long	Exposure;		// �ع�ֵ 1-500MS
	unsigned char	Gain[3];		// Gain[0]�������� 1-63. Gain[1],Gain[2]����
	unsigned char	Control;		// ����λ
	unsigned char	InternalUse;	// �û���Ҫ�Դ��ֽڽ��в���
	unsigned char	ColorOff[3];	// �û������治Ҫ�ı�������ֵ
	unsigned char	Reserved[4];	// ����λ
};
//CapInfoStruct m_tCamerParam;
/*-----------------------------------------------------------
	Control ����λ˵��
	BIT7       BIT6      BIT5     BIT4     BIT3     BIT2     BIT1     BIT0
	�û�IO	����Դʹ��								HDR    	 ����	  �ü�/����
	0�͵�ƽ   0										 0		 0			0�ü�
	1�ߵ�ƽ	  1										 1����	 1 �����ɼ�	1����	
  ===========================================================*/


/*-------------------------------------------------------------
	��ɫģʽ
  *===========================================================*/
enum	COLOR_MODE {
					COLOR_RGB24,
					COLOR_RGB24_CLEAR,
					COLOR_BW24,
					COLOR_GRAY,
					COLOR_RAWDATA,
					COLOR_Microscope	//��ɫУ��ģʽ(��΢��ģʽ)
				};


/*-------------------------------------------------------------
	��תģʽ Ŀǰ����RGB24,BW24��Ч
  *===========================================================*/
enum	FLIP_MODE {	
					FLIP_NATURAL,		// ������ʾ
					FLIP_LEFTRIGHT,	    // ���ҷ�ת
					FLIP_UPDOWN,			// ���·�ת
					FLIP_ROTATE180,		// ��ת180
					FLIP_ROTATE90,
					FLIP_ROTATE270
				};

enum	RZIMAGETYPR {  
						BMP,		// ����ͼ���ʽ���� 
					    JPEG,	    // 
					};

enum	RZCAMERA{	RZUNKOWN,		//�������
					RZ130,			
					RZ300,
					RZ130CF,
					RZ200CF,
					RZ300CF,
					RZ500CF,
					RZ900CF,
					RZ500P,			//
					RZ130C_1_3,
					RZ36M,
					RZ300C_FPGA,
					RZ130C_FPGA,
					RZ130M_FPGA,
					RZ80C_SP16,
					RZ130SC_YUV,
					RZ120C_FPGA,
					RZ300_LED,
					RZTEST,
					RZF1400CF,
					RZF1000CF,
					RZ50C,
					RZCCD140C,
					RZUL200MFG,
					MicroUH1200C,
					RZTRIGGER,
					MicroUH600C,
					SuperUH500,
					MicroUH300C,
					SuperUH130,
					SuperUH200,
					SuperUH50,
					SuperUH30
				};

enum	RZ_COLOR_TYPE{
					RZ_COLOR,
					RZ_GRAY
				};


enum COLOR_ADJUST_TYPE {					
					COLOR_ADJUST_NO,	//
					COLOR_ADJUST_COLD,	//��ɫ����
					COLOR_ADJUST_WARM	//ůɫ����
				};

//�Զ��ع�����Ч������
enum	RZ_AE_LEVEL
{
		RZ_AE_LEVEL_HIGH,	//����
		RZ_AE_LEVEL_NORMAL,	//����
		RZ_AE_LEVEL_LOW		//����
};

#endif