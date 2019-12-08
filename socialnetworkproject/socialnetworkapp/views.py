from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseBadRequest


#@login_required
def index(request):
    return render(request, 'socialnetworkapp/index.html')