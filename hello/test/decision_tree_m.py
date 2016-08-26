# -*- coding: utf-8 -*-
'''
Created on 2016年8月26日

@author: Administrator
'''
from math import log
import operator

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        a = float(labelCounts[key])/numEntries
        shannonEnt -= a * log(a, 2)
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVal in dataSet:
        if featVal[axis] == value:
            reducedFeatVec = featVal[:axis]  
            reducedFeatVec.extend(featVal[axis+1:])  
            retDataSet.append(reducedFeatVec)  
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    baseEntropy = calcShannonEnt(dataSet)
    numFeatures = len(dataSet[0])-1
    print numFeatures
    bestFeature = -1
    bestInfoGain = 0.0
    for i in range(numFeatures):
        #属性相同的一列元素
        featureList = [example[i] for example in dataSet]
        uniqueVals = set(featureList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i , value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        #获取该feature的信息增益
        infogain = baseEntropy - newEntropy
        if(infogain > bestInfoGain):
            bestInfoGain = infogain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for val in classList:
        if val not in classCount.keys():
            classCount[val] = 0
        classCount[val] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(dataSet)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValue = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValue)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

def createDataSet():  
    dataSet = [['a',1,1,'yes'],
               ['b',1,0,'yes'],
               ['a',1,0,'no'],
               ['a',0,1,'no'],
               ['a',0,1,'no']]
    labels = ['tom', 'no surfacing', 'flippers']
    return dataSet, labels

def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]  
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else: 
                classLabel = secondDict[key]
    return classLabel

myDat, labels = createDataSet()
myTree = createTree(myDat,labels)
print myTree
labels = ['tom', 'no surfacing', 'flippers']
print classify(myTree, labels, ['a',1,1])

def get_data(file_name):
    data = open(file_name)
    label = []
    for line in data:
        a = line.split(r',')
        label.append(a)
    return label
    



    
    
    
