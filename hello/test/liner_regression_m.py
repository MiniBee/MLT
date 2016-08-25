# -*- coding:utf-8 -*-
'''
Created on 2016年8月24日

@author: Administrator
'''
import numpy

def get_data(file_name):
    a = chr(32)
    lines = open(file_name)
    X_parameter = []
    Y_parameter = []

    for line in lines.readlines():
        x = line.split(a)
        xflt = []
        for xApp in x[:-1]:
            xflt.append(float(xApp))
        X_parameter.append(xflt)
        Y_parameter.append(float(x[-1]))
    return X_parameter, Y_parameter

def standRegres(xArr, yArr):
    xMat = numpy.mat(xArr)
    yMat = numpy.mat(yArr).T
    xTx = xMat.T*xMat
    if numpy.linalg.det(xTx) == 0.0:
        ws = numpy.linalg.pinv(xTx)*(xMat.T*yMat)  
        return ws
    return xTx.I*xMat.T*yMat

def lwlr(testPoint,xArr,yArr,k=1.0):
    xMat = numpy.mat(xArr); yMat = numpy.mat(yArr).T
    m = numpy.shape(xMat)[0]
    weights = numpy.mat(numpy.eye((m)))
    for j in range(m):                      #next 2 lines create weights matrix
        diffMat = testPoint - xMat[j,:]
        weights[j,j] = numpy.exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx = xMat.T * (weights * xMat)
    if numpy.linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint*ws

file_name = r'D:\data\abalone\m0f1i2Dataset.data'
x, y = get_data(file_name)

def lwlrTest(testArr, xArr, yArr, k): #当对testArr中所有点的估计，testArr=xArr时，即对所以点的全部估计  
    m = numpy.shape(testArr)[0]
    yHat = numpy.zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat
    
ws = standRegres(x, y)
s = x * ws

lwlrTest(x[0:600], x[0:600], y[0:600], 1)

