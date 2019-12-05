from django.urls import path
from . import views

app_name = 'stonebookapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('groups', views.groups, name='groups'),
    path('join_group/<int:pk>', views.join_group, name='join_group'),
    path('leave_group/<int:pk>', views.leave_group, name='leave_group'),
    path('profile', views.profile, name='profile'),

]