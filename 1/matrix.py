# -*- coding: utf-8 -*-
import numpy as np
# 全0矩阵
zero = np.zeros([3,5])
print '---zeros matrix---'
print zero

# 全1矩阵
one = np.ones([3,5])
print '---ones matrix---'
print one

# 随机矩阵
rand = np.random.rand(3,5)
print '---rand matrix---'
print rand

# 单位矩阵
eye = np.eye(5)
print '---eye matrix---'
print eye