# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 20:27:34 2020

@author: Gokulraj
"""

import socket
import sys
import time

s=socket.socket()
host=socket.gethostname()
print('server will start on host :',host)
port=8080
s.bind((host,port))
print('server is started')
s.listen(1)
conn,addr=s.accept()
print(addr,'has connected')
while True:
    message=input('>>')
    message=message.encode()
    conn.send(message)
    incom_msg=conn.recv(1024)
    incom_msg=incom_msg.decode()
    print('client :',incom_msg)