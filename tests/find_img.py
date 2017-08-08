import re
import os

filepath = "E:/Python/newwork/tests"

pathDir = os.listdir(filepath)
# pathlist=[]
for filename in pathDir:
    if filename.endswith(".py"):
        file = open(filename, 'rb')
        try:
            read = file.read()
            # print read
            way = r"IMG.+[\\/]"
            img_way= re.compile(way)
            imgname = img_way.findall(read)

            if imgname:
                # str="".join(imgname)
                print (set(imgname))
                 # pathlist.append(",".join(imgname))
        finally:
            file.close()
# print set(pathlist)