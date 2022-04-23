# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:29:09 2021

@author: jameswang
"""

def plusOne(digits):
    toString = ''
    for i in range(len(digits)):
        toString += str(digits[i])
    t = str(int(toString)+1)
    return[i for i in t] 
    
    
print(plusOne([1,2,3]))