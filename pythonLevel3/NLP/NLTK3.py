from __future__ import division
import nltk, re, pprint

# 3.1 访问网络电子书
from urllib.request import urlopen
url = "http://www.gutenberg.org/files/2554/2554.txt"
raw = urlopen(url).read()
print(len(raw))
# 指定代理的读取网络文件
proxies = {'http': 'http://www.someproxy.com:3128'}
raw = urlopen(url, proxies=proxies).read()
# 分词(NLTK 自带正则分词器)
tokens = nltk.word_tokenize(raw)  # 产生我们所熟悉的结构，一个词汇和标点符号的链表
text = nltk.Text(tokens)
# 寻找文本开头结束位置.
raw.find("PART I")
raw.rfind("End of Project Gutenberg's Crime")

# 3.2 处理的 HTML
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read()
raw = nltk.clean_html(html)  #返回原始文本
tokens = nltk.word_tokenize(raw)
# 寻找开头结尾,获得需要的文本
# 2 处理搜索引擎结果

# 3.3 词干提取器(自带/正则自定义0

# 3.4 词形归并
