#coding=utf-8
import pdb
import re

class Enum2ctypes(object):
    """docstring for Enum2ctypes"""
    def __init__(self):
        super(Enum2ctypes, self).__init__()
        # self.arg = arg

    def method(self):
        with open('doth\\enum.h', 'rb') as f:
            origin = f.readlines()
        print 'lines number', len(origin)
        annotation = self._metaWordSplit(origin)
        allcontext = []
        for x in annotation[1:]:
            name, context = self.typedefContextGet(x)
            context = self.eachLine(context)
            context = self._structHead(name, context)
            context[-2] = self._tailExchange(context[-2])
            allcontext.append(context)
            flattened = [val for sublist in allcontext for val in sublist]
        defLines = '''def enum(**enums):
    return type('Enum', (), enums)\n\r
        '''
        flattened = [defLines] + flattened
        with open('enumtest.py', 'wb') as f:
            f.writelines(flattened)


    def typedefContextGet(self, origin):
        print '------------------------ line ',len(origin)
        splited = [' '.join(s.split()) for s in origin]
        structFinded = self._isExist(splited,'enum')
        if structFinded[0]:
            # begin = structFinded[1]
            headFinded = self._isExist(splited, '{')
            head =  headFinded[1] + 1
            endFinded = self._isExist(splited[::-1], '}')
            end = len(splited) - endFinded[1] - 1
            # print 'end',end, 'all', len(splited), '-1', splited[head: end][-1]
            name = self._returnName(splited[end])
            print 'name', name
            # pdb.set_trace()
            # context = self.eachLine(splited[head : end])
        # print splited[end]
        # context[-1] = self._tailExchange(context[-1])

        return (name, splited[head : end])

    def eachLine(self, context):
        allcontext = []
        for index, line in enumerate(context):

            if line.find('= 0') != -1:
                line = line.replace('= 0', '')
            try:
                cmdline, comments = line.split(',', 1)
            except ValueError:
                if line.find('//') != -1:
                    cmdline, comments = line.split('//', 1)
                    comments = '//' + comments
                else:
                    cmdline = line
                    comments = '#'
            except Exception, e:
                # raise e
                pdb.set_trace()
            if comments.find('//') > 0:
                null, comments = comments.split('//', 1)
            try:
                comments = comments.decode('utf-8').encode('gbk')
            except Exception, e:
                pdb.set_trace()
            # aline =
            aline = '%s = %d ,#%s\n\r' % (cmdline, index, comments)
            allcontext.append(aline)
        return allcontext

    def _tailExchange(self, str_):
        # if str_.find('#') != -1:
        #     return str_
        print 'str', str_
        splited = str_.split('#', 1)
        replaceed = splited[0].replace(' ,', ') # ')
        # pdb.set_trace()
        if len(splited) > 1:
            return replaceed + splited[1]
        else:
            return replaceed

    def _metaWordSplit(self,origin):
        annotation = []
        astruct = []
        for x in origin:
            if x.find('enum') != -1:
                annotation.append(astruct)
                astruct = []
                # pdb.set_trace()
            astruct.append(x)
        # pdb.set_trace()
        annotation.append(astruct)
        print 'len annotation', len(annotation)

        return annotation

    def _structHead(self, name, context):
        line1 = '''\n\r%s = enum(\n\r''' % name.split()[0]
        return [line1] + context + ['\n\r']

    def _returnName(self, name):
        name = name.replace('}', ' ')
        name = name.replace(';', ' ')
        name.split()
        return name

    def _isExist(self, lst, str_):
        '''if str in strings'''
        for index, item in enumerate(lst):
            try:
                item = item.split('//',1)[0]
            except Exception, e:
                pass
            if len(item) > len(str_):
                if item.find(str_) != -1:
                    return (True, index)
            else:
                if str_ == item:
                    return (True, index)
        return (False, -2)


if __name__ == '__main__':
    e2c = Enum2ctypes()
    e2c.method()
