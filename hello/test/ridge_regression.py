# -*- coding:utf-8 -*-
'''
Created on 2016年8月25日

@author: Administrator

linear_model提供的岭回归，
和我自己写的岭回归结果有区别，
是由于没用进行数据标准化造成的

'''
import numpy
import pylab as plt

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
    return (X_parameter), (Y_parameter)

xArr, yArr = get_data(r'D:\data\abalone\m0f1i2Dataset.data')
from sklearn import linear_model
clf = linear_model.Ridge(fit_intercept=False)
coefs = []
for a in range(30):
    clf.set_params(alpha=numpy.exp(a - 10))
    clf.fit(xArr, yArr)
    coefs.append(clf.coef_)

fig = plt.figure()     
ax  = fig.add_subplot(111)  
ax.plot(coefs)  
plt.show() 




