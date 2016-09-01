# -*- coding: utf-8 -*-
'''
Created on 2016年9月1日

@author: Administrator
softmax回归，分类算法，解决多分类问题，类标签数量大于2，为logistic回归在多分类问题上的推广
'''

import numpy

def get_data(file_name):
    lines = open(file_name)
    dataMat = []
    labelMat = []
    lines.readline()
    for line in lines.readlines():
        lineArray = line.strip().split(r';')
        dataLineMat = []
        for a in lineArray[:-1]:
            dataLineMat.append(float(a))
        dataMat.append(dataLineMat)
        labelMat.append(float(lineArray[-1]))
    return numpy.mat(dataMat), numpy.mat(labelMat).T, set(labelMat)

def gradAscent(dataMat, labelMat, uniqueLabel, alpha = 0.01, maxCycle = 100):
    for j in range(80):
        m, n = numpy.shape(dataMat)
        weights = (numpy.ones((n, len(uniqueLabel))))
        error = numpy.mat(numpy.exp(dataMat * weights))
        rowsum = -error.sum(axis=1)
        rowsum = rowsum.repeat(len(uniqueLabel), axis=1)
        error = error / rowsum
        for i in range(m):
            error[i, labelMat[i, 0]] += 1
    weights += alpha * dataMat.T * error
    return weights

def classify(dataMat, weights):
    p = dataMat * weights
    return p.argmax(1)[0,0]

if __name__ == '__main__':
    file_name = r'D:\data\wineQ\winequality-white.csv'
    dataMat, labelMat, uniqueLabel = get_data(file_name)
    weights = gradAscent(dataMat[0:3000], labelMat[0:3000], uniqueLabel)
    print  weights
    testData = numpy.mat([6,0.21,0.38,0.8,0.02,22,98,0.98941,3.26,0.32,11.8])
    testLabel = numpy.mat([6])
    p = classify(testData, weights)
    print p
    
    
    
    



