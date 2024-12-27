from django.db import models

class Address(models.Model):
    AddressID = models.AutoField(primary_key=True)
    AddressLine1 = models.CharField(max_length=60)
    City = models.CharField(max_length=30)
    StateProvinceID = models.IntegerField()
    PostalCode = models.CharField(max_length=15)

    class Meta:
        db_table = '[Person].[Address]'
        managed = False
