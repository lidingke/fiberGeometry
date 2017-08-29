from PyQt4.QtCore import QString

from setting.config import PDF_PARAMETER
from jinja2 import Environment, PackageLoader, select_autoescape
from PyQt4.QtGui import QTextDocument, QPrinter, QApplication

def test_write_mypdf():
    env = Environment(
        loader=PackageLoader('report', 'template'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    PDF_PARAMETER={'title':'0',
    'worker': '1',
    'fibertype': '2',
    'producer':'3',
    'fiberNo':'4',
    'corediameter': '5',
    'claddiameter': '6',
    'coreroundness': '7',
    'cladroundness': '8',
    'concentricity': '9',
    'sharpindex':'10',
    # 'lightindex': '11',
    'date':'12',
    'fiberLength': '13'}

    template = env.get_template('template.html')

    myhtml = template.render(
        title=PDF_PARAMETER['title'],
        worker=PDF_PARAMETER['worker'],
        fibertype=PDF_PARAMETER['fibertype'],
        producer=PDF_PARAMETER['producer'],
        fiberNo=PDF_PARAMETER['fiberNo'],
        corediameter=PDF_PARAMETER['corediameter'],
        claddiameter=PDF_PARAMETER['claddiameter'],
        coreroundness=PDF_PARAMETER['coreroundness'],
        cladroundness=PDF_PARAMETER['cladroundness'],
        concentricity=PDF_PARAMETER['concentricity'],
        sharpindex=PDF_PARAMETER['sharpindex'],
        # lightindex=PDF_PARAMETER['lightindex'],
        date=PDF_PARAMETER['date'],
        fiberLength=PDF_PARAMETER['fiberLength']
        # src="img\img.jpg"
    )
    printer = QPrinter()
    printer.setOutputFormat(QPrinter.PdfFormat)
    # printer.setOutputFileName(dir_)
    printer.setPageSize(QPrinter.A4)
    text = QTextDocument()
    myhtmls = unicode(myhtml, 'utf-8', 'ignore').decode("utf-8")
    # myhtml = myhtml
    text.setHtml(QString(myhtmls))
    text.print_(printer)