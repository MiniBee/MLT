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
    for line in lines.readline():
        x = line.strip().split(a)
        xflt = []
        for xApp in x[:-1]:
            xflt.append(float(xApp))
        X_parameter.append(xflt)
        Y_parameter.append(float(x[-1]))
    return X_parameter, Y_parameter
get_data('')