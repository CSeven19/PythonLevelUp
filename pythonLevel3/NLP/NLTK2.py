#获取文本语料及词汇资源

import nltk
from nltk.corpus import gutenberg

# # 10.1获取文本语料

# print(gutenberg.fileids())
# emma = nltk.Text(gutenberg.words("austen-emma.txt"))
# print(emma.concordance("surprize"))

# # 10.2统计文本语料
# for fileid in gutenberg.fileids():
#     num_chars = len(gutenberg.raw(fileid))  #返回文本中出现的词汇个数，包括词之间的空格
#     num_words = len(gutenberg.words(fileid))  #
#     num_sents = len(gutenberg.sents(fileid))  #返回句子数
#     num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
#     print(int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid)  # ：平均词长、平均句子长度和本文中每个词出现的平均次数（我们的词汇多样性得分）。
#
# macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
# print(macbeth_sentences)

# # 10.3 网络文本，聊天记录
# # 网络文本
# from nltk.corpus import webtext
# for fileid in webtext.fileids():
#     print(fileid, webtext.raw(fileid)[:65], '...')
# # 聊天记录
# from nltk.corpus import nps_chat
# chatroom = nps_chat.posts('10-19-20s_706posts.xml')
# print(chatroom[123])

# # 10.4布朗语料库(参考P57 语料一览)
# from nltk.corpus import brown
# print(brown.categories())
# print(brown.words(categories='news'))
# print(brown.words(fileids=['cg22']))
# print(brown.sents(categories=['news', 'editorial', 'reviews']))
# # 文体学
# # (1)特定文体计数
# from nltk.corpus import brown
# news_text = brown.words(categories='news')
# fdist = nltk.FreqDist([w.lower() for w in news_text])
# modals = ['can', 'could', 'may', 'might', 'must', 'will']
# for m in modals:
#     print(m + ':', fdist[m], end=",")
# # (2)频率分布函数
# cfd = nltk.ConditionalFreqDist(
# (genre, word)
# for genre in brown.categories()
# for word in brown.words(categories=genre))
# genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']  #行索引,分类名
# modals = ['can', 'could', 'may', 'might', 'must', 'will']  #列,检索单词
# cfd.tabulate(conditions=genres, samples=modals)


# # 10.5 路透社语料库
# from nltk.corpus import reuters
# print(reuters.fileids())
# print(reuters.categories())
# print(reuters.categories('training/9865'))
# print(reuters.categories(['training/9865', 'training/9880']))
# print(reuters.fileids('barley'))
# print(reuters.fileids(['barley', 'corn']))
# print(reuters.words('training/9865')[:14])
# print(reuters.words(['training/9865', 'training/9880']))
# print(reuters.words(categories='barley'))
# print(reuters.words(categories=['barley', 'corn']))


# # 10.6 就职演说语料库(时间序列)
# from nltk.corpus import inaugural
# print(inaugural.fileids())
# print([fileid[:4] for fileid in inaugural.fileids()])
# cfd = nltk.ConditionalFreqDist(
#     (target, fileid[:4])
#     for fileid in inaugural.fileids()
#     for w in inaugural.words(fileid)
#     for target in ['america', 'citizen']
#     if w.lower().startswith(target))
# cfd.plot()


# # 10.7 其他语言的语料库
# # 世界人权宣言语料库中不同语言版本中的字长差异(y轴累计百分比。如Ibibio_Efik语中5字长以下的占比在80%)
# from nltk.corpus import udhr
# languages = ['Chickasaw', 'English', 'German_Deutsch',
#     'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
# cfd = nltk.ConditionalFreqDist(
#     (lang, len(word))
#     for lang in languages
#     for word in udhr.words(lang + '-Latin1'))
# cfd.plot(cumulative=True)


# 10.8 文本语料库的结构(参看P64 语料库函数一览)

# # 10.9 载入自己的语料库
# from nltk.corpus import PlaintextCorpusReader
# corpus_root = '/usr/share/dict'  # 默认自己文件地址
# wordlists = PlaintextCorpusReader(corpus_root, '.*')  # 载入函数
# print(wordlists.fileids())
# print(wordlists.words('connectives'))
# #
# from nltk.corpus import BracketParseCorpusReader
# corpus_root = r"C:\corpora\penntreebank\parsed\mrg\wsj"
# file_pattern = r".*/wsj_.*\.mrg"
# ptb = BracketParseCorpusReader(corpus_root, file_pattern)
# print(ptb.fileids())
# print(ptb.sents(fileids='20/wsj_2013.mrg')[19])

# # 2.10 条件频率分布(P69 方法一览)
# # 1 条件,事件
# # 每对的形式是：（条件，事件）。如果我们按文体处理整个布朗语料库，将有 15 个条件
# # （每个文体一个条件）和 1,161,192 个事件（每一个词一个事件）。
# # text = ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
# # pairs = [('news', 'The'), ('news', 'Fulton'), ('news', 'County'), ...]
# # 2 按文体计数词汇
# from nltk.corpus import brown
# cfd = nltk.ConditionalFreqDist(
#     (genre, word)
#     for genre in brown.categories()
#     for word in brown.words(categories=genre))
# print(len(cfd))

# 2.11 绘制分布图和分布表
# from nltk.corpus import inaugural
# cfd = nltk.ConditionalFreqDist(
#     (target, fileid[:4])
#     for fileid in inaugural.fileids()
#     for w in inaugural.words(fileid)
#     for target in ['america', 'citizen']
#     if w.lower().startswith(target))
# from nltk.corpus import udhr
# languages = ['Chickasaw', 'English', 'German_Deutsch',
#     'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
# cfd = nltk.ConditionalFreqDist(
#     (lang, len(word))
#     for lang in languages
#     for word in udhr.words(lang + '-Latin1'))
# cfd.tabulate(conditions=['English', 'German_Deutsch'],
#     samples=range(10), cumulative=True)

# #　2.12 使用双连词生成随机文本
# # sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven','and', 'the', 'earth', '.']
# # print(nltk.bigrams(sent))
# def generate_model(cfdist, word, num=155):
#     for i in range(num):
#         print(word, end=",")
#         word = cfdist[word].max()
# text = nltk.corpus.genesis.words('english-kjv.txt')
# bigrams = nltk.bigrams(text)
# cfd = nltk.ConditionalFreqDist(bigrams)
# print(cfd['living'])
# print(generate_model(cfd, 'living'))

# # 2.13 词汇列表语料库
# # 1 过滤文本
# def unusual_words(text):  #罕见或拼写错误词汇集
#     text_vocab = set(w.lower() for w in text if w.isalpha())  #总体样本
#     english_vocab = set(w.lower() for w in nltk.corpus.words.words())  #nltk.corpus.words.words() 常用词汇样本
#     unusual = text_vocab.difference(english_vocab)  #罕见词汇样本 = 总体样本 - 常用词汇样本
#     return sorted(unusual)
# print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')))
# print(unusual_words(nltk.corpus.nps_chat.words()))
# # 2 过滤高频词
# def content_fraction(text):
#     stopwords = nltk.corpus.stopwords.words('english')
#     content = [w for w in text if w.lower() not in stopwords]
#     return len(content) / len(text)  #非高频词/总词汇
# print(content_fraction(nltk.corpus.reuters.words()))
# # 3 猜字游戏
# puzzle_letters = nltk.FreqDist('egivrvonl')
# obligatory = 'r'
# wordlist = nltk.corpus.words.words()
# print([w for w in wordlist if len(w) >= 6 and obligatory in w and nltk.FreqDist(w) <= puzzle_letters])
# # 4 名字语料库
# names = nltk.corpus.names
# names.fileids()
# cfd = nltk.ConditionalFreqDist(
#     (fileid, name[-1])
#     for fileid in names.fileids()
#     for name in names.words(fileid))
# cfd.plot()  # 由图中可知，a结尾的名字一般是女性.


# # 2.14 发音词典
# # NLTK 中包括美国英语的 CMU 发音词典，它是为语音合成器使用而设计的。
# entries = nltk.corpus.cmudict.entries()
# print(len(entries))
# for entry in entries[39943:39951]:
#     print(entry)
# # 字典式查找
# prondict = nltk.corpus.cmudict.dict()
# print(prondict['fire'])
# # 过滤
# text = ['natural', 'language', 'processing']
# print([ph for w in text for ph in prondict[w][0]])


# # 2.15 比较词表
# from nltk.corpus import swadesh  #斯瓦迪士核心词列表
# print(swadesh.fileids())
# print(swadesh.words('en'))
# # 2 #法语转英语
# fr2en = swadesh.entries(["fr","en"])
# print(fr2en)
# translate = dict(fr2en)
# print(translate["chien"])

# # 2.16 词汇工具
# from nltk.corpus import toolbox
# print(toolbox.entries('rotokas.dic'))
# #条目包括一系列的属性-值对，如('ps', 'V')，表示词性是'V'(动词)，('ge', 'gag')表示
# # 英文注释是'gag'。最后的 3 个配对包含一个罗托卡特语例句和它的巴布亚皮钦语及英语翻译。

# # 2.17 WordNet
# # 1 意义与同义词
# from nltk.corpus import wordnet as wn
# print(wn.synsets('motorcar'))
# print(wn.synset('car.n.01').lemma_names)  # 同一词集
# print(wn.synset('car.n.01').definition)   #意义
# print(wn.synset('car.n.01').examples)  #例子
# print(wn.synset('car.n.01').lemmas)
# print(wn.lemma('car.n.01.automobile'))
# print(wn.lemma('car.n.01.automobile').synset)
# print(wn.lemma('car.n.01.automobile').name)
# print(wn.synsets('car'))
# for synset in wn.synsets('car'):
#     print(synset.lemma_names)
# print(wn.lemmas('car'))
# # 2 WordNet的层次结构(词汇关系)
# # 下位词
# from nltk.corpus import wordnet as wn
# motorcar = wn.synset('car.n.01')
# types_of_motorcar = motorcar.hyponyms()
# print(types_of_motorcar[26])
# # print(sorted([lemma.name for synset in types_of_motorcar for lemma in synset.lemmas]))  #更具体直接概念集
# # 上位词
# print(len(motorcar.hypernym_paths()))  #意义数(car : 车辆；容器 2个意义数)
# 其他关系(树-树枝，树叶)
# from nltk.corpus import wordnet as wn
# print(wn.synset('tree.n.01').part_meronyms())  #整体-部分:一棵树的部分是它的树干，树冠等
# print(wn.synset('tree.n.01').substance_meronyms())  #实质应用：一棵树的实质是包括心材和边材组成的
# print(wn.synset('tree.n.01').member_holonyms())  #树的集合:森林
# for synset in wn.synsets('mint', wn.NOUN):
#     print(synset.name, ":", synset.definition)
# # 动词之间关系
# print(wn.synset('walk.v.01').entailments())
# print(wn.synset('eat.v.01').entailments())
# # 反义词
# print(wn.lemma('supply.n.02.supply').antonyms())
# print(wn.lemma('staccato.r.01.staccato').antonyms())
#
# 3 语义相似度
from nltk.corpus import wordnet as wn
right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')
# 最低相同上位词
print(right.lowest_common_hypernyms(right))
print(right.lowest_common_hypernyms(minke))
print(right.lowest_common_hypernyms(orca))
print(right.lowest_common_hypernyms(tortoise))
print(right.lowest_common_hypernyms(novel))
print("*"*30)
# 同义词集深度量化
print(wn.synset('right_whale.n.01').min_depth())
print(wn.synset('baleen_whale.n.01').min_depth())
print(wn.synset('whale.n.02').min_depth())
print(wn.synset('vertebrate.n.01').min_depth())
print(wn.synset('entity.n.01').min_depth())
print("*"*30)
# 相似度
print(right.path_similarity(right))
print(right.path_similarity(minke))
print(right.path_similarity(orca))
print(right.path_similarity(tortoise))
print(right.path_similarity(novel))
# # 查看帮助
# print("*"*30)
# print(help(wn))