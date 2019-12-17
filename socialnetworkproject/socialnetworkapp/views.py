from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.models import User
from . import models
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

@login_required
def index(request):
    user = User.objects.filter(pk=1)[0]

    if request.method == 'GET':
        user_groups = models.AppGroup.objects.filter(users__username__contains=user.username)
        print(user, user_groups)
        posts = models.Post.objects.filter(group__in=user_groups).order_by('-created')[:10]

        context = {
            'user': user,
            'posts': posts,
            'user_groups': user_groups,
        }

        return render(request, 'socialnetworkapp/index.html', context=context)

    if request.method == 'POST':
        post = models.Post()
        post.text = request.POST['text']
        post.group = models.AppGroup.objects.get(pk=request.POST['group'])
        post.user = user
        post.save()
        return HttpResponseRedirect(reverse('socialnetworkapp:index'))

    return HttpResponseBadRequest()

def groups(request):
    user = User.objects.filter(pk=1)[0]
    if request.method == 'GET':
        user_groups = models.AppGroup.objects.filter(users__username__contains=user.username)
        not_user_groups = models.AppGroup.objects.exclude(users__username__contains=user.username)

        context = {
            'user_groups': user_groups,
            'not_user_groups': not_user_groups,
            'user': user,
        }

        return render(request, 'socialnetworkapp/groups.html', context=context)

    if request.method == 'POST':
        group = models.AppGroup()
        group.name = request.POST['name']
        group.description = request.POST['description']
        group.owner = user
        group.save()
        group.users.add(user)
        group.save()
        return HttpResponseRedirect(reverse('socialnetworkapp:groups'))

    return HttpResponseBadRequest()


def join_group(request, pk):
    user = User.objects.filter(pk=1)[0]
    group = models.AppGroup.objects.get(pk=pk)
    group.users.add(user)
    group.save()
    return HttpResponseRedirect(reverse('socialnetworkapp:groups'))


def leave_group(request, pk):
    user = User.objects.filter(pk=1)[0]
    group = models.AppGroup.objects.get(pk=pk)
    group.users.remove(user)
    group.save()
    return HttpResponseRedirect(reverse('socialnetworkapp:groups'))

class PostList(generics.ListCreateAPIView):
    queryset =  Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer