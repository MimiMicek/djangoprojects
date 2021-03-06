from django.urls import path
from . import views


app_name = 'loginapp'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('reset-password', views.reset_password, name='reset-password'),
    path('profile', views.profile, name='profile'),
]