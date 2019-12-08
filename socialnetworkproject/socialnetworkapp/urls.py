from django.urls import path
from . import views


app_name = 'socialnetworkapp'

urlpatterns = [
    path('', views.index, name='index')
]