from django.shortcuts import render


from django.shortcuts import render, redirect
from .models import *
from django.db import connection
from django.contrib.auth import login,logout,authenticate
import mysql.connector as mc
from base64 import b64decode, b64encode
import cv2
from multiprocessing.pool import ThreadPool as Pool
import os
import pandas as pd
import numpy as np
from time import time
from datetime import datetime

cursor = connection.cursor()
tableName = 'Thamu'

new_path = "C:/Users/ThamotharanC/OneDrive - Softcrylic LLC/Desktop/Django/facerec/facerecapp/static/temp_img/image.png"


def templatenew(i): 
    
    image=cv2.imread(new_path)  #small

    roi = [167, 29, 267, 343]
    im_cropped = image[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]


    output_path="C:/Users/ThamotharanC/OneDrive - Softcrylic LLC/Desktop/Django/facerec/facerecapp/static/saved_img"
    
    newcv = im_cropped
        
    var=""
    if(i.endswith('.bmp') or i.endswith('.jpg') or i.endswith('.png') or i.endswith('.jpeg')):
        serread=cv2.imread(i)  #big 
        sercv=serread.copy()
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
                    cv2.rectangle(img= sercv, pt1= pt,pt2= (pt[0]+nw,pt[1]+nh),color= (0,255,255),thickness= 1)
                    
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
            
            
            with open(f'{new_path}', 'wb') as image_file:
                image_file.write(img)
            
            # ---- **************** -------
                        
            
            # image = Image.open(BytesIO(img))
            # image.show()
            
            search_path="C:/Users/ThamotharanC/OneDrive - Softcrylic LLC/Desktop/Django/facerec/facerecapp/static/img"
            path_list=[search_path+"/"+i for i in os.listdir(search_path)]
            
            check = []
            
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