from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='main'),
    path('group/<slug:slug>/', views.group_posts, name='group_list')
=======
    path('', views.index),
    path('group/<slug:slug>/', views.group_posts),
>>>>>>> bd5d3c6eaee4b5927049c3e8dad3629b24cadc28
]