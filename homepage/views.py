from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import redirect
from .models import CustomerVoice, RecruitmentExample, Consultation
from django.forms.models import model_to_dict
import datetime
import calendar


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.settings import EMAIL_HOST_USER, EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_PASSWORD, DEFAULT_FROM_EMAIL


def homepage(request):
    template = loader.get_template('index.html')
    
    try:
        customer_voices = CustomerVoice.objects.all()
        recruit_examples = RecruitmentExample.objects.all()
        consultations = Consultation.objects.all()
        calendar = []

        today = datetime.datetime.now()

        month_name = datetime.datetime.strptime(str(today.month), "%m").strftime("%B")

        for item in consultations:
            year = item.time.year 
            month = item.time.month 
            day = item.time.day
                        
            if (today.year == year) & (today.month == month):
                calendar.append(day)

        return render(request, "index.html", {"customer_voices": customer_voices, "recruit_examples": recruit_examples,
                                                "calendar": calendar, "year": today.year,  "month": today.month, "month_name": month_name})
    except Exception as error:
        print(str(error))
    
    return HttpResponse(template.render())


def send_mail(request):
    
    msg = MIMEMultipart('alternative')
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = DEFAULT_FROM_EMAIL
    msg['Subject'] = "" 

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        
        try:
            # server = smtplib.SMTP(host=EMAIL_HOST, port=EMAIL_PORT, timeout=60)
            # server.ehlo()
            # server.starttls()
            # server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            message = f"{name}さんが相談を希望しています。 メールアドレスです：{email}  電話番号:{phone} 。`{description}`"
            print(message)
            # html_part = MIMEText(f"{message}", 'html')
            # msg.attach(html_part)
            
            # server.sendmail(msg['From'], msg['To'], msg.as_string())

            # print(f'Mail was send to {msg["To"]}')
            # server.quit()
        except Exception as error:
            print(error)

    return redirect('/')