from distutils.core import setup, Extension
import numpy

npinclude = numpy.get_include()
omninclude = "C:\Program Files (x86)\Ocean Optics\OmniDriverSPAM\include"
print "get np include:\n", npinclude,"\n",omninclude
module = Extension('pynir', sources=['pynir.cpp'],
        include_dirs=[npinclude,omninclude],
        libraries=['NIR_LIB.lib']
        )#,
        # library_dirs
setup(name= 'pynir',
      version= '1.1',
        ext_modules = [module])