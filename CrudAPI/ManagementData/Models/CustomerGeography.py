from django.db import models

class CustomerGeography(models.Model):
    CustomerGeographyID = models.IntegerField(primary_key=True)
    City = models.CharField(max_length=30)
    StateProvinceName = models.CharField(max_length=50)
    PostalCode = models.CharField(max_length=15)
    CountryRegionName = models.CharField(max_length=50)
    