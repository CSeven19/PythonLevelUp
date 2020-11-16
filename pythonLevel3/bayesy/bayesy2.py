# # 分布
#
# from pythonLevel3.bayesy.thinkbays import Pmf
# # 1设置一个骰子各面出现概率为1/6
# pmf = Pmf()
# for x in [1,2,3,4,5,6]:
#     pmf.Set(x,1/6.0)  #Pmf 创建一个空的没有赋值的 pmf。Set 方法设置每个值的概率为 1/6。
#
# # 2计算a出现概率
# word_list = ['a','b','c','2323','w10','a','a','c']
# pmf1 = Pmf()
# for word in word_list:
#     pmf1.Incr(word, 1)  #出现的单词加1
# pmf1.Normalize() # 典型概率计算各自单词出现概率
# print(pmf1.Prob('a'))  #显示a出现的概率

# # 3 先验+似然度
# # 先验分布(自己先假设的概率)
# from pythonLevel3.bayesy.thinkbays import Pmf
# pmf = Pmf()
# pmf.Set('Bowl1',0.5)
# pmf.Set('Bowl2',0.5)
# # 似然度(用以修正先验分布)
# pmf.Mult('Bowl1',0.75)
# pmf.Mult('Bowl2',0.5)
# pmf.Normalize()
# print(pmf.Prob('Bowl1'))

# # 4
# # 封装赋予先验分布的类
# from pythonLevel3.bayesy.thinkbays import Pmf
# class Cookie(Pmf):
#     #每个样本点赋予相同的先验概率
#     def __init__(self,hypos):
#         Pmf.__init__(self)
#         for hypo in hypos:
#             self.Set(hypo,1)
#             self.Normalize()
#     #Update 方法,它以 data 为参数并修正相应的概率
#     def Update(self, data):
#         for hypo in self.Values():
#             like = self.Likelihood(data, hypo)
#             self.Mult(hypo,like)
#             self.Normalize()
#     mixes = {
#         'Bowl1': dict(vanilla=0.75, chocolate=0.25),
#         'Bowl2': dict(vanilla=0.5, chocolate=0.5),
#     }
#     #似然度由 Likelihood 计算
#     def Likelihood(self, data, hypo):
#         mix = self.mixes[hypo]
#         like = mix[data]
#         return like
#
# hypos= ['Bowl1','Bowl2']
# pmf =Cookie(hypos)
# print(pmf.Prob('Bowl1'))
# pmf.Update('vanilla')  #以mixes[hypo]['vanilla']作为似然度进行后验。
# for hypo , prob in pmf.Items():
#     print(hypo,prob)
# dateset= ['vanilla', 'chocolate', 'vanilla']
# for data in dateset:
#     pmf.Update(data)
# for hypo , prob in pmf.Items():
#     print(hypo,prob)

# 5贝叶斯基本框架
# class Suite(Pmf)
#  “代表一套假设及其概率。”
#  def __init__(self,hypo=tuple())：
#  “初始化分配。”
#  def Update(self,data)：
#  “更新基于该数据的每个假设。”
#  def Print (self)：
#  “打印出假设和它们的概率。”

# 6M_AND_M豆(混合色彩问题)
from pythonLevel3.bayesy.thinkbays import Pmf
class M_and_M(Pmf):
    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo,1)
            self.Normalize()
    def Update(self, data):
        for hypo in self.Values():  #self.Values()=['A','B']
            like = self.Likelihood(data, hypo)
            self.Mult(hypo,like)
            self.Normalize()
    mix94 = dict(brown=30,
                 yellow=20,
                 red=20,
                 green=10,
                 orange=10,
                 tan=10)
    mix96 = dict(blue=24,
                 green=20,
                 orange=16,
                 yellow=14,
                 red=13,
                 brown=13)
    hypoA = dict(bag1=mix94, bag2=mix96)
    hypoB = dict(bag1=mix96, bag2=mix94)
    hypotheses = dict(A=hypoA, B=hypoB)
    def Likelihood(self, data, hypo):
        bag, color = data
        mix = self.hypotheses[hypo][bag]
        like = mix[color]
        return like
    def Print(self):
        for hypo , prob in self.Items():
            print(hypo,prob)
suite = M_and_M('AB')
suite.Update(('bag1', 'yellow'))
suite.Update(('bag2', 'green'))
# A:20 20 B 14 10跟这里的概率不一样。不知道他thinkbays算法怎么决定的。
suite.Print()