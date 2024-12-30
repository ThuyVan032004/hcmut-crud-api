from django.urls import path
from . import views

urlpatterns = [
    path('register', views.adminRegister, name='register'),
    path('login', views.adminLogin, name='login'),
]