from distutils.core import setup, Extension
import numpy
import os
path = os.getcwd()
scriptpath = path+'\\MindPyScript\\MindPyCEx\\'
print scriptpath
npinclude = numpy.get_include()
print npinclude
module = Extension('MindPy', sources=[scriptpath + 'MindPy.cpp'],
        include_dirs=[npinclude,scriptpath + 'Include'],
        library_dirs=[scriptpath + 'Lib'],
        libraries=[scriptpath + 'MVCAMSDK', scriptpath + 'MVCAMSDK_X64']
        )#,
        # library_dirs
setup(name= 'MindPyEx',
      version= '1.0',
      # py_modules=['mindpyex'],
        ext_modules = [module])


# workon cv2
# SET VS90COMNTOOLS=%VS140COMNTOOLS%
# python mindSetup.py build_ext --inplace