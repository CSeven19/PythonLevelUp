# _*_ coding: utf-8 _*_
# 作者: yhao
# 博客: http://blog.csdn.net/yhao2014
# 邮箱: yanhao07@sina.com
# SGD随机梯度下降算法

# 1训练集
# 每个样本点有3个分量 (x0,x1,x2)
x = [(1, 0., 3), (1, 1., 3), (1, 2., 3), (1, 3., 2), (1, 4., 4)]
# y[i] 样本点对应的输出
y = [95.364, 97.217205, 75.195834, 60.105519, 49.342380]

# 2初始化
epsilon = 0.0001  # 迭代阀值，当两次迭代损失函数之差小于该阀值时停止迭代
alpha = 0.01  #步长 # 学习率
diff = [0, 0]  #残差
# max_itor = 1000
error1 = 0  #损失函数
error0 = 0  #损失函数temp
count = 0  #计数
# 初始化参数
theta0 = 0  #Θ0
theta1 = 0  #Θ1
theta2 = 0  #Θ2

# 3主循环
while True:
    count += 1

    # 参数迭代计算
    for i in range(len(x)):
        # 拟合函数为 y = theta0 * x[0] + theta1 * x[1] +theta2 * x[2]
        # 计算残差
        diff[0] = (theta0 + theta1 * x[i][1] + theta2 * x[i][2]) - y[i]

        # 梯度 = diff[0] * x[i][j]
        theta0 -= alpha * diff[0] * x[i][0]  #Θ0 - a(hΘ0(xi)-yi)xi
        theta1 -= alpha * diff[0] * x[i][1]
        theta2 -= alpha * diff[0] * x[i][2]

    # 计算损失函数
    error1 = 0
    for lp in range(len(x)):
        error1 += ((theta0 + theta1 * x[lp][1] + theta2 * x[lp][2]) - y[lp]) ** 2 / 2  #SGD随机梯度下降法

    if abs(error1 - error0) < epsilon:
        break
    else:
        error0 = error1

    print(' theta0 : %f, theta1 : %f, theta2 : %f, error1 : %f' % (theta0, theta1, theta2, error1))
print('Done: theta0 : %f, theta1 : %f, theta2 : %f' % (theta0, theta1, theta2))
print('迭代次数: %d' % count)