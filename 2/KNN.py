from numpy import * # ����numpy
import operator # ���������
from os import listdir # �����г��ļ����ļ���ģ��

'''
�����ĸ��㣬�ֳ����ࡣPython֧�ַ��ض������
'''
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

group,labels = createDataSet()

'''
inX: ����������
dataSet��������
labels������ǩ
k���������
'''
def classify0(inX, dataSet, labels, k):
    # ��1������֪�������ݼ��е�ÿ�����뵱ǰ�����ŷʽ����
    dataSetSize = dataSet.shape[0] # ������
    diffMat = tile(inX, (dataSetSize,1)) - dataSet # ��
    sqDiffMat = diffMat**2 ## ��ƽ��
    sqDistances = sqDiffMat.sum(axis=1) # ���������
    distances = sqDistances**0.5 # ����
    
    # (2) ѡ�������С��K����
    sortedDistIndicies = distances.argsort() # ����������Ӧԭ����������Ҳ����֪������ݵ��к� 
    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]] # ȡ������ǩ
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1 # �ۼƾ�����������Ĵ�����get������������Ĭ��ֵ
    
    # ��3�������Ԫ������
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    
    # (4) ���Ƶ����ߵ����
    return sortedClassCount[0][0] # ����ͨ���±�ķ�ʽȡvalue��ֵ [('B', 2), ('A', 1)]

classify0([0,0],group,labels,3)

'''
���ļ�ȡ��������������ǩ
'''
def file2matrix(filename):
    fr = open(filename) # ���ļ�
    arrayLines = fr.readlines() # ���ж��ļ�
    numberOfLines = len(arrayLines) # ��ȡ�ļ�����
    returnMat = zeros((numberOfLines,3)) # ׼�����صľ���
    classLabelVector = [] # ׼�����ص�����ǩ
    fr = open(filename)
    index = 0
    for line in arrayLines:
        line = line.strip() # ȥ����β�ո�
        listFromLine = line.split('\t') # ��tab���ŷָ��ַ���
        returnMat[index,:] = listFromLine[0:3] # ȡǰ���и��Ƹ�����ĵ�ǰ��
        classLabelVector.append(int(listFromLine[-1])) # ȡ�����һ����ӵ�����ǩ������
        index += 1
    return returnMat,classLabelVector

datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')

'''
���ݱ�׼��
'''
def autoNorm(dataSet):
    minVals = dataSet.min(0) # 0ȡ�е���Сֵ
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))
    return normDataSet, ranges, minVals

normMat, ranges, minVals = autoNorm(datingDataMat)

'''
�鿴���ݷֲ�
'''
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels)) # XYֵ������������������ʾ��ͬ���ĵ�
ax.axis([-2,25,-0.2,2.0]) # ��������ʾ��ֵ��
plt.xlabel('Percentage of Time Spent Playing Video Games') # X����
plt.ylabel('Liters of Ice Cream Consumed Per Week') # Y����
plt.show()

'''
����
'''
def datingClassTest():
    hoRatio = 0.10      # ���Լ�ռ��
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')# ��������
    normMat, ranges, minVals = autoNorm(datingDataMat) # ����
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio) # ���Լ�����
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3) # ����
        print ("the classifier came back with: {0:d}, the real answer is: {1:d}".format(classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0 # �ۼƴ������
    print ("the total error rate is: {0:f}".format(errorCount/float(numTestVecs))) # ���������
    print (errorCount)
	
datingClassTest()