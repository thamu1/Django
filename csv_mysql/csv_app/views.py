from django.shortcuts import render, redirect
from .models import *
from django.db import connection
import mysql.connector as mc 
import pandas as pd 
from datetime import datetime
import os

cursor = connection.cursor()

db = 'csvDB'

logpath = r"C:\Users\ThamotharanC\OneDrive - Softcrylic LLC\Desktop\Django\csv_mysql\log.txt"

def log(txt):
    file = open(logpath,'a+')
    file.write(f"{datetime.now()} = {txt}\n\n")


def home(request):
    if request.method == 'POST':
        log("the request method is POST")
        if('upload' in request.POST):
            log("the request method is POST upload")
            file = request.FILES["csvFile"]
            log("file readed successfully")

            fileName = file.name

            file = pd.read_csv(file)
            df = pd.DataFrame(file)
            
            df = df.dropna()

            column = df.columns.to_list()

            dtype = []
            row1 = df.iloc[0].to_list()
            for i in row1:
                i = str(i)
                if i.isdigit():
                    dtype.append('int')
                elif i.isalpha():
                    n = len(i)
                    dtype.append(f'varchar ({str(n + 20)})')
                elif i.isalnum():
                    dtype.append('text')
                else:
                    try:
                        if isinstance(float(i), float):
                            dtype.append('float')
                    except:
                        dtype.append('text')

            tab = ""
            for j in range(0,len(dtype)):
                if(j == len(dtype)-1):
                    tab += f"`{column[j]}` {dtype[j]}"
                else:
                    tab += f"`{column[j]}` {dtype[j]},"   
                    
            log(f"create query is ready = {tab}")         
            
            try:
                cresql = f"create table if not exists {db}.{fileName[:-4]}({tab})"
                cursor.execute(cresql)
                text = "created successfully..."

                log(f"table created successfully")
                
                insarr = []
                for ins in range(len(df)):
                    insarr.append(tuple(df.iloc[ins].to_list()))
                    
                log(f"insert value ready = {insarr}")

                ia = str(insarr)
                inssql = f"insert into {db}.{fileName[:-4]} values{ia[1:len(ia)-1]}"
                cursor.execute(inssql)

                text = text + '\n' +"Insert Data Successfully..."
                
                log("data inserted successfully.")

                # dropsql = f"drop table {db}.{fileName[:-4]}"
                # cursor.execute(dropsql)
                
                # text = text + "\n" + "table dropped...."

                context = {"file":text}
                return render(request, 'home.html', context)
            except:
                context = {"file":"Your CSV file is not good man...Please correct ite"}
                return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')

