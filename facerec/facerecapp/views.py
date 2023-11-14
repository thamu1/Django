from django.shortcuts import render


from django.shortcuts import render, redirect
from .models import *
from django.db import connection
from django.contrib.auth import login,logout,authenticate
import cgi
import mysql.connector as mc
from base64 import b64decode, b64encode
from io import BytesIO
from PIL import Image
import cv2
from multiprocessing.pool import ThreadPool as Pool
import os
import pandas as pd
import numpy as np
from time import time
from datetime import datetime

cursor = connection.cursor()
tableName = 'Thamu'

new_path = "C:/Users/ThamotharanC/OneDrive - Softcrylic LLC/Desktop/Django/facerec/facerecapp/static/temp_img"
check = []

def templatenew(i, new_img_path= f"{new_path}/image.png"): 
    output_path="C:/Users/ThamotharanC/OneDrive - Softcrylic LLC/Desktop/Django/facerec/facerecapp/static/saved_img"
    
    newcv=cv2.imread(new_img_path)  #small
        
    var=""
    if(i.endswith('.bmp') or i.endswith('.jpg') or i.endswith('.png') or i.endswith('.jpeg')):
        serread=cv2.imread(i)  #big 
        sercv=serread
        nh,nw,ns=newcv.shape
        sh,sw,ss=sercv.shape
        if(sh>=nh and sw>=nw and ss>=ns):
            res=cv2.matchTemplate(sercv,newcv,cv2.TM_CCOEFF_NORMED)
            th=0.80
            loc=np.where(res>=th)
            if(len(loc[0])>0 and len(loc[1])):
                var="true"
                savepath=output_path+"/"+str(time())+".png"
                for pt in zip(*loc[::-1]):
                    cv2.rectangle(sercv,pt,(pt[0]+nw,pt[1]+nh),(0,255,255),2)
                    
                cv2.imwrite(savepath,sercv)
            else:
                var = "false"
                
        else:
            var = "false"
            
    return var

        
def home(request):
    return render(request, 'home.html')


def login(request):
    
    if request.method == 'POST':
        if 'submitFormButton' in request.POST:
            
            # img = request.FILES["capturedImageData"].read()
            # img = b64encode(img).decode('utf-8')
            # <img src="data:image/jpeg;base64,{{ img }}" alt="Decoded Image" width="100" height="100">
            
            core_img = request.POST["capturedImageData"]
                        
            img_byte = core_img.split(",")[1]
            
            img = b64decode(img_byte)
            
            
            with open(f'{new_path}/image.png', 'wb') as image_file:
                image_file.write(img)
            
            # ---- **************** -------
            
            
            # image = Image.open(BytesIO(img))
            # image.show()
            
            search_path="C:/Users/ThamotharanC/OneDrive - Softcrylic LLC/Desktop/Django/facerec/facerecapp/static/img"
            path_list=[search_path+"/"+i for i in os.listdir(search_path)]
            
            pool = Pool(10)
            for var in pool.map(templatenew, path_list):
                check.append(var)
                    
            
            # ---- **************** -------
               
            context = {"text": check}
            return render(request, 'login.html', context= context)
        else:
            context = {"text": "image not received"}
            return render(request, 'login.html', context= context)
    else:
        context = {"text": "No Process."}
        return render(request, 'login.html', context= context)