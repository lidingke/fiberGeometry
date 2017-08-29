#coding=utf-8
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('report', 'template'),
    autoescape=select_autoescape(['html', 'xml'])
)


template = env.get_template('template.html')

x= template.render(
    title=u'测试',
    worker= '1',
    fibertype= '2',
    producer= '3',
    fiberNo='4',
    corediameter= '5',
    claddiameter= '6',
    coreroundness= '7',
    cladroundness= '8',
    concentricity= '9',
    sharpindex='10',
    lightindex= '11',
    date='12',
    fiberLength= '13',
    src="img\img.jpg"
)

print x
print type(x)
# x=str(x)
# y=x.decode("utf-8")
# print y
# print type(y)