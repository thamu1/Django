from django.shortcuts import render, redirect
from django.db import connection
import json

from pathlib import Path
import numpy as np
from datetime import datetime, date
import smtplib

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

cursor = connection.cursor()


def send_mail(info, preab):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login("taahirimraan8601@gmail.com","cjveesehkihdeeii")
    # msg=f"{subject}\n\n YOU HAVE SUCCESSFULLY BOOKED... "

    sender = "taahirimraan8601@gmail.com"
    
    if(preab == 0):
        receiver = info[3] # input("enter your Mail id : ") 3
        name = info[2]
        content = f"""your work details on {date.today()}. \n\n You absent today. 
                \n your salary for today is = 0 """
                
    elif(preab == 1):
        receiver = info[2] # input("enter your Mail id : ") 3
        name = info[1]
        content = f"""your work details on {date.today()}, \n\n Hours of work = {info[3]} Minutes.
                \n You salary for today is = {info[5]}"""
    
    subject = f"{date.today()} - work and salary details"

    body = f"Hello {name} ,\n\n{content}."
    msg = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{body}"

    server.sendmail(sender,receiver,msg)

    print("mail sent")
    server.quit()



def employee():
    
    loc = f"{BASE_DIR}/fingerapp/static/json/emp_json.json"
    file = open(loc, "+w")
    allemp = """select distinct * from finger.employee;"""
    
    cursor.execute(allemp)
    res = cursor.fetchall()
    
    # result = list(np.array(res).reshape(-1))

    json.dump({"empid" : res}, file)
    
    
def endtrigger(emp):
    
    empid = emp[:,0]
    
    loc = f"{BASE_DIR}/fingerapp/static/json/emp_json.json"
    file = open(loc)
    jresult = json.load(file)['empid']
    id = np.array(jresult)
    
    for i in id:
  
        if(i[0] not in empid):

            ins = f"""INSERT INTO `finger`.`empwrktm` (`employee_id`, `user_name`, `mail`, `phoneNo`, `today_date`) 
            VALUES ('{i[0]}', '{i[2]}', '{i[3]}', '{i[4]}', '{datetime.today()}');"""
            
            cursor.execute(ins)

            send_mail(info = [i[0], i[2], i[3], datetime.today()], preab = 0)
    
    for j in emp:
        send_mail(info= j, preab= 1)
    

def home(request):
    
    if(request.method == "POST"):
        
        empid = request.POST['empID']
        
        if('in' in request.POST):
            pass
        
        elif('out' in request.POST):
            pass
        
        
        con = {"try":"yes"}
        return render(request, 'home.html', context=con)
        
    else:
        return render(request, 'home.html')


def emphrs(request):
    
    # employee()
    
    get_emp_hrs = """select *,
        case when hours_of_work is not null then hours_of_work * 1.04 else 0
        end as salary
        from (
        select employee_id, user_name, mail,
        sum(timestampdiff(minute, inTime, outTime)) as hours_of_work, today_date
        from finger.empwrktm
        group by employee_id, today_date, user_name, mail) as tar
        ;"""
            
    cursor.execute(get_emp_hrs)
    
    result = cursor.fetchall()
    
    # end trigger
    res = np.array(result)

    endtrigger(res)
    
    con = {"emphrs": result}
    
    return render(request, 'emphrs.html', context= con)


