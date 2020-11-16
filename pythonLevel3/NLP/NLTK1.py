# 准备

# 1.1 下载语料库
import nltk
from nltk.corpus import brown
# nltk.download()


# # 1.2 测试下载好的语料库
# from nltk.corpus import brown
# print(brown.words()[0:10])#打印前10个单词
# print(brown.tagged_words()[0:10])#打印前10个单词的标注
# print(len(brown.words()))#有多少个单词
# print(dir(brown))


# # 1.3 测试下载好的书籍
# from nltk.book import *
# # *** Introductory Examples for the NLTK Book ***
# # Loading text1, ..., text9 and sent1, ..., sent9
# # Type the name of the text or sentence to view it.
# # Type: 'texts()' or 'sents()' to list the materials.
# # text1: Moby Dick by Herman Melville 1851
# # text2: Sense and Sensibility by Jane Austen 1811
# # text3: The Book of Genesis
# # text4: Inaugural Address Corpus
# # text5: Chat Corpus
# # text6: Monty Python and the Holy Grail
# # text7: Wall Street Journal
# # text8: Personals Corpus
# # text9: The Man Who Was Thursday by G . K . Chesterton 1908
# print(text1.name)#书名
# print("*"*30)
# print(text1.concordance(word="very"))#上下文, 返回出现love的带上下文的句子
# print("*"*30)
# print(text1.similar(word="very"))#查找与very相似上下文场景, he is very beautiful/ he is so beautiful中 very/so相似上下文场景。
# print("*"*30)
# print(text1.common_contexts(words=["pretty","very"]))#返回"pretty","very"皆使用上的上下文组合. he is a very little/he is a pretty little中的a_little
# print("*"*30)
# text4.dispersion_plot(words=['citizens','freedom','democracy'])#美国总统就职演说词汇分布图
# print("*"*30)
# print(text3.generate(words=brown.words(categories='news')))  #随机文本自动生成
# print("*"*30)
# print(text1.collocations())  #词语搭配(短语)
# print("*"*30)
# print(type(text1))
# print("*"*30)
# print(text3.count("smote"))  #单词数
# print("*"*30)
# print(len(text1))#文本长度
# print("*"*30)
# print(len(set(text1)))#词汇长度
# # 频率分布
# print("*"*30)
# fword=FreqDist(text1)  #词条频率函数(参考P40 NLTK 频率分布类中定义的函数)
# print(text1.name)#书名
# print(fword)
# print("*"*30)
# voc=fword.most_common(50)#频率最高的50个字符
# fword.plot(50,cumulative=True)#绘出波形图
# print("*"*30)
# print(fword.hapaxes())#低频词


# # 1.4 控制
# from nltk.book import *
# print(sent7)
# print([w for w in sent7 if len(w)<4])  #正则单词  参考P42 一些常用相关字符串操作.
# print(len(w) for w in text1)  #单词矢量化操作
# print(w.upper() for w in text1)
# print(set([word.lower() for word in text1]))


# 1.5 自动理解自然语言


# # 1.4 分词和分句
# from nltk.tokenize import word_tokenize,sent_tokenize
# #分词  TreebankWordTokenizer PunktTokenizer
# print(word_tokenize(text="All work and no play makes jack a dull boy, all work and no play",language="english"))
# #分句
# data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
# print(sent_tokenize(data))
# from nltk.corpus import stopwords
# print(type(stopwords.words('english')))
# print([w for w in word_tokenize(text="All work and no play makes jack a dull boy, all work and no play",language="english") if w not in stopwords.words('english')])#去掉停用词


# # 1.5 时态 和 单复数
# from nltk.stem import PorterStemmer
# data=word_tokenize(text="All work and no play makes jack a dull boy, all work and no play,playing,played",language="english")
# ps=PorterStemmer()
# for w in data:
#     print(w,":",ps.stem(word=w))
# from nltk.stem import SnowballStemmer
# snowball_stemmer = SnowballStemmer('english')
# snowball_stemmer.stem('presumably')
# #u"presum"
#
# from nltk.stem import WordNetLemmatizer
# wordnet_lemmatizer = WordNetLemmatizer()
# wordnet_lemmatizer.lemmatize('dogs')
# u'dog'
#
#
# # 1.6 词性标注
# sentence = """At eight o'clock on Thursday morning... Arthur didn't feel very good."""
# tokens = nltk.word_tokenize(sentence)
# print(tokens)
# #['At', 'eight', "o'clock", 'on', 'Thursday', 'morning',
# # 'Arthur', 'did', "n't", 'feel', 'very', 'good', '.']
#
# nltk.help.upenn_tagset("NNP")#输出NNP的含义
# tagged = nltk.pos_tag(tokens)
# nltk.batch_pos_tag([["this", "is", "batch", "tag", "test"], ["nltk", "is", "text", "analysis", "tool"]])#批量标注
# print(tagged)
# # [('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'), ('on', 'IN'),
# # ('Thursday', 'NNP'), ('morning', 'NN')]
#
#
# # 1.7 自带分类器
# 查看P18模块简介
# from nltk.classify.api import ClassifierI, MultiClassifierI
# from nltk.classify.megam import config_megam, call_megam
# from nltk.classify.weka import WekaClassifier, config_weka
# from nltk.classify.naivebayes import NaiveBayesClassifier
# from nltk.classify.positivenaivebayes import PositiveNaiveBayesClassifier
# from nltk.classify.decisiontree import DecisionTreeClassifier
# from nltk.classify.rte_classify import rte_classifier, rte_features, RTEFeatureExtractor
# from nltk.classify.util import accuracy, apply_features, log_likelihood
# from nltk.classify.scikitlearn import SklearnClassifier
# from nltk.classify.maxent import (MaxentClassifier, BinaryMaxentFeatureEncoding,TypedMaxentFeatureEncoding,ConditionalExponentialClassifier)
#
#
# # 1.8 实例1：通过名字预测性别
# from nltk.corpus import names
# #特征取的是最后一个字母
# def gender_features(word):
#     return {'last_letter': word[-1]}
# #数据准备
# name=[(n,'male') for n in names.words('male.txt')]+[(n,'female') for n in names.words('female.txt')]
# print(len(name))
# #特征提取和训练模型
# features=[(gender_features(n),g) for (n,g) in name]
# classifier = nltk.NaiveBayesClassifier.train(features[:6000])
# #测试
# print(classifier.classify(gender_features('Frank')))
# from nltk import classify
# print(classify.accuracy(classifier,features[6000:]))
#
#
# # 1.9 实例2：情感分析
# import nltk.classify.util
# from nltk.classify import NaiveBayesClassifier
# from nltk.corpus import names
#
#
# def word_feats(words):
#     return dict([(word, True) for word in words])
#
# #数据准备
# positive_vocab = ['awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)']
# negative_vocab = ['bad', 'terrible', 'useless', 'hate', ':(']
# neutral_vocab = ['movie', 'the', 'sound', 'was', 'is', 'actors', 'did', 'know', 'words', 'not']
# #特征提取
# positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
# negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
# neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]
#
# train_set = negative_features + positive_features + neutral_features
# #训练
# classifier = NaiveBayesClassifier.train(train_set)
#
# # 测试
# neg = 0
# pos = 0
# sentence = "Awesome movie, I liked it"
# sentence = sentence.lower()
# words = sentence.split(' ')
# for word in words:
#     classResult = classifier.classify(word_feats(word))
#     if classResult == 'neg':
#         neg = neg + 1
#     if classResult == 'pos':
#         pos = pos + 1
#
# print('Positive: ' + str(float(pos) / len(words)))
# print('Negative: ' + str(float(neg) / len(words)))