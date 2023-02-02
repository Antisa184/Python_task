#!/usr/bin/python
from connect import connect
import glob
from readFile import readFile


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


if __name__ == '__main__':
    fileName=chooseFile()

    print("Reading the first sheet with pre-determined columns (for demo simplicity)")
    sheet = readFile(fileName)
        
    connect(sheet)