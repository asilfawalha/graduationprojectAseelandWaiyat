'''
author: Waiyat Hamdani                      project-term :Spring 2020 (3 months)
        Aseel Fawalha
'''
import sqlite3
global connections
connections=sqlite3.connect('swapshop.db',check_same_thread=False)



# for pi chart in /success path category and total pick up in pie chart
def binder():
    conn=connections.cursor()
    conn.execute("select sum(quantity) from itemout where category = 'binder' ")
    x=conn.fetchall()
    result= x[0][0]
    return result

def envelope():
    conn=connections.cursor()
    conn.execute("select sum(quantity) from itemout where category = 'envelope' ")
    x=conn.fetchall()
    result= x[0][0]
    return result

def dtl():
    conn=connections.cursor()
    conn.execute("select sum(quantity) from itemout where category = 'Divders, Tabs and Labels' ")
    x=conn.fetchall()
    result= x[0][0]
    return result

def fileandfolder():
    conn=connections.cursor()
    conn.execute("select sum(quantity) from itemout where category = 'Files and Folders' ")
    x=conn.fetchall()
    result= x[0][0]
    return result

def paper():
    conn=connections.cursor()
    conn.execute("select sum(quantity) from itemout where category = 'Paper' ")
    x=conn.fetchall()
    result= x[0][0]
    return result

def organizationalsupplies():
    conn=connections.cursor()
    conn.execute("select sum(quantity) from itemout where category = 'Organizational Supplies' ")
    x=conn.fetchall()
    result= x[0][0]
    return result

def generaloffice():
    conn=connections.cursor()
    conn.execute("select sum(quantity) from itemout where category = 'General Office Supplies' ")
    x=conn.fetchall()
    result= x[0][0]
    return result

def electronic():
    conn=connections.cursor()
    conn.execute("select sum(quantity) from itemout where category = 'Electronics' ")
    x=conn.fetchall()
    result= x[0][0]
    return result

def alltotalpickup():
    conn=connections.cursor()
    conn.execute("select sum(quantity) from itemout")
    x=conn.fetchall()
    result= x[0][0]
    return result

def totalweight():
    conn=connections.cursor()
    conn.execute("select sum(weight) from itemout")
    x=conn.fetchall()
    result= x[0][0]
    return result
