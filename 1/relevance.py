# -*- coding: utf-8 -*-
from numpy import *
z1=[-0.0000,0.3875,-0.0001,-0.5737,-0.0001,0.5212]
z2=[-0.0364,0.4415,-0.0198,-0.4228,-0.0194,0.5187] 

print "均值"
m1 = mean(z1)
m2 = mean(z2)

print m1
print m2

print "标准差"
s1 = std(z1)
s2 = std(z2)
print s1
print s2

print "相关系数"
c = mean(multiply(z1 - m1, z2 - m2)/(s1 * s2))
print c

print "相关系数矩阵"
print corrcoef(mat([z1,z2]))
