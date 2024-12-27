from django.urls import path
from . import views

urlpatterns = [
    path('addCustomer', views.addCustomer, name='addCustomer'),
    path('getAllCustomer', views.getAllCustomer, name='getAllCustomer'),
    path('deleteCustomer/<int:BusinessEntityID>', views.deleteCustomer, name='deleteCustomer'),
    path('updateCustomer/<int:BusinessEntityID>', views.updateCustomer, name='updateCustomer'),
]