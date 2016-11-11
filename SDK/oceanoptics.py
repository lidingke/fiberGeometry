#coding:utf-8
import  xlrd
import numpy as np
import pdb
class OceanOpticsTest(object):

    def __init__(self):
        pass

    def getData(self, length):
        # print 'get data'
        data = xlrd.open_workbook('SDK\\OceanOpticsScript\\20160920.xlsx')
        # table = data.sheet_by_name(u'25公里 200um狭缝')
        table = data.sheets()[0]
        wave = table.col_values(0)
        before = table.col_values(3)
        after = table.col_values(5)
        powers = []
        for x,y in zip(before, after):
            if y < 0:
                power = 0.0
            else:
                power = 10 * np.log10(x/y)/length
            # print 'power',x ,y ,power
            powers.append(power)
        return (wave, powers)