# 用于.pyx文件编译成C文件
# 'dot_cython' 是我们要生成的动态链接库的名字
# sources 里面可以包含 .pyx 文件，以及后面如果我们要调用 C/C++ 程序的话，还可以往里面加 .c / .cpp 文件
# language 其实默认就是 c，如果要用 C++，就改成 c++ 就好了
# include_dirs 这个就是传给 gcc 的 -I 参数
# library_dirs 这个就是传给 gcc 的 -L 参数
# libraries 这个就是传给 gcc 的 -l 参数
# extra_compile_args 就是传给 gcc 的额外的编译参数，比方说你可以传一个 -std=c++11
# extra_link_args 就是传给 gcc 的额外的链接参数（也就是生成动态链接库的时候用的）
# 如果你从来没见过上面几个 gcc 参数，说明你暂时还没这些需求，等你遇到了你就懂了
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy
setup(ext_modules = cythonize(Extension(
    'dot_cython',
    sources=['dot_cython.pyx'],
    language='c',
    include_dirs=[numpy.get_include()],
    library_dirs=[],
    libraries=[],
    extra_compile_args=[],
    extra_link_args=[]
)))