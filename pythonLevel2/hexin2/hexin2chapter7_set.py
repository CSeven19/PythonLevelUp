# 7.1 set
s = set('cheeseshop')
print(s) # {'e', 'h', 'p', 'o', 's', 'c'}
print(type(s))
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # 删除重复的{'orange', 'banana', 'pear', 'apple'}
print('orange' in basket)                 # 检测成员True
print('crabgrass' in basket)    #False
print('crabgrass' not in basket)    #True
# 以下演示了两个集合的操作:
#  集合类型操作符:
a = set('abracadabra')
b = set('alacazam')
print(a)                                  # a 中唯一的字母{'a', 'r', 'b', 'c', 'd'}
print(a - b)                             # 在 a 中的字母，但不在 b 中{'r', 'd', 'b'}
print(a | b)                              # 在 a 或 b 中的字母{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)                              # 在 a 和 b 中都有的字母{'a', 'c'}
print(a ^ b)                              # 在 a 或 b 中的字母，但不同时在 a 和 b 中{'r', 'd', 'b', 'm', 'z', 'l'}
a &= set('shop')
a |= set('pypi')
a -= set('pypi')
a ^= set('pypi')
print(a)
u = frozenset(a) #frozenset不可变集合
u |= set('pypidmm')
print(u)
print(u | b)
# 比较关系:
print(a == b)
print(a != b)
# 判断a,b的包含关系，超集，子集.
print(a <= b)
print(a >= b)
# 遍历:
for i in s:
    print(i)
# 增删改:
s.add('z')
s.update('pypi')
s.remove('o')
for i in s:
    print(i)
del s
# BIF:
# s.issubset(t) 如果s是t 的子集，则返回 True,否则返回 False
# s.issuperset(t) 如果t是s 的超集，则返回 True,否则返回 False
# s.union(t) 返回一个新集合，该集合是s和t 的并集
# s.intersection(t) 返回一个新集合，该集合是s和t 的交集
# s.difference(t) 返回一个新集合，该集合是 s 的成员，但不是 t 的成员
# s.symmetric_difference(t) 返回一个新集合，该集合是 s 或 t 的成员，但不是 s 和 t 共有的成员
# s.copy() 返回一个新集合，它是集合 s 的浅复制
# s.len()
# 仅适用于可变集合的： add(), remove(), discard(), pop(), clear()
print(len(a))
# 工厂函数:
print(set([]))
print(frozenset(['foo', 'bar']))
