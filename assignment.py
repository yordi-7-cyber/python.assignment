# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 09:16:40 2025

@author: female
"""

def swap(x,y):
    x,y=y,x
    return x,y
x=int(input("Enter your value of x:"))
y=int(input("Enter your value of y:"))
value=swap(x,y)
print("before swapping:",(x,y))
print("After swapping:",value)