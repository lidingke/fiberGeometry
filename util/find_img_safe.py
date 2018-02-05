import os
import shutil
import re
import pdb

TESTS_PATH = "./tests/"
IMG_PATH = "IMGold"
TARGET_PATH = "IMGold/old/"
INIT_PATHS = ['thr.png', '500edge.bmp', 'G652\\pk\\',
              "\\emptytuple\\eptlight0\\", "\\sharp\\oc1\\",
              "\\midoc.BMP"]


def get_img_paths(init_path, path_to_search):
    paths = []
    paths.extend(init_path)

    filenames = os.listdir(path_to_search)
    for filename in filenames:
        if filename.endswith(".py"):
            with  open(path_to_search + filename, 'rb') as file:
                read = file.read()
                way = r"\"IMG(.*?)\""
                img_way = re.compile(way)
                imgnames = img_way.findall(read)
                if imgnames:
                    for imgname in imgnames:
                        paths.append(imgname)
    return set(paths)


def files_form_dirs(img_paths, path_from):
    files = []
    for path in img_paths:
        path = path.replace('\\\\', '\\')
        __ = [path_from] + path.split('\\')
        path = os.path.join(*__)
        files.append(path)
    return files


def all_dirs_to_full_file_path(paths):
    files = []
    for path in paths:
        if os.path.isfile(path):
            files.append(path)
        elif os.path.isdir(path):
            endswiths = ('BMP', 'bmp', 'png')
            _ = [path + i for i in os.listdir(path) if i[-3:] in endswiths]
            files.extend(_)
        else:
            raise IOError(path)
    return set(files)


def safe_copy_file(paths, dir_):
    for path in paths:
        target_dir = dir_ + path
        print 'from', path, '\nto', target_dir
        try:
            shutil.copy(path, target_dir)
        except IOError:
            os.makedirs(os.path.dirname(target_dir))
            shutil.copy(path, target_dir)


if __name__ == '__main__':
    img_paths = get_img_paths(INIT_PATHS, TESTS_PATH)
    files = files_form_dirs(img_paths, IMG_PATH)
    files = all_dirs_to_full_file_path(files)
    safe_copy_file(files, TARGET_PATH)
    pdb.set_trace()
