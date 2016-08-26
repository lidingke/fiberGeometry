import pdb

with open('doth\\definePara.h', 'rb') as f:
    origin = f.readlines()
splited = [' '.join(s.split()) for s in origin]
eachLine = [x.split() for x in splited]
lines = []
for index, value in enumerate(eachLine):
    print index, len(value)
    if len(value) > 5:
        pdb.set_trace()
    line = "%s = %s #%s\r\n" % (value[1], value[2], value[3])
    lines.append(line)

with open('definepy.py', 'wb') as f:
    f.writelines(lines)

# print origin
