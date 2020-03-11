# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:27:25 2020

@author: Gokulraj
"""

import sqlite3

def creatTable(con,cur):
    cur.execute(""" CREATE TABLE student( regno integer,name text)""")
    con.commit()
def insertValuesInTable(con,cur):
    cur.execute("INSERT INTO student VALUES (1721118,'gokul')")
    con.commit()
def fetchValues(con,cur):
    cur.execute("SELECT * FROM student")
    print(cur.fetchall())
    con.commit()
if __name__=='__main__':
    con=sqlite3.connect("student1.db")
    cur=con.cursor()
    creatTable(con,cur)
    insertValuesInTable(con,cur)
    fetchValues(con,cur)
    con.close()