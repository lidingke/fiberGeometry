
//typedef struct special
//保存文件的格式类型
typedef enum
{
    FILE_JPG = 1,//JPG
    FILE_BMP = 2,//BMP 24bit
    FILE_RAW = 4,//相机输出的bayer格式文件,对于不支持bayer格式输出相机，无法保存为该格式
    FILE_PNG = 8, //PNG 24bit
    FILE_BMP_8BIT = 16,//BMP 8bit
    FILE_PNG_8BIT = 32, //PNG 8bit
    FILE_RAW_16BIT = 64
}emSdkFileType;

// 文字输出标志
typedef enum
{
    CAMERA_DT_VCENTER       = 0x1,      // 垂直居中
    CAMERA_DT_BOTTOM        = 0x2,      // 底部对齐
    CAMERA_DT_HCENTER       = 0x4,      // 水平居中
    CAMERA_DT_RIGHT         = 0x8,      // 右对齐
    CAMERA_DT_SINGLELINE    = 0x10,     // 单行显示
    CAMERA_DT_ALPHA_BLEND   = 0x20,     // Alpha混合
    CAMERA_DT_ANTI_ALIASING = 0x40,     // 抗锯齿
}emCameraDrawTextFlags;

//相机的配置参数，分为A,B,C,D 4组进行保存。
typedef enum
{
    PARAMETER_TEAM_DEFAULT = 0xff,
    PARAMETER_TEAM_A = 0,
    PARAMETER_TEAM_B = 1,
    PARAMETER_TEAM_C = 2,
    PARAMETER_TEAM_D = 3
}emSdkParameterTeam;
