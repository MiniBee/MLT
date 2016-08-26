 # -*- coding:utf-8 -*-
'''
Created on 2016年8月25日

@author: Administrator
'''
import numpy
import pylab as plt

def ridgeRegers(xMat, yMat, lam = 0.2):
    xTx = xMat.T*xMat
    denom = xTx + numpy.eye(numpy.shape(xMat)[1])*lam
    if numpy.linalg.det(denom) ==0.0:  
        print "this matrix is singular, cannot do inverse"  
        ws = numpy.linalg.pinv(denom)*(xMat.T*yMat)
    
    ws = denom.I * xMat.T * yMat
    return ws

def standard_data(xArr, yArr):
    xMat = numpy.mat(xArr)
    yMat = numpy.mat(yArr).T
    yMean = numpy.mean(yMat, 0)
    yMat = yMat - yMean
    xMean = numpy.mean(xMat, 0)
    xVar = numpy.var(xMat, 0)
    xMat = (xMat - xMean)/xVar
    return xMat, yMat

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
    return numpy.mat(X_parameter), numpy.mat(Y_parameter)

def ridgeTest(xMat, yMat):
    numTestPts = 30  
    wMat = numpy.zeros((numTestPts, numpy.shape(xMat)[1]))  
    for i in range(numTestPts):
        ws = ridgeRegers(xMat, yMat, numpy.exp(i-10))
        wMat[i,:] = ws.T
    return wMat

xArr, yArr = get_data(r'D:\data\abalone\m0f1i2Dataset.data')
xMat, yMat = standard_data(xArr, yArr)
ws = ridgeTest(xMat, yMat)

fig = plt.figure()     
ax  = fig.add_subplot(111)  
ax.plot(ws)  
plt.show() 

