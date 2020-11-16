# # 2.1简单输入输出
# myString = 'Hello World!'
# print(myString)
# user = input('Enter login name: ')
# print(user)
# print("%.2e" % (23.423))  #科学计数法
#
# # 2.2运算符
# # 算数运算符: + - * / // % ** 双斜杠用作浮点除法（对结果进行四舍五入）**乘方运算(类似^)
# print(-2 * 4 + 3 ** 2)
# # 比较运算符: < <= > >= == != <> (<>的不等于符号已经逐渐被淘汰)
# # Python 仅缓存简单整数，因为它认为在 Python 应用程序中这些小整数会经常被用到。
# a = 1
# id(a)
# #8402824
# b = 1
# id(b)
# #8402824
# c = 1.0
# id(c)
# #8651220
# d = 1.0
# id(d)
# #8651204
# # 逻辑运算符: and or not(布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。)
# print( not 6.2 <= 6 ) #6.2<=6为false
# print( 3 < 4 < 5 )
# # 赋值运算符：支持增量赋值：n *= 10，
# # 在赋值时，不管这个对象是新创建的，还是一个已经存在的，都是将该对象的引用（并不是值）赋值给变量。
# # 多重赋值x = y = z = 1
# # 多元赋值x, y, z = 1, 2, 'a string'
# # 交换变量实例
# x, y = 1, 2
# x, y = y, x
# x, y = x+y, x
# print(x,y)
# print(x)
# # 位运算符：& | ^ ~ << >>
# a = 0b00111100
# b = 0b00001101
# print("{0:b}".format(a))
# print("{0:b}".format(b))
# print("{0:b}".format(a & b))
# print("{0:b}".format(a | b))
# print("{0:b}".format(a ^ b))
# print("{0:b}".format(~a))
# print("{0:b}".format(a << 2))
# print("{0:b}".format(a >> 2))
# #成员运算符：in ,not in
# a = 2
# b = 20
# re_list = [1, 2, 3, 4, 5 ]
# if a in re_list:
#     print("1 - 变量 a 在给定的列表中 list 中")
# else:
#     print("1 - 变量 a 不在给定的列表中 list 中")
#
# if b not in re_list:
#     print("2 - 变量 b 不在给定的列表中 list 中")
# else:
#     print("2 - 变量 b 在给定的列表中 list 中")
# #身份运算符：is(判断两个标识符是不是引用自一个对象)，is not
# #is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
# a = 20
# b = 20
# if a is b:
#     print("1 - a 和 b 有相同的标识")
# else:
#     print("1 - a 和 b 没有相同的标识")
# if id(a) == id(b):
#     print("2 - a 和 b 有相同的标识")
# else:
#     print("2 - a 和 b 没有相同的标识")
# class A:
#     def __init__(self,name):
#         self.name = name
# #优先级
# *	指数 (最高优先级)
# ~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
# * / % //	乘，除，取模和取整除
# + -	加法减法
# >> <<	右移，左移运算符
# &	位 'AND'
# ^ |	位运算符
# <= < > >=	比较运算符
# <> == !=	等于运算符
# = %= /= //= -= += *= **=	赋值运算符
# is is not	身份运算符
# in not in	成员运算符
# not or and	逻辑运算符
#
# 2.3 变量
# 定义：类似C
# z 第一个字符必须是字母或下划线（_）
# z 剩下的字符可以是字母和数字或下划线
# z 大小写敏感
# 动态语言：无需事先声明变量类型，变量的类型和值在赋值那一刻被初始化。
# z 程序员不用关心内存管理
# z 变量名会被“回收”
# z del 语句能够直接释放资源
#
# 2.4数字
# # 1 六种数字类型：int (有符号整数) long (长整数) bool (布尔值) float (浮点值) complex (复数)  decimal(用于十进制浮点数,常用于金融，科学计算)
# # 2 复数：
# 1.23e-045+6.7e+089j
# # num.real 该复数的实部
# # num num.imag 该复数的虚部
# # num.conjugate() 返回该复数的共轭复数
# aComplex = -8.333-1.47j
# print(aComplex)
# #(-8.333-1.47j)
# print(aComplex.real)
# #-8.333
# print(aComplex.imag)
# #-1.47
# print(aComplex.conjugate())
# #(-8.333+1.47j)
# 3 数值函数:
# abs(x)	返回数字的绝对值，如abs(-10) 返回 10
# ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
# cmp(x, y) 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。使用 (x>y)-(x<y) 替换。
# exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
# fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
# import math
# print(math.fabs(-10.2)) #10.2
# floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
# log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
# max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
# modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
# pow(x, y)	x**y 运算后的值。
# round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
# sqrt(x)	返回数字x的平方根。
# math.gamma(i)
# math.lgamma(x) 返回x的绝对值的自然对数的伽玛函数
# math.erf(x)/ math.erfc(x) 误差函数(erfc = 1 - erf)  erf(x) = 2/sqrt(pi) * integral from 0 to x of exp(-t^2) dt.其值域范围为(-1, 1)，区间长度为2.
# 所以erfc是单调增函数，在通信原理中常用于计算误码率与信噪比的关系，信噪比越高，误码率越低。
# # 累加三方法：
# # sum()
# # fsum()
# import math
# values = [ 0.1 ] * 10
# print('Input values:', values)
# print('sum() : {:.20f}'.format(sum(values)))
# s = 0.0
# for i in values:
#     s += i
# print('for-loop : {:.20f}'.format(s))  # 循环累加
# print('math.fsum() : {:.20f}'.format(math.fsum(values)))
# # factorial()累乘
# import math
# for i in [ 0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.1 ]:
#     try:
#         print('{:2.0f} {:6.0f}'.format(i, math.factorial(i)))
#     except ValueError:
#         print('Error computing factorial(%s):' % i, 'valueError')
# # isinf()/ math.isnan(x)/math.modf(i/2.0)返回(小数,整数)的元组
# import math
# print(math.modf(5/2.0))
# print('{:^3} {:6} {:6} {:6}'.format('e', 'x', 'x**2', 'isinf'))
# print('{:-^3} {:-^6} {:-^6} {:-^6}'.format('', '', '', ''))
# for e in range(0, 201, 20):
#     x = 10.0 ** e
#     y = x*x
#     print('{:3d} {!s:6} {!s:6} {!s:6}'.format(e, x, y, math.isinf(y)))
# # 4 随机数函数:
# # choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
# # randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
# # random()	随机生成下一个实数，它在[0,1)范围内。
# # seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# # shuffle(lst)	将序列的所有元素随机排序
# # uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
# # random()
# import random
# for i in range(5):
#     print('%04.3f' % random.random())
# print()
# # uniform()
# import random
# for i in range(5):
#     print('%04.3f' % random.uniform(1, 100))
# print()
# # seed()
# import random
# random.seed(1)
# for i in range(5):
#     print('%04.3f' % random.random())
# print()
# #  Random Integers
# import random
# print([1, 100])
# for i in range(3):
#     print(random.randint(1, 100))
# print('\n[-5, 5]:')
# for i in range(3):
#     print(random.randint(-5, 5))
# print()
# # 列表中随机抽取。
# import random
# import itertools
# outcomes = {'heads':0, 'tails':0}
# sides = outcomes.keys()
# print(sides)
# for i in range(10000):
#     outcomes[random.choice(list(sides))] += 1  # 骰子类似。所以结果基本在5000左右各自。
# print('Heads:', outcomes['heads'])
# print('Tails:', outcomes['tails'])
# # shuffle(lst)随机序列
# import random
# import itertools
# FACE_CARDS = ('J', 'Q', 'K', 'A')
# SUITS = ('H', 'D', 'C', 'S')
# def new_deck():
#     return list(itertools.product(itertools.chain(range(2, 11), FACE_CARDS),SUITS,))
# def show_deck(deck):
#     p_deck = deck[:]
#     while p_deck:
#         row = p_deck[:13]
#         p_deck = p_deck[13:]
#         for j in row:
#             print('%2s%s' % j, end='')
#         print()
# # Make a new deck, with the cards in order
# deck = new_deck()
# print('Initial deck:')
# show_deck(deck)
# # Shuffle the deck to randomize the order
# random.shuffle(deck)
# print('\nShuffled deck:')
# show_deck(deck)
# # Deal 4 hands of 5 cards each
# hands = [[], [], [], []]
# for i in range(5):
#     for h in hands:
#         h.append(deck.pop())
# # Show the hands
# print('\nHands:')
# for n, h in enumerate(hands):
#     print('%d:' % (n+1), end='')
#     for c in h:
#         print('%2s%s' % c, end='')
#     print()
# # Show the remaining deck
# print('\nRemaining deck:')
# show_deck(deck)
# # sample(seq, n) 类似choice/shuffle从序列seq中选择n个随机且独立的元素
# import random
# words = ['a','b','c','2323','w10']
# words = [w.rstrip() for w in words]
# print(type(random.sample(words, 2)))
# for w in random.sample(words, 2):
#     print(w)
# # SystemRandom()
# import random
# import time
# print('Default initializiation:\n')
# r1 = random.SystemRandom()
# r2 = random.SystemRandom()
# for i in range(3):
#     print('%04.3f %04.3f' % (r1.random(), r2.random()))
# print('\nSame seed:\n')
# seed = time.time()
# r1 = random.SystemRandom(seed)
# r2 = random.SystemRandom(seed)
# for i in range(3):
#     print('%04.3f %04.3f' % (r1.random(), r2.random()))
#
# 5 三角函数:
# acos(x)	返回x的反余弦弧度值。
# asin(x)	返回x的反正弦弧度值。
# atan(x)	返回x的反正切弧度值。
# atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
# cos(x)	返回x的弧度的余弦值。
# hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
# sin(x)	返回的x弧度的正弦值。
# tan(x)	返回x弧度的正切值。
# degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
# radians(x)	将角度转换为弧度
# # radians
# # 实例1
# import math
# print('{:^7} {:^7} {:^7}'.format('Degrees', 'Radians', 'Expected'))
# print('{:-^7} {:-^7} {:-^7}'.format('', '', ''))
# for deg, expected in [ ( 0, 0),
# ( 30, math.pi/6),
# ( 45, math.pi/4),
# ( 60, math.pi/3),
# ( 90, math.pi/2),
# (180, math.pi),
# (270, 3/2.0 * math.pi),
# (360, 2 * math.pi),
# ]:
#     print('{: 7d} {: 7.2f} {: 7.2f}'.format(deg,math.radians(deg),expected,))  # 对应弧度->角度 math.degrees(rad)
# # 三角函数(Trigonometry)
# import math
# print('Degrees Radians Sine Cosine Tangent')
# print('------- ------- ------- -------- -------')
# fmt = ' '.join(['%7.2f'] * 5)
# for deg in range(0, 361, 30):
#     rad = math.radians(deg)
#     if deg in (90, 270):
#         t = float('inf')
#     else:
#         t = math.tan(rad)
#     print(fmt % (deg, rad, math.sin(rad), math.cos(rad), t))
# # 实例2
# import math
# for r in [ 0, 0.5, 1 ]:
#     print('arcsine(%.1f) = %5.2f' % (r, math.asin(r)))
#     print('arccosine(%.1f) = %5.2f' % (r, math.acos(r)))
#     print('arctangent(%.1f) = %5.2f' % (r, math.atan(r)))
#     print()
# # hypot(x, y)
# import math
# print('{:^7} {:^7} {:^10}'.format('X', 'Y', 'Hypotenuse'))
# print('{:-^7} {:-^7} {:-^10}'.format('', '', ''))
# for x, y in [ # simple points
# (1, 1),
# (-1, -1),
# (math.sqrt(2), math.sqrt(2)),
# (3, 4), # 3-4-5 triangle
# # on the circle
# (math.sqrt(2)/2, math.sqrt(2)/2), # pi/4 rads
# (0.5, math.sqrt(3)/2), # pi/3 rads
# ]:
#     h = math.hypot(x, y)
#     print('{:7.2f} {:7.2f} {:7.2f}'.format(x, y, h))
# 6 数字常量:
# pi 数学常量 pi（圆周率，一般以π来表示）
# e	数学常量 e，e即自然常数（自然常数）
# 数字常用模块：
# decimal 十进制浮点运算类 Decimal
# array 高效数值数组（字符，整数，浮点数等等）
# math/cmath 标准C库数学运算函数。常规数学运算在match模块，复数运算在cmath模块
# operator 数字运算符的函数实现。比如 tor.sub(m,n)等价于 m - n
# random 多种伪随机数生成器
#
# 7 序列定义：研究这样一些 Python 的类型，它们的成员有序排列的，并且可以通过下标偏移量访问到它的一个或者几个成员，这类 Python 类型统称为序列。
# 包括下面这些：字符串(普通字符串和 unicode 字符串)，列表，和元组类型。
# # # 8 分数
# import fractions
# for n, d in [ (1, 2), (2, 4), (3, 6) ]:
#     f = fractions.Fraction(n, d)
#     print('%s/%s = %s' % (n, d, f))
# # 9 decimal
# # 实例1:
# import decimal
# fmt = '{0:<25} {1:<25}'
# print(fmt.format('Input', 'Output'))
# print(fmt.format('-' * 25, '-' * 25))
# # Integer
# print(fmt.format(5, decimal.Decimal(5)))
# # String
# print(fmt.format('3.14', decimal.Decimal('3.14')))
# # Float
# f = 0.1
# print(fmt.format(repr(f), decimal.Decimal(str(f))))
# print(fmt.format('%.23g' % f, str(decimal.Decimal.from_float(f))[:25]))
# # 实例2： 特殊值
# import decimal
# for value in [ 'Infinity', 'NaN', '0' ]:
#     print(decimal.Decimal(value), decimal.Decimal('-' + value))
# print()
# print('Infinity + 1:', (decimal.Decimal('Infinity') + 1))
# print('-Infinity + 1:', (decimal.Decimal('-Infinity') + 1))
# # print(comparing NaN
# print(decimal.Decimal('NaN') == decimal.Decimal('Infinity'))
# print(decimal.Decimal('NaN') != decimal.Decimal(1))
# # 实例3: context 用于设置decimal
# import decimal
# import pprint
# context = decimal.getcontext()
# print('Emax =', context.Emax)
# print('Emin =', context.Emin)
# print('capitals =', context.capitals)
# print('prec =', context.prec)
# print('rounding =', context.rounding)
# print('flags =',pprint.pprint(context.flags))
# print('traps =',pprint.pprint(context.traps))
# # 实例4： Precision(保留位)
# import decimal
# d = decimal.Decimal('0.123456')
# for i in range(1, 5):
#     decimal.getcontext().prec = i
#     print(i, ':', d, d * 1)
# # 实例5：localcontext() 可以使用with的context
# import decimal
# with decimal.localcontext() as c:
#     c.prec = 3
#     print('Local precision:', c.prec)
#     print('3.14 / 3 =', (decimal.Decimal('3.14') / 3))
#     print()
#     print('Default precision:', decimal.getcontext().prec)
#     print('3.14 / 3 =', (decimal.Decimal('3.14') / 3))
# 10 Exponents and Logarithms
# # log
# # 实例1
# import math
# print(math.log(8))
# print(math.log(8, 2))
# print(math.log(0.5, 2))
# # 实例2
# import math
# print('{:2} {:^12} {:^10} {:^20} {:8}'.format(  # {:2} == 2个空格
# 'i', 'x', 'accurate', 'inaccurate', 'mismatch',
# ))
# print('{:-^2} {:-^12} {:-^10} {:-^20} {:-^8}'.format(  # {:-^2} == --
# '', '', '', '', '',
# ))
# for i in range(0, 10):
#     x = math.pow(10, i)
#     accurate = math.log10(x)
#     inaccurate = math.log(x, 10)
#     match = '' if int(inaccurate) == i else '*'
#     print('{:2d} {:12.1f} {:10.8f} {:20.18f} {:^5}'.format(
#     i, x, accurate, inaccurate, match,
#     ))
# # 实例3 log1p(x) is more accurate for values of x
# import math
#
# x = 0.0000000000000000000000001
# print('x:', x)
# print('1 + x:', 1 + x)
# print('log(1+x):', math.log(1+x))
# print('log1p(x):', math.log1p(x))
# # 指数
# # 实例1
# import math
# x = 2
# fmt = '%.20f'
# print(fmt % (math.e ** 2))
# print(fmt % math.pow(math.e, 2))
# print(fmt % math.exp(2))
# # 11 双曲函数(Hyperbolic Functions)
# import math
# print('{:^6} {:^6} {:^6} {:^6}'.format(
# 'X', 'sinh', 'cosh', 'tanh',
# ))
# print('{:-^6} {:-^6} {:-^6} {:-^6}'.format('', '', '', ''))
# fmt = ' '.join(['{:6.4f}'] * 4)
# for i in range(0, 11, 2):
#     x = i/10.0
#     print(fmt.format(x, math.sinh(x), math.cosh(x), math.tanh(x)))
#

# 2.5字符串
# 支持单，双，三引号：python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
# print('''python... is cool''' )
# para_str = """这是一个多行字符串的实例
# 多行字符串可以使用制表符
# TAB ( \t )。
# 也可以使用换行符 [ \n ]。
# """
# print((para_str))
# 字符串截取：
# var1 = 'Hello World!'
# var2 = "Runoob"
# print("var1[0]: ", var1[0])
# print("var2[1:5]: ", var2[1:5])
# print(("已更新字符串 : ", var1[:6] + 'Runoob!')
# 字符串运算:
# +	字符串连接	a + b 输出结果： HelloPython
# *	重复输出字符串	a*2 输出结果：HelloHello
# []	通过索引获取字符串中字符	a[1] 输出结果 e
# [ : ]	截取字符串中的一部分	a[1:4] 输出结果 ell
# in	成员运算符 - 如果字符串中包含给定的字符返回 True	H in a 输出结果 1
# not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	M not in a 输出结果 1
# r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	print(r'\n' prints \n 和 print(R'\n' prints \n
# %	格式字符串	请看下一节内容。
# a = "Hello"
# b = "Python"
# print("a + b 输出结果：", a + b)
# print("a * 2 输出结果：", a * 2)
# print("a[1] 输出结果：", a[1])
# print("a[1:4] 输出结果：", a[1:4])
# if "H" in a:
#     print("H 在变量 a 中")
# else:
#     print("H 不在变量 a 中")
# if "M" not in a:
#     print("M 不在变量 a 中")
# else:
#     print("M 在变量 a 中")
# print(r'\n')
# print(R'\n')
# print(("我叫 %s 今年 %d 岁!" % ('小明', 10))
# 字符串函数：
# 1
# capitalize()
# 将字符串的第一个字符转换为大写
# 2
# center(width, fillchar)
# 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
# 3
# count(str, beg= 0,end=len(string))
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
# 4
# bytes.decode(encoding="utf-8", errors="strict")
# Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
# 5
# encode(encoding='UTF-8',errors='strict')
# 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
# 6
# endswith(suffix, beg=0, end=len(string))
# 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
# 7
# expandtabs(tabsize=8)
# 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
# 8
# find(str, beg=0 end=len(string))
# 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
# 9
# index(str, beg=0, end=len(string))
# 跟find()方法一样，只不过如果str不在字符串中会报一个异常.
# 10
# isalnum()
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
# 11
# isalpha()
# 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
# 12
# isdigit()
# 如果字符串只包含数字则返回 True 否则返回 False..
# 13
# islower()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
# 14
# isnumeric()
# 如果字符串中只包含数字字符，则返回 True，否则返回 False
# 15
# isspace()
# 如果字符串中只包含空白，则返回 True，否则返回 False.
# 16
# istitle()
# 如果字符串是标题化的(见 title())则返回 True，否则返回 False
# 17
# isupper()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
# 18
# join(seq)
# 连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
# seq3 = ('hello','good','boy','doiido')
# print(':'.join(seq3))
# # hello:good:boy:doiido
# 19
# len(string)
# 返回字符串长度
# 20
# ljust(width[, fillchar])
# 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
# 21
# lower()
# 转换字符串中所有大写字符为小写.
# 22
# lstrip()
# 截掉字符串左边的空格或指定字符。
# 23
# maketrans()
# 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# 24
# max(str)
# 返回字符串 str 中最大的字母。
# 25
# min(str)
# 返回字符串 str 中最小的字母。
# 26
# replace(old, new [, max])
# 把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
# 27
# rfind(str, beg=0,end=len(string))
# 类似于 find()函数，不过是从右边开始查找.
# 28
# rindex( str, beg=0, end=len(string))
# 类似于 index()，不过是从右边开始.
# 29
# rjust(width,[, fillchar])
# 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
# 30
# rstrip()
# 删除字符串末尾的空格.
# 31
# split(str="", num=string.count(str))
# num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串
# 32
# splitlines([keepends])
# 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
# 33
# startswith(str, beg=0,end=len(string))
# 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
# 34
# strip([chars])
# 在字符串上执行 lstrip()和 rstrip()
# 35
# swapcase()
# 将字符串中大写转换为小写，小写转换为大写
# 36
# title()
# 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
# 37
# translate(table, deletechars="")
# 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
# 38
# upper()
# 转换字符串中的小写字母为大写
# 39
# zfill (width)
# 返回长度为 width 的字符串，原字符串右对齐，前面填充0
# 40
# isdecimal()
# 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
#
# 常用模板：
# string 字符串操作相关函数和工具，比如 Template 类.
# re 正则表达式:强大的字符串模式匹配模块
# struct 字符串和二进制之间的转换
# c/StringIO 字符串缓冲对象，操作方法类似于 file 对象.
# base64 Base 16,32,64 数据编解码
# codecs 解码器注册和基类
# crypt 进行单方面加密
# diffliba 找出序列间的不同
#  hashlibb 多种不同安全哈希算法和信息摘要算法的 API
# hmac HMAC 信息鉴权算法的 Python 实现
# md5d RSA 的 MD5 信息摘要鉴权
# rotor 提供多平台的加解密服务
# shad NIAT 的安全哈希算法 SHA
# stringprepe 提供用于 IP 协议的 Unicode 字符串
# textwrape 文本打包和填充
# unicodedata Unicode 数据库
# struct：
# import struct
# import binascii
#
# values = (1, b'abc', 2.7) # bytes类型前面要加b
# s = struct.Struct('I3sf')
# # s = struct.Struct('i4sh')
# packed_data = s.pack(*values)
# unpacked_data = s.unpack(packed_data)
#
# print('Original values:', values)
# print('Format string :', s.format)
# print('Uses :', s.size, 'bytes')
# print('Packed Value :', binascii.hexlify(packed_data))
# print('Unpacked Type :', type(unpacked_data), ' Value:', unpacked_data)
#

# # 2.6列表，元组
# # 区别：
# # 列表和元组可以存储不同类型的对象,索引从0开始.列表和元组有几处重要的区别。列表元素用中括号( [ ])包裹，元素的个数及元素的值可
# # 以改变。元组元素用小括号(( ))包裹，不可以更改（尽管他们的内容可以）。元组可以看成是
# # 只读的列表。
# #截取:
# aList = [1, 2, 3, 4]
# print(aList[:3])
# print(aList[2:])
# print(aList[-2:])#从右侧截取
# aTuple = ('robots', 77, 93, 'try')
# print(aTuple[:3])
# print(aTuple[0])
# # 更新：
# aList[2] = 2001
# print(("更新后的第三个元素为 : ", aList[2])
# # 删除:
# del aList[2]
# # 操作符：
# len([1, 2, 3]) #	3	长度
# [1, 2, 3] + [4, 5, 6]#	[1, 2, 3, 4, 5, 6]	组合
# ['Hi!'] * 4	#['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
# 3 in [1, 2, 3]#	True	元素是否存在于列表中
# for x in [1, 2, 3]: print(x, end=" ")#	1 2 3	迭代
# # 嵌套列表
# print([['a', 'b', 'c'], [1, 2, 3]])
# # list方法
# # 1	len(list)
# # 列表元素个数
# # 2	max(list)
# # 返回列表元素最大值
# # 3	min(list)
# # 返回列表元素最小值
# # 1	list.append(obj)
# # 在列表末尾添加新的对象
# # 2	list.count(obj)
# # 统计某个元素在列表中出现的次数
# # 3	list.extend(seq)
# # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# # 4	list.index(obj)
# # 从列表中找出某个值第一个匹配项的索引位置
# # 5	list.insert(index, obj)
# # 将对象插入列表
# # 6	list.pop(obj=list[-1])
# # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# # 7	list.remove(obj)
# # 移除列表中某个值的第一个匹配项
# # 8	list.reverse()
# # 反向列表中元素
# # 9	list.sort([func])
# # 对原列表进行排序，没有返回值的
# # 10	list.clear()
# # 清空列表
# # 11	list.copy()
# list = [1,2]
# list2 = list.copy()
# print(id(list),id(list2))
# print(list is list2)
# # 复制列表
# # 浅拷贝和深拷贝
# # 浅拷贝：复制，子集的变化会影响原始数据
# # 深拷贝：复制，子集不会影响原始数据
# # 浅拷贝：
# print("浅拷贝----->")
# hubby = ['joe', ['savings', 100.00]]
# wifey = hubby.copy()
# print([id(x) for x in [hubby, wifey]])
# wifey[0] = "james"
# print(hubby, wifey)
# hubby[1][1] = 50.00
# print(hubby, wifey)
# # 深拷贝：
# print("深拷贝------>")
# hubby = ['joe', ['savings', 100.00]]
# import copy
# wifey = copy.deepcopy(hubby)
# print([id(x) for x in [hubby, wifey]])
# wifey[0] = "james"
# print(hubby, wifey)
# hubby[1][1] = 50.00
# print(hubby, wifey)
#

# # 2.7字典
# # 定义:由键-值(key-value)对构成。几乎所有类型的 Python 对象都可以用作键，不过一般还是以数字或者字符串最为常用。字典本身是哈希的，所以是无序的。哈希表一般有很好的性能，因此用键查询相当快。
# # 值可以是任意类型的 Python 对象，字典元素用大括号({ })包裹。键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
# # 而用列表就不行
# aDict = {'host': 'earth'}  # create dict
# # 工厂法创建
# fdict = dict((['x', 1], ['y', 2]))
# print(fdict)
# ddict = {}.fromkeys(('x', 'y'), -1)
# print(ddict) # {'x': -1, 'y': -1}
# edict = {}.fromkeys(('foo', 'bar'))
# print(edict) #{'foo': None, 'bar': None}
# # 访问:
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print(("dict['Name']: ", dict['Name'])
# print(("dict['Age']: ", dict['Age'])
# dict2 = {'name': 'earth', 'port': 80}
# for key in dict2.keys():
#     print('key=%s, value=%s' % (key, dict2[key]))
# for num,key in enumerate(dict2):
#     print(num,key,dict2[key])
# # 更新,增加：
# dict['Age'] = 8;               # 更新 Age
# dict['School'] = "菜鸟教程"  # 添加信息
# # 删除:
# del dict['Name'] # 删除键 'Name'
# dict.clear()     # 删除字典
# del dict         # 删除字典
# # 字典函数：
# # 1	len(dict)
# # 计算字典元素个数，即键的总数。
# # >>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# # >>> len(dict)
# # 2	str(dict)
# # 输出字典，以可打印的字符串表示。
# # >>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# # >>> str(dict)
# # "{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"
# # 3	type(variable)
# # 返回输入的变量类型，如果变量是字典就返回字典类型。
# # >>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# # >>> type(dict)
# # <class 'dict'>
# # 1	radiansdict.clear()
# # 删除字典内所有元素
# # 2	radiansdict.copy()
# # 返回一个字典的浅复制
# dic1 = {"s":1}
# dic2 = dic1.copy()
# print(id(dic1),id(dic2))
# # 3	radiansdict.fromkeys()
# # 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# # 4	radiansdict.get(key, default=None)
# # 返回指定键的值，如果值不在字典中返回default值
# # 5	key in dict
# # 如果键在字典dict里返回true，否则返回false
# # 6	radiansdict.items()
# # 以列表返回可遍历的(键, 值) 元组数组
# # 7	radiansdict.keys()
# # 以列表返回一个字典所有的键
# # 8	radiansdict.setdefault(key, default=None)
# # 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# # 9	radiansdict.update(dict2)
# # 把字典dict2的键/值对更新到dict里
# dict1 = {"x":1,"y":2}
# dict2 = {"z":3}
# dict1.update(dict2)
# print(str(dict1))
# # 10	radiansdict.values()
# # 以列表返回字典中的所有值
# # 11	pop(key[,default])
# # 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
# # 12	popitem()
# # 随机返回并删除字典中的一对键和值(一般删除末尾对)。
# # 字典的键值是"只读"的，所以不能对键和值分别进行初始化，即以下定义是错的：
# dic = {}
# dic.keys = (1,2,3,4,5,6)
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # AttributeError: 'dict' object attribute 'keys' is read-only
# dic.values = ("a","b","c","d","e","f")
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # AttributeError: 'dict' object attribute 'values' is read-only
# # 字典是支持无限极嵌套的
# citys={
#     '北京':{
#         '朝阳':['国贸','CBD','天阶','我爱我家','链接地产'],
#         '海淀':['圆明园','苏州街','中关村','北京大学'],
#         '昌平':['沙河','南口','小汤山',],
#         '怀柔':['桃花','梅花','大山'],
#         '密云':['密云A','密云B','密云C']
#     },
#     '河北':{
#         '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
#         '张家口':['张家口A','张家口B','张家口C'],
#         '承德':['承德A','承德B','承德C','承德D']
#     }
# }
# for i in citys['北京']:
#     print(i)
# # 排序:
# # sorted(dic,value,reverse)
# dic = {'a': 3, 'b': 2, 'c': 1, 'z': 33, 'd': 222}
# # 按key排序
# print(sorted(dic.items(), key=lambda item: item[0], reverse=True))
# print(dic)
# print(sorted(dic.keys()))
# print(dic)
# # 按值排序
# print(sorted(dic.items(), key=lambda item: item[1], reverse=False))
# print(type(sorted(dic.items(), key=lambda item: item[1], reverse=False))) #<class 'list'>
# print(dic)
# # 遍历+比较 注意cmp()函数已被取消
# f = {'x': 2, 'y': 1, 'z': 3}
# d = {'x': 1, 'y': 2, 'z': 3}
# for key1 in f:
#     for key2 in d:
#         if key1 == key2:
#             print(key1, 'f corresponds to', f[key1])
#             print(key2, 'd corresponds to', d[key2])
#             if f[key1] > d[key2]:
#                 print("f > d")
#             elif f[key1] == d[key2]:
#                 print("f == d")
#             else:
#                 print("f < d")

# # 2.8类型转换
# # 数值转换：int(x) 将x转换为一个整数。float(x) 将x转换到一个浮点数。complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
# # list(seq):将元组转换为列表 tuple(seq):将列表转换为元组。
# # string,list互转:
# image ='1.jsp,2.jsp,3.jsp,4.jsp'
# image_list = image.strip(',').split(',')
# print(image_list)
# str_convert = ''.join(image_list)
# str_convert2 = str(image_list)
# print(str_convert)
# print(str_convert2)
# # string转字典：
# a='{"name":"yct","age":10,"tmp":"dddd"}'
# print(eval(a)["name"])
# # str(x )                 将对象 x 转换为字符串
# print(str(1))
# # repr(x )                将对象 x 转换为表达式字符串
# print( repr([0, 5, 9, 9]) )
#  str,repr类似。repr() 输出对 Python 比较友好， 而 str()的输出对人比较友好。
# # eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象
# # chr(x )                 将一个整数转换为一个字符
# # unichr(x )              将一个整数转换为Unicode字符
# # ord(x )                 将一个字符转换为它的整数值
# # hex(x )                 将一个整数转换为一个十六进制字符串
# # oct(x )                 将一个整数转换为一个八进制字符串
#

# # 2.9if
# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age < 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age -2)*5
#     print("对应人类年龄: ", human)
# # 8.1三元运算
# x = input("x")
# y = input("y")
# smaller = x if x < y else y
# print(smaller)
#

# # 2.10循环
# # while:
# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
# print("1 到 %d 之和为: %d" % (n, sum))
# # while else:
# count = 0
# while count < 5:
#     print(count, " 小于 5")
#     count = count + 1
# else:
#     print(count, " 大于或等于 5")
# # 简单语句:
# flag = 1
# while flag: print('欢迎访问菜鸟教程!')
# print("Good bye!")
# # for:
# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!")
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")
# # 结合enumerate输出序列号:
# nameList = ['Donn', 'Shirley', 'Ben', 'Janice','David', 'Yen', 'Wendy']
# for i, eachLee in enumerate(nameList):
#     print("%d %s Lee" % (i+1, eachLee))
# # 其他序列相关函数：sorted(), reversed(), zip() (( sorted() 和 zip() )返回一个序列(列表))(( reversed() 和 enumerate() ) 返回迭代器(类似序列) ):
# albums = ('Poe', 'Gaudi', 'Freud', 'Poe2')
# years = (1976, 1987, 1990, 2003)
# for album in sorted(albums):
#     print(album)
# for album in reversed(albums):
#     print(album)
# for i, album in enumerate(albums):
#     print(i, album)
# for album, yr in zip(albums, years):
#     print(yr, album)
# # range():
# # 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
# for i in range(5):
#     print(i)
# # break:
# for letter in 'Runoob':  # 第一个实例
#     if letter == 'b':
#         break
#     print('当前字母为 :', letter)
#
# var = 10  # 第二个实例
# while var > 0:
#     print('当期变量值为 :', var)
#     var = var - 1
#     if var == 5:
#         break
# print("Good bye!")
# # continue:
# for letter in 'Runoob':  # 第一个实例
#     if letter == 'o':  # 字母为 o 时跳过输出
#         continue
#     print('当前字母 :', letter)
#
# var = 10  # 第二个实例
# while var > 0:
#     var = var - 1
#     if var == 5:  # 变量为 5 时跳过输出
#         continue
#     print('当前变量值 :', var)
# print("Good bye!")
# # pass:
# # Python pass是空语句，是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句
# for letter in 'Runoob':
#     if letter == 'o':
#         pass
#         print('执行 pass 块')
#     print('当前字母 :', letter)
# print("Good bye!")
# # 循环中的else：
# # 在循环中使用时, else
# # 子句只在循环完成后执行, 也就是说 break 语句也会跳过 else 块.
# # 最大公约数案例为例子：
# def showMaxFactor(num):
#     count = num // 2
#     while count > 1:
#         if num % count == 0:
#             print('largest factor of %d is %d' % (num, count))
#         else:
#             print('%d has not factor'% (num))
#         break
#         count -= 1
#     else:
#         print(num, "is prime")
# for eachNum in range(1, 21):
#     showMaxFactor(eachNum)
# # 9*9乘法表
# i = 1
# while i <= 9:
#     #里面一层循环控制每一行中的列数
#     j = 1
#     while j <= i:
#         mut = j * i
#         print("%d*%d=%d" % (j, i, mut), end="  ")
#         j += 1
#     print("")
#     i += 1
# # 1-100值和
# print(sum(range(101)))
# # 遍历文件:
# myFile = open('config-win.txt')
# for eachLine in myFile:
#     print(eachLine) # comma suppresses extra \n
#

# # 2.11列表解析：
# #1 map类:
# map1 = map(lambda x: x ** 2, range(6))
# for i in map1:
#     print(i)
# print(map1)
# # [expr for iter_var in iterable]
# squared = [x ** 2 for x in range(4)] # 等价上式
# for i in squared:
#     print(i)
# #2 挑选奇数:
# seq = [11, 10, 9, 9, 10, 10, 9, 8, 23, 9, 7, 18, 12, 11, 12]
# seqfile = filter(lambda x: x % 2, seq)
# for i in seqfile:
#     print(i)
# # [expr for iter_var in iterable if cond_expr]
# seqfile2 = [x for x in seq if x % 2]  # 等价上式
# for i in seqfile2:
#     print(i)
# sqdEvens = [x ** 2 for x in range(8) if not x % 2]
# for i in sqdEvens:
#     print(i)
# # 迭代3*5的矩阵:
# matrix1 = [(x + 1, y + 1) for x in range(3) for y in range(5)]
# for i,j in matrix1:
#     print(i,j)
# # 文件遍历：
# f = open('hhga.txt', 'r')
# print(len([word for line in f for word in line.split()]))
# # 快速计算文件大小：
# import os
# os.stat('hhga.txt').st_size
# # 计算单词长度合：
# f.seek(0)
# sum([len(word) for line in f for word in line.split()])
#

# # 2.12生成器:
# # 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# # 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行 next()方法时从当前位置继续运行。
# # 一个函数 f，f 返回一个 list，这个 list 是动态计算出来的（不管是数学上的计算还是逻辑上的读取格式化），并且这个 list 会很大（无论是固定很大还是随着输入参数的增大而增大），
# # 这个时候，我们希望每次调用这个函数并使用迭代器进行循环的时候一个一个的得到每个 list 元素而不是直接得到一个完整的 list 来节省内存，这个时候 yield 就很有用。
# import sys
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if counter > n:
#             return
#         yield a # 将a保存到要返回的iter里面
#         a, b = b, a + b
#         counter += 1
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()
# # 交叉配对：
# rows = [1, 2, 3, 17]
# def cols(): # example of simple generator
#     yield 56
#     yield 2
#     yield 1
# x_product_pairs = ((i, j) for i in rows for j in cols())
# for pair in x_product_pairs:
#     print(pair)
# # 文件重构:
# # return max(len(x.strip()) for x in open('/etc/motd'))
#

# # 2.13迭代器及 iter() 函数
# #  Python 的迭代无缝地支持序列对象, 而且它还允许程序员迭代非序列类型, 包括用户定义的对象.是访问集合元素的一种方式
#
# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# print(next(it))   # 输出迭代器的下一个元素
# print(next(it))
# # for x in it:
# #     print(x, end=" ")
# import sys
# while True:
#     try:
#         print((next(it)),end=" ")
#     except StopIteration:
#         sys.exit()
# a = set('cheeseshop')
# it2 = iter(a)
# for x in it2:
#     print(x,end=";")