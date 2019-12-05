from django.shortcuts import render, reverse
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from . import models

def index(request):
    user = User.objects.filter(pk=1)[0]

    if not request.method == 'GET':
        return HttpResponseBadRequest()

    user_groups = models.AppGroup.objects.filter(users__username__contains=user.username)
    posts = models.Post.objects.filter(group__in=user_groups)

    context = {
        #the user which is logged in not the user which created the post
        'user': user,
        'posts': posts,
    }

    return render(request, 'stonebookapp/index.html', context=context)

    if request.method == 'POST':
        post = models.Post()
        post.text = request.POST['text']
        post.group = request.POST['group']
        post.user = user
        post.save()


def groups(request):
    user = User.objects.filter(pk=1)[0]

    if request.method == 'GET':
        user_groups = models.AppGroup.objects.filter(users__username__contains=user.username)
        not_user_groups = models.AppGroup.objects.exclude(users__username__contains=user.username)

        context = {
            # the user which is logged in not the user which created the post
            'user_groups': user_groups,
            'not_user_groups': not_user_groups,
            'user': user
        }

        return render(request, 'stonebookapp/groups.html', context=context)

    if request.method == 'POST':
        group = models.AppGroup()
        group.name = request.POST['name']
        group.description = request.POST['description']
        group.owner = user
        group.save()
        group.users.add(user)
        group.save()
        return HttpResponseRedirect(reverse('stonebookapp:groups'))

    return  HttpResponseBadRequest()


def join_group(request, pk):
    user = User.objects.filter(pk=1)[0]
    group = models.AppGroup.objects.get(pk=pk)
    group.users.add(user)
    group.save()

    return HttpResponseRedirect(reverse('stonebookapp:groups'))

def leave_group(request, pk):
    user = User.objects.filter(pk=1)[0]
    group = models.AppGroup.objects.get(pk=pk)
    group.users.remove(user)
    group.save()

    return HttpResponseRedirect(reverse('stonebookapp:groups'))


def profile(request):
    pass