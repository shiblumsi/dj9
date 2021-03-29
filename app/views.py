from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from .forms import *

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail




# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect('login')


def signup(request):
    form = Signup()
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)
            subject = 'Account created'
            message = render_to_string('email.html',{
                'domain' :current_site.domain,
                'user':user.username
            })
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)

            # current_site = get_current_site(request)
            # mail_subjects = 'Account created'
            # message = render_to_string('email.html',{
            #     'domain' :current_site.domain,
            #     'user':user.username
            # })
            # send_mail = form.cleaned_data.get('email')
            # print(send_mail)
            # email = EmailMessage(mail_subjects,message,to=[send_mail])
            # email.send()
            return redirect('login')
    return render(request, 'signup.html',{'form':form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        login(request,user)
        return redirect('home')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')