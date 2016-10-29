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

classify0([0,0],group,labels,3)

'''
读文件取出特征和特征标签
'''
def file2matrix(filename):
    fr = open(filename) # 打开文件
    arrayLines = fr.readlines() # 按行读文件
    numberOfLines = len(arrayLines) # 获取文件行数
    returnMat = zeros((numberOfLines,3)) # 准备返回的矩阵
    classLabelVector = [] # 准备返回的类别标签
    fr = open(filename)
    index = 0
    for line in arrayLines:
        line = line.strip() # 去除首尾空格
        listFromLine = line.split('\t') # 按tab符号分割字符串
        returnMat[index,:] = listFromLine[0:3] # 取前三列复制给矩阵的当前行
        classLabelVector.append(int(listFromLine[-1])) # 取出最后一列添加到类别标签数组里
        index += 1
    return returnMat,classLabelVector

datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')

'''
数据标准化
'''
def autoNorm(dataSet):
    minVals = dataSet.min(0) # 0取列的最小值
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))
    return normDataSet, ranges, minVals

normMat, ranges, minVals = autoNorm(datingDataMat)

'''
查看数据分布
'''
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels)) # XY值，后两参数可区分显示不同类别的点
ax.axis([-2,25,-0.2,2.0]) # 设置轴显示的值域
plt.xlabel('Percentage of Time Spent Playing Video Games') # X标题
plt.ylabel('Liters of Ice Cream Consumed Per Week') # Y标题
plt.show()

'''
测试
'''
def datingClassTest():
    hoRatio = 0.10      # 测试集占比
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')# 加载数据
    normMat, ranges, minVals = autoNorm(datingDataMat) # 正则化
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio) # 测试集行数
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3) # 分类
        print ("the classifier came back with: {0:d}, the real answer is: {1:d}".format(classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0 # 累计错误次数
    print ("the total error rate is: {0:f}".format(errorCount/float(numTestVecs))) # 计算错误率
    print (errorCount)
	
datingClassTest()