# String
#
# # 1.1 Template类(可以用来制作web页面的模板)
# # Template实例1：
# import string
# values = {'var':'foo'}
# t = string.Template("""
# Variable : $var
# Escape : $$
# Variable in text: ${var}iable
# """)
# print('TEMPLATE:', t.substitute(values))
# # Template例子2:
# import string
# template_text = '''
# Delimiter : %%
# Replaced : %with_underscore
# Ignored : %notunderscored
# '''
# d = {'with_underscore':'replaced', 'notunderscored':'not replaced'}
# # 重写Template类的匹配表达式.
# class MyTemplate(string.Template):
#     delimiter = '%'
#     idpattern = '[a-z]+_[a-z]+'  #notunderscored不属于匹配项，所以无法替换。not_underscored就可以替换掉。
# t = MyTemplate(template_text)
# print('Modified ID pattern:',t.safe_substitute(d))  #substitute比较严格，必须每一个占位符都找到对应的变量，不然就会报错，而safe_substitute则会把未找到的$XXX直接输出
#

# # 1.2 textwrap模板
# # 1实例1,wrap()按宽度分割.(fill(text[, width[, …]])类似，返回结果形式稍微不同)
# import textwrap
# sample_text = '''aaabbbcccdddeeeedddddfffffggggghhhhhhkkkkkkk'''
# sample_text2 = '''aaa bbb ccc ddd eeee ddddd fffff ggggg hhhhhh kkkkkkk'''
#
# print(sample_text)
# print(textwrap.wrap(sample_text,width=5))
# print(textwrap.wrap(sample_text2,width=5))
# # 2 dedent()类似tirm()
# import textwrap
# sample_text = '''
#     aaabbb
#                 cccdddee    eedddddfffffggggghhhhhhkkkkkkk'''
# print(sample_text)
# print(textwrap.dedent(sample_text))
# # 3 TextWrapper类设置
# import textwrap
# sample_text = '''   aaa'''
# textWrap = textwrap.TextWrapper()
# textWrap.expand_tabs = True  #字符串里的所有制表符都会被变成空格，相当于用了字符串方法的expandtabs()。
# textWrap.replace_whitespace = True  #replace_whitespace：如果设置为true，那么就会把字符串中的空白符转化为空格。
# textWrap.drop_whitespace = True  #drop_whitespace：默认true，如果设置为true，则每行开头和结尾的空白符都会被去掉，如果要去掉的空白符占据了整行，那么就会把整行去掉。
# textWrap.width = 2
# print(textWrap.wrap(sample_text))
# textWrap.initial_indent = 'bbb'  #初始化头部
# print(textWrap.wrap(sample_text))  #['bbb   aaa']
# textWrap.subsequent_indent = 'bbb'  #初始化头部外的所有行
# # fix_sentence_endings：默认为false，如果为true，那么就会试图检查每个句子的结尾是两个空格分割，这个只在等宽字体里被需要。但是这个检查的算法是有缺陷的，它假设了句子是以.!?等这些字符为结尾。
# # break_long_words：默认为true，切断长句子来让每行的数据宽度都小于width。
# # break_on_hyphens：连字符相关，默认true
#
#