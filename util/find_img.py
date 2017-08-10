# coding=utf-8
import re
import os
import shutil
import pdb

TESTS_PATH = "tests/"
IMG_PATH = "IMGold"
TARGET_PATH = "IMGold"

pathDir = os.listdir(TESTS_PATH)
print pathDir
# pathlist=[]
paths = ['/thr.png', '500edge.bmp', '/G652/pk/',
         "/emptytuple/eptlight0/", "/sharp/oc1/",
         "/midoc.BMP"]
# pathlist=[]

for filename in pathDir:
    if filename.endswith(".py"):
        with  open(TESTS_PATH + filename, 'rb') as file:

            read = file.read()
            way = r"\"IMG(.*?)\""
            img_way = re.compile(way)
            imgnames = img_way.findall(read)

            if imgnames:
                for imgname in imgnames:
                    paths.append(imgname)

paths = set(paths)
print paths
for get_path in paths:
    # print get_path
    if get_path:
        get_path = get_path.replace('\\\\', '\\')
        __ = [IMG_PATH] + get_path.split('\\')
        get_path = os.path.join(*__)
        __ = [TARGET_PATH] + get_path.split('\\')
        dir_ = os.path.join(*__)
        print 'dir:', get_path, ':', dir_
        if os.path.isfile(get_path):
            try:
                shutil.copy(get_path, dir_)
            except IOError:
                os.makedirs(os.path.dirname(dir_))
                shutil.copy(get_path, dir_)
        elif os.path.isdir(get_path):
            if os.path.exists(dir_):
                shutil.copytree(get_path, dir_)
        else:
            print 'error dir ', get_path

            # print(osget)
            # print(get_paths)
            # pdb.set_trace()
            # print set(pathlist)
