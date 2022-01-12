
from django.contrib import admin
from django.urls import path
from generate import views

urlpatterns = [
    path('', views.home, name='home'), #home.html
    path('password/', views.password, name='password'), #password.html
    path('about/', views.about, name='about'), #about.html
]
