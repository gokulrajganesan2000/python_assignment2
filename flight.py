# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:38:09 2020

@author: Gokulraj
"""

class Flight:
    def __init__(self,fligh_no,source,destination,fare):
        self.fligh_no=fligh_no
        self.source=source
        self.destination=destination
        self.fare=fare
    def flightInformation(self):
        return f'Flight number : {self.fligh_no} \n \
            Source : {self.source} \n \
            Destination : {self.destination} \n \
            Fare : {self.fare}'
flight1=Flight(1234, 'chennai', 'delhi', 40000)
print(flight1.flightInformation())  