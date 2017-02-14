from report.pdf import writePdf
import os

def test_write_pdf():
    writePdf("tests\\report")
    listdir = os.listdir("tests")
    # print listdir
    assert 'report.pdf' in listdir