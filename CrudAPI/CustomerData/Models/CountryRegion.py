from django.db import models

class CountryRegion(models.Model):
    CountryRegionCode = models.CharField(max_length=3, primary_key=True)
    Name = models.CharField(max_length=50)
    
    class Meta:
        db_table = '[Person].[CountryRegion]'
        managed = False