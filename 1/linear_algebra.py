# -*- coding: utf-8 -*-
from numpy import *
# 方阵的行列式
rand = random.rand(5,5)
print '---Matrix Determinant---'
print linalg.det(rand)

# 逆
print '---Matrix Inverse---'
print rand
print linalg.inv(rand)

# 对称
print '---symmetric matrix---'
randT = rand.T
print rand*rand.T

# 秩
print '---rank of matrix---'
print linalg.matrix_rank(rand)

# 可逆矩阵求解
print '---solve invertible matrix---'
a = [
[1,-1,0],
[-1,2,2],
[1,1,-1]
]
b = [1,1,0]
s = linalg.solve(a,b)
print s