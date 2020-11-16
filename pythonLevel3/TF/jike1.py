# 介绍

# # 1.1 实例1
# import tensorflow as tf
# import numpy as np
#
# # 使用 NumPy 生成假数据(phony data), 总共 100 个点.
# x_data = np.float32(np.random.rand(2, 100))  # 随机输入
# y_data = np.dot([0.100, 0.200], x_data) + 0.300
#
# # 构造一个线性模型
# #
# b = tf.Variable(tf.zeros([1]))
# W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
# y = tf.matmul(W, x_data) + b
#
# # 最小化方差
# loss = tf.reduce_mean(tf.square(y - y_data))
# optimizer = tf.train.GradientDescentOptimizer(0.5)
# train = optimizer.minimize(loss)
#
# # 初始化变量
# init = tf.initialize_all_variables()
#
# # 启动图 (graph)
# sess = tf.Session()
# sess.run(init)
#
# # 拟合平面
# for step in range(0, 201):
#     sess.run(train)
#     if step % 20 == 0:
#         print(step, sess.run(W), sess.run(b))
#
# # 得到最佳拟合结果 W: [[0.100  0.200]], b: [0.300]


# # 1.2 实例2
# import tensorflow as tf
# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# print(sess.run(hello))
# a = tf.constant(10)
# b = tf.constant(32)
# print(sess.run(a+b))


# 1.3 基础
# TensorFlow 是一个非常强大的用来做大规模数值计算的库。其所擅长的任务之一就是实现以及训练深度神经网络。
# 是一个编程系统, 使用图来表示计算任务. 图中的节点被称之为 op (operation 的缩写). 一个 op 获得 0 个或多个 Tensor, 执行计算,
# 产生 0 个或多个 Tensor. 每个 Tensor 是一个类型化的多维数组. 例如, 你可以将一小组图像集表示为一个四维浮点数数组, 这四个维度分别是 [batch, height, width, channels].
# 一个 TensorFlow 图描述了计算的过程. 为了进行计算, 图必须在 会话 里被启动. 会话 将图的 op 分发到诸如 CPU 或 GPU 之类的 设备 上,
# 同时提供执行 op 的方法. 这些方法执行后, 将产生的 tensor 返回. 在 Python 语言中, 返回的 tensor 是 numpy ndarray 对象; 在 C 和 C++ 语言中,
# 返回的 tensor 是 tensorflow::Tensor 实例.
# 计算图:TensorFlow 程序通常被组织成一个构建阶段(构建图)和一个执行阶段(执行图).
# 使用图 (graph) 来表示计算任务
# 在被称之为 会话 (Session) 的上下文 (context) 中执行图.
# 使用 tensor 表示数据.可以看作是一个 n 维的数组或列表. 一个 tensor 包含一个静态类型 rank, 和 一个 shape.
# 通过 变量 (Variable) 维护状态.
# 使用 feed 和 fetch 可以为任意的操作(arbitrary operation) 赋值或者从其中获取数据.

# # 实例(基本操作)1:
# import tensorflow as tf
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#
# # 1  构建图
# # 默认图现在有三个节点, 两个 constant() op, 和一个matmul() op. 为了真正进行矩阵相乘运算, 并得到矩阵乘法的 结果, 你必须在会话里启动这个图.
# # 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
# # 加到默认图中.
# #
# # 构造器的返回值代表该常量 op 的返回值.
# matrix1 = tf.constant([[3., 3.]])
#
# # 创建另外一个常量 op, 产生一个 2x1 矩阵.
# matrix2 = tf.constant([[2.],[2.]])
#
# # 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# # 返回值 'product' 代表矩阵乘法的结果.
# product = tf.matmul(matrix1, matrix2)
#
# # 2 执行图
# # 启动默认图.
# sess = tf.Session()
#
# # 调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数.
# # 上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回
# # 矩阵乘法 op 的输出.
# #
# # 整个执行过程是自动化的, 会话负责传递 op 所需的全部输入. op 通常是并发执行的.
# #
# # 函数调用 'run(product)' 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op) 的执行.
# #
# # 返回值 'result' 是一个 numpy `ndarray` 对象.
# result = sess.run(product)
# print(result)
# # ==> [[ 12.]]
#
# # 任务完成, 关闭会话.
# sess.close()
#
# # 实例2(交互式使用IPython):
# # 为了便于使用诸如 IPython 之类的 Python 交互环境, 可以使用 InteractiveSession 代替 Session 类,
# # 使用 Tensor.eval() 和 Operation.run() 方法代替 Session.run(). 这样可以避免使用一个变量来持有会话.
# # 进入一个交互式 TensorFlow 会话.
# import tensorflow as tf
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#
# sess = tf.InteractiveSession()
#
# x = tf.Variable([1.0, 2.0])
# a = tf.constant([3.0, 3.0])
#
# # 使用初始化器 initializer op 的 run() 方法初始化 'x'
# x.initializer.run()
#
# # 增加一个减法 sub op, 从 'x' 减去 'a'. 运行减法 op, 输出结果
# sub = tf.subtract(x, a)
# print(sub.eval())
# # ==> [-2. -1.]
#
# # 实例3: 变量(tensor,也可理解为对象)
# import tensorflow as tf
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#
# # 创建一个变量, 初始化为标量 0.
# state = tf.Variable(0, name="counter")
#
# # 创建一个 op, 其作用是使 state 增加 1
#
# one = tf.constant(1)  #常量op,返回one tensor
# new_value = tf.add(state, one)  #加法op
# update = tf.assign(state, new_value)  #用new_value 替换 state
#
# # 启动图后, 变量必须先经过`初始化` (init) op 初始化,
# # 首先必须增加一个`初始化` op 到图中.
# init_op = tf.global_variables_initializer()
#
# # 启动图, 运行 op
# with tf.Session() as sess:
#   # 运行 'init' op
#   sess.run(init_op)
#   # 打印 'state' 的初始值
#   print(sess.run(state))  #0
#   # 运行 op, 更新 'state', 并打印 'state'
#   for _ in range(3):
#     sess.run(update)
#     print(sess.run(state))  #1，2，3
#
# # 输出:
#
# # 0
# # 1
# # 2
# # 3
#
# # # 实例4:Fetch(取输出内容)
# import tensorflow as tf
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# input1 = tf.constant(3.0)
# input2 = tf.constant(2.0)
# input3 = tf.constant(5.0)
# intermed = tf.add(input2, input3)
# mul = tf.multiply(input1, intermed)
#
# with tf.Session() as sess:
#   result = sess.run([mul, intermed])  #取输出内容 tensor
#   print(result)
#
# # 实例5: Feed（feed 使用一个 tensor 值临时替换一个操作的输出结果.）
#   input1 = tf.placeholder(tf.float32)  #placeholder()创建临时tensor
#   print(input1)
#   input2 = tf.placeholder(tf.float32)
#   output = tf.multiply(input1, input2)
#
# with tf.Session() as sess:
#   print(sess.run([output], feed_dict={input1: [7.], input2: [2.]}))  #调用方法有效，方法结束，feed消失
#
# # 输出:
# # [array([ 14.], dtype=float32)]
#
# # 输出:
# # [array([ 21.], dtype=float32), array([ 7.], dtype=float32)]

