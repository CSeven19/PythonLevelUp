# NumPy

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv,qr,det
# # 4.1 ndarray(便于计算的多维数组对象(矢量化计算))
#
# # 1 创建ndarray
# # data = np.array([[0.9526,-0.246,-0.8856],[0.5639,0,2379,0.9104]])
# data = np.array([[1,2],[3,4]])
# print(data*10)  #方便乘法
# print(data.shape)  #维数
# print(data.ndim)  #行数
# print(data.dtype)
# # zeros()/empty()/ones()新建数组
# data2 = np.zeros((3,6))
# print(data2)
# data3 = np.empty((2,3,2))  #返回未初始化垃圾值
# print(data3)
# data6 = np.ones((2,3))
# print("data6",data6)
# # arange() 自然数组
# data4 = np.arange(15)
# print(data4)
# # eye 创建N*N单位阵
# data5 = np.eye(3)
# print(data5)
# # asarray() 将输入转化为ndarray
#
# # 2类型
# # astype(类型) 转化为对应类型执行
# arr = np.array([1,2,3,4,5])
# float_arr = arr.astype(np.float64)  #如果是浮点转int则小数部分会被截断掉
#
# # 3数组与标量间运算(不同大小数组间的运算叫做广播)
# arr = np.array([[1.,2.,3.],[4.,5.,6.]])
# print(arr*arr)  #平方
# print(arr-arr)
# print(1/arr)
# print(arr**0.5)
#
# # 4索引，切片(类似python,参看p104图)
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr[:2,1:])  #arr[1维，2维，3维。。。]
#
# # 5布尔型索引
# names = np.array(["Bob","Joe","Will","Bob","Joe","Will","Joe"])
# data = np.random.randn(7,4)  #生成高斯分布的随机数据
# print(names)
# print(data)
# print(names == "Bob")  #矢量化的比较
# print(data[names == "Bob" ])  #布尔型索引(names=="Bob"为True的行被选出),布尔型数组(data)长度必须跟被索引的数组(names)长度一致.
# print(data[names == "Bob",2:])
# print(data[-(names == "Bob")])
# print(data[(names == "Bob")|(names == "Will")])  # and/or关键字无效
# data[data<0] = 0  #负值设置为0
# print(data)
# data[names != "Joe"] = 7  #非Joe行设置为7
#
# # 6花式索引(区别切片，总是将数据复制到新数组中)
# arr = np.arange(32).reshape((8,4))  #reshape()重设置shape
# print(arr[[1,5,7,2],[0,3,1,2]])  #选取a10,a53,a71,a22的元素
# print(arr[[1,5,7,2]][:,[0,3,1,2]])  #选取a1i,a5i,a7i,a2i所在行所有元素并按[0,3,1,2]重新排序
# print(arr[np.ix_([1,5,7,2],[0,3,1,2])])  #同上
# # 花式索引等价函数: take/put
# arr1 = np.arange(10)
# print(arr.take([7,1,2,6]))
# arr1.put([7,1,2,6], 42)  #put(非修改列，其余列填充数据)
# print(arr1)
#
# 7数组转置(返回源数据视图不进行复制)及轴对换
# # (1)转置
# arr = np.arange(15).reshape((3,5))
# print(arr.T)
# # 高维转置
# arr = np.arange(16).reshape((2, 2, 4))
# print(arr)
# print(arr.transpose((1, 0, 2)))  #接受由轴编号(x=0,y=1,z=2)组成的元组进行转置
# print(arr.transpose((0, 2, 1)))  #x不变，y轴z轴互换
# # swapaxes(轴元组)
# arr = np.arange(16).reshape((2, 2, 4))
# print(arr.swapaxes(1,2))  #y轴z轴互换 等价于 arr.transpose((0, 2, 1))
# (2)计算内积
# print(arr*arr.T)  #异常
# # 方法1
# a=np.mat([[1],[2],[3]]);
# b=np.mat([[0],[2],[3]]);
# print(a.T*b)
# # 方法2
# arr = np.random.randn(6,3)
# print(arr)
# print(arr.T)
# print(np.dot(arr.T,arr))  #dot(a,b)返回点积的结果数组[3X3]


# 4.2通用函数ufunc(元素操作函数，可理解为矢量化包装器,如sqrt()/exp()函数)
# # 1 一元ufunc(参考110一览表)
# arr = np.arange(10)
# print(arr)
# print(np.sqrt(arr))
# print(np.exp(arr))  #e+01 == 10^1
#
# # 2 二元ufunc(参考111一览表)
# x = np.random.randn(8)
# y = np.random.randn(8)
# print(np.maximum(x,y))  #返回各对应元素最大值所组成的集合
# arr = np.random.randn(7)*5
# print(np.modf(arr))  #返回arr整数部分，小数部分的2个数组。
# # 2利用数组进行数据处理(矢量化,节省循环)
# points = np.arange(-5,5,0.01)  #arange(起点，终点，步长) 1000个间隔为0.01的点
# xs,ys = np.meshgrid(points,points)  #接受2个一维数组产生1个两维数组
# # print( np.meshgrid(points,points))
# z = np.sqrt(xs **2+ys**2)  #
# # print(z)
# plt.imshow(z,cmap=plt.cm.gray)  #z数据的y-z面投影图
# plt.colorbar()
# plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")


# 4.3将条件逻辑表述为数组运算
# # 2个值数组+1个布尔数组
# xarr = np.array([1.1,1.2,1.3,1.4,1.5])
# yarr = np.array([2.1,2.2,2.3,2.4,2.5])
# cond = np.array([True,False,True,True,False])
# result = [(x if c else y) for x,y,c in zip(xarr,yarr,cond)]
# print(result)
# # 方法2where()
# result = np.where(cond,xarr,yarr)  #等价于三目运算
# print(result)
# # 实例2 替换正负值
# arr = np.random.randn(4,4)
# print(arr)
# print(np.where(arr>0,2,-2))
# print(np.where(arr>0,2,arr))  #只将正值替换为2
# # where嵌套
# # print(np.where(cond1 & cond2,0,np.where(cond1,1,np.where(cond2,2,3))))


# # 4.4数学和统计方法(p116方法一览)
# arr = np.random.randn(5,4)
# print(arr)
# print(arr.mean())
# print(np.mean(arr))
# print(arr.sum())
# print(arr.mean(axis=1))  #y轴均值
# print(arr.sum(axis=0))  #x轴和
# print((arr > 0).sum())  #正值的和
# arr = np.array([[0,1,2],[3,4,5],[6,7,8]])
# print(arr)
# print(arr.cumsum())  #累计和
# print(arr.cumprod(1))  #累计积
# # bool判断
# # any判断数组中是否存在至少一个True
# # all判断数组是否全为True
# bools = np.array([False,False,True,False])
# print(bools.any())
# print(bools.all())


# # 4.5排序
# arr = np.random.randn(8)
# arr.sort()
# print(arr)  #默认升序排序
# # 多维排序
# arr = np.random.randn(5,3)
# print(arr)
# arr1 = np.sort(arr,axis=1)  #np.sort(arr)不修改arr本身
# print(arr1)
# print(arr)
# arr.sort(axis=1)  #y轴上排序,属于就地排序，修改arr本身。
# print(arr)
# # 计算分位数
# large_arr = np.random.randn(1000)
# large_arr.sort()
# print(large_arr[int(0.05*len(large_arr))])  #返回下分位0.05处的值


# # 4.6唯一化及其他集合逻辑(参考P118)
# names = np.array(["Bob","Joe","Will","Bob","Joe","Will","Joe"])
# print(np.unique(names))

# # 4.7 用于数组的文件I/O
#
# # 1数组保存/载入
# arr = np.arange(10)
# np.save("some_array",arr)  #生成some_array.npy文件
# print(np.load("some_array.npy"))
#
# # 2多个数组的保存/载入
# arr2 = np.arange(15)
# np.savez("array_archive.npz",a=arr,b=arr2)
# print(np.load("array_archive.npz")["b"])
#
# # 3存取文本文件
# # loadttxt()(类似genfromtxt) 加载
# arr = np.loadtxt("array_ex.txt",delimiter=",")
# print(arr)
# # savetxt() 保存
# np.savetxt("array_ex.txt1",arr)
# # pandas所属read_csv/read_table等等

# # 4.8 线代(参考P121 方法一览)
# #
# # 1点积dot()
# x = np.array([[1.,2.,3.],[4.,5.,6.]])
# print(np.ones(3))
# print(np.dot(x,np.ones(3)))  #[6. 15.]
#
# # 2矩阵分解，求逆，求|A|
# X = np.random.randn(5,5)
# mat = X.T.dot(X)
# print(X)
# print(mat)
# print(inv(mat))  #inv() 矩阵求逆
# print(det(mat))  #det() 矩阵求|mat|
# print(inv(mat)*det(mat))  #伴随阵
# q,r = qr(mat) #计算矩阵的QR分解。把矩阵A作为QR，q是正交的，r是上三角形。
# print(r)

# 4.9随机数生成(参考P122 方法一览)
#
# # 1 normal() 返回服从标准正太分布的随机数组.
# samples = np.random.normal(size=(4,4))
# print(samples)