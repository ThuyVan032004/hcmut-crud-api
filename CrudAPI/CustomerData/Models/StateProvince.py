from django.db import models

class StateProvince(models.Model):
    StateProvinceID = models.AutoField(primary_key=True)
    StateProvinceCode = models.CharField(max_length=3)
    CountryRegionCode = models.CharField(max_length=3)
    Name = models.CharField(max_length=50)
    class Meta:
        db_table = '[Person].[StateProvince]'
        managed = False