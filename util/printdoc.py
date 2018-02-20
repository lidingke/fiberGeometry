# coding:utf-8
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


multi_lines = []
multi_flag = False


class FilterPath(object):

    def __init__(self):
        self.multi_lines = []
        self.multi_flag = False

    def filter_lines(self, line):
        line = line.strip()
        if line.startswith("#"):
            return
        if self.multi_flag:
            self.multi_lines.append(line)
            if line.endswith("""\"\"\""""):
                multi_line = "    \n".join(self.multi_lines)
                self.multi_lines = []
                self.multi_flag = False
                return multi_line
        else:
            if line.startswith("class"):
                return line
            if line.startswith("def"):
                return "  " + line
            if line.startswith("""\"\""""):
                if line.endswith("""\"\"\""""):
                    return "  " + line
                else:
                    self.multi_flag = True
                    self.multi_lines.append(line)

            if line.startswith("u\"\""):
                if line.endswith("\"\"\""):
                    return "  " + line
                else:
                    self.multi_flag = True
                    self.multi_lines.append(line)

    def run(self, path):
        with open(path) as f:
            lines = f.readlines()
            filtered_lines = [self.filter_lines(l) for l in lines if l != None]
            return filtered_lines


if __name__ == '__main__':
    # pdb.set_trace()
    paths = relative_full_path(".")
    lines_length = 0
    for path in paths:
        # fs =
        fs = FilterPath().run(path)
        lines_length += len(fs)
        for f in fs:
            if f:
                print(f)
    print("lens:{}".format(lines_length))
    # 9508
