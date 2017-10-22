from distutils.core import setup, Extension
import numpy

npinclude = numpy.get_include()
print npinclude
module = Extension('MindPy', sources=['MindPy.cpp'],
        include_dirs=[npinclude,'Include'],
        library_dirs=['Lib'],
        libraries=['MVCAMSDK','MVCAMSDK_X64']
        )#,
        # library_dirs
setup(name= 'MindPyEx',
      version= '2.0',
      # py_modules=['mindpyex'],
        ext_modules = [module])


