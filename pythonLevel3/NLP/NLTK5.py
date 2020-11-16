# 分类和标注词汇

import nltk

# # 5.1 词性标注器
# text = nltk.word_tokenize("And now for something completely different")
# #词性标注器 在这里我们看到 and 是 CC，并列连词；now 和 completely 是 RB，
# # 副词；for 是 IN，介词；something 是 NN，名词；different 是 JJ，形容词。
# print(nltk.pos_tag(text))
# text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
# # 搜索 woman 找到名词；搜索 bought 找到的大部分是动词；搜索 over 一般会找到介词；搜索 the 找到几个限定词
# print(text.similar("woman"))  #找出拥有相同上下文的词
# print(text.similar('bought'))
# print(text.similar('over'))
# print(text.similar('the'))


# # 5.2 标注语料库(查看P175简化词性标记)
# # 1
# # 按照 NLTK 的约定，一个已标注的标识符使用一个由标识符和标记组成的元组来表示。
# # 我们可以使用函数str2tuple()从表示一个已标注的标识符的标准字符串创建一个这样的特殊元组
# tagged_token = nltk.tag.str2tuple('fly/NN')
# print(tagged_token)
# # 2 读取已标注的语料库
# print(nltk.corpus.brown.tagged_words())
# print(nltk.corpus.nps_chat.tagged_words())
# print(nltk.corpus.conll2000.tagged_words())
# print(nltk.corpus.treebank.tagged_words())
# # print(nltk.corpus.sinica_treebank.tagged_words())
# print(nltk.corpus.conll2002.tagged_words())
# # print(nltk.corpus.mac_morpho.tagged_words())
# # 3 简化标记
# # 名词
# from nltk.corpus import brown
# brown_news_tagged = brown.tagged_words(categories='news')
# tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
# print(tag_fd.keys())
# word_tag_pairs = nltk.bigrams(brown_news_tagged)
# print(list(nltk.FreqDist(a[1] for (a, b) in word_tag_pairs if b[1] == 'N')))
# # 动词
# wsj = nltk.corpus.treebank.tagged_words()
# word_tag_fd = nltk.FreqDist(wsj)
# print([word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('V')])
# cfd1 = nltk.ConditionalFreqDist(wsj)
# print(cfd1['yield'])
# print(cfd1['yield'].keys())  #返回cfd1['yield']的键集合(dict_keys(['VB', 'NN']) 词性标记集合)
# print(cfd1['cut'].keys())
# cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in wsj)
# print(cfd2['VBN'].keys())  #['seen', 'wanted', 'sought', 'corrected', 'heated', 'Estimated', 'condemned', 'pursued'...] 对应词性词汇集合
# # 要弄清 VD（过去式）和 VN（过去分词）之间的区别，让我们找到可以同是 VD 和 V
# # N 的词汇，看看一些它们周围的文字：
# print([w for w in cfd1.conditions() if 'VBD' in cfd1[w] and 'VBN' in cfd1[w]])
# # 形容词和副词
# # 4 未简化标记
# # 找出最频繁的名词标记的程序
# def findtags(tag_prefix, tagged_text):
#     cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text if tag.startswith(tag_prefix))
#     return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())
# tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))
# for tag in sorted(tagdict):
#     print(tag, tagdict[tag])
# # 跟在ofen后面的词语
# from nltk.corpus import brown
# brown_learned_text = brown.words(categories='learned')
# print(sorted(set(b for (a, b) in nltk.ibigrams(brown_learned_text) if a == 'often')))  #ofen accomplished/ofen associated
# # 查看跟随ofen后面那的词语词性分布
# brown_lrnd_tagged = brown.tagged_words(categories='learned', simplify_tags=True)
# tags = [b[1] for (a, b) in nltk.ibigrams(brown_lrnd_tagged) if a[0] == 'often']
# fd = nltk.FreqDist(tags)
# print(fd.tabulate())
# # 较大范围的上下文
# from nltk.corpus import brown
# def process(sentence):
#     for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
#         if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
#             print(w1, w2, w3)
# for tagged_sent in brown.tagged_sents():
#     process(tagged_sent)
# # 较大范围上下文词性
# from nltk.corpus import brown
# brown_news_tagged = brown.tagged_words(categories='news')
# data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_news_tagged)
# for word in data.conditions():
#     if len(data[word]) > 3:
#         tags = data[word].keys()
#         print(word, ' '.join(tags))


# 5.3 使用 Python 字典映射词及其属性

# 5.4 自动标注
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
# # 1 默认标注器
# tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
# nltk.FreqDist(tags).max()
# raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
# tokens = nltk.word_tokenize(raw)
# default_tagger = nltk.DefaultTagger('NN')
# print(default_tagger.tag(tokens))
# print(default_tagger.evaluate(brown_tagged_sents))
# # 2 正则标注器
# patterns = [
# (r'.*ing$', 'VBG'), # gerunds  #带ing结尾的认为是动词进行时.
# (r'.*ed$', 'VBD'), # simple past
# (r'.*es$', 'VBZ'), # 3rd singular present
# (r'.*ould$', 'MD'), # modals
# (r'.*\'s$', 'NN$'), # possessive nouns
# (r'.*s$', 'NNS'), # plural nouns
# (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
# (r'.*', 'NN') # nouns (default)
# ]
# regexp_tagger = nltk.RegexpTagger(patterns)
# regexp_tagger.tag(brown_sents[3])
# print(regexp_tagger.evaluate(brown_tagged_sents))
# # 3 查询标注器
# def performance(cfd, wordlist):
#     lt = dict((word, cfd[word].max()) for word in wordlist)
#     baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
#     return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))  # 0.6789983491457326
# def display():
#     import pylab
#     words_by_freq = list(nltk.FreqDist(brown.words(categories='news')))
#     cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
#     sizes = 2 ** pylab.arange(15)
#     perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
#     pylab.plot(sizes, perfs, '-bo')  #plot(x, y) x轴，y轴数据
#     pylab.title('Lookup Tagger Performance with Varying Model Size')
#     pylab.xlabel('Model Size')
#     pylab.ylabel('Performance')
#     pylab.show()
# display()
# # 4 一元(1-gram)标注器(一元标注器基于一个简单的统计算法：对每个标识符分配这个独特的标识符最有可能的标记)
# # (1)生成一元标注器
# from nltk.corpus import brown
# brown_tagged_sents = brown.tagged_sents(categories='news')
# brown_sents = brown.sents(categories='news')
# unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)  #生成一元标注器
# print(unigram_tagger.tag(brown_sents[2007]))
# print(unigram_tagger.evaluate(brown_tagged_sents))  #正确率  0.9349006503968017  比查询标注器高
# # (2) 分离训练和测试数据
# # 我们应该分割数据，90％为测试数据，其余 10％为测试数据：
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
unigram_tagger = nltk.UnigramTagger(train_sents)
# print(unigram_tagger.evaluate(test_sents))
# #  (3)一般的N元（N-gram） 的标注
# bigram_tagger = nltk.BigramTagger(train_sents)  #n元标注器
# bigram_tagger.tag(brown_sents[2007])
# unseen_sent = brown_sents[4203]
# bigram_tagger.tag(unseen_sent)
# print(bigram_tagger.evaluate(test_sents))  #正确率低，无法完成标注新词任务,原因是数据稀疏问题,所以精度和覆盖范围之间需要有一个权衡
# 5 组合标注器
# 1. 尝试使用 bigram 标注器标注标识符。
# 2. 如果 bigram 标注器无法找到一个标记，尝试 unigram 标注器。
# 3. 如果 unigram 标注器也无法找到一个标记，使用默认标注器。
# t0 = nltk.DefaultTagger('NN')  #指定回退标注器
# t1 = nltk.UnigramTagger(train_sents, backoff=t0)
# t2 = nltk.BigramTagger(train_sents, backoff=t1)
# print(t2.evaluate(test_sents))
# 6 标注生词