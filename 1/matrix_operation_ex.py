# -*- coding: utf-8 -*-
from numpy import *
# 矩阵行列数
one = ones([3,5])
[m,n] = shape(one)
print '---Matrix rows and colums---'
print '[',m,',',n,']'

# 按行切片
print '---Matrix slice by row---'
slice = one[0]
print slice

# 按列切片
print '---Matrix slice by colum---'
slice2 = one.T[0]
print slice2

# 矩阵复制
print '---Matrix copy---'
copy = one.copy()
print copy

# 矩阵比较
print '---Matrix compare---'
m = 2*random.rand(3,5)
print m < one
