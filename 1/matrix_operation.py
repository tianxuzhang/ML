# -*- coding: utf-8 -*-
from numpy import *
# 矩阵加减
one = ones([5,5])
eye = eye(5)
print '---Matrix Addition---'
print one + eye

print '---Matrix Subtraction---'
print one - eye

# 矩阵数乘
print '---scalar multiplication of matrix---'
a = 10
print a*one

# 矩阵所有元素求和
print '---Matrix Summation---'
print sum(one)

# 矩阵各元素的积
print '---Matrix Elements Multiplication---'
print multiply(2*ones([3,3]),3*ones([3,3]))
print multiply(2*ones([3,3]),3*ones([1,3]))

# 矩阵n次幂
print '---Matrix Power---'
print power(10*one,2)

# 矩阵相乘
print '---Matrix inner product---'
print mat(random.rand(2,4))*mat(random.rand(4,5))

# 矩阵转置
print '---Matrix tranpose---'
m = mat([[1,2,3],[4,5,6],[7,8,9]])
print '---before---'
print m
print '---m.T---'
print m.T
print '---m.transpose()---'
print m.transpose()