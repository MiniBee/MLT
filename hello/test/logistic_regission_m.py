# -*- coding: utf-8 -*-
'''
Created on 2016年8月29日

@author: Administrator
'''
import numpy
import time
import matplotlib.pyplot as plt

def sigmoid(inX):
    return 1.0 / (1+numpy.exp(-inX))

def gradAscent(dataMat, laberMat, alpha = 0.01, maxCycle = 500):
    start_time = time.time()
    m, n = numpy.shape(dataMat)
    weitht = numpy.ones((n, 1))
    for i in range(maxCycle):
        h = sigmoid(dataMat * weitht)
        error = laberMat - h
        weitht += alpha * dataMat.T * error
    print 'time = ', time.time() - start_time
    return weitht

def stocGradAscent(dataMat, labelMat, alpha = 0.01):
    start_time = time.time()
    m, n = numpy.shape(dataMat)
    weight = numpy.ones((n, 1))
    for i in range(m):
        h = sigmoid(dataMat[i] * weight)
        error = labelMat[i] - h
        weight += alpha * dataMat[i].T * error
    print 'time = ', time.time() - start_time
    return weight

def betterStocGradAscent(dataMat, labelMat, alpha = 0.01, numIter = 150):
    start_time = time.time()
    m, n = numpy.shape(dataMat)
    weight = numpy.ones((n, 1))
    for j in range(numIter):
        for i in range(m):
            alpha = 4 / (1 + j + i) + 0.01
            h = sigmoid(dataMat[i] * weight)
            error = labelMat[i] - h
            weight += alpha * dataMat[i].T * error
    
    print 'time = ', time.time() - start_time
    return weight

def show(dataMat, labelMat, weights):
    m, n = numpy.shape(dataMat)
    min_x = min(dataMat[:,1])[0, 0]
    max_x = max(dataMat[:,1])[0, 0]
    xcoord1 = []; ycoord1 = []
    xcoord2 = []; ycoord2 = []
    for i in range(m):
        if int(labelMat[i, 0]) == 0:
            xcoord1.append(dataMat[i, 1]); ycoord1.append(dataMat[i, 2])
        elif int(labelMat[i, 0]) == 1:
            xcoord2.append(dataMat[i, 1]); ycoord2.append(dataMat[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcoord1, ycoord1, s=30, c="red", marker="s")
    ax.scatter(xcoord2, ycoord2, s=30, c="green")
    x = numpy.arange(min_x, max_x, 0.1)
    y = (-weights[0] - weights[1]*x) / weights[2]
    
    ax.plot(x, y)
    plt.xlabel("x1"); plt.ylabel("x2")
    plt.show()

def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    print prob
    if prob > 0.5: return 1.0
    else: return 0.0

def get_data(file_name):
    lines = open(file_name)
    dataMat = []; labelMat = []
    for line in lines.readlines():
        array = line.split('\t')
        dataM = [1,]
        for data in array[:-1]:
            dataM.append(float(data))
        dataMat.append(dataM)
        labelMat.append(float(array[-1]))
    return numpy.mat(dataMat), numpy.mat(labelMat).T

if __name__ == '__main__':
    dataMat, labelMat = get_data(r'D:\data\logisticRegression\testSet.txt')
    weights = betterStocGradAscent(dataMat, labelMat, numIter=80)
    print weights
#     weights = stocGradAscent(dataMat, labelMat, 0.01)
#     dataTest, labelTest = get_data(r'D:\data\logisticRegression\testSet2.txt')
    m = numpy.shape(dataMat)[0]
    count = 0.0
    for i in range(m):
        if classifyVector(dataMat[i], weights) == labelMat[i][0]:
            count += 1
    print count /m
    show(dataMat, labelMat, weights)
    
    
    

