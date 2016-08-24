# -*- coding:utf-8 -*-
'''
Created on 2016年8月24日

@author: Administrator
'''
import numpy
from sklearn import datasets, linear_model


def get_data(file_name):
    data = open(file_name)
    X_parameter = []
    Y_parameter = []
    a = chr(32)
    for line in data.readlines():
        xArr = []
        curLine = line.split(a)
        for x in curLine[:-1]:
            xArr.append(float(x))
        X_parameter.append(xArr)
        Y_parameter.append(float(curLine[-1]))
        
    return X_parameter, Y_parameter

def line_model_main(X_parameters,Y_parameters,predict_value):
    #最小二乘法
    regr = linear_model.LinearRegression(fit_intercept=False)
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_                #theta0
    predictions['coefficient'] = regr.coef_                   #theta1,2,3
    predictions['predicted_value'] = predict_outcome
    return predictions
    
    
if __name__ == '__main__':
    file_name = r'D:\data\abalone\m0f1i2Dataset.data'
    data, label = get_data(file_name)
    predict_value = data[2]
    predictions = line_model_main(data, label, predict_value)
    print predictions

# -0.18407619,   7.56568374,  12.5885849 ,  14.55197454, 8.70127448, -21.23243391, -12.09970498,   6.40656255
# -0.3884832 ,  -0.82639908,  11.96403178,  11.20449196, 9.07020864, -20.10614364, -10.15510106,   8.70110596