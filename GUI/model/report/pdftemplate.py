#coding:utf-8
originHTML =  '''
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <style>{mystyle}</style>
    <title>{title}</title>
</head>
<body>
    <h1 id="_1">{title}</h1>
    <h2 id="_2">测 试 人 员</h2>
    <p>日 期：{date}
        <br /> 操 作 人：{worker}
        <br /> 光 纤 型 号：{fibertype}
        <br /> 生 产 厂 家：{producer}
        <br /> 光 纤 编 号：{fiberNo}
        <br /> 光 纤 长 度：{fiberLength}
    </p>
    <h2 id="_2">测 试 结 果</h2>
    <p> 纤 芯 直 径：{corediameter}
        <br /> 包 层 直 径：{claddiameter}
        <br /> 纤 芯 不 圆 度：{coreroundness}
        <br /> 包 层 不 圆 度：{cladroundness}
        <br /> 芯 包 同 心 度: {concentricity}
    </p>
    <h2 id="_3">测 试 参 数</h2>
    <p>清 晰 度 指 数：{sharpindex}
        <br /> 纤 芯 饱 和 度 指数：{corelight}
        <br /> 包 层 饱 和 度 指数：{cladlight}
        <br /></p>
</body>
</html>'''
with open('setting\\report.css') as f:
    mystyle = f.readlines()
mystyle = ''.join(mystyle)

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
    'corelight': '',
    'cladlight': '',
    'date': '',
    'fiberLength': '',
    'mystyle':mystyle
}

