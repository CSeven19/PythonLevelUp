# -*-coding:gbk-*-
# Run as:  
#    python setup.py build_ext --inplace  

import sys
from distutils.msvc9compiler import query_vcvarsall

sys.path.insert(0, "..")

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = cythonize("Simulate.pyx")

setup(
    ext_modules=ext_modules,
    # vc_env = query_vcvarsall(17.0, 'x64')
) 