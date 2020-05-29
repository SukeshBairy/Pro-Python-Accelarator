# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:57:59 2020

@author: Sukesh
"""

def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b


print("before swapping")
a=int(input('enter the number of a:'))
b=int(input('enter the number of b:'))
print("after swapping")

print("the value of a and b are ",swap(a,b))



    
    
    
    
