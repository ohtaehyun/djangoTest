from django.urls import path
from . import views

urlpatterns=[
    path('',views.about_me, name='about_me'),
    path('about_me',views.about_me, name='about_me'),
    path('project', views.project, name='project'),
    path('post_list',views.post_list, name='post_list'),
    path('post/<int: pk>/', views.post_detail, name='post_detail'),
    path('hi_ramji', views.hi_ramji, name='hi_ramji')
    
]
