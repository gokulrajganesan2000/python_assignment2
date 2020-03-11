# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 20:34:58 2020

@author: Gokulraj
"""

import socket
import sys
import time

s=socket.socket()
host=input(str('Enter Host Name : '))
port=8080
s.connect((host,port))
while True:
    incomming_msg=s.recv(1024)
    incomming_msg=incomming_msg.decode()
    print('server :',incomming_msg)
    sent_msg=input('>>')
    sent_msg=sent_msg.encode()
    send_msg=s.send(sent_msg)