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
        
    
get_data('')