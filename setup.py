from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("_stm", ["_stm.pyx"])]

setup(
  name = 'Software Transactional Memory',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
