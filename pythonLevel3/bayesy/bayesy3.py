# from pythonLevel3.bayesy.thinkbays import Pmf
# from pythonLevel3.bayesy.thinkbays import Suite
#
#
# class Dice(Suite):
#     def __init__(self, hypos):
#         Pmf.__init__(self)
#         for hypo in hypos:
#             self.Set(hypo,1)
#             self.Normalize()
#     def Update(self, data):
#         for hypo in self.Values():  #self.Values()=['A','B']
#             like = self.Likelihood(data, hypo)
#             self.Mult(hypo,like)
#             self.Normalize()
#     mix94 = dict(brown=30,
#                  yellow=20,
#                  red=20,
#                  green=10,
#                  orange=10,
#                  tan=10)
#     mix96 = dict(blue=24,
#                  green=20,
#                  orange=16,
#                  yellow=14,
#                  red=13,
#                  brown=13)
#     hypoA = dict(bag1=mix94, bag2=mix96)
#     hypoB = dict(bag1=mix96, bag2=mix94)
#     hypotheses = dict(A=hypoA, B=hypoB)
#
#     def Likelihood(self, data, hypo):
#         if hypo < data:  #骰子点数大于骰子最大值, 似然度给予0
#             return 0
#         else:
#             return 1.0 / hypo
#     def Print(self):
#         for hypo , prob in self.Items():
#             print(hypo,":",prob)
#
# suite=Dice([ 4, 6, 8, 12, 20 ])
# suite.Update(6)
# suite.Print()

