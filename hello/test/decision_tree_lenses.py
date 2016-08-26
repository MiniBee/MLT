# -*- coding: utf-8 -*-
'''
Created on 2016年8月26日

@author: Administrator
'''
from math import log
import operator

def get_base_entropy(dataSet):
    num_entries = len(dataSet)
    labelCounts = {}
    for featVal in dataSet:
        featLabel = featVal[-1]
        if featLabel not in labelCounts.keys():
            labelCounts[featLabel] = 0
        labelCounts[featLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prop = float(labelCounts[key])/float(num_entries)
        shannonEnt -= prop * log(prop, 2)
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
    baseEntropy = get_base_entropy(dataSet)
    bastFearture = -1
    newEntropy = 0.0
    numEntries = len(dataSet[0])-1
    bastInfoGain = 0.0
    for i in range(numEntries):
        featureList = [example[i] for example in dataSet]
        uniqueFet = set(featureList)
        newEntropy = 0.0
        for value in uniqueFet:
            subDataSet = splitDataSet(dataSet, i, value)
            prop = float(len(subDataSet))/float(len(dataSet))
            newEntropy += prop * get_base_entropy(subDataSet)
        infogain = baseEntropy - newEntropy
        if infogain > bastInfoGain:
            bastInfoGain = infogain
            bastFearture = i
    return bastFearture

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
    bastLabel = labels[bestFeat]
    myTree = {bastLabel: {}}
    del(labels[bestFeat])
    featValue = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValue)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bastLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree
 
def classify(myTree, labels, testVec):
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    featIndex = labels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], labels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel    
    
def get_data(file_name):
    lines = open(file_name)
    dataSet = []
    for line in lines:
        lineSub = line.split('\t')
        dataSet.append(lineSub)
    return dataSet

labels = ['a','b','c','d']
dataSet = get_data(r'D:\data\lenses.txt')
myTree = createTree(dataSet, labels)
print myTree
 
testVec = ['young', 'myope', 'no', 'normal']
labels = ['a','b','c','d']
print classify(myTree, labels, testVec)



