import os
import hashlib
import pickle
import pdb
import sys


def ui2pyCml(name):
    cml = 'activate Anaconda2'
    os.system(cml)
    cml = 'pyuic4 {}.ui -o {}UI.py'.format(name,name)
    print(cml)
    os.system(cml)

def isUI(file):
    if file.find('.') > 0:
        filesplit = file.split('.')
        name = filesplit[0]
        stye = filesplit[-1]
        if stye == 'ui':
            return name
    return False

def getFileHash(file):
    sha1 = hashlib.sha1()
    with open(file,'rb') as f:
        sha1.update(f.read())
    return sha1.hexdigest()

def loadDiffPick():
    try:
        with open('diff.pickle','rb') as f:
            difflist = pickle.load(f)
    except Exception:
        difflist = {}
    return difflist


def saveDiffPick(pick):
        with open('diff.pickle','wb') as f:
            # print('savePick',pick)
            pickle.dump(pick,f)


if __name__ == '__main__':
    sys.path.append("..")
    for file in os.listdir():
        name = isUI(file)
        # pdb.set_trace()
        if name:
            difflist = loadDiffPick()
            shanum = getFileHash(file)
            if file in difflist.keys():
                print(file,'\n',difflist[file],'\n',shanum)
                if difflist[file] != shanum:
                    difflist[file] = shanum
                    ui2pyCml(name)
            else:
                difflist[file] = shanum
                ui2pyCml(name)
    saveDiffPick(difflist)

