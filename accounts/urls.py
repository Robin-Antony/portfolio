from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [ 
    path('',views.register_page,name='register'),
    path('login_page',views.login_page,name='login_page'),
]