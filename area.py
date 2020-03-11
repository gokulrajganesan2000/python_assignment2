# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:49:25 2020

@author: Gokulraj
"""
import math

class ShapeArea:
    def area(length,width):
        return length*width
    def area(half,base,height):
        return half*(base*height)
    def area(radius):
        return 4*(math.pi*(radius**2))
s=ShapeArea()
print(s.area(1,2))