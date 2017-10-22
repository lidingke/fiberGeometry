#coding:utf-8
import xlwt
import xlrd

def save2xlsx(file_name,datas):
    workbook = xlrd.open_workbook(file_name)
    sheets = workbook.sheet_names()
    sheet_name = u"sheet{}".format(len(sheets)+1)
    print "sheet",sheet_name
    workbook = xlwt.Workbook()
    #
    booksheet = workbook.add_sheet(sheet_name)

    for i, row in enumerate(datas):
        for j, col in enumerate(row):
            booksheet.write(i, j, col)
    workbook.save(file_name)


def test_save2xlsx():
    file_ = u"..\\report\\重复性20400_20170828\\test.xls"
    datas = (
        (u"1",u"2"),
        (u"3",u"4")
    )
    save2xlsx(file_,datas)
