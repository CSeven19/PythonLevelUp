import numpy as np

# 1 比较
# arr = np.random.randn(5, 5) # 返回(5,5)的标态分布的数组
# print(arr)
# arr[::2].sort(1)
# print(arr[:, :-1])
# print(arr[:, 1:])
# print(arr[:, :-1] < arr[:, 1:]) # [行start:行end,列start:列end]

# 2 矩阵乘法
arr = np.random.randn(5, 5)
print(arr)
print(arr.T)
mat = arr.T.dot(arr)
print(mat)

arr1 = np.array([2, 3])
arr2 = np.array([4, 5])
arr3 = np.dot(arr1, arr2)
arr4 = arr2.dot(arr1)
print(arr3)
print(arr4)

arr5 = np.array([[2, 3], [4, 5]])
arr6 = np.array([[6, 7], [8, 9]])
arr7 = np.dot(arr5, arr6)
print(arr7)

# 3 QR分解
q, r = np.linalg.qr(arr7)
print(q)
print(r)
