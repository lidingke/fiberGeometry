#coding=utf-8
import pdb
import re

class Struct2ctypes(object):
    """docstring for Struct2ctypes"""
    def __init__(self, ):
        super(Struct2ctypes, self).__init__()
        self._typesdict()

    def method(self):
        with open('doth\\struct.h', 'rb') as f:
            origin = f.readlines()
        print 'lines number', len(origin)
        annotation = []
        astruct = []
        for x in origin:
            if x.find('struct') != -1:
                annotation.append(astruct)
                astruct = []
                # pdb.set_trace()
            astruct.append(x)
        # pdb.set_trace()
        annotation.append(astruct)
        print 'len annotation', len(annotation)
        allcontext = []
        for x in annotation[1:]:
            name ,context = self.typedefContextGet(x)
            context = self._structHead(name, context)
            # context =
            allcontext.append(context)
        flattened = [val for sublist in allcontext for val in sublist]
        with open('structtest.py', 'wb') as f:
            f.writelines(flattened)


    def typedefContextGet(self, origin):
        # print 'origin', origin
        print '------------------------ line ',len(origin)
        splited = [' '.join(s.split()) for s in origin]
        structFinded = self._isExist(splited,'struct')
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
            context = self.eachLine(splited[head : end])
        print splited[end]
        context[-1] = self._tailExchange(context[-1])

        return (name, context)


    def eachLine(self, context):
        allcontext = []
        for line in context:
            # print 'line', line
            # pdb.set_trace()
            if line.find(';') <= 0:
                continue
            cmdline, comments = line.split(';', 1)
            if comments.find('//') > 0:
                null, comments = comments.split('//', 1)
            comments = comments.decode('utf-8').encode('gbk')
            if cmdline.find('*') > 0:
                isPointer = True
                cmdline = cmdline.replace('*', ' ')
                # cmdline = ' '.join(cmdline.split())
            else:
                isPointer = False
            if cmdline.find('[') > 0:
                isArray = True
                arrayLen = ''.join(re.findall('[(\d+)]', cmdline))
                cmdline = cmdline[:cmdline.find('[') - 1]
            else:
                isArray = False
            # pdb.set_trace()
            try:
                dataType, dataName = cmdline.split()
            except Exception, e:
                # raise e
                pdb.set_trace()

            #处理
            if isArray == True:
                dataType = dataType + ' * ' + arrayLen
            if isPointer == True:
                dataType = 'pointer(' + dataType + ')'
            typesGet = self.types.get(dataType, '-1')
            if typesGet != '-1':
                dataType = typesGet
            aline = '''    ("%s", %s), #%s\n''' % (dataName, dataType, comments)
            allcontext.append(aline)
        return allcontext

    def _structHead(self, name, context):
        line1 = "\r\nclass %s(Structure):\r\n" % name.split()[0]
        line2 = "    _fields_ = [\r\n"
        lineEnd = "    \r\n"
        return [line1] + [line2] + context + [lineEnd]

    def _tailExchange(self, str_):
        splited = str_.split('#', 1)
        return splited[0].replace('),', ')] # ') + splited[1]

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


    def _typesdict(self):
        self.types = {
        'INT': 'c_int',
        'UINT': 'c_uint',
        'char': 'c_char',
        'BOOL': 'c_bool',
        'float': 'c_float',
        'BYTE': 'c_byte'
        }

if __name__ == '__main__':
    s2c = Struct2ctypes()
    s2c.method()
