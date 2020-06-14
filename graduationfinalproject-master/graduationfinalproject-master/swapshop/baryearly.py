'''
author: Waiyat Hamdani                      project-term :Spring 2020 (3 months)
        Aseel Fawalha
'''

import sqlite3
import sys
global connections
connections=sqlite3.connect('swapshop.db',check_same_thread=False)


# for pi chart in /success path category and total pick up in pie chart
def binder(x,y):
    conn=connections.cursor()
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'binder' and yearout = '{}' and monthout='{}' ".format(x,y)) #total value is actually value per item , I name it wrong.
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

def envelope(x,y):
    conn=connections.cursor()
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'envelope' and yearout = '{}' and monthout='{}' ".format(x,y)) #total value is actually value per item , I name it wrong.
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

def dtl(x,y):
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Divders, Tabs and Labels' and yearout = '{}'and monthout='{}' ".format(x,y))
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

def fileandfolder(x,y):
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Files and Folders' and yearout = '{}' and monthout='{}' ".format(x,y))
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

def paper(x,y):
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Paper' and yearout = '{}' and monthout='{}' ".format(x,y))
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

def organizationalsupplies(x,y):
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Organizational Supplies' and yearout = '{}'and monthout='{}' ".format(x,y))
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

def generaloffice(x,y):
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'General Office Supplies' and yearout = '{}' and monthout='{}' ".format(x,y))
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

def electronic(x,y):
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where category = 'Electronics' and yearout = '{}' and monthout='{}' ".format(x,y))
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

def allsalestatistic(x,y):
    conn=connections.cursor()
    #total value is actually value per item , I name it wrong.-------------------------
    conn.execute("select sum(quantity*totalvalue) from itemout where yearout = '{}' and monthout='{}' ".format(x,y))
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
