import cython
import numpy as np
cimport numpy as np
cimport cython


# Cython 程序的扩展名是 .pyx
# cimport 是 Cython 中用来引入 .pxd 文件的命令。有关 .pxd 文件，可以简单理解成 C/C++ 中用来写声明的头文件，更具体的我会在后面写到。这里引入的两个是 Cython 预置的。
# @cython.boundscheck(False) 和 @cython.wraparound(False) 两个修饰符用来关闭 Cython 的边界检查
# Cython 的函数使用 cdef 定义，并且他可以给所有参数以及返回值指定类型。比方说，我们可以这么编写整数 min 函数：

# 1.1 定义cython风格的.pyx文件
@cython.boundscheck(False)
@cython.wraparound(False)
cdef np.ndarray[, ndim=2] _naive_dot(np.ndarray[, ndim=2] a, np.ndarray[, ndim=2] b):
    cdef np.ndarray[, ndim=2] c
    cdef int n, p, m
    cdef np.float32_t s
    if a.shape[1] != b.shape[0]:
        raise ValueError('shape not matched')
    n, p, m = a.shape[0], a.shape[1], b.shape[1]
    c = np.zeros((n, m), dtype=np.float32)
    for i in range(n):
        for j in range(m):
            s = 0
            for k in range(p):
                s += a[i, k] * b[k, j]
            c[i, j] = s
    return c

def naive_dot(a, b):
    return _naive_dot(a, b)

# 1.2 准备编译文件setup.py, 参考下载的vcvarsall.dat修复文档+cython教程命令编译.
# Cython 程序需要先编译之后才能被 Python 调用，流程是：
#
# 1Cython 编译器把 Cython 代码编译成调用了 Python 源码的 C/C++ 代码
# 2把生成的代码编译成动态链接库
# 3Python 解释器载入动态链接库