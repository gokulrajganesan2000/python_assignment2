# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:08:24 2020

@author: Gokulraj
"""

class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def printDetail(self):
        print('*'*40)
        print('Car Detail')
        print('*'*40)
        print(f'model :{self.model}\nname :{self.name}')
        print('*'*40)
class Bus:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def printDetail(self):
        print('*'*40)
        print('bus Detail')
        print('*'*40)
        print(f'model :{self.model}\nname :{self.name}')
        print('*'*40)
class Vehicle(Car,Bus):
    def __init__(self,name,model,vehicle):
        if vehicle=='car':
            Car.__init__(self,name,model)
            Car.printDetail(self)
        if vehicle=='bus':
            Bus.__init__(self,name,model)
            Bus.printDetail(self)
vehicle1=Vehicle('benz', '1010', 'bus')
vehicle2=Vehicle('renolt', '1010', 'car')       