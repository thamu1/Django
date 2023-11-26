from django.shortcuts import render, redirect
from .models import *
from django.db import connection
from django.contrib.auth import login,logout,authenticate
import cgi
import mysql.connector as mc
from base64 import b64encode, b64decode
from datetime import datetime, timedelta, date


cursor = connection.cursor()
tableName = 'product'


def login(request):
    if(request.method == 'POST' and ('login' in request.POST)):
        email = request.POST['username']
        password = request.POST['password']
        if(email == 'thamu@gmail.com' and password == '123'):
            request.session['user'] = email
            # request.session['user'] = userName
            request.session.save()
            # session_key=request.session.session_key
            return redirect('home')
        else:
            context = {'failed':'Login failed'}
            return redirect('home')
            # return render(request , 'emptyhome.html',context)
            
    else:
        return render(request, 'login.html')

def logout(request):
    if request.session.has_key('user'):
        del request.session['user']
        return redirect('login')
    else:
        return redirect('login')
    
    
def home(request):
    if 'user' in request.session:
        
        select_product = """select product_name, price_of_product,
        product_image, quantity, company_name
        from ecom.product_details
        where product_status = 1"""
        
        cursor.execute(select_product)
        
        all_product = cursor.fetchall()
        
        img_arr = []
        for i in all_product:
            img_arr.append(i[2].decode('utf-8'))
        
        con = {"product": zip(all_product, img_arr)}
        return render(request, 'home.html', context= con)
    else:
        con = {"yes": "Not Logged in."}
        return render(request, 'login.html', context= con)


def seller(request):
    if request.method == 'POST':
        if 'product_details' in request.POST:
            productName = request.POST['productName']
            productPrice = request.POST['productPrice']
            productQuantity = request.POST['productQuantity']
            productImage = request.FILES['productImage'].read()
            productDescription = request.POST['productDescription']
            companyID = request.POST['companyID']
            companyName = request.POST['companyName']
            companyLocation = request.POST['companyLocation']
            companyAddress = request.POST['companyAddress']
            companyEmail = request.POST['companyEmail']
            companyPhoneNo = request.POST['companyPhoneNo']
            
            productID = hash(productName)
            img = b64encode(productImage).decode('utf-8')
            
            
            # data = [productID, productName, productPrice, productQuantity,companyLocation,
            #         productDescription, companyID, companyName, companyAddress,
            #         companyEmail, companyPhoneNo]
        
            
            company_table = f"create table if not exists ecom.company("\
                f"company_id varchar(255) primary key,company_name varchar(255) not null,"\
                f"location varchar(255) not null,address varchar(255) not null,"\
                f"email varchar(255) not null,contact_details varchar(20) not null)"
                
            cursor.execute(company_table)
            

            product_table = f"create table if not exists ecom.product_details("\
                f"product_id varchar(255), product_name varchar(255),"\
                f"price_of_product varchar(255), product_image blob, product_description text,"\
                f"company_id varchar(255) not null, company_name varchar(255) not null,"\
                f"location varchar(255) not null, address varchar(255) not null,"\
                f"email varchar(255) not null, contect_details varchar(20) not null,"\
                f"quantity int not null, availablility int not null,"\
                f"product_status int not null, ins_up varchar(255) default 'insert',"\
                f"insert_date timestamp);"
                
            cursor.execute(product_table)
            
            
            getCompanyDetails = "select count(1) from ecom.company where company_id = %s and company_name = %s"
            getCompanyValue = [companyID, companyName] 
                
            cursor.execute(getCompanyDetails, getCompanyValue)
            com_cnt = cursor.fetchall()
            
            company_count = com_cnt[0][0]
            
            if(company_count <=0):
                
                company_insert_record = """insert into ecom.company(company_id, company_name, location,
                    address, email, contact_details) values(%s, %s, %s, %s, %s, %s)"""
                company_insert_values = [companyID, companyName, companyLocation, companyAddress, companyEmail, companyPhoneNo]
                cursor.execute(company_insert_record, company_insert_values)
                
                # try:
                #     company_insert_record = """insert into ecom.company(company_id, company_name, location, 
                #         address, email, contact_details) values(%s, %s, %s, %s, %s, %s)"""
                #     company_insert_value = [companyID, companyName, companyLocation, companyAddress, companyEmail, companyPhoneNo]
                #     cursor.execute(company_insert_record, company_insert_value)
                    
                #     company_insert_query_status = 1
                    
                # except:
                #     company_insert_query_status = 0
            
            
            getDetailsOfProduct = f"select count(1) from ecom.product_details "\
                f"where product_id = '{productID}' and company_id = '{companyID}'"
                
            cursor.execute(getDetailsOfProduct)
            pro_cnt = cursor.fetchall()
            
            product_count = pro_cnt[0][0]
            
            if(product_count <= 0):
                availability = productQuantity
                productStatus = 1
                insertUpdate = 'insert'
                insertDate = datetime.now()
                
            else:
                
                availability_check = f"select availablility from ecom.product_details "\
                    f"where product_id = '{productID}' and company_id = '{companyID}' "\
                    f"group by product_id, company_id "\
                    f"order by insert_date desc limit 1"
                        
                cursor.execute(availability_check)
                avail = cursor.fetchall()
                
                availability = avail[0][0] + productQuantity
                productStatus = 1
                insertUpdate = 'update'
                insertDate = datetime.now()
                
            
            product_insert_record = """insert into ecom.product_details(
                product_id, product_name,
                price_of_product, product_image, product_description,
                company_id, company_name,
                location, address, email, contect_details,
                quantity, availablility, product_status, ins_up, insert_date) 
                values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s);"""
                
            product_insert_values = [productID, productName, productPrice, img, productDescription,
                    companyID, companyName, companyLocation, companyAddress, companyEmail, companyPhoneNo,
                    productQuantity, availability, productStatus, insertUpdate, insertDate]
                
            cursor.execute(product_insert_record, product_insert_values)
            
            
            # con = {"pro_image" : img}
            
            con = {"pro_image": [company_count, product_count]}
            return render(request, 'seller_product_details.html', context= con)
            
        else:
            return render(request, 'seller_product_details.html')
        
    else:
        return render(request, 'seller_product_details.html')