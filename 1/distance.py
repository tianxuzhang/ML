# -*- coding: utf-8 -*-
from numpy import *
#import scipy.spatial.distance.pdist as dist
# 欧式距离
rand = random.rand(5,5)
print '---Euclidean Distance---'
v1 = mat([1,2,3])
v2 = mat([4,5,6])
diff = v1 - v2
print sqrt(diff * diff.T)

# 曼哈顿距离
print '---manhattan Distance---'
print sum(abs(diff))

# 切比雪夫距离
print '---Chebyshev Distance---'
print abs(diff).max()

# 余弦夹角
print '---Cosine---'
cos = dot([1,2,3],[4,5,6])/(linalg.norm(v1)*linalg.norm(v2))
# Note:dot(v1,v2) return error?
print cos

# 汉明距离
print '---Hamming Distance---'
V = mat([[1,1,0,1,0,0,1],[1,0,1,1,0,0,1]])
n = nonzero(V[0]-V[1])
h = shape(n[0])[0]
print h

# 杰卡德距离
#print '---Jaccard Similarity Coefficient---'
#print dist.pdist(V,'jaccard')