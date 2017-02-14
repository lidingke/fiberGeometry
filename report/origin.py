#coding:utf-8
originHTML =  '''
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <style>
    body {{
        /*overflow-y:scroll;*/
        width: 45em;
        border: 1px solid #ddd;
        outline: 1300px solid #fff;
        margin: 16px auto;
        font-family: 'Microsoft YaHei', freesans, sans-serif;

    }}

    h1 {{
        border-bottom: 1px solid #eee;
        margin-top: 1em;
        margin-bottom: 16px;
        margin-left: 30px;
        margin: 0.67em 0;
        padding-left: 8px;
        padding-bottom: 0.3em;
        font-size: 50px;
        font-weight: bold;
        color: #283c51;
    }}

    h2 {{
        border-bottom: 1px solid #eee;
        padding-bottom: 0.3em;
        margin-left: 30px;
        padding-left: 20px;
        font-size: 40px;
        font-weight: bold;
        color: #2EA9DF;

    }}

    p {{
        padding-left: 20px;
        /*margin-left: 45px;
        font-size: 20px;*/
    }}

    img {{
        -moz-box-sizing: border-box;
        box-sizing: border-box;

    }}
    </style>
    <title>{title}</title>
</head>
<body>
    <h1 id="_1">{title}</h1>
    <p>日期：{date}
        <br /> 操作人：{worker}
        <br /> 光纤型号：{fibertype}
        <br /> 生产厂家：{producer}
        <br /> 光纤编号：{fiberNo}
        <br /> 光纤长度：{fiberLength}
    </p>
    <h2 id="_2">测试结果</h2>
    <p> 纤芯直径：{corediameter}
        <br /> 包层直径：{claddiameter}
        <br /> 纤芯不圆度：{coreroundness}
        <br /> 包层不圆度：{cladroundness}
        <br /> 芯包同心度: {concentricity}
    </p>
    <h2 id="_3">测试参数</h2>
    <p>清晰度指数：{sharpindex}
        <br /> 纤芯亮度指数：{lightindex}
        <br /></p>
</body>
</html>'''

htmlpara = {
    'title': '标题',
    'worker': '操作人',
    'fibertype': '光纤型号',
    'producer': '生产厂家',
    'fiberNo': '光纤编号',
    'corediameter': '纤芯直径',
    'claddiameter': '包层直径',
    'coreroundness': '',
    'cladroundness': '',
    'concentricity': '',
    'sharpindex': '',
    'lightindex': '',
    'date': '',
    'fiberLength': ''
}
