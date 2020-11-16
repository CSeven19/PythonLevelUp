//============================================================================
// Name        : pydev.cpp
// Author      : seven
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include "Python.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define BUFSIZE 10
//1 基本实现细节的函数.
int fac(int n) {
    if (n < 2)
        return 1;
    return n * fac(n - 1);
}

char *reverse(char *s) {
    register char t;
    char *p = s;
    char *q = (s + (strlen(s) - 1));
    while (p < q) {
        t = *p;
       *p++ = *q;
       *q-- = t;
    }
    return s;
}
//2 python模板函数包装（代理函数）
//你需要为所有想被 Python 环境访问的函数都增加一个静态的函数，函数的返回值类型为 PyObject*，函数名前面要加上模块名和一个下划线(_)。
//在使用这个函数的 Python 脚本中，使用方法是先"import Extest"然后调用 "Extest.fac()"
//包装函数的用处就是先把 Python 的值传递给 C，然后调用我们想要调用的相关函数。当这个函数完成要返回 Python 的时候，把函数的计算结果转换成 Python 的对象，然后返回给 Python。
//相关内部转换底层函数:
//在从 Python 到 C 的转换就用PyArg_Parse*系列函数。在从 C 转到 Python 的时候，就用 Py_BuildValue()函数
//Python to C
//int PyArg_ParseTuple() 把 Python 传过来的参数转为 C
//int PyArg_ParseTupleAndKeywords() 与 PyArg_ParseTuple()作用相同，但是同时解析关键字参数
//C to Python
//PyObject* Py_BuildValue() 把 C 的数据转为 Python 的一个对象或一组对象，然后返回之。
static PyObject *
Extest_fac(PyObject *self, PyObject *args) {
    int res;
    int num;
    PyObject* retval;

    res = PyArg_ParseTuple(args, "i", &num);
    if (!res) {
        return NULL;
    }
    res = fac(num);
    retval = (PyObject *)Py_BuildValue("i", res);
    return retval;
}

static PyObject *
Extest_reverse(PyObject *self, PyObject *args) {
    char *orignal;
    if (!(PyArg_ParseTuple(args, "s", &orignal))) {
        return NULL;
    }
    return (PyObject *)Py_BuildValue("s", reverse(orignal));
}

static PyObject *
Extest_doppel(PyObject *self, PyObject *args) {
    char *orignal;
    char *resv;
    PyObject *retval;
    if (!(PyArg_ParseTuple(args, "s", &orignal))) {
        return NULL;
    }
    retval = (PyObject *)Py_BuildValue("ss", orignal, resv=reverse(strdup(orignal)));
    free(resv);
    return retval;
}

//3 函数列表
//static PyMethodDef
//ExtestMethods[] = {
//    {"fac", Extest_fac, METH_VARARGS},
//    {"doppel", Extest_doppel, METH_VARARGS},
//    {"reverse", Extest_reverse, METH_VARARGS},
//    {NULL, NULL},
//};
static struct PyModuleDef ExtestMethods =
{
    PyModuleDef_HEAD_INIT,
    "Extest", /* name of module */
    "test",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    Extest_fac,
    Extest_doppel,
    Extest_reverse
};
//4 初始化函数列表
PyMODINIT_FUNC PyInit_cModPyDem(void)
{
    return PyModule_Create(&ExtestMethods);
}
//5 测试
int main() {
    char s[BUFSIZE];
    printf("4! == %d\n", fac(4));
    printf("8! == %d\n", fac(8));
    printf("12! == %d\n", fac(12));
    strcpy(s, "abcdef");
    printf("reversing 'abcdef', we get '%s'\n", reverse(s));
    strcpy(s, "madam");
    printf("reversing 'madam', we get '%s'\n", reverse(s));
//    test();
    return 0;
}

// 实例2
////自定义异常
//static PyObject* SpamError;
////模块的功能函数
//static PyObject* spam_system(PyObject* self, PyObject* args)
//{
//        const char* command;
//        int sts;
//        if (!PyArg_ParseTuple(args, "s", &command))
//                return NULL;
//        sts = system(command);
//        if (sts < 0) {
//                PyErr_SetString(SpamError, "System command failed");
//                return NULL;
//        }
//        return PyLong_FromLong(sts);
//}
//方法表
//static PyMethodDef SpamMethods[] = {
//        {"system", spam_system, METH_VARARGS,
//        "Execute a shell command."},
//        {NULL, NULL, 0, NULL}
//};
////模块的结构体定义 v3.4
//static struct PyModuleDef spammodule = {
//        PyModuleDef_HEAD_INIT,
//        "spam",
////        spam_doc,
//        -1,
//        spam_system
//};
////模块初始化函数
//PyMODINIT_FUNC PyInit_spam(void) // v3.4
////PyMODINIT_FUNC initspam(void)
//{
//        PyObject* m;
//        m = PyModule_Create(&spammodule); // v3.4
////        m = Py_InitModule("spam", SpamMethods);
//        if (m == NULL){
//        	return NULL;
//        }
//        SpamError = PyErr_NewException("spam.error",NULL,NULL);
//        Py_INCREF(SpamError);
//        PyModule_AddObject(m,"error",SpamError);
//}
