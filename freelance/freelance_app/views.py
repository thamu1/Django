from django.shortcuts import render, redirect
from .models import *
from django.db import connection
from django.contrib.auth import login,logout,authenticate
# import cgi
# import mysql.connector


# cursor = connection.cursor()
# tableName = 'freelance'


# def query_exec(query, typeOfExec = "select"):
#     if(typeOfExec in ["select"]):
#         cursor.execute(query)
#         result = cursor.fetchall()
        
#         return(result)
        
#     elif(typeOfExec in ["update", "insert", "create"]):
#         cursor.execute(query)
        
#         return(cursor.rowcount)

def home(request):
    if(request.method == 'POST'):
        if('submit' in request.POST):
            firstname=request.POST["firstname"]
            lastname=request.POST["lastname"]
            email=request.POST["email"]
            phone=request.POST["phone"]
            message=request.POST["message"]
            submit=request.POST["submit"]
            
            # create_table = f"create table if not exists freelance.freelance_user_entry"\
            #             f"(firstname varchar(50), lastname varchar(50),"\
            #             f"email varchar(100) primary key, phone_number varchar(10) not null,"\
            #             f"message varchar(255) default 'nothing')"
                    
                        
            # ressult = query_exec(query= create_table, typeOfExec= "create")
            
            # insert_sql = f"insert into freelance_user_entry"\
            # f"(firstname, lastname, email, phone_number, message)"\
            # f"values ('{firstname}', '{lastname}', '{email}', '{phone}', '{message}')"
            
            # result = query_exec(query= insert_sql, typeOfExec= "insert")
            
            # if(result == 1):
            #     val = { "val" : "You are our family now"}
            # else:
            #     val = {"val" : "ohh!, please check your data"}

            val = { "val" : "You are our family now"}
            
            return render(request, 'index.html', context= val)
            
        pass
    else:
        return render(request, 'index.html')



