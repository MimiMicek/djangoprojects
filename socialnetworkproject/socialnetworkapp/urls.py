from django.urls import path
from . import views
from .views import  PostList, PostDetail


app_name = 'socialnetworkapp'

urlpatterns = [
    path('index', views.index, name='index'),
    path('groups', views.groups, name='groups'),
    path('join_group/<int:pk>', views.join_group, name='join_group'),
    path('leave_group/<int:pk>', views.leave_group, name='leave_group'),
    path('<int:pk>/', PostDetail.as_view()),
    path('api/v1/', PostList.as_view()),
]