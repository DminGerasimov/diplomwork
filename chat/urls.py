# chat/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.main, name="main"),
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    # path('logout/', views.logoutView, name='logout'),

    
]