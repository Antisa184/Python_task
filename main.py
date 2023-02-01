#!/usr/bin/python
import pandas as pd
import psycopg2
from config import config
import glob
import readFile

def chooseFile():
    while(True):
        print("Choose an excel file from the following (type the order number and press ENTER): ")
        arr=glob.glob('./*.xls*')
        for i,file in enumerate(arr):
            print(str(i+1)+'.',file)
        i=input()
        if not i.isnumeric() or (i.isnumeric() and int(i)>len(arr)):
            continue
        else:
            i=int(i)
            break
    return arr[i-1]

def connect(sheet):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
    # create a table
     
    # load rows
   
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    fileName=chooseFile()

    print("Reading the first sheet with pre-determined columns (for demo simplicity)")
    sheet = readFile.readFile(fileName)
        
    connect(sheet)