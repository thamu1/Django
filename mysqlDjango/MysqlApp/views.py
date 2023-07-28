from django.shortcuts import render
from django.db import connection

import mysql.connector as mc


conn = mc.connect(
    host='127.0.0.1',
    user='root',
    password='Mysql.08',
    database='world'
)

cursor = conn.cursor()

# conn = mc.connect(
#             host='127.0.0.1',
#             user='root',
#             password='Mysql.08',
#             database='world'
#         )

# cursor = conn.cursor()

# def home(request):

#     if(request.method == 'POST'):
#         if 'insert' in request.POST:
#             city = request.POST['city']
#             name1 = request.POST['name1']
#             name2 = request.POST['name2']
#             amount = request.POST['amount']
#             extra = request.POST['extra']

#             inssql = 'insert into functions(city,name1,name2,amount,extra_special) values(%s,%s,%s,%s,%s)'
#             insval = [city,name1,name2,amount,extra]
#             cursor.execute(inssql,insval) 

#             text = f'{name1}-{name2} insert {amount} successfully...'

#             context = {'insert':text}

#             return render(request , 'home.html',context)

        # elif 'get' in request.POST:
        #     selsql = 'select * from functions order by id desc limit 1'
        #     cursor.execute(selsql)
        #     result = cursor.fetchall()
        #     context = {'get':result}

        #     return render(request , 'home.html',context)

def home(request):
    # selsql = 'select * from city limit 50'
    # cursor.execute(selsql)
    # result = cursor.fetchall()
    context = {'get':"Pch"}
    
    return render(request,'home.html',context)
def insert(request):
    return render(request,'insert.html')
