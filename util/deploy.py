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
    paths = relative_full_path(".")
    for p in paths:
        print p
    direction = "G:\\cvcx3_0"
    copy_to_path(paths, direction)

