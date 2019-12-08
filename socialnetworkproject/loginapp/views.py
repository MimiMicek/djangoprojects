from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout

#from .utils import random_string


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

        user = User.objects.create_user(request.POST['user'], password = request.POST['password'])
        user.save()
        dj_login(request, user)
        return HttpResponseRedirect(reverse('socialnetworkapp:index'))

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
