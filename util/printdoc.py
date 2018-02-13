#coding:utf-8
import os
import pdb
import re

IGNORE_RULE_STARTS = (".idea", "IMG", '.git',
                      '.cache', "dist", "build", "VSProject")
IGNORE_RULE_ENDS = (".pyc", ".pdf")
fulls = (("tests", "data"), ("SDK", "MindPyScript"), ("SDK", "OceanOpticsScript"))
IGNORE_RULE_FULLS = {".".join(f) for f in fulls}
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def is_py(root):
    # pdb.set_trace()
    if root.endswith('.py'):
        return True
    else:
        return False

def relative_full_path(root):
    full_paths = []
    dirs = os.listdir(root)
    for d in dirs:
        full = os.path.join(root, d)
        if is_ignore(full, d,
                     IGNORE_RULE_STARTS, IGNORE_RULE_ENDS, IGNORE_RULE_FULLS):
            continue

        if os.path.isfile(full) and is_py(full):
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

def filter_path(path):
    def filter_lines(line):
        line = line.strip()
        if line.startswith("class"):
            return line
        if line.startswith("def"):
            return "  "+line
        if line.startswith("""\"\"\""""):
            return "  "+line
        if line.startswith("""u\"\"\""""):
            return "  "+line

    with open(path) as f:
        lines = f.readlines()
        filtered_lines = [filter_lines(l) for l in lines if l != None]
        return filtered_lines


if __name__ == '__main__':
    paths = relative_full_path(".")
    for path in  paths:
        fs = filter_path(path)
        for f in fs:
            if f:
                print(f)