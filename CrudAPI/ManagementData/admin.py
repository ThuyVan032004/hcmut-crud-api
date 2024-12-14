from django.contrib import admin
from .models import CustomerDemographics, CustomerGeography, FactTable

# Check if CustomerDemographics is defined correctly in models.py
admin.site.register(CustomerDemographics) 
admin.site.register(CustomerGeography)
admin.site.register(FactTable)

