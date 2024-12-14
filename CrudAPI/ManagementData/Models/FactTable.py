from django.db import models
from . import CustomerDemographics, CustomerGeography

class FactTable(models.Model):
    CustomerDemographicsID = models.ForeignKey(CustomerDemographics, on_delete=models.CASCADE)
    CustomerGeographyID = models.ForeignKey(CustomerGeography, on_delete=models.CASCADE)