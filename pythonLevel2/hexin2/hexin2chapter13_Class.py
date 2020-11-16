# class
#
# # 13.1文档字符串
# def functionName(args):
#     """function documentation string""" #函数文档字符串
#     function_suite #函数体
# class ClassName(object):
#     """class documentation string"""  # 类文档字符串
#     class_suite  # 类体
#
# # 13.2类属性
# 13.2.1数据属性:
# # 定义于类中，但是在方法外。类似java中的static,可以使用(类.类属性)调用
# class C(object):
#     foo = 100
# print(C.foo)
# C.foo = C.foo + 1
# print(C.foo)
# # 13.2.2普通方法():
# # 1Python 严格要求，没有实例，方法是不能被调用的。(区别与类外定义的方法可以直接用模块名字.方法调用)
# # 首先，方法仅仅是类内部定义的函数。(这意味着方法是类属性而不
# # 是实例属性)。
# # 其次，方法只有在其所属的类拥有实例时，才能被调用。当存在一个实例时，方法才被认为是
# # 绑定到那个实例了。没有实例时方法就是未绑定的。
# # 最后，任何一个方法定义中的第一个参数都是变量 self，它表示调用此方法的实例对象。
# # 2调用绑定方法(实例调用的)
# # 3调用非绑定方法(调用非绑定方法并不经常用到。需要调用一个还没有任何实例的类中的方法的一个主要的场景
# # 是:你在派生一个子类,而且你要覆盖父类的方法，这时你需要调用那个父类中想要覆盖掉的构造方
# # 法。):
# class EmplAddrBookEntry(AddrBookEntry):
#     '''Employee Address Book Entry class''' # 员工地址记录条目
#     def __init__(self, nm, ph, em):
#         AddrBookEntry.__init__(self, nm, ph)
#         self.empid = id
#         self.email = em
# # 13.2.3静态方法，类方法(类似java中的static方法)
# #  staticmethod()和 classmethod()
# class TestStaticMethod:
#     def foo():
#         print('calling static method foo()')
#     foo = staticmethod(foo)  # 静态方法
# class TestClassMethod:
#     def foo(cls):
#         print('calling class method foo()')
#         print('foo() is part of class:', cls.__name__)
#     foo = classmethod(foo)  # 类方法
# # 函数修饰符式定义
# class TestStaticMethod:
#     @staticmethod
#     def foo():
#         print('calling static method foo()')
# class TestClassMethod:
#     @classmethod
#     def foo(cls):
#         print('calling class method foo()')
#         print('foo() is part of class:', cls.__name__)
# #  我们可以通过类或者实例调用这些函数.
# tsm = TestStaticMethod()
# TestStaticMethod.foo()
# # calling static method foo()
# tsm.foo()
# # calling static method foo()
# tcm = TestClassMethod()
# TestClassMethod.foo()
# # calling class method foo()
# # foo() is part of class: TestClassMethod
# tcm.foo()
# # calling class method foo()
# # foo() is part of class: TestClassMethod
#
# 13.3类的特殊类属性
# dir(C) 查看类中方法集合
# C.__name__ 类Ｃ的名字（字符串）
# C.__doc__ 类Ｃ的文档字符串
# C.__bases__ 类Ｃ的所有父类构成的元组
# C.__dict__ 类Ｃ的属性
# C.__slots__ 类似__dict__但是更节约内存
# C.__module__ 类Ｃ定义所在的模块（1.5 版本新增）
# C.__class__ 实例Ｃ对应的类（仅新式类中)
#
# # 13.4__new__(),__del__()
# # __new__() “构造器”方法:
# # 继承自object的新式类才有__new__
# # __new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
# # 区别__init__,__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
# # __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
# # 若__new__没有正确返回当前类cls的实例，那__init__是不会被调用的，即使是父类的实例也不行
# class A(object):
#     def __init__(self):
#         print("init")
#     def __new__(cls,*args, **kwargs):
#         print("new %s"%cls)
#         return object.__new__(cls, *args, **kwargs)
# A()
# # __del__() "解构器"方法
# class P:
#     def __del__(self):
#         print("P delete")
# class C(P): # class declaration 类声明
#     def __init__(self): # "constructor" 构造器
#         print('initialized')
#     def __del__(self): # "destructor" 解构器
#          P.__del__(self) # call parent destructor print 'deleted' 调用父类解构器来打印
# c1 = C() # instantiation initialized 实例初始化
# c2 = c1 # create additional alias 创建另外一个别名
# c3 = c1 # create a third alias 创建第三个别名
# id(c1), id(c2), id(c3) # all refer to same object 同一对象所有引用
# del c1 # remove one reference 清除一个引用
# del c2 # remove another reference 清除另一个引用
# del c3 # remove final reference deleted # destructor finally invoked 解构器最
#
# # #13.5实例属性
# # # 特殊属性:
# #1： 当类属性不可变时，同名实例属性无法影响类属性
# class C(object):  # define class 定义类
#     version = 1.2  # static member 静态成员
# c = C()  # instantiation 实例化
# print(C.version)  # access via class 通过类来访问
# print(c.version)  # access via instance 通过实例来访问
# C.version += 0.1  # update (only) via class 通过类（只能这样）来更新,我们只有当使用类引用 version 时，才能更新它的值
# print(C.version)  # class access 类访问 1.3
# print(c.version)  # instance access, which 实例访问它，其值已被改变 1.3
# c.version += 0.1
# print(C.version)  # 1.3
# print(c.version)  # 1.4000000000000001 仅该实例的version改变了。
# del c.version
# print(c.version)  # 1.3
# # 2： 注意 当类属性可变时，同名实例属性会影响类属性
# # 使用实例属性来试着修改类属性是很危险的。原因在于实例拥有它们
# # 自已的属性集，在 Python 中没有明确的方法来指示你想要修改同名的类属性，比如，没有 global
# # 关键字可以用来在一个函数中设置一个全局变量（来代替同名的局部变量）。修改类属性需要使用类
# # 名，而不是实例名。
# class Foo(object):
#     x = {2003: 'poe2'}
# foo = Foo()
# print(foo.x)  #{2003: 'poe2'}
# foo.x[2004] = 'valid path'
# print(foo.x)  #{2003: 'poe2', 2004: 'valid path'}
# print(Foo.x) # it works!!! 生效了 {2003: 'poe2', 2004: 'valid path'}
# del foo.x # no shadow so cannot delete 没有遮蔽所以不能删除掉 Traceback (most recent call last): File "<stdin>", line 1, in ? del foo.x AttributeError: x
#
# # 13.6代码中利用类:组合
# 当类之间有显著的不同，并且(较小的类)是较大的类所需要的组件时，组合表现得很好，但当
# 你设计“相同的类但有一些不同的功能”时，派生就是一个更加合理的选择了。
# class NewAddrBookEntry(object): # class definition 类定义
#     '''new address book entry class'''
#     def __init__(self, nm, ph): # define constructor 定义构造器
#         self.name = Name(nm) # create Name instance 创建 Name 实例
#         self.phone = Phone(ph) # create Phone instance 创建 Phone 实例 组合了2个类实例。
#         print('Created instance for:', self.name)
# # 13.6.2：派生
# # 1多继承,从左至右搜索,覆盖
# class Parent(object): # define parent class 定义父类
#     def parentMethod(self):
#         print('calling parent method')
#     def count(self):
#         print('parent count')
# class Child(Parent): # define child class 定义子类
#     def childMethod(self):
#         print('calling child method')
#     def count(self):
#         print('child count')
#
# # 2标准类型子类化
# # 不可变标准类型:
# class RoundFloat(float):
#     def __new__(cls, val):
#         return float.__new__(cls, round(val, 2))
# print(RoundFloat(1.5955))
# # 可变标准类型：不可用
# class SortedKeyDict(dict):
#     def keys(self):
#         return sorted(super(SortedKeyDict, self).keys())
# d = SortedKeyDict((('zheng-cai', 67), ('hui-jun', 68),('xin-yi', 2))).keys()
# print(d)  # {'zheng-cai': 67, 'xin-yi': 2, 'hui-jun': 68}
#
# 13.7BIF
# issubclass()
# isinstance()
# hasattr(), getattr(),setattr(), delattr()(类似js)
# dir(),vars()
# super()
#
# 13.8特殊方法定制类(类似__init__的各种特殊方法)
# 用来定制类的特殊方法
# 特殊方法 描述
# 基本定制型
# C.__init__(self[, arg1, ...]) 构造器（带一些可选的参数）
# C.__new__(self[, arg1, ...]) 构造器（带一些可选的参数）；通常用在设置不变数据类型的子类。
# C.__del__(self) 解构器
# C.__str__(self) 可打印的字符输出；内建 str()及 print 语句
# C.__repr__(self) 运行时的字符串输出；内建 repr() 和‘‘ 操作符
# C.__unicode__(self) Unicode 字符串输出；内建 unicode()
# C.__call__(self, *args) 表示可调用的实例
# C.__nonzero__(self) 为 object 定义 False 值；内建 bool() （从 2.2 版开始）
# C.__len__(self) “长度”（可用于类）；内建 len()
# 对象（值）比较 c
# C.__cmp__(self, obj) 对象比较；内建 cmp()
# C.__lt__(self, obj) and 小于/小于或等于；对应<及<=操作符
# C.__gt__(self, obj) and 大于/大于或等于；对应>及>=操作符
# C.__eq__(self, obj) and 等于/不等于；对应==,!=及<>操作符
# 属性
# C.__getattr__(self, attr) 获取属性；内建 getattr()；仅当属性没有找到时调用
# C.__setattr__(self, attr, val) 设置属性
# C.__delattr__(self, attr) 删除属性
# C.__getattribute__(self, attr) a 获取属性；内建 getattr()；总是被调用
# # 描述符
# # C.__get__(self, attr) a （描述符）获取属性
# # C.__set__(self, attr, val) a （描述符）设置属性
# # C.__delete__(self, attr) a （描述符）删除属性
# class DevNull2(object):
#     def __get__(self, obj, typ=None):
#         print('Accessing attribute... ignoring')
#     def __set__(self, obj, val):
#         print('Attempt to assign %r... ignoring' % (val))
#     def __getattribute__(self, foo):
#         self.foo = foo
#         print("__getattribute__")
#     def __getattr__(self, foo):
#         self.foo = foo
#         print("__getattr__")
#     def __call__(self, *args, **kwargs):
#         print("__call__")
# class C2(object):
#     foo = DevNull2()
# c2 = DevNull2()
# c2.foo = 'bar' # 调用__set__
# x = c2.foo # 调用__get__
# print('c2.foo contains:', x)
# # property(fget=None, fset=None, fdel=None, doc=None)可以用来替换描述符
# # __get__替换实例:
# class ProtectAndHideX(object):
#     def __init__(self, x):
#         assert isinstance(x, int),'"x" must be an integer!'
#         self.__x = ~x
#     def get_x(self):
#         return ~self.__x
#     x = property(get_x)  #x仅能被赋值一次
# # inst = ProtectAndHideX('foo')
# inst = ProtectAndHideX(10)
# print('inst.x =', inst.x)
# inst.x = 20
# print('inst.x =', inst.x)
# # __set__替换实例:
# class HideX(object):
#     def __init__(self, x):
#         self.x = x
#     def get_x(self):
#         return ~self.__x
#     def set_x(self, x):
#         assert isinstance(x, int), '"x" must be an integer!'
#         self.__x = ~x
#     x = property(get_x, set_x) #x可以被多次赋值
# inst = HideX(20)
# print(inst.x)
# inst.x = 30
# print(inst.x)
# # __set__定制doc:
# from math import pi
# def get_pi(dummy):
#     return pi
# class PI(object):
#     pi = property(get_pi, doc='Constant "pi"')
# inst = PI()
# inst.pi
# print(PI.pi.__doc__)  #Constant "pi"
# # 修饰符写法:
# class HideX(object):
#     def __init__(self, x):
#         self.x = x
#     @property
#     def x(self):
#         def fget(self):
#             return ~self.__x
#         def fset(self, x):
#             assert isinstance(x, int), \
#                 '"x" must be an integer!'
#             self.__x = ~x
#             return locals()
# 定制类/模拟类型
# 数值类型：二进制操作符
# C.__*add__(self, obj) 加；+操作符
# C.__*sub__(self, obj) 减；-操作符
# C.__*mul__(self, obj) 乘；*操作符
# C.__*div__(self, obj) 除；/操作符
# C.__*truediv__(self, obj) e True 除；/操作符
# C.__*floordiv__(self, obj) e
#  Floor 除；//操作符
# C.__*mod__(self, obj) 取模/取余；%操作符
# C.__*divmod__(self, obj) 除和取模；内建 divmod()
# C.__*pow__(self, obj[, mod]) 乘幂；内建 pow();**操作符
# C.__*lshift__(self, obj) 左移位；<<操作符
# 数值类型：二进制操作符
# C.__*rshift__(self, obj) 右移；>>操作符
# C.__*and__(self, obj) 按位与；&操作符
# C.__*or__(self, obj) 按位或；|操作符
# C.__*xor__(self, obj) 按位与或；^操作符
# 数值类型：一元操作符
# C.__neg__(self) 一元负
# C.__pos__(self) 一元正
# C.__abs__(self) 绝对值；内建 abs()
# C.__invert__(self) 按位求反；~操作符
# 数值类型：数值转换
# C.__complex__(self, com) 转为 complex(复数);内建 complex()
# C.__int__(self) 转为 int;内建 int()
# C.__long__(self) 转为 long；内建 long()
# C.__float__(self) 转为 float；内建 float()
# 数值类型：基本表示法（String）
# C.__oct__(self) 八进制表示；内建 oct()
# C.__hex__(self) 十六进制表示；内建 hex()数值类型：数值压缩
# C.__coerce__(self, num) 压缩成同样的数值类型；内建 coerce()
# C.__index__(self) 在有必要时,压缩可选的数值类型为整型（比如：用于切片索引等等）
# 序列类型
# C.__len__(self) 序列中项的数目
# C.__getitem__(self, ind) 得到单个序列元素
# C.__setitem__(self, ind,val) 设置单个序列元素
# C.__delitem__(self, ind) 删除单个序列元素
# C.__getslice__(self, ind1,ind2) 得到序列片断
# C.__setslice__(self, i1, i2,val) 设置序列片断
# C.__delslice__(self, ind1,ind2) 删除序列片断
# C.__contains__(self, val) 测试序列成员；内建 in 关键字
# C.__*add__(self,obj) 串连；+操作符
# C.__*mul__(self,obj) 重复；*操作符
# C.__iter__(self) e 创建迭代类；内建 iter()
# 映射类型
# C.__len__(self) mapping 中的项的数目
# C.__hash__(self) 散列(hash)函数值
# C.__getitem__(self,key) 得到给定键(key)的值
# C.__setitem__(self,key,val) 设置给定键(key)的值
# C.__delitem__(self,key) 删除给定键(key)的值
# C.__missing__(self,key) 给定键如果不存在字典中，则提供一个默认值
#
# # 13.9 私有化
# # 1、 _xx 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问。若内部变量标示，如： 当使用“from M import”时，不会将以一个下划线开头的对象引入 。
# # 2、 __xx 双下划线的表示的是私有类型的变量。只能允许这个类本身进行访问了，连子类也不可以用于命名一个类属性（类变量），调用时名字被改变（在类FooBar内部，__boo变成_FooBar__boo,如self._FooBar__boo）
# # 3、 __xx__定义的是特列方法。用户控制的命名空间内的变量或是属性，如init , __import__或是file 。只有当文档有说明时使用，不要自己定义这类变量。 （就是说这些是python内部定义的变量名）
# class A(object):
#     def __init__(self):
#         self.__private()
#         self.public()
#
#     def __private(self):
#         print('A.__private()')
#
#     def public(self):
#         print('A.public()')
#
#
# class B(A):
#     def __private(self):
#         print('B.__private()')
#
#     def public(self):
#         print('B.public()')
#
#
# a = A()  # 实例化对象a #A.__private()  A.public()
# b = B()  # 实例化对象b #A.__private()  B.public()
# print(a.__private())  # 这里会报错,说 AttributeError: 'a' object has no attribute '__private'
# print(b.__private())  # 这里会报错,说 AttributeError: 'B' object has no attribute '__private'
# print('======')
# print(b._A__private())  # 因为私有变量轧压机制,__private方法变成_A__private()
# print(dir(b))  # 通过自省方法dir(),查看b所具有的属性
# print('======')
#
# # 13.10包装类(类似integer)
# # 实例(复数的包装类):
# class WrapMe(object):
#     def __init__(self, obj):
#         self.__data = obj
#     def get(self):
#         return self.__data
#     def __repr__(self):
#         return self.__data
#     def __str__(self):
#         return str(self.__data)
#     def __getattr__(self, attr):
#         return getattr(self.__data, attr)
# wrappedComplex = WrapMe(3.5+4.2j)
# print(wrappedComplex)
# print(wrappedComplex.real)
# print(wrappedComplex.imag)
# print(wrappedComplex.conjugate())
# print(wrappedComplex.get())
#
# # 13.11 模板类:Metaclasses 和__metaclass__
# from time import ctime
# print('*** Welcome to Metaclasses!')
# print('\tMetaclass declaration first.')
# class MetaC(type):
#     def __init__(cls, name, bases, attrd):
#         super(MetaC, cls).__init__(name, bases, attrd)
#         print('*** Created class %r at: %s' % (name, ctime()))
#     print('\tClass "Foo" declaration next.')
# class Foo(object):
#     __metaclass__ = MetaC  #  模板类为MetaC
#     def __init__(self):
#         print('*** Instantiated class %r at: %s' % (self.__class__.__name__, ctime()))
# print('\tClass "Foo" instantiation next.')
# f = Foo()
# print('\tDONE')
# # 实例:
# from warnings import warn
# class ReqStrSugRepr(type):
#     def __init__(cls, name, bases, attrd):
#         super(ReqStrSugRepr, cls).__init__(name, bases, attrd)
#         if '__str__' not in attrd:
#             raise TypeError("Class requires overriding of __str__()")
#         if '__repr__' not in attrd:
#             warn('Class suggests overriding of __repr__()\n',stacklevel=3)
# print('*** Defined ReqStrSugRepr (meta)class\n')
# class Foo(object):
#     __metaclass__ = ReqStrSugRepr
#     def __str__(self):
#         return 'Instance of class:', self.__class__.__name__
#     def __repr__(self):
#         return self.__class__.__name__
# print('*** Defined Foo class\n')
# class Bar(object):
#     __metaclass__ = ReqStrSugRepr
#     def __str__(self):
#         return 'Instance of class:', self.__class__.__name__
# print('*** Defined Bar class\n')
# class FooBar(object):
#     __metaclass__ = ReqStrSugRepr
# print('*** Defined FooBar class\n')
#
# 13.12相关模块
# UserList 提供一个列表对象的封装类
# UserDict 提供一个字典对象的封装类
# UserString a 提供一个字符串对象的封装类；它又包括一个 MutableString 子类，如果有需要，可以提供有关功能
# types 定义所有 Python 对象的类型在标准 Python 解释器中的名字
# operator 标准操作符的函数接口
