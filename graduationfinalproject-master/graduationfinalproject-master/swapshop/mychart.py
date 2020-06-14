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
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'binder' ") #total value is actually value per item , I name it wrong.
    x=conn.fetchall()
    result= x[0][0]
    return result

def envelope():
    conn=connections.cursor()
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'envelope' ") #total value is actually value per item , I name it wrong.
    x=conn.fetchall()
    result= x[0][0]
    return result

def dtl():
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Divders, Tabs and Labels' ")
    #total value is actually value per item , I name it wrong.------------------------
    x=conn.fetchall()
    result= x[0][0]
    return result

def fileandfolder():
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Files and Folders' ")
    #total value is actually value per item , I name it wrong.-------------------------
    x=conn.fetchall()
    result= x[0][0]
    return result

def paper():
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Paper' ")
    #total value is actually value per item , I name it wrong.-------------------------
    x=conn.fetchall()
    result= x[0][0]
    return result

def organizationalsupplies():
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Organizational Supplies' ")
    #total value is actually value per item , I name it wrong.-------------------------
    x=conn.fetchall()
    result= x[0][0]
    return result

def generaloffice():
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'General Office Supplies' ")
    #total value is actually value per item , I name it wrong.-------------------------
    x=conn.fetchall()
    result= x[0][0]
    return result

def electronic():
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Electronics' ")
    #total value is actually value per item , I name it wrong.-------------------------
    x=conn.fetchall()
    result= x[0][0]
    return result

def allsalestatistic():
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout ")
    #total value is actually value per item , I name it wrong.-------------------------
    x=conn.fetchall()
    result= x[0][0]
    return result
