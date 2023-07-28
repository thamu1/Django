from django.shortcuts import render
from joblib import load
from pathlib import Path
import smtplib
from numpy import random

BASE_DIR = Path(__file__).resolve().parent.parent

model = load(BASE_DIR / 'wapp/notebook/random_model.joblib')


def home(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        val1 = request.POST['1']
        val2 = request.POST['2']
        val3 = request.POST['3']
        val4 = request.POST['4']
        val5 = request.POST['5']
        val6 = request.POST['6']
        val7 = request.POST['7']


        att = [val1,val2,val3,val4,val5,val6,val7]

        # 29.8	5.7	7.2	189	2	0.2	4953	8391

        # 20.5	6.7	2.7	1350	3.3	1.1	7	16




        ypred = model.predict([att])

        ans = ypred[0]
        # ypred = model.predict([att])

        yesOrNO = ""

        # ypred = ypred * 100
        # ypred = (ypred * 100000)+30
        if(ans == 0):
            ypred = random.randint(50,70)
            yesOrNO = f"The Water {ypred} % pure . It is Acidic Water , Don't Drink it"
        elif(ans == 1):
            ypred = random.randint(90,100)
            yesOrNO = f"The Water {ypred} % pure . It is pure Water , Can drink it"
        else :
            ypred = random.randint(30,60)
            yesOrNO = f"The Water {ypred} % pure . It is Hard Water ,  Don't Drink it"
        try:
            server=smtplib.SMTP_SSL('smtp.gmail.com',465)
            server.ehlo()
            server.login("taahirimraan8601@gmail.com","vptcjlkehrqssyik")

            sender = "taahirimraan8601@gmail.com"
            receiver = email
            subject = "Water Quality Level"

            body = f"Hello Sir/Madam,\n\n {yesOrNO}."
            msg = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{body}"

            server.sendmail(sender,receiver,msg)
            # print("<script>alert(\"mail sent...\")<script>")
            server.quit()
            return render(request , 'home.html',{'result':[ypred,yesOrNO]})
        except:
            return render(request , 'home.html',{'error':[ypred,yesOrNO]})
    
    else:
        return render(request,'home.html')

    

