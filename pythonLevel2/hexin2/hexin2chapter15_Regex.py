# 正则
#
# 15.1re
# re 模块的函数和 regex 对象的方法
# compile(pattern,flags=0) 将string 转换成 RegexObject ,对正则表达式模式 pattern进行编译，flags是可选标志符，并返回一个 regex 对象
# match(pattern,string, flags=0) 尝试用正则表达式模式 pattern 匹配字符串 string首部，flags 是可选标志符，如果匹配成功，则返回一个匹配对象；否则返回 None
# search(pattern,string, flags=0) 在整个字符串 string 中查找正则表达式模式 pattern 的第一次出现，flags 是可选标志符，如果匹配成功，则返回一个匹配对象；否则返回 None,允许在reg中使用()分组，可以用group(num)获得对应分组.
# findall(pattern,string[,flags]) 在整个字符串 string 中查找正则表达式模式 pattern 的所有(非重复)出现；返回一个匹配对象的列表
# finditer(pattern,string[, flags]) 和 findall()相同，但返回的不是列表而是迭代器；对于每个匹配，该迭代器返回一个匹配对象
# 匹配对象的方法
# split(pattern,string, max=0) 根据正则表达式 pattern 中的分隔符把字符 string 分割为一个列表，返回成功匹配的列表，最多分割 max 次(默认是分割所有匹配的地方)。
# sub(pattern, repl, string, max=0) 把字符串 string 中所有匹配正则表达式 pattern 的地方替换成字符串 repl,如果 max 的值没有给出，则对所有匹配的地方进行替换(另外，请参考 subn(),它还会返回一个表示替换次数的数值)。
# group(num=0) 返回全部匹配对象(或指定编号是 num 的子组)
# groups() 返回一个包含全部匹配的子组的元组(如果没有成功匹配，就返回一个空元组)
#
# # 1 compile,match(regex object),group()应用:
# import re
# regex = re.compile(r'foo')  # 'r'是防止字符转义的 如果路径中出现'\t'的话 不加r的话\t就会被转义 而加了'r'之后'\t'就能保留原有的样子
# result = re.match(regex, 'food on the table fooooo....')
# # result = regex.match('food on the table fooooo....')
# # result = r'foo'.match('food on the table fooooo....') 无法运行
# print(result)
#
# # 2 search(),match()区别:
# # match ("匹配")/search() ("搜索")
# # re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
# m = re.match('foo', 'seafood')  # no match 匹配失败
# if m is not None:
#     print("match:"+m.group(0))
# else:
#     print("can't match foo ,because 头部没有该foo")
#
# import re
# n = re.search('foo', 'sea food foood fooood')
# if n:
#     print("search:"+n.group(0)+" start at :"+str(n.start())+" end at :"+str(n.end()))  #search:foo start at :3 end at :6
#     print(n.groups())
#     # print("search:"+n.group(1)+" start at :"+str(n.start())+" end at :"+str(n.end()))  # 会报错。只能匹配到第一个搜索到的对象。
# else:
#     print("can't seach foo ,because整个句子都没有该foo")
#
# # 3 findall()
# #findall()和 match()与search()不同之处是，findall()总返回一个列表。同search相同点是检索整个str.
#
# # 4 sub(regex,newstr,str)
# import re
# newstr = re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
# print(newstr)
# # 5 split()
# split = re.split(':','str1:str2:str3')
# print(split)
#
# # 15.2高级
# # 实例1
# import re
# pattern = 'this'
# text = 'Does this text match the pattern?'
# match = re.search(pattern, text)
# s = match.start()
# e = match.end()
# print('Found "%s"\nin "%s"\nfrom %d to %d ("%s")'% (match.re.pattern, match.string, s, e, text[s:e]))
#
# # 实例2
# import re
# # Precompile the patterns
# regexes = [ re.compile(p) for p in ['this', 'that']]
# text = 'Does this text match the pattern?'
# print('Text: %r\n'% text)
# for regex in regexes:
#     print('Seeking "%s" ->'% regex.pattern,)
#     if regex.search(text):
#         print('match!')
#     else:
#         print('no match')
#
# # 实例3 findall() 返回匹配到的所有的List
# import re
# text = 'abbaaabbbbaaaaa'
# pattern = 'ab'
# for match in re.findall(pattern, text):
#     print('Found "%s"' % match)  #Found "ab"  \n Found "ab"
#
# # 实例4 finditer()
# import re
# text = 'abbaaabbbbaaaaa'
# pattern = 'ab'
# for match in re.finditer(pattern, text):
#     s = match.start()
#     e = match.end()
#     print('Found "%s" at %d:%d' % (text[s:e], s, e))  #返回迭代器而非List Found "ab" at 0:2  Found "ab" at 5:7
#
# # 实例5
# import re
# def test_patterns(text, patterns=[]):
#     """Given source text and a list of patterns, look for
#     matches for each pattern within the text and print
#     them to stdout.
#     """
#     # Look for each pattern in the text and print the results
#     for pattern, desc in patterns:
#         print('Pattern % r( % s)\n' % (pattern, desc))  #pattern = 'ab'  desc = "'a'  followed by 'b'"
#         print('% r' % text)
#         for match in re.finditer(pattern, text):
#             s = match.start()
#             e = match.end()
#             substr = text[s:e]
#             n_backslashes = text[:s].count('\\')  #str.count(sub, start= 0,end=len(string)) 用于统计字符串里某个字符出现的次数
#             prefix = '.'*(s + n_backslashes)
#             print('% s % r' % (prefix, substr))
#         print()
#     return
# if __name__ == '__main__':
#     test_patterns('abbaaabbbbaaaaa', [('ab', "'a'  followed by 'b'"), ])
#
# # 实例6 单词
# import re
# text = 'This is some text 12is23w-- with punctuation.'
# pattern = re.compile(r'\b\w*is\w*\b')  # \b单词边界，\w大小写字母或数字
# print('Text:', text)
# print()
# pos = 0
# while True:
#     match = pattern.search(text, pos)
#     if not match:
#         break
#     s = match.start()
#     e = match.end()
#     print('%2d : %2d = "%s"' % (s, e-1, text[s:e]))
#     # Move forward in text for the next search
#     pos = e
#
# # # 实例7
# import re
# text = 'This is some text -- with punctuation.'
# print(text)
# print()
# patterns = [
# (r'^(\w+)', 'word at start of string'),
# (r'(\w+)\S*$', 'word at end, with optional punctuation'),
# (r'(\bt\w+)\W+(\w+)', 'word starting with t, another word'),
# (r'(\w+t)\b', 'word ending with t')
# ]
# for pattern, desc in patterns:
#     regex = re.compile(pattern)
#     match = regex.search(text)
#     print('Pattern %r (%s)\n' % (pattern, desc))
#     print('',  match.groups())
#     print()
#
# # 实例8
# import re
#
# line = "Cats are smarter than dogs"
#
# # (.*) = group(1)  (.*?) = group(2)
# searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)  # 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
#
# if searchObj:
#    print("searchObj.groups() : ", searchObj.groups())
#    print("searchObj.group() : ", searchObj.group())  #匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
#    print("searchObj.group(0) : ", searchObj.group(0))
#    print("searchObj.group(1) : ", searchObj.group(1))
#    print("searchObj.group(2) : ", searchObj.group(2))
# else:
#    print("Nothing found!!")
#
# # 实例9
# import re
# m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
# print(m.groupdict())  # 返回一个包含所有命名组的名字和子串的字典，default参数，用于给那些没有匹配到的组做默认值，它的默认值是None
#
# # 实例10 search限制
# import re
# text = 'This is some text -- with punctuation.'
# pattern = r'\bT\w+'
# with_case = re.compile(pattern)
# without_case = re.compile(pattern, re.IGNORECASE)  #multiline = re.compile(pattern, re.MULTILINE)   dotall = re.compile(pattern, re.DOTALL) 匹配所有字符,包括换行符 re.LOCALE/re.UNICODE/re.VERBOSE 能够使用 REs 的 verbose 状态，使之被组织得更清晰易懂
# print('Text:\n %r' % text)
# print('Pattern:\n %s' % pattern)
# print('Case-sensitive:')
# for match in with_case.findall(text):
#     print(' %r' % match)
#     print('Case-insensitive:')
# for match in without_case.findall(text):
#     print('%r' % match)
#
# import re
# address = re.compile('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)',re.UNICODE)
# candidates = [
#     u'first.last@example.com',  #匹配到t@.com 打印了整个句子但是。
#     u'first.last+category@gmail.com',
#     u'valid-address@mail.example.com',
#     u'not-valid@example.foo',
# ]
# for candidate in candidates:
#     match = address.search(candidate)
#     print('%-30s %s' % (candidate, 'Matches' if match else 'No match'))

