from numpy import * # 引入numpy
import operator # 引入操作符
from os import listdir # 引入列出文件和文件夹模块

'''
创建四个点，分成两类。Python支持返回多个参数
'''
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

group,labels = createDataSet()

'''
inX: 待分类向量
dataSet：样本集
labels：类别标签
k：最近邻数
'''
def classify0(inX, dataSet, labels, k):
    # （1）用已知分类数据集中的每个点与当前点计算欧式距离
    dataSetSize = dataSet.shape[0] # 样本数
    diffMat = tile(inX, (dataSetSize,1)) - dataSet # 差
    sqDiffMat = diffMat**2 ## 的平方
    sqDistances = sqDiffMat.sum(axis=1) # 按特征求和
    distances = sqDistances**0.5 # 开方
    
    # (2) 选择距离最小的K个点
    sortedDistIndicies = distances.argsort() # 数组排序后对应原来的索引，也是已知类别数据的行号 
    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]] # 取出类别标签
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1 # 累计距离最近的类别的次数，get函数可以设置默认值
    
    # （3）将类别元组排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    
    # (4) 输出频次最高的类别
    return sortedClassCount[0][0] # 可以通过下标的方式取value的值 [('B', 2), ('A', 1)]
