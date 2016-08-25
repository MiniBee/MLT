 # -*- coding:utf-8 -*-
'''
Created on 2016年8月22日

@author: Administrator
线性回归算法
'''
import pandas
from sklearn import datasets, linear_model, pipeline
from sklearn import preprocessing 

def get_data(file_name):
    data = pandas.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
#     "TV","Radio","Newspaper","Sales"
    for TV, Radio, Newspaper, Sales in zip(data['TV'], data['Radio'], data['Newspaper'], data['Sales']):
        X_parameter_sub = []
        X_parameter_sub.append(TV)
        X_parameter_sub.append(Radio)
        X_parameter_sub.append(Newspaper)
        X_parameter.append(X_parameter_sub)
        Y_parameter.append(Sales)

    return X_parameter, Y_parameter

def linear_model_main(X_parameters,Y_parameters,predict_value):
#    用的最小二乘法
#     regr = pipeline.Pipeline([('poly', preprocessing.PolynomialFeatures(degree=2)),  
#                     ('linear', linear_model.LinearRegression(fit_intercept=False))])  
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters,Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_                #theta0
    predictions['coefficient'] = regr.coef_                   #theta1,2,3...
    predictions['predicted_value'] = predict_outcome
    return predictions


X, Y = get_data(r'D:\Advertising.csv')
print len(X)
print len(Y)
predictvalue = [232.1,8.6,8.7]
# print linear_model_main(X, Y, predictvalue)

# Y_Predict = []
# for x in X:
#     Y_Predict.append(linear_model_main(X, Y, x).get('predicted_value'))

# print Y_Predict







