from django.urls import path
from . import views

urlpatterns = [
    path('customer/demographics/getAll', views.getAllCustomerDemographics),
    path('customer/demographics/add', views.addCustomerDemographics),
    path('customer/demographics/remove', views.removeCustomerDemographics),
    path('customer/geography/getAll', views.getAllCustomerGeography),
    path('customer/geography/add', views.addCustomerGeography),
    path('customer/geography/remove', views.removeCustomerGeography),
]