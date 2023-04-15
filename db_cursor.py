#read from a database sqlite and output the data to console
import sqlite3
import sys
import os

#get full path of CARMDI.db
path = os.path.dirname(os.path.realpath(__file__))


#connect to the database
conn = sqlite3.connect(os.path.join(path, "CARMDI.db"), check_same_thread=False)
c = conn.cursor()

def handle_data(data, col_names):
    dataJSON = []
    for row in data:
        dataJSON.append(dict(zip(col_names, row)))
    return dataJSON


# select data from the table  matching a specific number, wrap it in a function
def select_cars(value):
    c.execute('SELECT * FROM CARMDI WHERE ActualNB = ?', (value,))
    #get column names
    col_names = [cn[0] for cn in c.description]
    data = c.fetchall()
    return handle_data(data, col_names)

def handle_phone_number(telNum):
    output=""
    for ch in telNum:
        if ch.isdigit():
            output+=ch
    
    return output

def select_phone_numbers(value):
    #select from CARMDI where TelProp like '%value%'
    c.execute('SELECT * FROM CARMDI WHERE TelProp LIKE ?', ('%'+value+'%',))
    col_names = [cn[0] for cn in c.description]
    data = c.fetchall()
    return handle_data(data, col_names)

# print(select_phone_numbers("697278"))





    




