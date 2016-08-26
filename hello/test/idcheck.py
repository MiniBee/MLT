 # -*- coding:utf-8 -*-
'''
Created on 2016年8月21日

@author: Administrator
'''
class idcheck:
    import string
    alphas = string.letters + '_'
    nums = string.digits
    print 'Welcome to the Identifier Checker v1.0'
    print 'Testees must be at least 2 chars long.'
    
    myInput = raw_input('Identifier to test?')
    if len(myInput) >1 :
        if myInput[0] not in alphas:
            print ''' invalid: first symbol must be
             alphabetic '''
        else:
            for otherChar in myInput[1:]:
                if otherChar not in (alphas + nums):
                    print 'invalid: remaining symbols must be alphamuberic'
                    break
            else:
                print 'okay as an \n identifier'
                    
#     print nums

if __name__ == '__main__':
    idcheck
    pass