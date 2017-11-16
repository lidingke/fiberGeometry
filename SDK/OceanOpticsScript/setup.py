from distutils.core import setup, Extension
import numpy

npinclude = numpy.get_include()
print "get np include:\n", npinclude
module = Extension('pynir', sources=['pynir.cpp'],
        include_dirs=[npinclude,],
        libraries=['NIR_DLL']
        )#,
        # library_dirs
setup(name= 'pynir',
      version= '1.1',
        ext_modules = [module])