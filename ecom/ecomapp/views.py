
from django.shortcuts import render, redirect
from .models import *
from django.db import connection
from django.contrib.auth import login,logout,authenticate
import cgi
import mysql.connector as mc
import shutil
import os


# conn = mc.connect(
#     host='127.0.0.1',
#     user='root',
#     password='Mysql.08',
#     database='functions'
#     )

# cursor = conn.cursor()

cursor = connection.cursor()
tableName = 'Thamu'

def home(request):
    path = "C:/Users/ThamotharanC/OneDrive - Softcrylic LLC/Desktop/Django/ecom/ecomapp/static/img/"
    
    l = list(os.walk(f"{path}"))
    
    
    context  = {"try" : l[0][2]}
    
    return render(request, 'home.html', context= context)
