# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:07:49 2020

@author: Gokulraj
"""

class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,regno): 
        super().__init__(name)
        self.regno=regno
class mark(student):
    total=0
    def __init__(self,name,regno,marks):
        super().__init__(name,regno)
        self.marks=marks
    def calculate_total(self):
        for i in self.marks:
            self.total+=i
    def print_detail(self):
        print(self.name,self.regno,self.total)
        
d=mark('gokul',1721118,[50,40,45,55])
d.calculate_total()
d.print_detail()

