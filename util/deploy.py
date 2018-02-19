#coding:utf-8
import os
import pdb
import re
import shutil

IGNORE_RULE_STARTS = (".idea", "IMG", '.git',
                      '.cache', "tests", "dist", "build", "VSProject")
IGNORE_RULE_ENDS = (".pyc", ".pdf")
fulls = (("tests", "data"), ("SDK", "MindPyScript"), ("SDK", "OceanOpticsScript"))
IGNORE_RULE_FULLS = {".".join(f) for f in fulls}
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def relative_full_path(root):
    u"""
    :param root:源路径
    :return full_paths：完整的路径列表
     迭代的递归所有的路径，并拼接成完整路径。
     迭代过程中根据规则做过滤。
    """
    full_paths = []
    dirs = os.listdir(root)
    for d in dirs:
        full = os.path.join(root, d)
        if is_ignore(full, d,
                     IGNORE_RULE_STARTS, IGNORE_RULE_ENDS, IGNORE_RULE_FULLS):
            continue
        if os.path.isfile(full):
            full_paths.append(full)
        elif os.path.isdir(full):
            fulls = relative_full_path(full)
            full_paths.extend(fulls)
    return full_paths


def is_ignore(full, path, starts, ends, fulls):
    for ig in starts:
        if path.startswith(ig):
            return True
    for ig in ends:
        if path.endswith(ig):
            return True
    for f in fulls:
        if re.findall(f, full):
            return True


def copy_to_path(paths, direction):
    u"""
    :param paths: 源地址
    :param direction: 目标地址
    :return:
    shutil是一个文件操作库，操作相对路径容易失败，因此输入拼接完整的路径。
    """
    for path in paths:
        target_dir = os.path.join(direction, path)
        print 'from', path, '\nto', target_dir
        try:
            shutil.copy(path, target_dir)
        except IOError:
            os.makedirs(os.path.dirname(target_dir))
            shutil.copy(path, target_dir)


# file0 = "view\\view.py"
# file1 = "view.py"
# file2 = "GUI\\view\\view.py"
if __name__ == '__main__':
    u"""执行部署脚本，基本功能是将代码拷到u盘，流程如下
    1、获取所有代码完整路径。
    2、打印路径。
    3、目标文件夹
    4、复制到目标文件夹。"""
    paths = relative_full_path(".")
    for p in paths:
        print p
    direction = "G:\\cvcx3_0"
    copy_to_path(paths, direction)

