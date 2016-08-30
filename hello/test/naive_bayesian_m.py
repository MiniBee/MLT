# -*- coding: utf-8 -*-
'''
Created on 2016年8月30日

@author: Administrator
'''
import numpy
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]
    return postingList, classVec

def createVocabList(dataSet):
    vocabSet = set([])
    for data in dataSet:
        vocabSet = vocabSet | set(data)
    return list(vocabSet)

def setOfWord2Vec(vocabSet, inputSet):
    returnVec = [0] * len(vocabSet)
    for word in inputSet:
        if word in vocabSet:
            returnVec[vocabSet.index(word)]+=1
        else:
            print 'hello...'
    return returnVec

def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pa = sum(trainCategory)/float(numTrainDocs)  
    r1 = numpy.ones(numWords)
    r0 = numpy.ones(numWords)
    d0 = 2.0; d1 = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 0:
            r0 += trainMatrix[i]
            d0 += sum(trainMatrix)
        else:
            r1 += trainMatrix[i]
            d1 += sum(trainMatrix)
    p0 = numpy.log(r0 / d0)
    p1 = numpy.log(r1 / d1)
    return p0, p1, pa
            
def classifyNB(vec2Classify, p0, p1, pclass):
    p1 = numpy.sum(vec2Classify * p1) + numpy.log(pclass)
    p0 = numpy.sum(vec2Classify * p0) + numpy.log(1-pclass)
    if p1 > p0:
        return 1
    else:
        return 0
    
def testingNB():
    dataArr, labelArr = loadDataSet()
    dataVec = createVocabList(dataArr)
    trainMat = []
    for data in dataArr:
        trainMat.append(setOfWord2Vec(dataVec, data))
    p0, p1, pa = trainNB0(numpy.array(trainMat), numpy.array(labelArr))
    testEntry = ['love','my','dalmation']
    thisDoc = setOfWord2Vec(dataVec, testEntry)
    print classifyNB(thisDoc, p0, p1, pa)
    
    testEntry = ['stupid','garbage']
    thisDoc = setOfWord2Vec(dataVec, testEntry)
    print classifyNB(thisDoc, p0, p1, pa)


def testParse(bigString):
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

def spamTest():
    docList = []; classList = []; fullText = []
    for i in range(1, 26):
        #1为垃圾邮件。。。
        wordList = testParse(open(r'D:\data\email\spam\%d.txt' % i).read())
        docList.append(wordList)
        classList.append(1)
        fullText.extend(wordList)
        wordList = testParse(open(r'D:\data\email\ham\%d.txt' % i).read())
        docList.append(wordList)
        classList.append(0)
        fullText.extend(wordList)
    vocabList = createVocabList(docList)
    trainingSet = range(50)
    testSet = []
    for i in range(10):
        randIndex = int(numpy.random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []; trainClass = []
    for docIndex in trainingSet:
        trainMat.append(setOfWord2Vec(vocabList, docList[docIndex]))
        trainClass.append(classList[docIndex])
    p0, p1, pa = trainNB0(numpy.array(trainMat), numpy.array(trainClass))
    errorCount = 0.0
    for docIndex in testSet:
        wordVec = setOfWord2Vec(vocabList, docList[docIndex])
        print '预测值：', classifyNB(numpy.array(wordVec), p0, p1, pa), '->', '实际值：',classList[docIndex]
        if classifyNB(numpy.array(wordVec), p0, p1, pa) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is: ', float(errorCount)/len(testSet)
    
if __name__ == '__main__':
#     testingNB()
    spamTest()
    






