from django.shortcuts import render,redirect
from .models import *
from django.db import connection
import mysql.connector as mc
import numpy as np
from base64 import b64encode, b64decode
from PIL import Image
from io import BytesIO

con = mc.connect(
    user = "root",
    host = "localhost",
    password = "Mysql.08",
    database = "book"
)
    
cursor = con.cursor()


def home(request):
    if(request.method == "POST"):
        if 'upload' in request.POST:
            img = request.FILES['img'].read()
            # img = b64encode(img).decode('utf-8')
            
            i1 = Image.open(BytesIO(img))
            
            i1.resize(size= (100,100))
            
            resized = BytesIO()
            
            i1.save(resized, format= 'PNG')
            
            img = b64encode(resized.getvalue()).decode('utf-8')
            
            # img = b64encode(i1).decode('utf-8')
            
            # im_arr = Image.open(img).resize(size=(100,100))
            
            # sql = "create table if not exists book_store(id int auto_increment, img longblob, primary key(id))"
            # cursor.execute(sql)
            # text = "created"
            
            # sql = f"insert into book_store(img) values(%s)"
            # val = (img,)
            # cursor.execute(sql, val)
            # con.commit()
            
            # img = Image.fromarray(im_arr)
            
            # img = img.
            
            # text += " " +"image inserted"
            
            # sql = "select img from book_store where img is not null"
            # cursor.execute(sql)
            # re = cursor.fetchall()
            
            # img_arr = []
            # for i in re:
            #     img_arr.append(i[0].decode('utf-8'))
            
            
            return render(request,'home.html',context={"img":img})
        
        elif('drop' in request.POST):
            # sql = "drop table book_store"
            # cursor.execute(sql)
            # con.commit()
            context = {"drop": "table dropped successfully."}
            return render(request, 'home.html',context=context)
            
        else:
             return render(request, 'home.html')
    else:
        return render(request, 'home.html')



