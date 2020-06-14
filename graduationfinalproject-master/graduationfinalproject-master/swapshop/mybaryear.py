'''
author: Waiyat Hamdani                      project-term :Spring 2020 (3 months)
        Aseel Fawalha
'''

import sqlite3
import sys
global connections
connections=sqlite3.connect('swapshop.db',check_same_thread=False)


# for pi chart in /success path category and total pick up in pie chart
def binder(x):
    conn=connections.cursor()
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'binder' and yearout = '{}' ".format(x)) #total value is actually value per item , I name it wrong.
    x=conn.fetchall()
    #print(x, file=sys.stderr)
    temp= x[0][0]
    if temp == 'null' or temp == None or temp =='None' or temp == 'none':
        result=0
        #print(result, file=sys.stderr)
        return result
    else:
        result=temp
        #print(result, file=sys.stderr)
        return result

def envelope(x):
    conn=connections.cursor()
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'envelope' and yearout = '{}' ".format(x)) #total value is actually value per item , I name it wrong.
    x=conn.fetchall()
    temp= x[0][0]
    if temp == 'null' or temp == None or temp =='None' or temp == 'none':
        result=0
        #print(result, file=sys.stderr)
        return result
    else:
        result=temp
        #print(result, file=sys.stderr)
        return result

def dtl(x):
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Divders, Tabs and Labels' and yearout = '{}' ".format(x))
    #total value is actually value per item , I name it wrong.------------------------
    x=conn.fetchall()
    temp= x[0][0]
    if temp == 'null' or temp == None or temp =='None' or temp == 'none':
        result=0
        print(result, file=sys.stderr)
        return result
    else:
        result=temp
        #print(result, file=sys.stderr)
        return result

def fileandfolder(x):
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Files and Folders' and yearout = '{}'  ".format(x))
    #total value is actually value per item , I name it wrong.-------------------------
    x=conn.fetchall()
    temp= x[0][0]
    if temp == 'null' or temp == None or temp =='None' or temp == 'none':
        result=0
        #print(result, file=sys.stderr)
        return result
    else:
        result=temp
        #print(result, file=sys.stderr)
        return result

def paper(x):
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Paper' and yearout = '{}' ".format(x))
    #total value is actually value per item , I name it wrong.-------------------------
    x=conn.fetchall()
    temp= x[0][0]
    if temp == 'null' or temp == None or temp =='None' or temp == 'none':
        result=0
        #print(result, file=sys.stderr)
        return result
    else:
        result=temp
        #print(result, file=sys.stderr)
        return result

def organizationalsupplies(x):
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Organizational Supplies' and yearout = '{}' ".format(x))
    #total value is actually value per item , I name it wrong.-------------------------
    x=conn.fetchall()
    temp= x[0][0]
    if temp == 'null' or temp == None or temp =='None' or temp == 'none':
        result=0
        #print(result, file=sys.stderr)
        return result
    else:
        result=temp
        #print(result, file=sys.stderr)
        return result

def generaloffice(x):
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'General Office Supplies' and yearout = '{}' ".format(x))
    #total value is actually value per item , I name it wrong.-------------------------
    x=conn.fetchall()
    temp= x[0][0]
    if temp == 'null' or temp == None or temp =='None' or temp == 'none':
        result=0
        #print(result, file=sys.stderr)
        return result
    else:
        result=temp
        #print(result, file=sys.stderr)
        return result

def electronic(x):
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Electronics' and yearout = '{}' ".format(x))
    #total value is actually value per item , I name it wrong.-------------------------
    x=conn.fetchall()
    temp= x[0][0]
    if temp == 'null' or temp == None or temp =='None' or temp == 'none':
        result=0
        #print(result, file=sys.stderr)
        return result
    else:
        result=temp
        #print(result, file=sys.stderr)
        return result

def allsalestatistic(x):
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where yearout = '{}' ".format(x))
    #total value is actually value per item , I name it wrong.-------------------------
    x=conn.fetchall()
    temp= x[0][0]
    if temp == 'null' or temp == None or temp =='None' or temp == 'none':
        result=0
        #print(result, file=sys.stderr)
        return result
    else:
        result=temp
        #print(result, file=sys.stderr)
        return result
