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
