from distutils.core import setup, Extension
import numpy

npinclude = numpy.get_include()
print npinclude
module = Extension('MindPy', sources=['MindPy.cpp'],
        include_dirs=[npinclude]
        )#,
        # library_dirs
setup(ext_modules = [module])


