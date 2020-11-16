# 入门:mnist实例


# 2.1 mnist实例
# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Functions for downloading and reading MNIST data."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gzip
import os
import tempfile

import numpy
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
from tensorflow.examples.tutorials.mnist import input_data
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 1准备
# # MNIST数据集(60000训练集，10000测试集)
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
# xs = [60000, matrix(784)] ys = [60000, matrix(10)]
# 参考模型原理图
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))  #权重，偏移因为是要被学习出来的量，可以任意值初始化
b = tf.Variable(tf.zeros([10]))
# softmax回归模型
y = tf.nn.softmax(tf.matmul(x, W) + b)

# 2 评判模块
# 损失函数
y_ = tf.placeholder("float", [None, 10])  #输入正确值
cross_entropy = -tf.reduce_sum(y_*tf.log(y))  #计算交叉熵

# 3 训练方式
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)  #在这里，我们要求TensorFlow用梯度下降算法（gradient descent algorithm）以0.01的学习速率最小化交叉熵。

# 4 运行程序
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
# 开始训练(随机梯度下降训练)
# 该循环的每个步骤中，我们都会随机抓取训练数据中的100个批处理数据点，然后我们用这些数据点作为参数替换之前的占位符来运行train_step。
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# 5 评估我们的模型
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))  #1的有偏估计y_与1的值的正确预测
print(correct_prediction)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))  #布尔值转换成浮点数，然后取平均值
print(accuracy)
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))  #计算正确率