# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:34:27 2020

@author: Gokulraj
"""
import math
def area(length,width):
    return length*width
def area(half,base,height):
    return half*(base*height)
def area(radius):
    return 4*(math.pi*(radius**2))
print(area(1))
print(area(0.5))
print(area(8,9,-))