from django.contrib import admin
from django.urls import path
from a import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('login',views.login_ ,name='login'),
    path('signup',views.signup, name= 'signup'),
    path('contact',views.contact,name='contact'),
]