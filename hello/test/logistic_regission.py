# -*- coding: utf-8 -*-
'''
Created on 2016年8月29日

@author: Administrator

用于解决线性分类问题

'''
from sklearn import linear_model


def get_data(file_name):
    lines = open(file_name)
    dataMat = []; labelMat = []
    for line in lines.readlines():
        array = line.split('\t')
        dataM = []
        for data in array[:-1]:
            dataM.append(float(data))
        dataMat.append(dataM)
        labelMat.append(float(array[-1]))
    return dataMat, labelMat

file_name = r'D:\data\logisticRegression\testSet2.txt'
x_train, y_train = get_data(file_name)
logreg = linear_model.LogisticRegression(C=1e5, solver='lbfgs', multi_class='multinomial')
logreg.fit(x_train, y_train)
x_test, y_test = get_data(r'D:\data\logisticRegression\testSet3.txt')
logreg_prob = logreg.predict_proba(x_test)
logreg_pred = logreg.predict(x_test)
print logreg_prob, logreg_pred



