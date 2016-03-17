# -*- coding: utf-8 -*-
from numpy import *

a = [[4,6,2],[8,5,7],[1,3,9]]
val,vec = linalg.eig(a)
print 'eigenvalue'
print val

print 'eigenvector'
print vec