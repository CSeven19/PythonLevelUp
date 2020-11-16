# # 15.1 gettext模块/locale模块 i18模块
# # 15.2 pydoc python文档工具(cmd到Scripts包 python修改python3)
# # 15.3 doctest doctest模块会搜索那些看起来像是python交互式会话中的代码片段，然后尝试执行并验证结果。
# '''
# 这个例子展示如何在源码中嵌入doctest用例。
# '>>>' 开头的行就是doctest测试用例。
# 不带 '>>>' 的行就是测试用例的输出。
# 如果实际运行的结果与期望的结果不一致，就标记为测试失败。
# '''
# def multiply(a, b):
#     """
#     >>> multiply(4, 3)  # 该处为测试信息。如果注销就不会产生测试.
#     12
#     >>> multiply('a', 3)
#     'aaa'
#     """
#     return a * b
# if __name__=='__main__':
#     import doctest
#     doctest.testmod(verbose=True)
#
# # 15.4 unittest
# # unittest单元测试框架不仅可以适用于单元测试，还可以适用WEB自动化测试用例的开发与执行，该测试框架可组织执行测试用例，
# # 并且提供了丰富的断言方法，判断测试用例是否通过，最终生成测试结果。今天笔者就总结下如何使用unittest单元测试框架来进行WEB自动化测试。
# # setUp():setUp()方法用于测试用例执行前的初始化工作。如测试用例中需要访问数据库，可以在setUp中建立数据库连接并进行初始化。如测试用例需要登录web，可以先实例化浏览器。
# # tearDown():tearDown()方法用于测试用例执行之后的善后工作。如关闭数据库连接。关闭浏览器。
# # assert*():一些断言方法：在执行测试用例的过程中，最终用例是否执行通过，是通过判断测试得到的实际结果和预期结果是否相等决定的。
# # assertEqual(a,b，[msg='测试失败时打印的信息']):断言a和b是否相等，相等则测试用例通过。
# # assertNotEqual(a,b，[msg='测试失败时打印的信息']):断言a和b是否相等，不相等则测试用例通过。
# # assertTrue(x，[msg='测试失败时打印的信息'])：断言x是否True，是True则测试用例通过。
# # assertFalse(x，[msg='测试失败时打印的信息'])：断言x是否False，是False则测试用例通过。
# # assertIs(a,b，[msg='测试失败时打印的信息']):断言a是否是b，是则测试用例通过。
# # assertNotIs(a,b，[msg='测试失败时打印的信息']):断言a是否是b，不是则测试用例通过。
# # assertIsNone(x，[msg='测试失败时打印的信息'])：断言x是否None，是None则测试用例通过。
# # assertIsNotNone(x，[msg='测试失败时打印的信息'])：断言x是否None，不是None则测试用例通过。
# # assertIn(a,b，[msg='测试失败时打印的信息'])：断言a是否在b中，在b中则测试用例通过。
# # assertNotIn(a,b，[msg='测试失败时打印的信息'])：断言a是否在b中，不在b中则测试用例通过。
# # assertIsInstance(a,b，[msg='测试失败时打印的信息'])：断言a是是b的一个实例，是则测试用例通过。
# # assertNotIsInstance(a,b，[msg='测试失败时打印的信息'])：断言a是是b的一个实例，不是则测试用例通过。
# import unittest
#
#
# # 定义测试类，父类为unittest.TestCase。
# # 可继承unittest.TestCase的方法，如setUp和tearDown方法，不过此方法可以在子类重写，覆盖父类方法。
# # 可继承unittest.TestCase的各种断言方法。
# class Test(unittest.TestCase):
#     # 定义setUp()方法用于测试用例执行前的初始化工作。
#     # 注意，所有类中方法的入参为self，定义方法的变量也要“self.变量”
#     # 注意，输入的值为字符型的需要转为int型
#     def setUp(self):
#         self.number = input('Enter a number:')
#         self.number = int(self.number)
#
#     # 定义测试用例，以“test_”开头命名的方法
#     # 注意，方法的入参为self
#     # 可使用unittest.TestCase类下面的各种断言方法用于对测试结果的判断
#     # 可定义多个测试用例
#     # 最重要的就是该部分
#     def test_case1(self):
#         print()
#         self.number
#         self.assertEqual(self.number, 10, msg='Your input is not 10')
#
#     def test_case2(self):
#         print()
#         self.number
#         self.assertEqual(self.number, 20, msg='Your input is not 20')
#
#     @unittest.skip('暂时跳过用例3的测试')
#     def test_case3(self):
#         print()
#         self.number
#         self.assertEqual(self.number, 30, msg='Your input is not 30')
#
#     # 定义tearDown()方法用于测试用例执行之后的善后工作。
#     # 注意，方法的入参为self
#     def tearDown(self):
#         print('Test over')
#
#
# # 如果直接运行该文件(__name__值为__main__),则执行以下语句，常用于测试脚本是否能够正常运行
# if __name__ == '__main__':
#     # 执行测试用例方案一如下：
#     # unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行它们。
#     # 执行顺序是命名顺序：先执行test_case1，再执行test_case2
#     unittest.main()
#
# '''
# #8.2执行测试用例方案二如下：
# #8.2.1先构造测试集
# #8.2.1.1实例化测试套件
#     suite=unittest.TestSuite()
# #8.2.1.2将测试用例加载到测试套件中。
# #执行顺序是安装加载顺序：先执行test_case2，再执行test_case1
#     suite.addTest(Test('test_case2'))
#     suite.addTest(Test('test_case1'))
# #8.2.2执行测试用例
# #8.2.2.1实例化TextTestRunner类
#     runner=unittest.TextTestRunner()
# #8.2.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）
#     runner.run(suite)
# '''
#
# '''
# #8.3执行测试用例方案三如下：
# #8.3.1构造测试集（简化了方案二中先要创建测试套件然后再依次加载测试用例）
# #执行顺序同方案一：执行顺序是命名顺序：先执行test_case1，再执行test_case2
#     test_dir = './'
#     discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
# #8.3.2执行测试用例
# #8.3.2.1实例化TextTestRunner类
#     runner=unittest.TextTestRunner()
# #8.3.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）
#     runner.run(discover)
# '''
#
# # 15.5 traceback 异常详细信息模块
# # 普通异常
# try:
#     1/0
# except Exception:
#     print(Exception)
# # 详细异常
# import traceback
# try:
#     1/0
# except Exception:
#     traceback.print_exc()
#
# 15.6 pdb 调试模板，因pycharm自带调试可忽略
# 15.7 timeit 测试运行时间
# 15.8 compileall 此模块可以将指定目录下的.py文件编译成python的二进制文件.pyc或者.pyo文件。


# # 15.9language tools
#
# # 1 warnings
# import warnings
# warnings.filterwarnings('ignore', '.*do not.*',)
# print('Before the warning')
# warnings.warn('This is a warning message')
# warnings.warn('old_function() is deprecated, use new_function() instead',stacklevel=2)
# print('After the warning')
#
# # 2 abc 抽象类，方法模块(因python是动态类型语言无abstract)
# from abc import ABCMeta, abstractmethod, abstractproperty
#
#
# class Drawable(metaclass=ABCMeta):
#     """docstring for Drawable"""
#
#     @property  #抽象属性，对应return
#     def size(self):
#         # return 'mysize'
#         pass
#
#     @abstractmethod
#     def draw(self, x, y, scale=1.0):
#         # print(x * scale, y * scale)
#         pass
#
#     def double_draw(self, x, y):
#         self.draw(x, y, scale=2.0)
#
#
# class Cicle(Drawable):
#     # 1. 使用继承的方法
#     """docstring for Cicle"""
#
#     def draw(self, x, y, scale=1.0):
#         print(x * scale, y * scale)
#
#     @property
#     def size(self):
#         return 'Cicle size'
#
#
# # Cicle如果没有override draw函数和size 属性，那么实例化的时候就会报错
# # TypeError: Can't instantiate abstract class Cicle with abstract methods draw, size
# c = Cicle()
# print(dir(c))
# c.draw(1, 2)
# c.double_draw(1, 2)
# print(isinstance(c, Drawable))  # True
#
#
# class Rectangle():
#     """docstring for Cicle"""
#     pass
#
# # 使用抽象类函数的register方法注册具体的class
# # 通过注册的类，可以直接实例化，但是无法访问抽象类的所有成员
# # 其实就是只是让isinstance、issubclass识别注册的类为抽象类的成员和实例
# Drawable.register(Rectangle)
#
# r = Rectangle()
# # r.double_draw(1, 2)
# # AttributeError: 'Rectangle' object has no attribute 'double_draw'
# print(dir(r))
# print(isinstance(r, Drawable))  # True
# print(issubclass(Rectangle, Drawable))  # True
# r.draw(1, 2)
#
# # 输出
# # ['__abstractmethods__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', 'double_draw', 'draw', 'size']
# # 1.0 2.0
# # 2.0 4.0
# # True
# # True
# # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# # True
# # True
# # [Finished in 0.2s]
#
# 3 dis模块  通过dis模块包含的一些内置属性可以了解到Python字节码指令的信息
# 格式如下：python -m dis test.py

