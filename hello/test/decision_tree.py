# -*- coding: utf-8 -*-
'''
Created on 2016年8月25日

@author: Administrator

数据必须为数字

'''
from sklearn import tree
import liner_regression_m

def get_data(file_name):
    lines = open(file_name)
    X_parameter = []
    Y_parameter = []
    lines.readline()
    for line in lines.readlines():
        w = line.strip().split(r';')
        x = []
        for a in w[:-1]:
            x.append(float(a))
        X_parameter.append(x)
        Y_parameter.append(float(w[-1]))
    return X_parameter, Y_parameter

def fit_it(X_parameter, Y_parameter, X_train):
    clf = tree.DecisionTreeClassifier(criterion='entropy', splitter='best')
    clf.fit(X_parameter, Y_parameter)
    return clf.feature_importances_, clf.predict(X_train)
    
file_name = r'D:\data\wineQ\winequality-white.csv'
x, y = get_data(file_name)
imp, pre = fit_it(x[100:4000], y[100:4000], x[0:100])
 
print imp
y[0:100]
 
count = 0
for i in range(len(pre)):
    print pre[i], '->', y[i]
    if pre[i] == y[i]:
        count +=1
print count

