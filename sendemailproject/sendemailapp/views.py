from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login
from celery import Celery
import yagmail

# def login(request):
#     context = {}
#     if request.method == 'POST':
#         user = authenticate(request,
#                             username=request.POST['user'],
#                             password=request.POST['password'])
#
#
#     return render(request, 'sendemailapp/login.html', context)

def signup(request):
    context = {}
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['user'], password=request.POST['password'])
        user.save()
        dj_login(request, user)

        app = Celery()
        app.config_from_object('celeryconfig')

        receiver = "micekpython@gmail.com"
        body = "This is your email working"

        yag = yagmail.SMTP("micekpython@gmail.com")
        yag.send(
            to=receiver,
            subject="Test email working",
            contents=body,
        )
        return render(request, 'sendemailapp/login.html', context)

    return render(request, 'sendemailapp/index.html')

