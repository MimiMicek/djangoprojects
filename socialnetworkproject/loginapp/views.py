from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
import sys
sys.path.append('/your/dir/to/tensorflow/models') # point to your tensorflow dir
sys.path.append('/your/dir/to/tensorflow/models/slim') # point ot your slim dir
from celery import Celery
import yagmail


def login(request):
    context = {}
    if request.method == 'POST':
        user = authenticate(request,
                            username = request.POST['user'],
                            password = request.POST['password'])

        if user:
            dj_login(request, user)
            return HttpResponseRedirect(reverse('socialnetworkapp:index'))
        else:
            context['error'] = 'Username or password is wrong.'

    return render(request, 'loginapp/login.html', context)


def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('loginapp:login'))


def signup(request):
    if User.is_authenticated:
        dj_logout(request)
    context = {}

    if request.method == 'POST':
        if not request.POST['password'] == request.POST['repeatpassword']:
            context['error'] = 'Passwords do not match.'
            return render(request, 'loginapp/signup.html', context)

        if len(User.objects.filter(username = request.POST['user'])) > 0:
            context['error'] = 'Username already exists.'
            return render(request, 'loginapp/signup.html', context)

        if len(User.objects.filter(email = request.POST['email'])) > 0:
            context['error'] = 'Email already exists.'
            return render(request, 'loginapp/signup.html', context)

        user = User.objects.create_user(request.POST['user'], password = request.POST['password'])
        user.save()
        dj_login(request, user)

        app = Celery()
        app.config_from_object('celeryconfig')

        receiver = "email@gmail.com"
        body = "Congratulations, you are now a part of Social Network. Your life is officially over"

        yag = yagmail.SMTP("email@gmail.com")
        yag.send(
            to=receiver,
            subject="Signup confirmation for Social Network",
            contents=body
        )
        return HttpResponseRedirect(reverse('loginapp:login'))

    return render(request, 'loginapp/signup.html')


def reset_password(request):
    context = {}

    if request.method == 'POST':
        users = User.objects.filter(username = request.POST['user'])

        if users:
            user = users[0]
            new_password = random_string()
            user.set_password(new_password)
            user.save()
            print(f'**** User {user} change password to {new_password}')
            return HttpResponseRedirect(reverse('loginapp:login'))
        else:
            context['error'] = 'Username does not exist! Try again!'

    return render(request, 'loginapp/reset-password.html', context)

@login_required
def profile(request):
    return render(request, 'loginapp/profile.html')